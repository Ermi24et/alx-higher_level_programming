#!/usr/bin/python3
""" a script that lists all states from the daatbase """
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, port=3306, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
