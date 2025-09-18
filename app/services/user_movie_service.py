from sqlalchemy.orm import Session
from app.models.user_movie import UserMovieModel
from app.schemas.user_movie import UserMovieCreate, UserMovieUpdate


def add_user_movie(db: Session, user_movie: UserMovieCreate):
    new_user_movie = UserMovieModel(
        user_id=user_movie.user_id,
        movie_id=user_movie.movie_id,
        rating=user_movie.rating,
        review=user_movie.review
    )
    db.add(new_user_movie)
    db.commit()
    db.refresh(new_user_movie)
    return new_user_movie


def update_user_movie(db: Session, user_movie_id: int, user_movie: UserMovieUpdate):
    db_user_movie = db.query(UserMovieModel).filter(UserMovieModel.id == user_movie_id).first()
    if not db_user_movie:
        return None

    db_user_movie.rating = user_movie.rating
    db_user_movie.review = user_movie.review
    db.commit()
    db.refresh(db_user_movie)
    return db_user_movie


def delete_user_movie(db: Session, user_movie_id: int):
    db_user_movie = db.query(UserMovieModel).filter(UserMovieModel.id == user_movie_id).first()
    if not db_user_movie:
        return False

    db.delete(db_user_movie)
    db.commit()
    return True


def get_user_movies(db: Session, user_id: int):
    return db.query(UserMovieModel).filter(UserMovieModel.user_id == user_id).all()