#!/usr/bin/python3
"""Module that recursively queries the Reddit API and prints a
sorted count of given keywords found in hot article titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses titles of all hot
    articles for a subreddit, and prints a sorted count of given
    keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count (case-insensitive).
        after (str): Pagination token for the next page of results.
        counts (dict): Running word count accumulator.

    Returns:
        None
    """
    if counts is None:
        counts = {}
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:count.words.titles:v1.0 (by /u/hbtn_student)"
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
        return

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        for token in title.split():
            cleaned = "".join(
                c for c in token if c.isalnum()
            ).lower()
            if cleaned in counts:
                counts[cleaned] += 1

    next_after = data.get("after")
    if next_after is None:
        results = [(word, cnt) for word, cnt in counts.items() if cnt > 0]
        results.sort(key=lambda x: (-x[1], x[0]))
        for word, cnt in results:
            print("{}: {}".format(word, cnt))
        return

    return count_words(subreddit, word_list, next_after, counts)
