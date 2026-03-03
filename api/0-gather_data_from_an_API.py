#!/usr/bin/python3
"""Module to gather data from an API."""

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID", file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer", file=sys.stderr)
        sys.exit(1)

    base = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base}/users/{employee_id}").json()
    if user.status_code != 200:
        sys.exit(1)
    employee_name = user.get("name")

    todos = requests.get(f"{base}/todos", params={"userId": employee_id}).json()
    if todos.status_code != 200:
        sys.exit(1)

    completed = [t for t in todos if t.get("completed") is True]

    header = (
        f"Employee {employee_name} is done with tasks"
        f"({len(completed)}/{len(todos)}):"
    )
    print(header)

    for task in completed:
        title = task.get("title")
        print("\t {}".format(title))


if __name__ == "__main__":
    main()