#!/usr/bin/python3
"""Returns to-do list information (progress) for a given employee ID."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users/{}".format(argv[1])).json()
    username = user_data.get("username")

    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(argv[1]), "w") as f:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, f)
