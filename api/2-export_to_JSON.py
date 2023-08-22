#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress.
Exports the data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]

    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    user_name = employee['username']
    file_name = f"{id}.json"

    user_dict = {id: []}
    for task in employee_todos:
        user_dict[id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        })

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(user_dict, file, indent=4)
