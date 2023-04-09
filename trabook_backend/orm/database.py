from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# Replace these values with your PostgreSQL connection details

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres@localhost:5433/trabook"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
