from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./shelfsense.db"

# object that knows how to talk to the db
# This creates engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# unit used to interact with the DB in app code
# This creates session instances
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# parent class ORM models inheret from
class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
