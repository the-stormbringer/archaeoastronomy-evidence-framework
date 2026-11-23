"""Adversarial controls: false closure and malformed contracts must fail."""
from pathlib import Path
import copy
import os
import subprocess
from unittest.mock import patch
import hashlib
import json
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from repository import ROOT, load_pipeline, contract_errors
from governance import governance_errors, receipt_errors, record_errors, locator_errors, identity_premise_errors
from jsonschema import Draft202012Validator


class ContractTests(unittest.TestCase):
    def test_valid_contract(self):
        self.assertEqual(contract_errors(load_pipeline()), [])

    def test_duplicates_fail_even_with_changed_hash_inventory(self):
        c = load_pipeline(); c['execution_order'][1] = c['execution_order'][0]
        c['sha256'].pop('analysis/geometry_sensitivity.py')
        self.assertTrue(contract_errors(c))

    def test_escape_and_absolute_staging_fail(self):
        for value in ['/tmp/escape', '../escape', 'elsewhere']:
            c = load_pipeline(); c['staged_input_directory'] = value
            self.assertTrue(contract_errors(c))

    def test_nonfinite_or_broadened_tolerance_fails(self):
        for value in [float('inf'), float('nan'), -1, 1e-3]:
            c = load_pipeline(); c['tolerance']['absolute_degrees'] = value
            self.assertTrue(contract_errors(c))
        c = load_pipeline(); c['tolerance']['columns'].append('arithmetic_radial_mean_deg')
        self.assertTrue(contract_errors(c))


