#!/usr/bin/python3
''' Gets info from API and outputs formatted data to CSV file '''
import requests
import sys
import csv


todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
user_info_url = 'https://jsonplaceholder.typicode.com/users/'

if sys.argv[1]:
    user_id = sys.argv[1]
    if int(user_id) > 10 or int(user_id) < 1:
        print("Employee doesn't exist")
        exit(0)

user_response = requests.get(user_info_url + user_id)
todos_response = requests.get(todo_url + user_id)

user_data = user_response.json()
user_todos = todos_response.json()

with open('USER_ID.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for todo in user_todos:
        writer.writerow([
            user_id,
            user_data['name'],
            todo['completed'],
            todo['title']
        ])
