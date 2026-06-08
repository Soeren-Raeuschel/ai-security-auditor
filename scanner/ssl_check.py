import ssl
import socket
from datetime import datetime

def check_ssl(url: str) -> dict:
    """Check SSL certificate validity for a given URL."""
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                return {
                    "valid": True,
                    "expires": expiry.strftime("%Y-%m-%d"),
                    "days_remaining": (expiry - datetime.utcnow()).days
                }
    except Exception as e:
        return {"valid": False, "error": str(e)}
