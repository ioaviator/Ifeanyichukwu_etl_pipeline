import json


def load_files_to_dir(data, list_id):
  with open(f'./data/imdb_{list_id}.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'imdb_movie_list_{list_id}.json successfully loaded to folder')

  return True
