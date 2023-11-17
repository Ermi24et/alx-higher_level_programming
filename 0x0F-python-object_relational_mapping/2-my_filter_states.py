#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table
of hbtn...usa where name matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st_name_srch = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, db=db_name)
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id ASC".format(st_name_srch))
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    db.close()
