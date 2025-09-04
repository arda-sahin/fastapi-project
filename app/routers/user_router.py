from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import create_user, update_user, delete_user, search_by_id


router = APIRouter(prefix="/users", tags=["Users"]) 

# Register user
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
        new_user = create_user(db, user)
        return new_user


# Update user
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
            db_user = update_user(db, user_id, user)
            
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")
            
            return db_user

# Delete user
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
            user_exist = delete_user(db, user_id)
        
            if not user_exist:
                raise HTTPException(status_code=404, detail="User not found")
            
            return {"message": "User deleted successfully"}


# Get user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    search_user = search_by_id(db, user_id)
    if not search_user:
        raise HTTPException(status_code=404, detail="User not found")
    return search_user