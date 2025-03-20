
from database.db_setup import get_db
from database.models import Base
from extract import imdb_extract
from transform import transform_data


def main():
  try:
    db = get_db()
    Base.metadata.create_all(db)
    print('Database and tables successfully initialized')
    api_connect = imdb_extract()
    transform = transform_data()
  except:
    pass

  return None


if __name__ == "__main__":
  main()
  