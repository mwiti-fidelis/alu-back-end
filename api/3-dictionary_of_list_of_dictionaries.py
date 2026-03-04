#!/usr/bin/python3
"""Exports all employees to-do list information to a single JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_data = {}
    for user in users:
        u_id = str(user.get("id"))
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": u_id}).json()
        
        all_data[u_id] = []
        for task in todos:
            all_data[u_id].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)