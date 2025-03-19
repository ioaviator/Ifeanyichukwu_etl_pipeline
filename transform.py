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
  df_list = [load_json_with_polars(file) for file in json_files]

  # print(df_list)
  # Concatenate all JSON DataFrames into one
  combined_json = pl.concat(df_list)

  combined_json = combined_json.rename({col: col.lower() for col in combined_json.columns})

  # Verify changes
  print(combined_json.columns)

transform()