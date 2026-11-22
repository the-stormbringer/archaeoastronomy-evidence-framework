"""Failure-mode tests: tolerances must not conceal missing data or changed claims."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from repository import compare_table, integrity_errors, state_errors, markdown_link_errors


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        self.reference = self.directory / "reference.csv"
        self.generated = self.directory / "generated.csv"
        self.reference.write_text("label,origin_constrained_TLS_deg,mean\nA,10.0,12.0\n", encoding="utf-8")
        self.rule = {"file": "estimand.csv", "columns": ["origin_constrained_TLS_deg"], "absolute_degrees": 1e-10}

    def compare(self, text=None, file="estimand.csv"):
        if text is not None:
            self.generated.write_text(text, encoding="utf-8")
        return compare_table(self.reference, self.generated, file, self.rule)

    def test_missing_output_fails(self):
        self.assertFalse(self.compare()["agreement"])

    def test_only_allowed_float_field_can_differ(self):
        result = self.compare("label,origin_constrained_TLS_deg,mean\nA,10.000000000001,12.0\n")
        self.assertTrue(result["agreement"])
        self.assertFalse(result["byte_identical"])

    def test_tolerance_does_not_apply_to_other_field(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\nA,10.0,12.000000000001\n")["agreement"])

    def test_tolerance_does_not_apply_to_other_table(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\nA,10.000000000001,12.0\n", "other.csv")["agreement"])

    def test_out_of_tolerance_fails(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\nA,10.001,12.0\n")["agreement"])

    def test_nonfinite_value_fails(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\nA,nan,12.0\n")["agreement"])

    def test_missing_row_fails(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\n")["agreement"])

    def test_changed_identity_fails(self):
        self.assertFalse(self.compare("label,origin_constrained_TLS_deg,mean\nB,10.0,12.0\n")["agreement"])


class RepositoryTests(unittest.TestCase):
    def test_locked_pipeline_intact(self):
        self.assertEqual(integrity_errors(), [])

    def test_current_state_targets_and_dependencies(self):
        self.assertEqual(state_errors(), [])

    def test_portable_markdown_links(self):
        self.assertEqual(markdown_link_errors(), [])


if __name__ == "__main__":
    unittest.main()
