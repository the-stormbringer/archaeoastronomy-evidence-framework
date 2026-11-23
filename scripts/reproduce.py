"""Run the preserved ten-script pipeline in a fresh isolated working directory."""
import argparse
from datetime import datetime, timezone
import hashlib
import platform
import os
import importlib.metadata
import json
from pathlib import Path
import shutil
import subprocess
import sys

from repository import ROOT, compare_table, integrity_errors, load_pipeline


def child_environment():
    environment = {**os.environ, "PYTHONUTF8": "1"}
    environment.pop("PYTHONOPTIMIZE", None)
    return environment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New output directory; defaults to a timestamped runs/ subdirectory")
    args = parser.parse_args()
    if not __debug__:
        parser.error("Do not use Python -O: the historical scripts rely on assertions")
    errors = integrity_errors()
    if errors:
        print(json.dumps({"passed": False, "errors": errors}, indent=2))
        return 1
    started = datetime.now(timezone.utc).isoformat()
    dependencies = {}
    try:
        for name in ["numpy", "pyproj", "mpmath", "certifi", "jsonschema"]:
            dependencies[name] = importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError as exc:
        parser.error("Install requirements.txt first: " + str(exc))
    default = ROOT / "runs" / ("reproduce-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"))
    output = (args.output or default).expanduser().resolve()
    # Only the runs/ subtree is a legitimate output location inside the repository.
    if output == ROOT or (ROOT in output.parents and ROOT / "runs" not in output.parents):
        parser.error("Output inside the repository must be a new child of runs/")
    if output.exists():
        parser.error("Output already exists; select a new directory (nothing is overwritten)")
    output.mkdir(parents=True)
    work, logs = output / "work", output / "logs"
    work.mkdir(); logs.mkdir()
    contract = load_pipeline()
    contract_bytes = (ROOT / "data/pipeline.json").read_bytes()
    (output / "PIPELINE.json").write_bytes(contract_bytes)
    def git_value(*arguments):
        result = subprocess.run(["git", "-C", str(ROOT), *arguments], capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else None
    try:
        revision = git_value("rev-parse", "HEAD")
        dirty = git_value("status", "--porcelain")
    except FileNotFoundError:
        revision, dirty = None, None
    provenance = {
        "started_utc": started, "git_revision": revision,
        "git_worktree_dirty": bool(dirty) if dirty is not None else None,
        "platform": platform.platform(),
        "contract_sha256": hashlib.sha256(contract_bytes).hexdigest(),
        "locked_files_sha256": contract["sha256"],
        "runner_files_sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in sorted((ROOT / "scripts").glob("*.py"))},
        "requirements_sha256": hashlib.sha256((ROOT / "requirements.txt").read_bytes()).hexdigest(),
        "command": [sys.executable, *sys.argv],
        "environment_scope": "Selected non-secret execution settings only; not a complete machine image",
        "python_utf8": "1", "python_optimized": False,
    }
    inputs = work / contract["staged_input_directory"]
    inputs.mkdir()
    for name in contract["execution_order"]:
        shutil.copy2(ROOT / "analysis" / name, work / name)
    for name in contract["inputs"]:
        shutil.copy2(ROOT / "data/source" / name, inputs / name)
    staged_hashes = {}
    for name in contract["execution_order"]:
        staged_hashes["analysis/" + name] = hashlib.sha256((work / name).read_bytes()).hexdigest()
    for name in contract["inputs"]:
        staged_hashes["data/source/" + name] = hashlib.sha256((inputs / name).read_bytes()).hexdigest()
    provenance["staged_files_sha256"] = staged_hashes
    if any(contract["sha256"][name] != value for name, value in staged_hashes.items()):
        raise RuntimeError("Staged input differs from locked contract")
    (output / "PROVENANCE.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    child_env = child_environment()
    scripts = []
    for name in contract["execution_order"]:
        try:
            process = subprocess.run([sys.executable, str(work / name)], cwd=work,
                                     capture_output=True, text=True, encoding="utf-8", timeout=300,
                                     env=child_env)
            record = {"script": name, "exit_code": process.returncode}
            (logs / (name + ".log")).write_text(process.stdout + "\nSTDERR:\n" + process.stderr, encoding="utf-8")
        except subprocess.TimeoutExpired:
            record = {"script": name, "exit_code": None, "error": "300-second script timeout"}
            (logs / (name + ".log")).write_text(record["error"] + "\n", encoding="utf-8")
        scripts.append(record)
        if record["exit_code"] != 0:
            break
    tables = []
    if len(scripts) == len(contract["execution_order"]) and all(s["exit_code"] == 0 for s in scripts):
        for name in contract["reference_outputs"]:
            tables.append(compare_table(ROOT / "data/reference" / name, work / name, name, contract["tolerance"]))
    unchanged = not integrity_errors() and (ROOT / "data/pipeline.json").read_bytes() == contract_bytes
    passed = (len(tables) == len(contract["reference_outputs"]) and all(t["agreement"] for t in tables) and unchanged)
    artifacts = {str(path.relative_to(output)): hashlib.sha256(path.read_bytes()).hexdigest()
                 for path in sorted((work / "analysis").rglob("*")) if path.is_file()}
    report = {"passed": passed, "generated_artifacts_sha256": artifacts, "scope": "Numerical repeatability, not archaeological or external scientific acceptance",
              "provenance": provenance, "completed_utc": datetime.now(timezone.utc).isoformat(),
              "python": sys.version, "dependencies": dependencies, "scripts": scripts, "tables": tables,
              "locked_repository_inputs_unchanged": unchanged, "output": str(output), "tolerance": contract["tolerance"]}
    (output / "VALIDATION.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"passed": passed, "scripts_completed": sum(s["exit_code"] == 0 for s in scripts),
                      "tables_compared": len(tables), "byte_identical": sum(t["byte_identical"] for t in tables),
                      "report": str(output / "VALIDATION.json")}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
