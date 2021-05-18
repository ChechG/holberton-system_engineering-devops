#!/usr/bin/python3
"""Recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit"""


import requests
import requests.auth


def recurse(subreddit, hot_list=[], nex=''):
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
    res = requests.get(base_url + '/r/' + subreddit + '/hot.json?after=' + nex,
                       headers=heads, allow_redirects=False)

    if res:
        dict_u = res.json()
        dic = len(dict_u['data']['children'])
        for i in dict_u['data']['children']:
            hot_list.append(i['data']['title'])
            nex = dict_u['data']['after']
            if nex is not None:
                recurse(subreddit, hot_list, nex)
        return hot_list
    else:
        return None
