#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    emp_id = argv[1]
    user_data = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(emp_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()
    username = user_data[0]['username']

    with open(str(emp_id) + ".csv", mode="w") as emp_f:
        f_write = csv.writer(emp_f, quoting=csv.QUOTE_ALL)

        for task in tasks:
            f_write.writerow([task['userId'], username,
                             task['completed'], task['title']])
