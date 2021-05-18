#!/usr/bin/python3
""" function that queries the Reddit API and returns
the number of subscribers for a given subreddit """


import requests
import requests.auth


def number_of_subscribers(subreddit):
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
    response = requests.get(base_url + '/r/' + subreddit, headers=headers)
    if response:
        dict_u = response.json()
        return dict_u['data']['children'][1]['data']['subreddit_subscribers']
    else:
        return 0
