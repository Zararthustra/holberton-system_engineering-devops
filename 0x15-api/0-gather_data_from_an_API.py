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
    username = user_data[0]['name']
    done_tasks = []
    done = 0
    total = 0

    for done_task in tasks:
        if done_task.get('completed') is True:
            done += 1
            done_tasks.append(done_task.get('title'))
        total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(username, done, total))

    for task in done_tasks:
        print("\t {}".format(task))