class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'docs', self.root / 'docs')
        shutil.copytree(ROOT / 'data', self.root / 'data')
        shutil.copytree(ROOT / 'analysis', self.root / 'analysis')

    def mutate(self, field, operation):
        p = self.root / field; d = json.loads(p.read_text()); operation(d)
        p.write_text(json.dumps(d))

    def test_baseline_valid(self):
        self.assertEqual(governance_errors(self.root), [])
        self.assertEqual(record_errors(self.root), [])
        self.assertEqual(locator_errors(self.root), [])

    def test_invented_status_rejected(self):
        self.mutate('docs/PROJECT_STATE.json', lambda d: d['workplan'][1].update(status='invented'))
        self.assertTrue(governance_errors(self.root))

    def test_unreceipted_completion_rejected(self):
        self.mutate('docs/PROJECT_STATE.json', lambda d: d['workplan'][1].update(status='complete'))
        self.assertTrue(governance_errors(self.root))

    def test_unknown_objective_dependency_rejected(self):
        self.mutate('docs/PROJECT_STATE.json', lambda d: d['tasks'][0].update(depends_on=['unknown']))
        self.assertTrue(governance_errors(self.root))

    def test_deleted_required_stage_or_task_edge_rejected(self):
        self.mutate('docs/PROJECT_STATE.json', lambda d: d['workplan'][4].update(depends_on=[]))
        self.assertTrue(governance_errors(self.root))
        self.mutate('docs/work_packages/WORK_QUEUE.json', lambda d: d['tasks'][6].update(depends_on=[]))
        self.assertTrue(governance_errors(self.root))

    def test_accepted_record_requires_real_inputs_and_hash_bound_output(self):
        evidence_path = 'docs/PROJECT_PLAN.md'
        record = {'record_type':'experiment_result', 'experiment':'E1', 'scenario_id':'test', 'protocol_version':'v1',
                  'input_hashes':{'does-not-exist.csv':'a'*64}, 'source_version':'v1', 'membership':'declared',
                  'complete':False, 'method':'none', 'result_scope':'source_interpretation', 'outcome':'uncomputable',
                  'output_path':'missing.md', 'review_status':'accepted', 'reviewer':'main agent',
                  'interpretation':'Input unavailable', 'evidence':[{'path':evidence_path,
                  'sha256':hashlib.sha256((self.root/evidence_path).read_bytes()).hexdigest()}]}
        p = self.root/'docs/records/test.json'; p.write_text(json.dumps(record))
        errors = record_errors(self.root)
        self.assertTrue(any('input' in x for x in errors))
        self.assertTrue(any('output' in x for x in errors))
        record['input_hashes'] = {evidence_path:'a'*64}; p.write_text(json.dumps(record))
        self.assertTrue(any('stale input' in x for x in record_errors(self.root)))
        record['input_hashes'] = {evidence_path:record['evidence'][0]['sha256']}
        record['output_path'] = evidence_path; p.write_text(json.dumps(record))
        self.assertEqual(record_errors(self.root), [])

    def test_queue_cycle_rejected(self):
        self.mutate('docs/work_packages/WORK_QUEUE.json', lambda d: d['tasks'][0].update(depends_on=['E1']))
        self.assertTrue(governance_errors(self.root))

    def test_stale_acceptance_evidence_rejected(self):
        p = self.root / 'docs/PROJECT_PLAN.md'; p.write_text(p.read_text() + '\nchanged\n')
        self.assertTrue(governance_errors(self.root))

    def test_valid_receipt_does_not_bypass_pending_dependencies(self):
        p = self.root / 'docs/acceptance/W0.json'; receipt = json.loads(p.read_text()); receipt['id'] = 'W2'
        (self.root / 'docs/acceptance/W2.json').write_text(json.dumps(receipt))
        self.mutate('docs/PROJECT_STATE.json', lambda d: d['workplan'][2].update(status='complete', acceptance_record='docs/acceptance/W2.json'))
        self.assertTrue(governance_errors(self.root))

    def test_reasoned_omission_is_permitted_only_for_conditional_branches(self):
        receipt = json.loads((self.root / 'docs/acceptance/W0.json').read_text()); receipt.update(id='E5', decision='omitted_with_reason')
        (self.root / 'docs/acceptance/E5.json').write_text(json.dumps(receipt))
        self.assertEqual(receipt_errors(self.root, 'docs/acceptance/E5.json', 'E5'), [])
        receipt['id'] = 'E1'; (self.root / 'docs/acceptance/E1.json').write_text(json.dumps(receipt))
        self.assertTrue(receipt_errors(self.root, 'docs/acceptance/E1.json', 'E1'))

    def test_nested_records_cannot_escape_validation(self):
        folder = self.root/'docs/records/nested'; folder.mkdir()
        (folder/'bad.json').write_text('{"nonsense":true}')
        self.assertTrue(record_errors(self.root))

    def test_corrected_crosswalk_cannot_silently_reuse_historical_identity_claim(self):
        self.assertEqual(identity_premise_errors(self.root), [])
        spec = json.loads((self.root/'docs/IDENTITY_PREMISE.json').read_text())
        path = self.root/spec['documentary_crosswalk']
        path.write_text(path.read_text().replace('A-4,r/20,', 'A-4,s/20,'))
        self.assertTrue(identity_premise_errors(self.root))
        spec['crosswalk_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        (self.root/'docs/IDENTITY_PREMISE.json').write_text(json.dumps(spec))
        self.assertTrue(any('disagrees' in error for error in identity_premise_errors(self.root)))

    def test_claim_locator_missing_target_rejected(self):
        self.mutate('docs/CLAIM_EVIDENCE_MAP.json', lambda d: next(iter(d.values())).update(path='missing.md'))
        self.assertTrue(locator_errors(self.root))


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.validator = Draft202012Validator(json.loads((ROOT / 'docs/work_packages/OUTPUT_SCHEMAS.json').read_text()))
        self.record = {'record_type':'experiment_result', 'experiment':'E1', 'scenario_id':'test', 'protocol_version':'v1',
                       'input_hashes':{'data/source/example.csv':'a'*64}, 'source_version':'v1', 'membership':'declared',
                       'complete':False, 'method':'none', 'result_scope':'source_interpretation', 'outcome':'uncomputable',
                       'output_path':'docs/evidence/decision.md', 'review_status':'pending'}

    def test_arbitrary_root_rejected(self):
        self.assertFalse(self.validator.is_valid({'nonsense':True}))

    def test_provisional_uncomputable_is_valid(self):
        self.assertTrue(self.validator.is_valid(self.record))

    def test_empty_hashes_rejected(self):
        self.record['input_hashes'] = {}; self.assertFalse(self.validator.is_valid(self.record))

    def test_accepted_requires_review_evidence(self):
        self.record['review_status'] = 'accepted'; self.assertFalse(self.validator.is_valid(self.record))

    def test_accepted_uncomputable_is_not_forbidden(self):
        self.record.update(review_status='accepted', reviewer='main agent', interpretation='Unavailable input bounds the result',
                           evidence=[{'path':'docs/evidence/decision.md','sha256':'a'*64}])
        self.assertTrue(self.validator.is_valid(self.record))


class ExecutionEnvironmentTests(unittest.TestCase):
    def test_inherited_optimization_cannot_disable_child_assertions(self):
        from reproduce import child_environment
        with patch.dict(os.environ, {'PYTHONOPTIMIZE':'1'}):
            environment = child_environment()
            result = subprocess.run([sys.executable, '-c', 'print(__debug__)'],
                                    env=environment, capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout.strip(), 'True')
        self.assertNotIn('PYTHONOPTIMIZE', environment)


if __name__ == '__main__':
    unittest.main()
