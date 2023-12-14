import functools
import re
import constant

# Decorator for validating JSON file name input
def check_json_filename(func):
    @functools.wraps(func)
    def filename_wrapper(*args, **kwargs):
        filename = func(*args, **kwargs)
        while True:
            if filename.lower() == 'none':
                return 'default_movie_data.json'
            elif re.match(r'^[\w_-]+\.json$', filename):
                return filename
            else:
                filename = input("Invalid input. Enter a JSON file name or 'None' for default (movie_data.json): ")

    return filename_wrapper

# Decorator for validating input based on given options
def check_option_input(func):
    @functools.wraps(func)
    def option_wrapper(*args, **kwargs):
        user_selection = func(*args, **kwargs)
        while True:
            available_options = set(args[0]) if isinstance(args[0], list) else set(map(str, args[0].keys()))
            if user_selection.issubset(available_options):
                return list(user_selection)
            else:
                user_selection = set(input(f"Invalid input: {user_selection - available_options}. Please enter valid options: ").split())

    return option_wrapper

# Decorator for validating numeric choice within a range
def check_numeric_choice(func):
    @functools.wraps(func)
    def numeric_choice_wrapper(*args, **kwargs):
        choice = func(*args, **kwargs)
        while True:
            if choice.isdigit() and int(choice) in range(1, 6):
                return choice
            else:
                choice = input("Invalid choice. Please enter a number between 1 and 5: ")

    return numeric_choice_wrapper

# Decorator for validating detailed input against a list
def check_detailed_input(func):
    @functools.wraps(func)
    def detailed_input_wrapper(*args, **kwargs):
        details = func(*args, **kwargs)
        valid_items = set(args[1].keys())
        while True:
            details_set = set(details.split(","))
            if details_set.issubset(valid_items):
                return details.split(",")
            else:
                details = input("Invalid movie names. Enter valid names separated by commas: ")

    return detailed_input_wrapper

# Function to get user input for JSON filename
@check_json_filename
def self_input(prompt):
    return input(prompt)

# Function to get user input for start criteria
@check_option_input
def start_input(database=None):
    prompt_message = "Enter genre codes separated by spaces: " if isinstance(database, dict) else "Enter movie years separated by spaces: "
    return set(input(prompt_message).split())

# Function to get user choice input
@check_numeric_choice
def choice_input(prompt):
    return input(prompt)

# Function to get user input for movie details
@check_detailed_input
def detail_input(prompt, recommendation_data):
    return input(prompt)
