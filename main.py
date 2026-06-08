import argparse
from scanner.headers import check_headers
from scanner.ssl_check import check_ssl
from scanner.ai_report import generate_report
from governance.audit_log import log_decision

def scan(url: str):
    print(f"\nScanning: {url}")
    print("━" * 40)

    header_results = check_headers(url)
    ssl_results = check_ssl(url)

    report = generate_report(url, header_results, ssl_results)
    log_decision(url, header_results, ssl_results, report)

    print(report)
    print("━" * 40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Security Auditor")
    parser.add_argument("--url", required=True, help="URL to scan")
    args = parser.parse_args()
    scan(args.url)
