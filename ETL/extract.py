import requests

from .config import rapid_host, rapid_key
from .load_to_dir import load_files_to_dir

headers = {"x-rapidapi-key": rapid_key, "x-rapidapi-host": rapid_host}

BASE_URL = f"https://{rapid_host}/list/"


def imdb_extract():
    for list_id in range(1, 11):
        try:
            url = f"{BASE_URL}{list_id}"

            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"Invalid movie list_id value {list_id}")
                continue
        except Exception as e:
            print(f"Error fetching {e}")
            raise e

        data = response.json()

        load_to_dir = load_files_to_dir(data, list_id)

    return None
