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
    file_name = argv[1] + '.json'
    user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    work = 'https://jsonplaceholder.typicode.com/users/' + argv[1] + '/todos'
    r_user = requests.get(user)
    r_work = requests.get(work)
    dic_u = r_user.json()
    list_w = r_work.json()
    my_dict = {}
    lista = []
    u_id = str(dic_u['id'])
    u_name = dic_u['name']
    for w in list_w:
        dentro = {}
        dentro['task'] = w['title']
        dentro['completed'] = w['completed']
        dentro['username'] = u_name
        lista.append(dentro)
    my_dict[u_id] = lista

    with open(file_name, "w") as f:
        json.dump(my_dict, f)
