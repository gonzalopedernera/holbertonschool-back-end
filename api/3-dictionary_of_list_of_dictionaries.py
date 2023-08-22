#!/usr/bin/python3
"""
For all employees, returns information about their TODO list progress.
Exports the data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    employee_users = requests.get(
        f'https://jsonplaceholder.typicode.com/users').json()
    employee_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()

    user_dict = {}
    file_name = "todo_all_employees.json"

    for user in employee_users:
        id = user.get("id")
        user_dict[id] = []
        for task in employee_todos:
            if user.get('id') == task.get('userId'):
                user_dict[id].append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(user_dict, file, indent=4)
