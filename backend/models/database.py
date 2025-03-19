from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base  # NEW (SQLAlchemy 2.0)
import os
Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/child_recovery_db")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for all tables
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
