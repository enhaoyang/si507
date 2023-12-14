import plotly
import plotly.graph_objs as go
import plotly.subplots as sp
import json

from cache import load_cached_movies
from treeStruct import tree_from_given_title


def pie_rating(data):
    # Collect vote averages
    # Extracting the 'rating' field from each movie
    data = json.loads(data)
    vote_averages = {movie: details['rating'] for movie, details in data.items()}
    # print(vote_averages)

    # Define categories for vote averages
    categories = {
        "0-1": 0,
        "1-2": 0,
        "2-3": 0,
        "3-4": 0,
        "4-5": 0,
        "5-6": 0,
        "6-7": 0,
        "7-8": 0,
        "8-9": 0,
        "9-10": 0,
    }

    # Count the vote averages for each category
    for name, vote_average in vote_averages.items():
        # print(vote_average)
        for category, upper_bound in zip(categories.keys(), range(1, 11)):
            # print(type(vote_average))
            # print(type(upper_bound))
            if vote_average <= upper_bound:
                categories[category] += 1
                break

    # Generate the pie chart
    labels = list(categories.keys())
    sizes = list(categories.values())

    # Generate the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3,
                                 marker=dict(colors=plotly.colors.qualitative.Plotly),
                                 textinfo='label+percent',
                                 hoverinfo='label+value',
                                 pull=[0.1 if size == max(sizes) else 0 for size in sizes])])

    # Update layout
    fig.update_layout(
        title_text="Distribution of Categories",
        legend_title="Category Names",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="right",
            x=1
        ),
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="RebeccaPurple"
        )
    )

    # Show the plot
    fig.show()


if __name__ == '__main__':
    data = load_cached_movies("movie_data.json")
    # new_data = tree_from_given_title(data.keys(), data)
    pie_rating(data)
