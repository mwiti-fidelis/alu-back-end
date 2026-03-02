#!/usr/bin/python3
"""Module to gather data from an API."""

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
    with open(str(employee_id) + ".csv", "w") as userfile:
        for todo in todos:
            userfile.write(
                '"' + str(employee_id) + '",' +
                '"' + employee_name + '",' +
                '"' + str(todo["completed"]) + '",' +
                '"' + todo["title"] + '"\n'
            )