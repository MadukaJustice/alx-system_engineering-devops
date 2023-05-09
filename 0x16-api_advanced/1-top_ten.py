#!/usr/bin/python3
"""
    Task 1
"""
import requests


def top_ten(subreddit):
    """
        Returns the number of subscribers for a given subreddit.
        Returns 0 if invalid subreddit was given
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            "User-Agent": "redditdev scraper by u/coderboy-exe",
            "From": "jonasjustice98@gmail.com"
    }

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()

        top_ten = data.get("data", {}).get("children", [])
        for post in top_ten:
            print(post.get("data").get("title"))
    else:
        print("None")
