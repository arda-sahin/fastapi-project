from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.database import Base

class UserMovieModel(Base):
    __tablename__ = "user_movies"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Integer, nullable=True)
    review = Column(Text, nullable=True)

