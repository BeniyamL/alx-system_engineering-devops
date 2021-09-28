#!/usr/bin/python3
""" a module to find the number of subscriber of a given subreddit """
import requests


def top_ten(subreddit):
    """ a method to find the number of a subscriber of a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {'User-Agent': 'Python/requests'}
    params = {'limit': 10}
    response = requests.get(url, headers=agent, params=params,
                            allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        print("None")
        return
    hot_titles = response.json().get('data').get('children')
    for title in hot_titles:
        print(title.get('data').get('title'))
