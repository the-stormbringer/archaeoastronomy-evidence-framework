"""Structural acceptance controls; these never adjudicate scientific truth."""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import json

STATUS = {'pending', 'ready', 'in_progress', 'conditional', 'deferred', 'complete', 'blocked'}
EXPECTED_STAGES = {f'W{i}' for i in range(8)}
# Versioned stage/queue dependencies implement the accepted plan; changing them requires
# an explicit plan and validator amendment rather than silently deleting an edge.
STAGE_DEPS = {'W0': [], 'W1': ['W0'], 'W2': ['W1'], 'W3': ['W2'],
              'W4': ['W1', 'W2', 'W3'], 'W5': ['W4'], 'W6': ['W5'], 'W7': ['W6']}
TASK_DEPS = {**{f'W1-0{i}': [] for i in range(1, 7)},
             'E1': ['W1-01', 'W1-02'], 'E2': ['W1-01', 'W1-02'],
             'E3': ['E1', 'E2', 'W1-06'], 'E4': ['W1-03', 'W1-04'],
             'E5': ['E1', 'E2', 'E3', 'E4'], 'E6': ['E1', 'E2', 'E3', 'E4']}
OBJECTIVE_DEPS = {'S1': [], 'S2': ['S1'], 'S3': ['S2'], 'S4': ['S2'],
                  'S5': ['S3', 'S4'], 'S6': ['S5']}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_path(root, value):
    """Require a canonical, portable path to an existing repository file."""
    if not isinstance(value, str) or not value or '\\' in value:
        return None
    p = PurePosixPath(value)
    if p.is_absolute() or '..' in p.parts or str(p) != value:
        return None
    candidate = root / value
    if not candidate.is_file() or not candidate.resolve().is_relative_to(root.resolve()):
        return None
    if p.parts[0] in {'legacy', 'agent_artifacts', 'runs', '.git'}:
        return None
    return candidate


def evidence_errors(root, evidence, label):
    if not isinstance(evidence, list) or not evidence:
        return [f'{label}: nonempty evidence required']
    errors = []
    for item in evidence:
        if not isinstance(item, dict):
            errors.append(f'{label}: malformed evidence'); continue
        path = local_path(root, item.get('path'))
        if path is None or digest(path) != item.get('sha256'):
            errors.append(f'{label}: missing, unsafe or stale evidence {item.get("path")}')
    return errors


def receipt_errors(root, name, identifier):
    path = local_path(root, name)
    if path is None:
        return [f'{identifier}: completion requires a portable acceptance receipt']
    try:
        receipt = json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, OSError):
        return [f'{identifier}: unreadable acceptance receipt']
    errors = []
    if not isinstance(receipt, dict):
        return [f'{identifier}: malformed acceptance receipt']
    if receipt.get('id') != identifier or receipt.get('decision') not in {'accepted', 'omitted_with_reason'}:
        errors.append(f'{identifier}: receipt identity/decision mismatch')
    if receipt.get('decision') == 'omitted_with_reason' and identifier not in {'W3', 'E5', 'E6'}:
        errors.append(f'{identifier}: omission cannot close this item')
    for field in ('reviewer', 'date', 'scope', 'rationale', 'limitations'):
        if not isinstance(receipt.get(field), str) or not receipt[field].strip():
            errors.append(f'{identifier}: receipt needs {field}')
    criteria = receipt.get('criteria')
    if not isinstance(criteria, list) or not criteria or any(not isinstance(x, dict) or not x.get('criterion') or x.get('met') is not True for x in criteria):
        errors.append(f'{identifier}: all explicit acceptance criteria must be met')
    errors += evidence_errors(root, receipt.get('evidence'), identifier)
    if identifier in {'W6', 'P2', 'P3'}:
        errors += evidence_errors(root, receipt.get('external_attestations'), identifier + ' external scrutiny')
    return errors


def graph_errors(root, entries, label, expected=None):
    errors = []
    if not isinstance(entries, list) or any(not isinstance(x, dict) for x in entries):
        return [label + ': expected a list of records']
    ids = [x.get('id') for x in entries]
    if any(not isinstance(x, str) for x in ids) or len(ids) != len(set(ids)):
        return [label + ': missing or duplicate IDs']
    if expected is not None and set(ids) != expected:
        errors.append(label + ': required IDs differ')
    by_id = {x['id']: x for x in entries}
    visited, visiting = set(), set()
    def visit(key):
        if key not in by_id:
            errors.append(label + ': unknown dependency ' + str(key)); return
        if key in visiting:
            errors.append(label + ': cycle at ' + key); return
        if key in visited:
            return
        visiting.add(key)
        deps = by_id[key].get('depends_on', [])
        if not isinstance(deps, list) or any(not isinstance(x, str) for x in deps):
            errors.append(label + ': malformed dependencies for ' + key); deps = []
        if len(deps) != len(set(deps)):
            errors.append(label + ': duplicate dependencies for ' + key)
        for dep in deps:
            visit(dep)
        visiting.remove(key); visited.add(key)
    for item in entries:
        key = item['id']; visit(key)
        if item.get('status') not in STATUS:
            errors.append(label + ': invalid status for ' + key)
        if item.get('status') == 'complete':
            errors += receipt_errors(root, item.get('acceptance_record'), key)
            for dep in item.get('depends_on', []):
                if by_id.get(dep, {}).get('status') != 'complete':
                    errors.append(f'{key}: dependency {dep} is not complete')
    return errors


