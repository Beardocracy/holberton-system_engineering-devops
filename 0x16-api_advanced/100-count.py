#!/usr/bin/python3
''' This module contains the count function  '''
import re
import requests


def count_words(subreddit, word_list, hot_list=[], print_flag=0):
    ''' Prints the number of occurrences for a list of keywords in a subs
    hotlist
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'tbearden'}

    if (len(word_list) == 0):
        print()
        return (None)
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

    children = []
    if 'data' in data.keys() and 'children' in data['data'].keys():
        children = data['data']['children']
    if len(children) == 0:
        return (None)
    else:
        for child in children:
            hot_list.append(child)
        print_flag += 1
        count_words(subreddit, word_list, hot_list, print_flag)

    titles = [listing['data']['title'].lower() for listing in hot_list]
    if print_flag == 1:
        print_matches(titles, word_list)


def print_matches(titles, word_list):
    ''' Prints out the keyword match rankings '''
    '''
    word_list = set([x.lower() for x in word_list])
    '''
    kw_count = {}
    for kw in word_list:
        kw_count[kw] = 0
    for title in titles:
        for kw in word_list:
            expr = "(^|[ ]){}([ ]|$)".format(kw)
            matches = re.findall(r"{}".format(expr), title, re.I)
            kw_count[kw] += len(matches)
    for kw in sorted(kw_count, key=lambda kw: (-kw_count[kw], kw)):
        if kw_count[kw] > 0:
            print("{}: {}".format(kw, kw_count[kw]))
