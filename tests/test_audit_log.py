import json
import os
from governance.audit_log import log_decision

def test_log_creates_entry(tmp_path, monkeypatch):
    log_file = tmp_path / "audit_log.json"
    monkeypatch.setattr("governance.audit_log.LOG_FILE", str(log_file))

    log_decision("https://example.com", {}, {}, "test report")

    with open(log_file) as f:
        logs = json.load(f)

    assert len(logs) == 1
    assert logs[0]["url"] == "https://example.com"
