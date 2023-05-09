#!/usr/bin/python3
"""
    Task 0
"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given subreddit.
        Returns 0 if invalid subreddit was given
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    """https://stackoverflow.com/questions/10606133/"""
    headers = {
            "User-Agent": "redditdev scraper by u/coderboy-exe",
            "From": "coderboy.exe@gmail.com"
    }

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data.get("data").get("subscribers")
    else:
        return 0
