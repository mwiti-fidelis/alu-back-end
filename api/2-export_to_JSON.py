#!/usr/bin/python3
"""Module to gather data from an API."""

import json
import requests
import sys

if __name__ == "__main__":
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    employee = requests.get(
        BASE_URL + '/users/{}/'.format(employee_id)
    ).json()
    employee_name = employee.get("username")
    todos = requests.get(
        BASE_URL + '/users/{}/todos'.format(employee_id)
    ).json()
    todo_list = []
    for todo in todos:
        todo_list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee_name
        })
    userdata = {employee_id: todo_list}
    with open(str(employee_id) + ".json", "w") as userfile:
        json.dump(userdata, userfile, indent=4)