#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to CSV format.
"""
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

    # Write to CSV file: USER_ID.csv
    with open("{}.csv".format(user_id), "w") as csvfile:
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ))