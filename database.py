from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_Database = "postgresql://postgres:root@localhost:5432/TodoData"

engine = create_engine(URL_Database)

LocalSession = sessionmaker(bind=engine)

Base = declarative_base()
