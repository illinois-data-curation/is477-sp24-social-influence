import praw
import json
import csv
import os
from datetime import datetime


# Create 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Function to convert the date to UNIX timestamp
def to_unix_time(year, month, day):
    return int(datetime(year, month, day).timestamp())

# Function to sanitize data by removing newlines from Reddit posts
def sanitize_data(text):
    return text.replace('"', '""').replace('\n', ' ').replace('\r', ' ')


# Load credentials
with open('credentials.json', 'r') as file:
    credentials = json.load(file)

# Connect to reddit
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent=credentials['user_agent'])

# Define the start time for the search
start_time = to_unix_time(2024, 1, 1)  # Beginning of the current year since we're using
                                       # Disney YTD stock price data

# Search all of Reddit and save posts and comments to CSV files
def search_disney_boycott(query, start_time):
    post_list = []
    comment_list = []

    try:
        # Search through submissions across all of Reddit
        for submission in reddit.subreddit('all').search(f'title:({query})', sort='new', syntax='lucene', limit=None):
            if submission.created_utc >= start_time and 'disney' in submission.title.lower() and 'boycott' in submission.title.lower():
                post_list.append([submission.id, submission.title, submission.url, submission.selftext])
                
                # Get all the comments
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    comment_list.append([comment.id, submission.id, comment.body])
    except Exception as e:
        print(f"An error occurred: {e}")

    # Write the posts to CSV
    with open('data/posts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['post_id', 'title', 'url', 'selftext'])
        for post in post_list:
            writer.writerow([sanitize_data(field) for field in post])

    # Write the comments to CSV
    with open('data/comments.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['comment_id', 'post_id', 'body'])
        for comment in comment_list:
            writer.writerow([sanitize_data(field) for field in comment])


if __name__ == '__main__':
    search_query = 'Disney AND boycott'
    search_disney_boycott(search_query, start_time)
