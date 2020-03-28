#!/usr/bin/python3
''' Lists all states from the database '''
import MySQLdb
import sys


def show_states():
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    show_states()
