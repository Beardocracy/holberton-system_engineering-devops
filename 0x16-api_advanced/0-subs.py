#!/usr/bin/python3
''' This module contains the number of subscribers function '''
import requests


def number_of_subscribers(subreddit):
    ''' This returns the number of subscribers for a subreddit '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}

    r = requests.get(url, headers=headers)
    data = r.json()

    if 'data' in data.keys():
        if 'subscribers' in (data['data']).keys():
            return (data['data']['subscribers'])
        else:
            return (0)
    else:
        return (0)
