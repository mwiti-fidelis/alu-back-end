#!/usr/bin/python3
"""
Exports todo list data for a given employee ID to a JSON file.
Format: { 
"USER_ID": [ {"task": "...", "completed": ..., "username": "..."}, ... ] }
"""
import json
import requests
import sys


if __name__ == "__main__":
    # URL and User ID setup
    url = "https://jsonplaceholder.typicode.com/"
    u_id = sys.argv[1]

    # Fetch User data to get the 'username'
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")

    # Fetch TODO data
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    # Structure the data as a list of dictionaries
    tasks_list = []
    for t in todos:
        tasks_list.append({
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        })

    # Create the final dictionary with USER_ID as the key
    data = {u_id: tasks_list}

    # Write to JSON file: Must be minified (no indent)
    with open("{}.json".format(u_id), "w") as jsonfile:
        json.dump(data, jsonfile)
