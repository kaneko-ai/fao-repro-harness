import json
from pathlib import Path
import pytest

RESULT_PATH = Path("outputs/qc_summary.json")

@pytest.fixture
def qc_summary():
    assert RESULT_PATH.exists(), "qc_summary.json not found"
    return json.loads(RESULT_PATH.read_text())

def test_provenance_hash_present(qc_summary):
    assert len(qc_summary.get("input_sha256", "")) == 64

def test_missing_rate_within_bounds(qc_summary):
    assert qc_summary["missing_rate"] < 0.05

def test_positive_control_and_fdr(qc_summary):
    assert qc_summary["positive_control_passed"] is True
    assert qc_summary["fdr"] < 0.05
