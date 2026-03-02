#!/usr/bin/python3
"""Module to gather data from an API."""

import json
import requests


def get_employees_ids():
    """Get all employee IDs from the API."""
    base_url = 'https://jsonplaceholder.typicode.com/users'
    users_data = requests.get(base_url).json()
    employee_ids = [user["id"] for user in users_data]
    return employee_ids


def get_employee_tasks(employee_id):
    """Get all tasks for a specific employee."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_info = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user_info["username"]
    
    todos = requests.get(f"{base_url}/users/{employee_id}/todos").json()
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
    employees_tasks = {}
    for emp_id in all_employee_ids:
        employees_tasks[str(emp_id)] = get_employee_tasks(emp_id)
    
    with open("todo_all_employees.json", "w") as employees_file:
        json.dump(employees_tasks, employees_file, indent=4)

        