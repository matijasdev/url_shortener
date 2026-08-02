from utils import extract_code, validate_url, valid_input_length
from config import DOMAIN, MAX_INPUT_LENGTH


def test_extract_code_from_shortener_url():
    url = f"{DOMAIN}/code"

    result = extract_code(url)

    assert result == "code"


def test_extract_code_without_domain_returns_original_value():
    user_input = "website"

    result = extract_code(user_input)

    assert result == user_input


def test_validate_url_accepts_valid_url():
    url = "https://website.com"

    result = validate_url(url)

    assert result == url



def test_validate_url_adds_missing_https():
    url = "website.com"

    result = validate_url(url)

    assert result == f"https://{url}"



def test_validate_url_rejects_invalid_url():
    user_input = "not a website"

    result = validate_url(user_input)

    assert result is None



def test_valid_input_length_accepts_max_length():
    user_input = "a" * MAX_INPUT_LENGTH

    result = valid_input_length(user_input, MAX_INPUT_LENGTH)

    assert result is True



def test_valid_input_length_rejects_over_max_length():
    user_input = "a" * (MAX_INPUT_LENGTH + 1)

    result = valid_input_length(user_input, MAX_INPUT_LENGTH)

    assert result is False