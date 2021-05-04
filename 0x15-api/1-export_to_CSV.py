#!/usr/bin/python3
""" Script that, using a REST API, for a given employee
ID, returns info about his/her TODO list progress."""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    file_name = argv[1] + '.csv'
    users = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    work = 'https://jsonplaceholder.typicode.com/users/' + argv[1] + '/todos'
    r_user = requests.get(users)
    r_work = requests.get(work)
    dic_u = r_user.json()
    list_w = r_work.json()
    u_id = dic_u['id']
    u_name = dic_u['name']
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        for done in list_w:
            writer.writerow([u_id, u_name, done['completed'], done['title']])
