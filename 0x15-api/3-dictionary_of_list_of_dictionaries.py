#!/usr/bin/python3
"""Returns to-do list information (progress) for a given employee ID."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    todos = requests.get(url + "todos").json()

    to_json = {}
    with open("todo_all_employees.json", "w") as f:
        for u in users:
            all_todos = []
            for t in todos:
                res = {
                    "username": u.get("username"),
                    "task": t.get("title"),
                    "completed": t.get("completed")
                }
                all_todos.append(res)
            to_json.update({str(u["id"]): all_todos})
        json.dump(to_json, f)
