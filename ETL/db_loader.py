
import polars as pl

from .config import data_dir


def load_data(db_engine):
  imdb_movies = pl.read_parquet(f'{data_dir}/processed_data.parquet')

  imdb_movies = imdb_movies.with_columns(
    pl.col("imdb_rating").cast(pl.Float32).alias("imdb_rating"),
    pl.col("meta_score").cast(pl.Int32).alias("meta_score"),
    pl.col("gross").str.replace_all(",", "").cast(pl.Int64).alias("gross")
  )
  

  imdb_movies.write_database('imdb_1000_movies', 
                             connection=db_engine,
                             if_table_exists='replace'
                             )
  print('movie records loaded into database table')
  return None
