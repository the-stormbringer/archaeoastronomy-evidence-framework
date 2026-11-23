"""Integrity and table-comparison helpers for the preserved research pipeline."""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]


def load_pipeline(root=ROOT):
    return json.loads((root / "data/pipeline.json").read_text(encoding="utf-8"))


def contract_errors(contract):
    if not isinstance(contract, dict):
        return ["Pipeline contract must be an object"]
    errors = []
    for key, count in [("execution_order", 10), ("inputs", 3), ("reference_outputs", 13)]:
        values = contract.get(key)
        if not isinstance(values, list) or any(not isinstance(x, str) for x in values):
            errors.append("Invalid pipeline list: " + key); continue
        if len(values) != count or len(set(values)) != count:
            errors.append("Wrong count or duplicate pipeline entry: " + key)
        for value in values:
            path = PurePosixPath(value)
            if not value or path.is_absolute() or ".." in path.parts or "\\" in value or str(path) != value:
                errors.append("Unsafe pipeline path: " + value)
            if key in {"execution_order", "inputs"} and len(path.parts) != 1:
                errors.append("Expected flat pipeline filename: " + value)
    if contract.get("staged_input_directory") != "source_reconciliation-2026-10-22":
        errors.append("Historical staging directory changed")
    tolerance = contract.get("tolerance", {})
    expected_file = "analysis/geometry-comparison-2026-10-23/estimand_comparison.csv"
    if not isinstance(tolerance, dict) or tolerance.get("file") != expected_file or tolerance.get("columns") != ["origin_constrained_TLS_deg", "TLS_minus_arithmetic_deg"] or tolerance.get("absolute_degrees") != 1e-10:
        errors.append("Historical tolerance policy changed; requires explicit versioned policy review")
    hashes = contract.get("sha256")
    if not isinstance(hashes, dict):
        errors.append("Missing hash inventory")
    else:
        for name, value in hashes.items():
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or "\\" in name or str(path) != name:
                errors.append("Unsafe hash path: " + name)
            if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
                errors.append("Malformed hash: " + name)
    return errors


def integrity_errors(root=ROOT):
    try:
        contract = load_pipeline(root)
    except (ValueError, OSError) as exc:
        return ["Cannot read pipeline contract: " + str(exc)]
    errors = contract_errors(contract)
    if errors:
        return errors
    for name, expected in contract["sha256"].items():
        path = root / name
        if not path.is_file():
            errors.append("Missing locked file: " + name)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append("Hash mismatch: " + name)
    scripts = {"analysis/" + n for n in contract["execution_order"]}
    inputs = {"data/source/" + n for n in contract["inputs"]}
    references = {"data/reference/" + n for n in contract["reference_outputs"]}
    if scripts | inputs | references != set(contract["sha256"]):
        errors.append("Pipeline membership does not match locked hashes")
    actual = {str(p.relative_to(root / "data/reference")) for p in (root / "data/reference").rglob("*.csv")}
    if actual != set(contract["reference_outputs"]):
        errors.append("Reference table inventory differs from declared outputs")
    if len(contract["execution_order"]) != 10 or len(contract["reference_outputs"]) != 13:
        errors.append("Historical pipeline must declare ten scripts and thirteen tables")
    return errors


def compare_table(reference, generated, relative_name, tolerance):
    result = {"file": relative_name, "exists": generated.is_file(), "byte_identical": False,
              "agreement": False, "differences": []}
    if not generated.is_file():
        result["error"] = "Missing generated table"
        return result
    result["byte_identical"] = reference.read_bytes() == generated.read_bytes()
    with reference.open(newline="", encoding="utf-8") as f:
        expected = list(csv.reader(f))
    with generated.open(newline="", encoding="utf-8") as f:
        actual = list(csv.reader(f))
    if not expected or len(expected) != len(actual) or expected[0] != actual[0]:
        result["error"] = "Row count or column headers differ"
        return result
    good = True
    for row_number, (left, right) in enumerate(zip(expected[1:], actual[1:]), 2):
        if len(left) != len(right) or len(left) != len(expected[0]):
            result["error"] = "Row width differs at row " + str(row_number)
            return result
        for column, (old, new) in enumerate(zip(left, right)):
            if old == new:
                continue
            field = expected[0][column]
            permitted = relative_name == tolerance["file"] and field in tolerance["columns"]
            try:
                delta = abs(float(old) - float(new))
                accepted = permitted and math.isfinite(delta) and delta <= tolerance["absolute_degrees"]
            except ValueError:
                delta, accepted = None, False
            result["differences"].append({"row": row_number, "field": field,
                                          "absolute_difference": delta if delta is None or math.isfinite(delta) else None,
                                          "accepted": accepted})
            good = good and accepted
    result["agreement"] = good
    return result


def state_errors(root=ROOT):
    state = json.loads((root / "docs/PROJECT_STATE.json").read_text(encoding="utf-8"))
    stages = state["workplan"]
    ids = [s["id"] for s in stages]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append("Duplicate workplan IDs")
    by_id = {s["id"]: s for s in stages}
    visiting, visited = set(), set()
    def visit(stage_id):
        if stage_id not in by_id:
            errors.append("Unknown dependency: " + stage_id)
            return
        if stage_id in visiting:
            errors.append("Cyclic workplan dependency: " + stage_id)
            return
        if stage_id in visited:
            return
        visiting.add(stage_id)
        for dependency in by_id[stage_id]["depends_on"]:
            visit(dependency)
        visiting.remove(stage_id)
        visited.add(stage_id)
    for stage_id in ids:
        visit(stage_id)
    for section in ["artifacts", "work_packages"]:
        for key, value in state.get(section, {}).items():
            if not (root / value).exists():
                errors.append("Missing state target: " + key + " -> " + value)
    from governance import governance_errors
    return errors + governance_errors(root)


def markdown_link_errors(root=ROOT):
    errors = []
    files = list(root.glob("*.md")) + list((root / "docs").rglob("*.md")) + [root / "data/README.md"]
    for file in files:
        if not file.exists():
            continue
        # Skip fenced command examples; only resolve authored local links.
        text = re.sub(r"```.*?```", "", file.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\]\(([^\n)]+)\)", text):
            target = target.strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if Path(target).is_absolute() or not (file.parent / target).exists():
                errors.append(str(file.relative_to(root)) + ": " + target)
    return errors
