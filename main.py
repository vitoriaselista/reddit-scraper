import pandas as pd
import praw

# Initialize the Reddit API wrapper with the necessary credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='USER_AGENT'
)
# Define a function to retrieve the top submissions from a list of subreddit names
def get_content_from_reddit(subreddit_names, limit=5):

    # Create an empty list to hold the submissions data
    submissions = []

    # Loop through each subreddit and retrieve the top submissions
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=limit):
            if submission.selftext and not submission.media:
                submissions.append({
                    'title': submission.title,
                    'body': submission.selftext,
                    'id': submission.id
                })

    # Convert the submissions list to a pandas DataFrame
    submissions_df = pd.DataFrame(submissions)
    print(submissions_df)

# Call the function with the desired subreddit names and limit
get_content_from_reddit(['SUBREDDIT_NAME'], 5)

