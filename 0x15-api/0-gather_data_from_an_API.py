#!/usr/bin/python3
""" Script that, using a REST API, for a given employee
ID, returns info about his/her TODO list progress."""


import requests
from sys import argv


if __name__ == "__main__":
    users = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    work = 'https://jsonplaceholder.typicode.com/users/' + argv[1] + '/todos'
    tasks = 0
    t_done = 0
    r_users = requests.get(users)
    r_work = requests.get(work)
    dic_u = r_users.json()
    list_w = r_work.json()
    name = dic_u['name']
    for done in list_w:
        tasks += 1
        if done["completed"] is True:
            t_done += 1
    print("Employee {} is done with tasks({}/{}):".format(name, t_done, tasks))
    for task in list_w:
        if task["completed"] is True:
            print("\t{}".format(task["title"]))
