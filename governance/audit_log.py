import json
import os
from datetime import datetime

LOG_FILE = "governance/audit_log.json"

def log_decision(url: str, headers: dict, ssl: dict, report: str):
    """Log every scan for AI auditability (EU AI Act compliance)."""
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "url": url,
        "inputs": {
            "headers": headers,
            "ssl": ssl
        },
        "output": report,
        "model": "placeholder",  # Update in Phase 3
        "tokens_used": None       # Update in Phase 3
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
