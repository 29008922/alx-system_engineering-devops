#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API to retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects
        response.raise_for_status()  # Raise an exception for error status codes

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)  # Safely retrieve subscriber count

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching subreddit data: {e}")
        return 0

# Example usage:
subreddit_name = "learnpython"  # Replace with the subreddit you want to check
subscriber_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscriber_count} subscribers.")
