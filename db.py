from sqlalchemy import create_engine, MetaData
from config import DATABASE

metadata = MetaData()

db = DATABASE

engine = create_engine(db)



