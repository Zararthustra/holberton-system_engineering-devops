#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import json
import requests


def top_ten(subreddit):
    """Looks up 10 recent hot posts from a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    pull = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()

    if 'data' in pull:
        data = pull.get('data').get('children')
        for hot in data:
            subdata = hot.get('data').get('title')
            print(subdata)
    else:
        print('None')
        return None
