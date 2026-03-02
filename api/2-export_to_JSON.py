#!/usr/bin/python3
"""
    Module to gather data from an API.
    This script accesses employee data and their TODO list from
    the JSONPlaceholder API and displays completed tasks.
"""
import requests
import sys
import json

if __name__ == "__main__": 
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    employee = requests.get(
        BASE_URL + f'/users/{employee_id}/').json()
    employee_name = employee.get("username")
    todos = requests.get(
        BASE_URL + f'/users/{employee_id}/todos').json()
    todo_list = []
    for todo in todos:
        todo_list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee_name
        })
# saving the data in .json file
    userdata = {employee_id: todo_list}
    with open(str(employee_id) + ".json", "w") as userfile:
        json.dump(userdata, userfile, indent=4)
    print(f"Tasks fo employee {employee_id} have successfully been exported to {employee_id}.json") 
