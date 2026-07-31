from sqlalchemy.exc import IntegrityError
from queries import insert_url
from nanoid import generate
import validators
from config import DOMAIN


def create_code(url):
    for _ in range(5):
        code = generate(size=6)

        try:
            insert_url(url, code)
            return code
        except IntegrityError:
            continue

    return None


def validate_url(url):
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    if not validators.url(url):
        return None

    return url


def extract_code(url):
    if DOMAIN in url:
        url = url.removeprefix(DOMAIN + "/")

    return url


def process_url(url):
    clean_url = validate_url(url)

    if not clean_url:
        return None

    code = create_code(clean_url)

    if code is None:
        return None

    short_url = f"{DOMAIN}/{code}"

    return short_url
