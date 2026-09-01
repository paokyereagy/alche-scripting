#!/usr/bin/python3
"""Module that recursively queries the Reddit API for hot article
titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The running list of titles collected so far.
        after (str): The pagination token for the next page of
            results.

    Returns:
        list: A list of all hot post titles, or None if the
            subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:recurse.hot.titles:v1.0 (by /u/hbtn_student)"
    }
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    posts = data.get("children", [])
    if not posts and after is None:
        return None

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after is None:
        return hot_list

    return recurse(subreddit, hot_list, next_after)
