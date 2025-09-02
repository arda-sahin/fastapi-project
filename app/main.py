from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User as UserModel, Base
from app.schemas import UserCreate, userUpdate, UserResponse
from typing import List
from typing import Optional


app = FastAPI()

def get_db():
    db = SessionLocal()  # create a new database session
    try:
        yield db # provide the session to the endpoint
    finally:
        db.close() # close the session after the request is done


# POST endpoint to register a new user
@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(db_user)  # add new user
    db.commit()      # save to database
    db.refresh(db_user)  # get the updated user with ID
    return db_user


# PUT endpoint to update an existing user
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: userUpdate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.email = user.email
    db_user.password = user.password
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


# DELETE endpoint to delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


# GET endpoint to search for users by id, username, or email
@app.get("/users/search", response_model=List[UserResponse])
def get_users(
    user_id: Optional[int] = Query(None, description="Filter by user ID"),
    username: Optional[str] = Query(None, description="Filter by username"),
    email: Optional[str] = Query(None, description="Filter by email"),
    db: Session = Depends(get_db)
):
    query = db.query(UserModel)

    if user_id is not None:
        query = query.filter(UserModel.id == user_id)
    elif email is not None:
        query = query.filter(UserModel.email == email)
    elif username is not None:
        query = query.filter(UserModel.username == username)
    else:
        raise HTTPException(status_code=400, detail="At least one query parameter (user_id, username, email) must be provided")
    
    if not query.first():
        raise HTTPException(status_code=404, detail="User not found")
    
    users = query.all()
    return users


