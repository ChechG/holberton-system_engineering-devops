#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit"""


import requests
import requests.auth


def recurse(subreddit, hot_list=[]):
    