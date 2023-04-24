#!/usr/bin/python3
"""Returns to-do list information (progress) for a given employee ID."""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    done = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(done), len(todos)))
    [print("\t {}".format(d)) for d in done]
