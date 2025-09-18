from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title: str
    director: str
    year: int

class MovieResponse(BaseModel):
    id: int
    title: str
    director: str
    year: int

class Config:
    from_attributes = True
