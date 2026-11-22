"""Check the curated repository without requiring the ignored local archive."""
import json
from repository import integrity_errors, state_errors, markdown_link_errors


def main():
    checks = {"pipeline": integrity_errors(), "state": state_errors(), "links": markdown_link_errors()}
    print(json.dumps({"passed": not any(checks.values()), "checks": checks}, indent=2))
    return int(any(checks.values()))


if __name__ == "__main__":
    raise SystemExit(main())
