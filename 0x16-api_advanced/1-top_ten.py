#!/usr/bin/python3
''' Prints the titles of the first 10 hot posts listed for a subreddit '''
import requests


def top_ten(subreddit):
    ''' Prints top ten hot posts for a subreddit '''
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}

    r = requests.get(url, headers=headers)
    data = r.json()

    children = data['data']['children']
    if len(children) == 0:
        print("None")
    else:
        headlines = [child['data']['title'] for child in children]
        for i in range(10):
            print(headlines[i])
