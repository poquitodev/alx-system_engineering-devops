#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            m.get("id"): [{
                "task": k.get("title"),
                "completed": k.get("completed"),
                "username": m.get("username")
            } for k in requests.get(url + "todos",
                                    params={"userId": m.get("id")}).json()]
            for m in users}, jsonfile)
