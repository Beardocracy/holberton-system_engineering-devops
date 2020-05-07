#!/usr/bin/python3
''' Prints the titles of the first 10 hot posts listed for a subreddit '''
import requests


def top_ten(subreddit):
    ''' Prints top ten hot posts for a subreddit '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}
    params = {'limit': 10}

    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    children = []
    if 'data' in data.keys() and 'children' in data['data'].keys():
        children = data['data']['children']
    if len(children) == 0:
        print("None")
    else:
        headlines = [child['data']['title'] for child in children]
        for titles in headlines:
            print(titles)
