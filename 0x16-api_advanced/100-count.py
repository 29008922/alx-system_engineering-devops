#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after="", counts={}):
    """Recursively queries the Reddit API, counts keyword occurrences in hot post titles,
       and prints the results in sorted order.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): Continuation token for pagination. Defaults to "".
        counts (dict, optional): Dictionary to store keyword counts. Defaults to {}.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "YourAppName/0.1 (for educational purposes)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                for word in word_list:
                    word = word.lower()  # Case-insensitive comparison
                    if word in title.lower().split():
                        counts[word] = counts.get(word, 0) + title.lower().split().count(word)  # Count multiple occurrences

        after = data.get("data", {}).get("after")  # Check for next page
        if after:
            count_words(subreddit, word_list, after, counts)  # Recursive call for pagination

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    else:
        if counts:
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))  # Sort by count (descending), then alphabetically
            for word, count in sorted_counts:
                print(f"{word}: {count}")

# Example usage:
subreddit_name = "programming"
words_to_count = ["JAVA", "javascript", "python", "java"]
count_words(subreddit_name, words_to_count)
