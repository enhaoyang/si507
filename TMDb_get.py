import requests
import constant
from cache import cache_data_to_json as save_to_cache
from Input import self_input as prompt_for_input
# from Input import prompt_json_filename as prompt_for_input
import config

API_KEY_TMDb = config.TMDb_API_KEY


# Retrieve detailed movie information by ID
def obtain_movie_info(movie_reference):
    query_url = f'https://api.themoviedb.org/3/movie/{movie_reference}'
    parameters = {
        'api_key': API_KEY_TMDb,
        'append_to_response': 'credits',
    }
    result = requests.get(query_url, params=parameters)
    return result.json()


# Acquire a list of movies filtered by year and genre
def acquire_films(page_number=1, release_year=None, genre_list=None, order_by='popularity.desc'):
    query_url = 'https://api.themoviedb.org/3/discover/movie'
    parameters = {
        'api_key': API_KEY_TMDb,
        'page': page_number,
        'sort_by': order_by,
    }

    if release_year:
        parameters['primary_release_year'] = release_year

    if genre_list:
        parameters['with_genres'] = ','.join(str(genre) for genre in genre_list)

    result = requests.get(query_url, params=parameters)
    films_found = result.json()['results']
    collected_data = []
    for film in films_found:
        info = obtain_movie_info(film['id'])
        film['cast'] = [actor['name'] for actor in info['credits']['cast']]
        film['filmmakers'] = [crew_member['name'] for crew_member in info['credits']['crew'] if
                              crew_member['job'] == 'Director']
        film['categories'] = [constant.genre_id_to_name[genre] for genre in film['genre_ids']]
        try:
            film_details = {
                'id': film['id'],
                'title': film['title'],
                'release_year': release_year,
                'categories': film['categories'],
                'cast': film['cast'][:5],
                'filmmakers': film['filmmakers'][0],
                'synopsis': film['overview'],
                'fame': film['popularity'],
                'rating': film['vote_average'],
                'votes': film['vote_count']
            }
            collected_data.append(film_details)
        except:
            continue
    return collected_data


def gather_films_extended(periods, genre_list=None, mode=1):
    compiled_data = []

    if mode == 1:
        for period in periods:
            print(f"Retrieving films from {period}...")
            film_selection = acquire_films(release_year=period, genre_list=genre_list)
    if mode == 2:
        for period in periods:
            print(f"Retrieving films from {period}...")
            for category in genre_list:
                print(f"Looking for films in {category}...")
                film_selection = acquire_films(release_year=period, genre_list=genre_list)

    if len(film_selection) <= 6:
        print('The criteria provided is too restrictive. Try broadening the year range or genre selection.')
        return 0, None

    file_name = prompt_for_input(
        "The necessary data will be fetched and stored in a JSON file. The default file is 'movie_data.json'. "
        "Would you like to assign a new file name? If yes, type it in; otherwise, reply with 'None': ")
    save_to_cache(file_name, film_selection)

    return film_selection, file_name

