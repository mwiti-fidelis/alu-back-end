#!/usr/bin/python3
import requests
import json
import sys

'''
    Accessing the data resourse from the api using requests module
'''
# Creating a function to get the employees ids from the users object
def get_employees_ids():
    base_url = 'https://jsonplaceholder.typicode.com/users'
    users_data = requests.get(base_url).json()
    employee_ids = [user["id"] for user in users_data]
    return employee_ids
# function to get the tasks completed by the employee using the employee's unique id
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
# saving all employees details in a .json file
    with open("todo_all_employees.json", "w") as employees_file:
        employees_tasks = {}
        for id in all_employee_ids:
            employees_tasks[str(id)] = get_employee_tasks(id)
            employees_file.write(json.dumps(employees_tasks, indent=4))

    
