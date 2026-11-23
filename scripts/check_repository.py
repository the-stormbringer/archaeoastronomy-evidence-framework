"""Check the curated repository without requiring the ignored local archive."""
import json
from repository import ROOT, integrity_errors, state_errors, markdown_link_errors
from governance import record_errors, locator_errors, identity_premise_errors


def main():
    checks = {"pipeline": integrity_errors(), "state": state_errors(), "links": markdown_link_errors(), "records": record_errors(ROOT), "claim_evidence": locator_errors(ROOT), "identity_premise": identity_premise_errors(ROOT)}
    print(json.dumps({"passed": not any(checks.values()), "checks": checks}, indent=2))
    return int(any(checks.values()))


if __name__ == "__main__":
    raise SystemExit(main())
