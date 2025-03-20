
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 'rank', 'series_title', 'released_year', 'certificate', 
# 'runtime', 'genre', 'imdb_rating', 'overview', 
# 'meta_score', 'director', 
# 'star1', 'star2', 'star3', 'star4', 'gross'

class IMDB_1000_Movies(Base):
  __tablename__ = 'imdb_1000_movies'
  __table_args__ = {'extend_existing': True}

  rank = Column(Integer(), primary_key=True)
  series_title = Column(String())
  released_year =  Column(String())
  certificate = Column(String())
  runtime = Column(String())
  genre = Column(String())
  imdb_rating =  Column(Float(3,2))
  overview = Column(String())
  meta_score = Column(Integer())
  director = Column(String())
  star1 =  Column(String())
  star2 = Column(String())
  star3 = Column(String())
  star4 = Column(String())
  gross = Column(Integer())

  def to_dict(self):
    return {c.name: getattr(self, c.name) 
                for c in self.__table__.columns}
