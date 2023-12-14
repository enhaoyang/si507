# Movie Recommendation System

## Overview
This Personalized Movie Recommendation System leverages the TMDb and Reddit APIs to deliver a comprehensive movie exploration experience. Written in Python, it allows users to input their preferences and receive tailored movie suggestions, complete with detailed information, ratings distribution, discussion topics, and graphical representations of similar movies.

## Features
- **Customized Movie Recommendations**: Users can specify their preferences based on genres and release years. The system uses these preferences to fetch a curated list of movies.
- **Detailed Movie Information**: For each recommended movie, the system provides an in-depth tree structure display of movie details.
- **Ratings Distribution Visualization**: A pie chart representation shows the distribution of ratings for the recommended movies, giving users an overview of the overall ratings landscape.
- **Similar Movie Recommendations**: The system generates a graphical representation of similar movies based on user-selected titles, making it easier to find movies with similar themes or styles.
- **Discussion Topics Fetching**: Users can view relevant discussion topics or threads from Reddit for any selected movie, enhancing their understanding of public perception and opinions about the film.

## How to Use
1. **Start the System**: Run the `main.py` script to initiate the system.
2. **Enter Preferences**: Input your preferred movie genres and release years.
3. **Explore Recommendations**: Browse through the list of recommended movies based on your input.
4. **Select an Option**: Choose to view detailed information, ratings distribution, discussion topics, or similar movies.
5. **View Graphical Representations**: Explore pie charts for ratings and graphs for similar movies.
6. **Participate in Discussions**: Access and read movie-related discussions from Reddit.

## Modules and External APIs
- **TMDb API**: Used for fetching movie details based on user preferences.
- **Reddit API**: Provides access to movie-related discussions and threads.
- **Graphical Representation**: Utilizes `plotly` and `networkx` for generating interactive charts and graphs.
- **Data Handling**: Custom modules like `cache`, `Input`, and `graphStruct` are used for data processing and user input handling.

## Requirements
- Python 3.x
- External libraries: `shutil`, `time`, `jsonschema`, `plotly`, `networkx`
- API keys for TMDb and Reddit

## Installation
1. Clone the repository.
2. Install the required Python packages.
3. Set up the API keys for TMDb and Reddit in `config.py`.
4. Run `main.py` to start the system.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
