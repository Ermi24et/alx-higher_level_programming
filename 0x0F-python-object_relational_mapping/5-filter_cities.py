#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities
of that database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, db=db_name)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities WHERE state_id =\
            (SELECT id FROM states WHERE name = %s) ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end='')
        if (row != query_rows[-1]):
            print(end=', ')
    print()
    cur.close()
    db.close()
