#!/usr/bin/python3
"""Returns to-do list information (progress) for a given employee ID."""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users/{}".format(argv[1])).json()
    username = user_data.get("username")

    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([argv[1], username,
                            t.get("completed"), t.get("title")])
