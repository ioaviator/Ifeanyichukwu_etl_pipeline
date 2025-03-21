import os
from pathlib import Path

from dotenv import load_dotenv

parent_dir = Path(__file__).resolve().parent

# Go one level up and then into data_store
data_dir = parent_dir.parent / "data"

data_dir.mkdir(exist_ok=True)

load_dotenv()

rapid_key=os.getenv('RAPID_KEY')
rapid_host=os.getenv('RAPID_HOST')