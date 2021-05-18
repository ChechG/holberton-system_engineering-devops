#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit"""


import requests
import requests.auth


def recurse(subreddit, hot_list=[]):
    base_url = 'https://www.reddit.com/'
    u = 'ChechG'
    p = 'liverpool'
    u_id = 'u-ff2BP3dLBRIg'
    s_key = 'Hm0PSCGrsPGC0G5WNYWJHnP-hC8--A'
    data = {'grant_type': 'password', 'username': u, 'password': p}
    auth = requests.auth.HTTPBasicAuth(u_id, s_key)
    r = requests.post(base_url + 'api/v1/access_token',
                      data=data,
                      headers={'user-agent': 'chechApp'},
                      auth=auth)
    d = r.json()
    token = 'bearer ' + d['access_token']

    base_url = 'https://oauth.reddit.com'

    heads = {'Authorization': token, 'User-Agent': 'chechApp'}
    res = requests.get(base_url + '/r/' + subreddit + '/hot', headers=heads)

    if res:
        dict_u = res.json()
        length = len(hot_list)
        dato = dict_u['data']['children'][length]['data']['title']
        len_list = len(dict_u['data']['children'])
        if len_list == 0:
            return None
        if length <= len_list - 1:
            if dato not in hot_list:
                hot_list.append(dato)
                if length < len_list - 1:
                    recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
