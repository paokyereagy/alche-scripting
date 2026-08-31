#!/usr/bin/python3
"""Module that queries the Reddit API for subreddit subscriber counts."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subscriber.counter:v1.0 (by /u/holbertonstudent)"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
    except requests.exceptions.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
