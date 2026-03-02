#!/usr/bin/python3
"""
    Module to gather data from an API.
    This script accesses employee data and their TODO list from
    the JSONPlaceholder API and displays completed tasks.
"""
import requests
import sys

if __name__ == "__main__": 
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    employee = requests.get(
        BASE_URL + f'/users/{employee_id}/').json()
    employee_name = employee.get("username")
    todos = requests.get(
        BASE_URL + f'/users/{employee_id}/todos').json()
    todo_list = {}
    for todo in todos:
        todo_list.update({todo.get("title"): todo.get("completed")})
        todo_list_length = len(todo_list)

    completed_todo = len([key for key, value in todo_list.items() if value is True])
# saving the employee details in a csv file
    with open(str(employee_id) + ".csv", "w") as userfile:
        [
            userfile.write(
            '"' + str(employee_id) + '", ' +
            '"' + employee_name +'", '+
            '"' + str(todo["completed"])+ '", '+
            '"' + todo["title"] + '", '+"\n"
        )
        for todo in todos
        ]
