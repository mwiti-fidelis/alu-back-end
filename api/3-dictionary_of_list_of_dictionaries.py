#!/usr/bin/python3
"""
Exports TODO list information for all employees to a single JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Get all users to build the full dictionary
    users = requests.get(url + "users").json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Get tasks for this specific user
        params = {"userId": user_id}
        todos = requests.get(url + "todos", params=params).json()

        # Build the list of task dictionaries for this user
        user_list = []
        for task in todos:
            user_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks[user_id] = user_list

    # Write to JSON file: todo_all_employees.json without indentation
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)