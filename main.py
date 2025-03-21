
from database.db_setup import db_engine, get_db
from database.models import Base
from ETL.db_loader import load_data
from ETL.extract import imdb_extract
from ETL.transform import transform_data


def main():
  try:
    # api_connect = imdb_extract()
    transform = transform_data()
    # proceed to next step if all json records were extracted from api
    if transform:
      db = get_db()
      Base.metadata.create_all(db)
      print('Database and tables successfully initialized')
      load = load_data(db_engine)
  except:
    pass

  return None


if __name__ == "__main__":
  main()
  