def governance_errors(root):
    try:
        state = json.loads((root / 'docs/PROJECT_STATE.json').read_text(encoding='utf-8'))
        queue = json.loads((root / 'docs/work_packages/WORK_QUEUE.json').read_text(encoding='utf-8'))
    except (ValueError, OSError) as exc:
        return ['Cannot read state/queue: ' + str(exc)]
    errors = graph_errors(root, state.get('workplan'), 'stages', EXPECTED_STAGES)
    errors += graph_errors(root, state.get('tasks'), 'objectives', {f'S{i}' for i in range(1, 7)})
    errors += graph_errors(root, queue.get('tasks'), 'queue', {f'W1-0{i}' for i in range(1, 7)} | {f'E{i}' for i in range(1, 7)})
    for entries, expected in [(state.get('workplan', []), STAGE_DEPS),
                              (state.get('tasks', []), OBJECTIVE_DEPS),
                              (queue.get('tasks', []), TASK_DEPS)]:
        for entry in entries:
            if entry.get('id') in expected and entry.get('depends_on') != expected[entry['id']]:
                errors.append(entry['id'] + ': required dependency edges changed')
    stages = {x['id']: x for x in state.get('workplan', [])}
    tasks = {x['id']: x for x in queue.get('tasks', [])}
    for stage, children in {'W1': [f'W1-0{i}' for i in range(1, 7)], 'W2': ['E1', 'E2', 'E3', 'E4'], 'W3': ['E5', 'E6']}.items():
        if stages.get(stage, {}).get('status') == 'complete' and any(tasks.get(key, {}).get('status') != 'complete' for key in children):
            errors.append(stage + ': required work items are not closed')
    gates = state.get('publication_gates', [])
    if {x.get('id') for x in gates} != {f'P{i}' for i in range(5)} or len(gates) != 5:
        errors.append('Publication gate IDs differ')
    for gate in gates:
        if gate.get('status') not in {'in_progress', 'open_external', 'pending_submission_stage', 'complete', 'blocked'}:
            errors.append('Invalid publication gate status: ' + str(gate.get('id')))
        if gate.get('status') == 'complete':
            errors += receipt_errors(root, gate.get('acceptance_record'), gate['id'])
    return errors


def record_errors(root):
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        return ['Install requirements.txt: jsonschema is required for record validation']
    schema = json.loads((root / 'docs/work_packages/OUTPUT_SCHEMAS.json').read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = []
    for path in sorted((root / 'docs/records').rglob('*.json')):
        record = json.loads(path.read_text(encoding='utf-8'))
        schema_errors = list(validator.iter_errors(record))
        errors.extend(f'{path.name}: {e.message}' for e in schema_errors)
        if schema_errors:
            continue
        if isinstance(record, dict) and record.get('review_status') == 'accepted':
            errors += evidence_errors(root, record.get('evidence'), path.name)
            for name, expected in record.get('input_hashes', {}).items():
                input_path = local_path(root, name)
                if input_path is None or digest(input_path) != expected:
                    errors.append(path.name + ': missing, unsafe or stale input ' + name)
            if local_path(root, record.get('output_path')) is None:
                errors.append(path.name + ': missing or unsafe accepted output')
            evidence_paths = {x.get('path') for x in record.get('evidence', []) if isinstance(x, dict)}
            if record.get('output_path') not in evidence_paths:
                errors.append(path.name + ': accepted output must be hash-bound in evidence')
        if isinstance(record, dict) and record.get('record_type') == 'claim_audit' and record.get('main_agent_disposition') in {'accepted_as_attributed', 'qualified'}:
            errors += evidence_errors(root, record.get('accepted_evidence'), path.name)
    return errors


def locator_errors(root):
    register = root / 'data/reference/analysis/case-study-2026-10-24/claim_register.csv'
    with register.open(encoding='utf-8', newline='') as stream:
        claims = list(csv.DictReader(stream))
    expected = {part.strip() for c in claims for part in c['evidence'].split(';')}
    mapping = json.loads((root / 'docs/CLAIM_EVIDENCE_MAP.json').read_text(encoding='utf-8'))
    if set(mapping) != expected:
        return ['Claim evidence map must cover every frozen locator exactly']
    return [f'Unresolved claim evidence: {old}' for old, value in mapping.items() if local_path(root, value.get('path')) is None or not value.get('scope')]


def identity_premise_errors(root):
    """Flag documentary drift against the hardcoded historical same-square scenario."""
    spec = json.loads((root / 'docs/IDENTITY_PREMISE.json').read_text(encoding='utf-8'))
    errors = []
    for key, hash_key in [('script', 'script_sha256'), ('documentary_crosswalk', 'crosswalk_sha256')]:
        path = local_path(root, spec.get(key))
        if path is None or digest(path) != spec.get(hash_key):
            errors.append('Identity premise changed: ' + key + '; substantive review required')
    ledger = local_path(root, spec.get('documentary_crosswalk'))
    if ledger is not None:
        with ledger.open(encoding='utf-8', newline='') as stream:
            rows = list(csv.DictReader(stream))
        for label, square in spec['encoded_squares'].items():
            matches = [row for row in rows if row['label'] == label]
            if len(matches) != 1 or matches[0]['sector_B_square_as_reported'] != square:
                errors.append('Historical identity premise disagrees with crosswalk: ' + label)
    return errors
