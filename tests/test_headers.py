from scanner.headers import check_headers

def test_check_headers_returns_dict():
    result = check_headers("https://example.com")
    assert isinstance(result, dict)

def test_check_headers_contains_csp():
    result = check_headers("https://example.com")
    assert "Content-Security-Policy" in result

def test_header_result_has_present_key():
    result = check_headers("https://example.com")
    for header, value in result.items():
        if isinstance(value, dict):
            assert "present" in value
