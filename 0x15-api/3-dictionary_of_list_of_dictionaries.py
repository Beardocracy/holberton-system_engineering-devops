#!/usr/bin/python3
''' Exports data from API in JSON '''
import json
import requests
import sys

if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    user_info_url = 'https://jsonplaceholder.typicode.com/users/'

    users_list = requests.get(user_info_url).json()

    data = {}
    for user in users_list:
        user_id = user['id']
        todo_resp = requests.get(todo_url + str(user_id))
        user_todos = todo_resp.json()

        task_data = [{
            "task":         todo['title'],
            "completed":    todo['completed'],
            "username":     user['username']
        } for todo in user_todos]

        data[user_id] = task_data

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data, f)
