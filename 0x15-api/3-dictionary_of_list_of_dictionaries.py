#!/usr/bin/python3
""" Script that, using a REST API, for a given employee
ID, returns info about his/her TODO list progress."""


import csv
import json
import requests
from sys import argv


""" with open("mobos.json", "w") as outfile:
    json.dump(products, outfile) """

if __name__ == "__main__":
    file_name = 'todo_all_employees.json'
    users = 'https://jsonplaceholder.typicode.com/users'
    r_users = requests.get(users)
    dic_users = r_users.json()
    final_dict = {}
    for i in range(1, len(dic_users) + 1):
        my_dict = {}
        lista = []
        w = 'https://jsonplaceholder.typicode.com/users/' + str(i) + '/todos'
        r_work = requests.get(w)
        user = 'https://jsonplaceholder.typicode.com/users/' + str(i)
        r_user = requests.get(user)
        dic_u = r_user.json()
        list_w = r_work.json()
        u_name = dic_u['username']
        for w in list_w:
            dentro = {}
            dentro['task'] = w['title']
            dentro['completed'] = w['completed']
            dentro['username'] = u_name
            lista.append(dentro)
        final_dict[i] = lista
    with open(file_name, "w") as f:
        json.dump(final_dict, f)
