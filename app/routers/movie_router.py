from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from app.services.movie_service import create_movie, get_movie_by_id, update_movie, delete_movie, get_all_movies
from typing import List

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=MovieCreate, status_code=status.HTTP_201_CREATED)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = create_movie(db, movie)
    return new_movie


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return movie


@router.put("/{movie_id}", response_model=MovieResponse)
def edit_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    updated_movie = update_movie(db, movie_id, movie)
    if not updated_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return updated_movie

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_movie(movie_id: int, db: Session = Depends(get_db)):
    del_movie = delete_movie(db, movie_id)
    if not del_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    return {"Movie deleted successfully"}


@router.get("/", response_model=list[MovieResponse])
def list_movies(db: Session = Depends(get_db)):
    movies = get_all_movies(db)
    return movies
