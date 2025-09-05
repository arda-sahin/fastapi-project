from sqlalchemy import Column, Integer, String
from app.db.database import Base

class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String, nullable=False)
    