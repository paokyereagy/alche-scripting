import requests


def top_ten(subreddit):
  """Queries the Reddit API and prints the titles of the

  first 10 hot posts listed for a given subreddit.
  Prints 'OK' if the subreddit is invalid.
  """
  url = f"https://www.reddit.com/r/{subreddit}/hot.json"

  # Reddit API requires a custom User-Agent to avoid 429/403 errors
  headers = {"User-Agent": "python:subreddit.counter:v1.0 (by /u/your_username)"}

  try:
    # Disable redirects to catch invalid subreddits that redirect to search
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code is not 200 (e.g., 302 redirect, 404 not found, etc.)
    if response.status_code != 200:
      print("OK")
      return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
      print("OK")
      return

    # Print the titles of the first 10 hot posts
    for i in range(min(10, len(posts))):
      print(posts[i]["data"]["title"])

  except Exception:
    print("OK")
