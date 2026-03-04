#!/usr/bin/python3
"""
Queries a REST API for a given employee ID and returns TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user data - ensure we use the integer ID from sys.argv
    user = requests.get(url + "users/{}".format(employee_id)).json()
    name = user.get("name")

    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task))
