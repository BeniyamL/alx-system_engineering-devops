#!/usr/bin/python3
""" a module to find the number of subscriber of a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ a method to find the number of a subscriber of a subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    agent = {'User-Agent': 'Python/requests'}
    response = requests.get(url, headers=agent, allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        return 0
    return response.json().get('data').get('subscribers')
