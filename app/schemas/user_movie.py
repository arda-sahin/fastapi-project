from pydantic import BaseModel

class UserMovieCreate(BaseModel):
    user_id: int
    movie_id: int
    rating: int | None = None
    review: str | None = None

class UserMovieUpdate(BaseModel):
    rating: int | None = None
    review: str | None = None

class UserMovieResponse(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: int | None = None
    review: str | None = None

class Config:
    from_attributes = True
