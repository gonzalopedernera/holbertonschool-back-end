#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    task_done = 0
    total_task = 0
    completed_tasks = []

    employee = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}'
            )
    employee_to_do = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/todos'
            )

    for task in employee_to_do.json():
        if task.get('completed') is True:
            task_done += 1
            total_task += 1
            completed_tasks.append(task.get('title'))
        else:
            total_task += 1

    name = employee.json()['name']

    print(
        f"Employee {name} is done with tasks({task_done}/{total_task}):")
    for task in completed_tasks:
        print(f"\t {task}")
