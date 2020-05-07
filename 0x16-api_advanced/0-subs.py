#!/usr/bin/python3
''' This module contains the number of subscribers function '''
import requests
import json


def number_of_subscribers(subreddit):
    ''' This returns the number of subscribers for a subreddit '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}

    r = requests.get(url, headers=headers)
    data = r.json()

    if data['kind'] != "t5":
        return (0)
    return (data['data']['subscribers'])
