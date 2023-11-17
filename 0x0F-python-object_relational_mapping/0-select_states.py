#!/usr/bin/env python3
import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', passwd='root', port=3306, db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
