#!/usr/bin/python3
""" python script that returns informatin about a given employ """

import requests
import sys

if __name__ == "__main__":
    """ main method to display inormation about a given employ """

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    cmpltd = [td.get("title") for td in todos if td.get("completed") is True]
    total = len(todos)
    tsk_len = len(cmpltd)
    print("Employee {} is done with tasks({}/{}):".format(users.get("name"),
                                                          tsk_len, total))
    for tsk in cmpltd:
        print("\t {}".format(tsk))
