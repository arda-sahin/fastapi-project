from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from models import User as UserModel, Base

app = FastAPI()

def get_db():
    db = SessionLocal()  # create a new database session
    try:
        yield db # provide the session to the endpoint
    finally:
        db.close() # close the session after the request is done


class User(BaseModel):
    username: str
    email: str
    password: str

# POST endpoint to register a new user
@app.post("/register")
def register_user(user: User, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(db_user)  # add new user
    db.commit()      # save to database
    db.refresh(db_user)  # get the updated user with ID
    return db_user


# PUT endpoint to update an existing user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return {"error": "User not found"}

    db_user.email = user.email
    db_user.password = user.password
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


# DELETE endpoint to delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).one_or_none()
    if not db_user:
        return {"error": "User not found"}
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


# Simple GET endpoint
@app.get("/")
def get_method():
    return {"HELLO"}


