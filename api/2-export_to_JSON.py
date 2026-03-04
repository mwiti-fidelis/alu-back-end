#!/usr/bin/python3
"""Exports todo list data for a given employee ID to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    data = {u_id: []}
    for t in todos:
        data[u_id].append({
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        })

    with open("{}.json".format(u_id), "w") as f:
        json.dump(data, f)
