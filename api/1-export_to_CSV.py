#!/usr/bin/python3
"""
Exports todo list data for a given employee ID to a CSV file.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import requests
import sys


if __name__ == "__main__":
    # The URL base for JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    # Fetch User Info to get the 'username' (e.g., Bret)
    user_res = requests.get(url + "users/{}".format(user_id))
    user_data = user_res.json()
    username = user_data.get("username")

    todos_res = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_res.json()

    file_name = "{}.csv".format(user_id)
    with open(file_name, "w") as csvfile:
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ))
