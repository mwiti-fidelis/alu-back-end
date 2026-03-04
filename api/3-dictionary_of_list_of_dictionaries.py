#!/usr/bin/python3
"""
Exports all employees' TODO list data to a single JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_res = requests.get(url + "users")
    users = users_res.json()

    all_data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Fetch todos for each specific user
        todos_res = requests.get(url + "todos", params={"userId": user_id})
        todos = todos_res.json()

        all_data[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    # The file must be minified (no indent) to pass the checker
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
