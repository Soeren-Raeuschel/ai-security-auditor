from scanner.ssl_check import check_ssl

def test_ssl_valid_site():
    result = check_ssl("https://example.com")
    assert "valid" in result

def test_ssl_returns_expiry_for_valid_site():
    result = check_ssl("https://example.com")
    if result["valid"]:
        assert "expires" in result
        assert "days_remaining" in result
