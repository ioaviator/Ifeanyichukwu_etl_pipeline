import os
from pathlib import Path

from dotenv import load_dotenv

parent_dir = Path(__file__).resolve().parent

# Go one level up and then into data_store
data_folder = parent_dir.parent / "data"

# Build the path to the 'data' folder relative to this file
# data_folder = os.path.join(os.path.dirname(__file__), 'data')

load_dotenv()

rapid_key=os.getenv('RAPID_KEY')
rapid_host=os.getenv('RAPID_HOST')