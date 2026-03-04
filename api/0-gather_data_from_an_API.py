#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    # Ensure the script only runs when not imported
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Get TODO list information
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    # Filter completed tasks
    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))

    # Print first line in exact specified format
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print completed tasks with 1 tabulation and 1 space
    for title in completed:
        print("\t {}".format(title))