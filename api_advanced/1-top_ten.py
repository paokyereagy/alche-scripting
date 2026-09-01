
dule that queries the Reddit API for the top ten hot posts."""
import requests
import sys

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts for a given subreddit. If invalid, prints "OK" (no newline).
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:top.ten.posts:v1.0 (by /u/hbtn_student)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.exceptions.RequestException:
        sys.stdout.write("OK")
        return

    if response.status_code != 200:
        sys.stdout.write("OK")
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            sys.stdout.write("OK")
            return
        for post in posts:
            print(post.get("data", {}).get("title"))
    except ValueError:
        sys.stdout.write("OK")
