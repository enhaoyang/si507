import os
import json

def load_cached_movies(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file_reader:
            cached_data = json.load(file_reader)
        return cached_data
    else:
        print("No data file found. Please check the path.")
        return None

def cache_data_to_json(file_path, data):
    with open(file_path, 'w') as file_writer:
        json.dump(data, file_writer)
    print("Movie data has been saved to the specified JSON file.")

def add_one_layer_to_json(movies):
    modified_data = {}
    for movie in movies:
        modified_data[movie['title']] = movie
    with open('enhanced_movie_data.json', 'w') as file_writer:
        json.dump(modified_data, file_writer)
    return modified_data

if __name__ == '__main__':
    # Retrieve and display cached movie data
    cached_movies = load_cached_movies('movie_data.json')

    if cached_movies:
        print(json.dumps(cached_movies, indent=2))
    else:
        print("No movie data available in the cache.")
