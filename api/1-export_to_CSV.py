#!/usr/bin/python3
"""Exports todo list data for a given employee ID to a CSV file."""
import requests
import sys


if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    with open("{}.csv".format(u_id), "w") as csvfile:
        for t in todos:
            # All fields must be quoted: "ID","USERNAME","STATUS","TITLE"
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                u_id, username, t.get("completed"), t.get("title")))
