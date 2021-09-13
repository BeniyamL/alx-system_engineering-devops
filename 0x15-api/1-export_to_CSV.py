#!/usr/bin/python3
""" python script that returns exports emploty infromation to csv """

import csv
import requests
import sys

if __name__ == "__main__":
    """ main method that converts to csv format """

    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    users = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for ts in todos:
            writer.writerow([user_id, users.get("username"),
                            ts.get("completed"), ts.get("title")])
