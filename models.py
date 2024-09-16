from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# the SQLite database
def setup_database():
    engine = create_engine('sqlite:///home_database.db')
    Base.metadata.create_all(engine)