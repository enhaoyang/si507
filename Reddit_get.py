import praw
import config

# Establishing Reddit API credentials
ID_REDDIT = config.REDDIT_CLIENT_ID
SECRET_REDDIT = config.REDDIT_SECRET
AGENT_USER = config.REDDIT_USER_AGENT

# Setting up the Reddit connection
reddit_access = praw.Reddit(
    client_id=ID_REDDIT,
    client_secret=SECRET_REDDIT,
    user_agent=AGENT_USER
)

# Function to gather discussions from Reddit about a specific movie
def retrieve_film_discussions(subreddit_focus, film_name, max_results=3):
    subreddit = reddit_access.subreddit(subreddit_focus)
    query_for_search = f'title:{film_name}'
    fetched_submissions = subreddit.search(query_for_search, limit=max_results)

    list_of_reviews = []
    for post in fetched_submissions:
        # Extend comments to include those hidden by the 'load more comments' link
        post_comments = post.comments.list()
        details = {
            'headline': post.title,
            'rating': post.score,
            'link': post.url,
            'poster': post.author.name if post.author else 'Anonymous',
            'discussions': post_comments[:10]  # Limiting to top 10 comments for brevity
        }
        list_of_reviews.append(details)

    return list_of_reviews

# Display the discussion topics related to a movie
def output_discussion_topics(film_title):
    # Retrieving movie discussions using the predefined function
    focus_subreddit = 'movies'
    gathered_reviews = retrieve_film_discussions(focus_subreddit, film_title)
    for discussion in gathered_reviews:
        print(f"Headline: {discussion['headline']}")
        print(f"Rating: {discussion['rating']}")
        print(f"Discussion Link: {discussion['link']}")
        print(f"Posted by: {discussion['poster']}")
        if discussion['discussions']:
            initial_comment = discussion['discussions'][0]
            subsequent_comment = discussion['discussions'][1]
            print(f"Leading comment: {initial_comment.body}")
            print(f"Following comment: {subsequent_comment.body}")
        else:
            print("No discussions available.")

        print('-' * 80)
