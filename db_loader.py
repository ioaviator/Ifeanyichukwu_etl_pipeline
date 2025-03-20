import os

import polars as pl

from database.db_setup import get_db_engine

# Build the path to the 'data' folder relative to this file
data_folder = os.path.join(os.path.dirname(__file__), 'data')

def load_data():
  imdb_movies = pl.read_parquet(f'{data_folder}/processed_data.parquet')

  imdb_movies.write_database('imdb_1000_movies', 
                             connection=get_db_engine,
                             if_table_exists='replace'
                             )
  return None

load_data()