import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check_headers(url: str) -> dict:
    """Fetch and evaluate security headers for a given URL."""
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        results = {}
        for header in SECURITY_HEADERS:
            results[header] = {
                "present": header in headers,
                "value": headers.get(header, None)
            }
        return results
    except requests.RequestException as e:
        return {"error": str(e)}
