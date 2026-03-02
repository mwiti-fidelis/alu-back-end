#!/usr/bin/python3
"""
    Module to gather data from an API.
"""
import requests
import json
import sys

def get_employees_ids():
    base_url = 'https://jsonplaceholder.typicode.com/users'
    users_data = requests.get(base_url).json()
    employee_ids = [user["id"] for user in users_data]
    return employee_ids
def get_employee_tasks(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    user_info = requests.get(f"{base_url}/{employee_id}").json()
    employee_name = user_info["username"]

    todos = requests.get(f"{base_url}/{employee_id}/todos").json()
    return [
        {
            "username": employee_name,
            "task": todo["title"],
            "completed": todo["completed"]
        }
        for todo in todos
    ]

if __name__ == "__main__": 
    all_employee_ids = get_employees_ids()
    with open("todo_all_employees.json", "w") as employees_file:
        employees_tasks = {}
        for id in all_employee_ids:
            employees_tasks[str(id)] = get_employee_tasks(id)
            employees_file.write(json.dumps(employees_tasks, indent=4))

