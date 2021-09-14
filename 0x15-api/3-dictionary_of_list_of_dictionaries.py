#!/usr/bin/python3
""" python script that returns exports employ infromation to json"""

import json
import requests


def get_tasks_of_employ(todos, user_id, user_name):
    """ method to get tasks of a given employ """
    task_detail = list()
    for tsk in todos:
        if tsk.get("userId") == user_id:
            data = {
                'username': user_name,
                'task': tsk.get("title"),
                'completed': tsk.get("completed")
            }
            task_detail.append(data)
    return task_detail


if __name__ == "__main__":
    """ main method that exports dictionary of list dictionaries to json"""

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    user_task_detail = dict()
    for usr in users:
        user_id = usr.get("id")
        user_name = usr.get("username")
        user_task = get_tasks_of_employ(todos, user_id, user_name)
        user_task_detail[user_id] = user_task

    with open("todo_all_employees.json", "w", encoding="utf-8") as file_json:
        file_json.write(json.dumps(user_task_detail))
