#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information to get the USERNAME
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Get all tasks for this user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create the dictionary structure: { "USER_ID": [ {"task":...,...}, ... ] }
    dictionary = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    # Write to JSON file: USER_ID.json without indentation (minified)
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(dictionary, jsonfile)