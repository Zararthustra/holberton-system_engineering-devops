#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == "__main__":
    import json
    import requests

    users_data = requests.get(
            'https://jsonplaceholder.typicode.com/users').json()
    json_dict = {}

    for user in users_data:
        emp_id = user.get('id')
        tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(emp_id)).json()
        tasks_list = []

        for task in tasks:
            info = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')}

            tasks_list.append(info)

        json_dict[emp_id] = tasks_list

    with open("todo_all_employees.json", mode="w") as emps_f:
        json.dump(json_dict, emps_f)
