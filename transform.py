import glob
import json
import os

import polars as pl

# Build the path to the 'data' folder relative to this file
data_folder = os.path.join(os.path.dirname(__file__), 'data')

# Get all JSON files in the folder
json_files = glob.glob(os.path.join(data_folder, '*.json'))


def load_json_with_polars(file_path):
  with open(file_path, 'r', encoding="utf-8") as f:
    data = json.load(f)
  # Extract the 'result' list and convert it into a Polars DataFrame
  return pl.DataFrame(data.get("result", []))

def transform():
  # Use list comprehension to load each file into a DataFrame
  movies_list_df = [load_json_with_polars(file) for file in json_files]

  # Concatenate all JSON DataFrames into one
  combined_json = pl.concat(movies_list_df)
  # Rename columns to lowercase
  combined_json = combined_json.rename({col: col.lower() for col in combined_json.columns})

  #Drop unwanted columns
  combined_json = combined_json.drop(['poster_link','no_of_votes'])
  
  # Verify changes
  # print(combined_json.columns)

  # Drop duplicate values
  combined_json = combined_json.unique()

  # Handle missing values in columns
  combined_json = combined_json.with_columns([
    pl.col("meta_score").fill_null(0),
    pl.col('certificate').fill_null('Unspecified'),
    pl.col('gross').fill_null(0)
])
  # tt = combined_json.to_pandas()
  
  # Load dataframe to parquet file
  combined_json.write_parquet(f'{data_folder}/processed_data.parquet')
  


transform()