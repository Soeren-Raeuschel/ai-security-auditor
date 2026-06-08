# Placeholder for LLM-generated report (Phase 3)
# Will integrate Groq / Claude API

def generate_report(url: str, headers: dict, ssl: dict) -> str:
    """Generate a security report. LLM integration coming in Phase 3."""
    issues = [h for h, v in headers.items() if isinstance(v, dict) and not v.get("present")]
    ssl_status = "✓ Valid" if ssl.get("valid") else f"✗ Invalid ({ssl.get('error', '')})"

    report = f"\nSSL Certificate: {ssl_status}\n"
    if ssl.get("days_remaining"):
        report += f"  Expires in {ssl['days_remaining']} days\n"

    report += "\nSecurity Headers:\n"
    for header, result in headers.items():
        if isinstance(result, dict):
            status = "✓" if result["present"] else "✗"
            report += f"  [{status}] {header}\n"

    if issues:
        report += f"\n⚠ {len(issues)} missing header(s) detected.\n"
    else:
        report += "\n✓ All security headers present.\n"

    return report
