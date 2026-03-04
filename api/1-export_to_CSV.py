#!/usr/bin/python3
"""
Exports todo list data for a given employee ID to a CSV file.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        for t in todos:
            # Manual formatting ensures double quotes around every field
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, t.get("completed"), t.get("title")))
            