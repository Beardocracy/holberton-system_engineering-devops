#!/usr/bin/python3
''' Gets info from API and outputs formatted data to CSV file '''
import csv
import requests
import sys


if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    user_info_url = 'https://jsonplaceholder.typicode.com/users/'

    if sys.argv[1]:
        user_id = sys.argv[1]
        if int(user_id) > 10 or int(user_id) < 1:
            exit(0)
    else:
        exit(0)

    user_response = requests.get(user_info_url + user_id)
    todos_response = requests.get(todo_url + user_id)

    user_data = user_response.json()
    user_todos = todos_response.json()

    with open('{}.csv'.format(user_id), mode='w') as f:
        writer = csv.writer(f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in user_todos:
            writer.writerow([
                user_id,
                user_data['username'],
                todo['completed'],
                todo['title']
            ])
