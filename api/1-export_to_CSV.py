#!/usr/bin/python3
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