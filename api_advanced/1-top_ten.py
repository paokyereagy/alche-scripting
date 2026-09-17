#!/usr/bin/python3
import requests


def top_ten(subreddit):
  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  headers = {"User-Agent": "python:subreddit.counter:v1.0 (by /u/paokyereagy)"}

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
      print("OK")
      return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
      print("OK")
      return

    for i in range(min(10, len(posts))):
      print(posts[i]["data"]["title"])

  except Exception:
    print("OK")
