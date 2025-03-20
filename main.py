
from database.db_setup import get_db
from database.models import Base, IMDB_Movies
from extract import imdb_scrape


def main():
  api_connect = imdb_scrape()



if __name__ == "__main__":
  main()
  db = get_db()
  Base.metadata.create_all(db)