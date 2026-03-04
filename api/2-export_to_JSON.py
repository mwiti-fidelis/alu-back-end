#!/usr/bin/python3
"""
Exports todo list data for a given employee ID to a JSON file.
Format: { "USER_ID": [ {"task": "...", "completed": ..., "username": "..."}, ... ] }
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Build the required dictionary structure
    data = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)
