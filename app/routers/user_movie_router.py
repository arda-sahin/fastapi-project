from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user_movie import UserMovieCreate, UserMovieUpdate, UserMovieResponse
from app.services.user_movie_service import add_user_movie, update_user_movie, delete_user_movie, get_user_movies
from typing import List

router = APIRouter(prefix="/user-movies", tags=["UserMovies"])

@router.post("/", response_model=UserMovieResponse, status_code=status.HTTP_201_CREATED)
def create_user_movie(user_movie: UserMovieCreate, db: Session = Depends(get_db)):
    new_user_movie = add_user_movie(db, user_movie)
    return new_user_movie


@router.put("/{user_movie_id}", response_model=UserMovieResponse)
def edit_user_movie(user_movie_id: int, user_movie: UserMovieUpdate, db: Session = Depends(get_db)):
    updated_user_movie = update_user_movie(db, user_movie_id, user_movie)
    if not updated_user_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return updated_user_movie


@router.delete("/{user_movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_user_movie(user_movie_id: int, db: Session = Depends(get_db)):
    del_user_movie = delete_user_movie(db, user_movie_id)
    if not del_user_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return {"Movie deleted successfully"}


@router.get("/user/{user_id}", response_model=List[UserMovieResponse])
def list_user_movies(user_id: int, db: Session = Depends(get_db)):
    user_movies = get_user_movies(db, user_id)
    return user_movies

