#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    emp_id = argv[1]
    user_data = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(emp_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()
    username = user_data[0]['username']
    tasks_list = []
    json_dict = {}

    for task in tasks:
        info = {"task": task.get('title'), "completed": task.get('completed'),
                "username": username}

        tasks_list.append(info)

    json_dict = {emp_id: tasks_list}

    with open(str(emp_id) + ".json", mode="w") as emp_f:
        json.dump(json_dict, emp_f)
