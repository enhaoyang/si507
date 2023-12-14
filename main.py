import shutil
import time
from pprint import pprint
import json

import constant
from Reddit_get import output_discussion_topics
from TMDb_get import gather_films_extended
from cache import load_cached_movies, add_one_layer_to_json, cache_data_to_json
from Input import start_input, self_input, choice_input, detail_input
from jsonschema import validate, ValidationError
from pieStruct import pie_rating
from treeStruct import print_tree


def main():
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    print("Welcome to the Movie Recommendation System!")
    print("\n" + "*" * width)
    print("Let's begin by setting up your movie preferences.")
    print("*" * width + "\n")
    print("Below are the available movie genres:")
    pprint(constant.genre_id_to_name)

    # User input for genres and years
    genre_ids = start_input(constant.genre_id_to_name)
    years = start_input(constant.year_can_be_get)

    # Choice of movie selection criteria
    chose = input("Would you prefer movies that match all selected genres (1) or any one of them (2)? Enter 1 or 2: ")
    while chose not in ['1', '2']:
        chose = input("Invalid input. Please enter 1 (all genres) or 2 (any genre): ")

    # Gathering movies
    while True:
        movie_data, path = gather_films_extended(years, genre_list=genre_ids, mode=int(chose))
        if movie_data == 0:
            print("Adjusting your preferences for a better match.")
            genre_ids = start_input(constant.genre_id_to_name)
            years = start_input(constant.year_can_be_get)
        else:
            break

    # Processing movie data
    movie_data_final = add_one_layer_to_json(movie_data)
    add_layer_path = self_input("Enter a filename to save the final movie data: ")
    cache_data_to_json(add_layer_path, movie_data_final)

    # Main interactive loop
    while True:
        print("\n" + "*" * width)
        print("Here's a list of recommended movies based on your preferences:\n")
        print(', '.join(movie_data_final.keys()) + '\n')
        print("*" * width)
        print("Choose an option to proceed:")
        print("1. View detailed information about a specific movie.")
        print("2. Explore the rating distribution of the recommended movies.")
        print("3. Discover discussion topics related to a specific movie.")
        print("4. Exit the system.")

        your_choice = choice_input("Your choice: ")
        if your_choice == '1':
            detail_need_movie = detail_input("Enter the movie name(s) to view details: ", movie_data_final)
            print("\nDetailed Movie Information:")
            print("-" * width)
            print_tree(detail_need_movie, movie_data_final)
            time.sleep(3)

        elif your_choice == '2':
            data_rating = load_cached_movies(add_layer_path)
            json_data = json.dumps(data_rating, indent=4)
            pie_rating(json_data)

        elif your_choice == '3':
            movie_topics = detail_input("Enter a movie name to view related discussions: ", movie_data_final)
            output_discussion_topics(movie_topics)
        else:
            print("Thank you for using the Movie Recommendation System. Goodbye!")
            break


if __name__ == '__main__':
    main()