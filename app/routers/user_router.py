from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import create_user, update_user, delete_user, search_by_id


router = APIRouter(prefix="/users", tags=["Users"]) 

# Register user
@router.post("/register", response_model=UserResponse, status_code = status.HTTP_201_CREATED) # 201 Created for successful creation
def register_user(user: UserCreate, db: Session = Depends(get_db)):
        new_user = create_user(db, user)
        if not new_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exixts") # 409 Conflict for existing user
        return new_user


# Update user
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
            db_user = update_user(db, user_id, user)
            
            if not db_user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") # 404 Not Found for non-existing user
            
            return db_user

# Delete user
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT): # 204 No Content for successful deletion
            
            user_exist = delete_user(db, user_id)
            if not user_exist:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") # 404 Not Found for non-existing user
            
            return {"message": "User deleted successfully"}


# Get user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    search_user = search_by_id(db, user_id)
    if not search_user:
        raise HTTPException(status_code=404, detail="User not found") # 404 Not Found for non-existing user
    
    return search_user