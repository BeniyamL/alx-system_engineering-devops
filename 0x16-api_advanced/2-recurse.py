#!/usr/bin/python3
""" a module to find the title of all hot articles """
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """ a method that returns a list containing the title of hot articles """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {'User-Agent': 'Python/requests'}

    params = {'after': after, 'count': count, 'limit': 100}
    response = requests.get(url, headers=agent, params=params,
                            allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        return None
    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    hot_titles = data.get('children')
    for title in hot_titles:
        hot_list.append(title.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    return hot_titles
