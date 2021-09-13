#!/usr/bin/python3
""" python script that returns exports employ infromation to csv """

import json
import requests
import sys

if __name__ == "__main__":
    """ main method that converts to csv format """

    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    users = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    task_detail = list()
    for tsk in todos:
        data = {
            'task': tsk.get("title"),
            'completed': tsk.get("completed"),
            'username': users.get("username")
        }
        task_detail.append(data)

    with open("{}.json".format(user_id), "w") as file_json:
        file_json.write(json.dumps({user_id: task_detail}))
