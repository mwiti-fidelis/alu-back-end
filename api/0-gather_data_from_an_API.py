#!/usr/bin/python3
"""Module to gather data from an API."""

import requests
import sys

if __name__ == "__main__":
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + '/users/{}/'.format(sys.argv[1])
    ).json()
    employee_name = employee.get("name")
    todos = requests.get(
        BASE_URL + '/users/{}/todos'.format(sys.argv[1])
    ).json()
    todo_list = {}
    for todo in todos:
        todo_list.update({todo.get("title"): todo.get("completed")})
    todo_list_length = len(todo_list)
    completed_todo = len([key for key, value in todo_list.items()
                         if value is True])
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_todo, todo_list_length))
    for key, val in todo_list.items():
        if val is True:
            print("\t {}".format(key))