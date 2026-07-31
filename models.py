from db import metadata
from sqlalchemy import Table, Column, String, Integer, DateTime, func, text


table = Table("links", metadata,
              Column("id", Integer, primary_key=True),
              Column("code", String, nullable=False, unique=True),
              Column("original_url", String, nullable=False),
              Column("click_count", Integer, server_default=text("0")),
              Column("created_at", DateTime, nullable=False, server_default=func.now()),
              )

