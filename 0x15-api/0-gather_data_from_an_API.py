#!/usr/bin/python3
''' Returns information about an employees TODO list '''
import requests
import sys

if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    user_info_url = 'https://jsonplaceholder.typicode.com/users/'

    if sys.argv[1]:
        user_id = sys.argv[1]
        if int(user_id) > 10 or int(user_id) < 1:
            print("Employee doesn't exist")
            exit (0)

    user_response = requests.get(user_info_url + user_id)
    todos_response = requests.get(todo_url + user_id)

    user_data = user_response.json()
    user_todos = todos_response.json()

    completed_todos = []
    for todo in user_todos:
        if todo['completed'] is True:
            completed_todos.append(todo['title'])

    print("Employee {} is done with tasks({}/{}):".format(user_data['name'],
                                                          len(completed_todos),
                                                          len(user_todos)
                                                          ))
    for todo in completed_todos:
        print("\t {}".format(todo))
