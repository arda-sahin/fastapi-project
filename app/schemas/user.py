from pydantic import BaseModel, EmailStr

# Schemas for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr # EmailStr for email validation
    password: str

# Schemas for user update
class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schemas for user response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
