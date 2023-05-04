# Reddit Content Scraper

This script uses the PRAW (Python Reddit API Wrapper) library to retrieve the top submissions from a list of subreddits and saves the resulting data as a pandas DataFrame. The script filters out submissions that have no text body or contain media.

**Prerequisites**

    >Python 3.x
    >pandas and praw libraries installed (you can install them via pip)

**Usage**

    >Open reddit_content_scraper.py in your preferred Python editor or IDE.
    >Replace the client_id, client_secret, and user_agent values in the praw.Reddit() call with your own Reddit API credentials.
    >Replace subreddit_names with the names of the subreddits you want to retrieve submissions from (as a list of strings).
    >Optionally, change the limit parameter to adjust the number of submissions to retrieve (default is 5).
    >Run the script. The resulting DataFrame will be printed to the console.

**Example**

>To retrieve the top 10 submissions from the "conspiracy" subreddit:


`get_content_from_reddit(['conspiracy'], 10)`

