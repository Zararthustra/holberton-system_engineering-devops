#!/usr/bin/python3
"""
queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is
given, the function should return 0.
"""

import json
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers to a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    pull = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    check = list(pull.keys())
    if 'data' in check:
        subs = pull.get('data').get('subscribers')
    else:
        subs = 0
    return subs
