#!/usr/bin/python3
''' This module contains the recurse function  '''
import requests


def recurse(subreddit, hot_list=[]):
    ''' Recursively gets the hot posts for a subreddit '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}

    items = len(hot_list)
    if items == 0:
        params = {'limit': 100}
    else:
        last_listing = hot_list[items - 1]
        last_fullname = "{}_{}".format(last_listing['kind'],
                                       last_listing['data']['id'])
        params = {'after': last_fullname, 'limit': 100}

    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    children = data['data']['children']
    if len(children) == 0:
        return (None)
    else:
        for child in children:
            hot_list.append(child)
        recurse(subreddit, hot_list)

    return [listing['data']['title'] for listing in hot_list]
