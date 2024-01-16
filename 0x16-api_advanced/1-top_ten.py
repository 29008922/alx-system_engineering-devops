#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects
        response.raise_for_status()  # Raise an exception for error status codes

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if posts:
            for post in posts[:10]:  # Print titles of the first 10 posts
                title = post.get("data", {}).get("title")
                print(title)
        else:
            print("No posts found.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching subreddit data: {e}")
        print("None")  # Indicate invalid subreddit or error

# Example usage:
subreddit_name = "news"  # Replace with the subreddit you want to check
top_ten(subreddit_name)
