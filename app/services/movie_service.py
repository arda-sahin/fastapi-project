from sqlalchemy.orm import Session
from app.db.models.movie import MovieModel
from app.schemas.movie import MovieCreate, MovieUpdate

def create_movie(db: Session, movie: MovieCreate):
    new_movie = MovieModel(title=movie.title, director=movie.director, year=movie.year)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(MovieModel).filter(MovieModel.id == movie_id).first()


def update_movie(db: Session, movie_id: int, movie: MovieUpdate):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not db_movie:
        return None
    db_movie.title = movie.title
    db_movie.director = movie.director
    db_movie.year = movie.year
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    del_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not del_movie:
        return False
    db.delete(del_movie)
    db.commit()
    return True

def get_all_movies(db: Session):
    return db.query(MovieModel).all()