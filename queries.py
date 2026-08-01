from sqlalchemy import insert, select, update
from models import table
from db import engine


def insert_url(url: str, code: str) -> None:
    with engine.begin() as conn:
        conn.execute(insert(table).values(original_url=url, code=code))


def get_original_link(code: str) -> str|None:
    with engine.connect() as conn:
        original_link = conn.execute(select(table.c.original_url).where(table.c.code == code)).scalar_one_or_none()

    return original_link


def increment_click_count(code: str) -> None:
    with engine.begin() as conn:
        conn.execute(update(table).values(click_count=table.c.click_count + 1).where(table.c.code == code))


def get_stats(code: str) -> object|None:
    with engine.connect() as conn:
        result = conn.execute(select(table.c.original_url, table.c.click_count, table.c.created_at).where(table.c.code == code)).one_or_none()

    return result