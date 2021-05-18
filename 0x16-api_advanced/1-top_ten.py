#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit"""


import requests
import requests.auth


def top_ten(subreddit):
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

    headers = {'Authorization': token, 'User-Agent': 'chechApp'}
    p = {'limit': 10}
    response = requests.get(base_url + '/r/' + subreddit,
                            headers=headers, params=p)
    if response:
        dict_u = response.json()
        for i in range(10):
            print(dict_u['data']['children'][i]['data']['title'])
    else:
        print("None")
