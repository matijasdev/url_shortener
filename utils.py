from sqlalchemy.exc import IntegrityError
from queries import insert_url
from nanoid import generate
import validators
from config import DOMAIN


def create_code(url: str) -> str|None:
    """
    Generate a random 6 character code and store the URL.

    Returns None if a code can't be created after multiple attempts.
    """
    for _ in range(5):
        code = generate(size=6)

        try:
            insert_url(url, code)
            return code
        except IntegrityError:
            continue

    return None


def validate_url(url: str) -> str|None:
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    if not validators.url(url):
        return None

    return url


def extract_code(url: str) -> str:
    if url.startswith(DOMAIN + "/"):
        url = url.removeprefix(DOMAIN + "/")

    return url


def valid_input_length(user_input: str, max_input_length: int) -> bool:
    return len(user_input) <= max_input_length


def process_url(url: str, max_input_length: int) -> str|None:
    if not valid_input_length(url, max_input_length):
        return None

    clean_url = validate_url(url)

    if clean_url is None:
        return None

    code = create_code(clean_url)

    if code is None:
        return None

    short_url = f"{DOMAIN}/{code}"

    return short_url
