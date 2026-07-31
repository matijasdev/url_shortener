from sqlalchemy import create_engine, MetaData

metadata = MetaData()

db = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

engine = create_engine(db)



