#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress.
Exports the data in the CSV format.
"""
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]

    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    name = employee['username']
    file_name = f"{id}.csv"
    with open(file_name, "w", encoding="utf-8") as file:
        for task in employee_todo:
            completed_status = task.get('completed')
            task_title = task.get('title')
            file.write(
                f'"{id}","{name}","{completed_status}","{task_title}"\n')
