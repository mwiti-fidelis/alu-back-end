#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__": 
    '''
        Accessing the data resourse from the api using requests module
    '''
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    employee_name = employee.get("name")
    todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()
    todo_list = {}
    for todo in todos:
        todo_list.update({todo.get("title"): todo.get("completed")})
        todo_list_length = len(todo_list)

    completed_todo = len([key for key, value in todo_list.items() if value is True])

    print("Employee {} is done with tasks ({}/{})".format(employee_name, completed_todo, todo_list_length))
    #Printing the list of all activities completed
    for key, val in todo_list.items():
        if val is True:
            print("\t {}".format(key))