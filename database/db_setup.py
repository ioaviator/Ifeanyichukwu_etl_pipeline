from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


def get_db():
    url = f"postgresql://{'postgres'}:{1234}@{'localhost'}:{5433}/{'imdb_100_movies'}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, echo=False)
    return engine

get_db_engine = get_db()

Session = sessionmaker(bind=get_db_engine)
session = Session()