from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db():
    db = SessionLocal()  # create a new database session
    try:
        yield db # provide the session to the endpoint
    finally:
        db.close() # close the session after the request is done
