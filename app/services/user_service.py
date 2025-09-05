from sqlalchemy.orm import Session
from app.db.models.user import UserModel
from app.schemas.user import UserCreate, UserUpdate

# Create user for POST /register
def create_user(db: Session, user: UserCreate):
    # Check if user with same username or email already exists
    existing_user = db.query(UserModel).filter((UserModel.username == user.username) | (UserModel.email == user.email)).first()
    if existing_user:
        return None
    
    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Update user for PUT /{user_id}
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return None

    db_user.email = user.email
    db_user.password = user.password
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


# Delete user for DELETE /{user_id}
def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return False

    db.delete(db_user)
    db.commit()
    return True


# Search user by ID for GET /{user_id}
def search_by_id(db: Session, user_id: int):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return None
    
    return user
