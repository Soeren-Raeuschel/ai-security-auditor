# 🔐 AI Security Auditor

> An automated web security analysis tool powered by AI — combining OWASP-based checks, LLM-generated reports, and EU AI Act compliance documentation.

---

## 🚀 What it does

AI Security Auditor scans a given URL and automatically:

- Analyzes HTTP security headers (CSP, HSTS, X-Frame-Options, etc.)
- Validates SSL/TLS certificate status
- Generates a human-readable security report using an LLM
- Logs all AI decisions for auditability (EU AI Act compliance)
- Measures resource efficiency (Green Coding — token usage, scan duration)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **requests** — HTTP analysis
- **ssl** — Certificate validation
- **pytest** — Automated testing
- **GitHub Actions** — CI/CD pipeline
- **Groq API / Claude API** — LLM-powered report generation

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-security-auditor.git
cd ai-security-auditor

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py --url https://example.com
```

**Example output:**
```
Scanning: https://example.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[✓] SSL Certificate: Valid
[✗] Content-Security-Policy: Missing
[✗] HSTS: Missing
[✓] X-Frame-Options: Present

AI Report: 2 critical issues found. Recommend adding CSP and HSTS headers immediately...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scan duration: 1.32s | API tokens used: 214
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

Tests cover header analysis logic, SSL checks, and LLM output consistency.

---

## ⚖️ AI Governance

This project was built with EU AI Act compliance in mind:

- **Risk classification:** Minimal risk (informational tool, no automated decisions affecting individuals)
- **Auditability:** All LLM inputs and outputs are logged to `audit_log.json`
- **Consistency:** Automated tests verify that identical inputs produce equivalent outputs
- **Transparency:** Model, prompt version, and token usage are recorded per scan

See [`docs/governance.md`](docs/governance.md) for the full AI governance documentation.

---

## 🌱 Green Coding

Resource efficiency is tracked on every scan:

- Scan duration logged per run
- API token usage minimized through prompt optimization
- Carbon footprint estimated using the [GSF Software Carbon Intensity specification](https://sci.greensoftware.foundation/)

---

## 📁 Project Structure

```
ai-security-auditor/
├── main.py              # Entry point
├── scanner/
│   ├── headers.py       # HTTP header analysis
│   ├── ssl_check.py     # SSL/TLS validation
│   └── ai_report.py     # LLM report generation
├── governance/
│   ├── audit_log.json   # AI decision log
│   └── governance.md    # EU AI Act documentation
├── tests/
│   └── test_scanner.py  # pytest test suite
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

- [x] HTTP header analysis
- [ ] SSL certificate validation
- [ ] LLM-generated reports
- [ ] pytest test suite + GitHub Actions CI
- [ ] AI audit logging
- [ ] Green Coding metrics
- [ ] Web UI

---

## 👤 Author

**Sören**
Computer Science Student | Werkstudent in Quality Management
[GitHub](https://github.com/yourusername) · [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

MIT License — feel free to use and adapt.
