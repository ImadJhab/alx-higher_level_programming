#!/usr/bin/python3
"""importing models"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port="3306", user=argv[1],
                         passw=argv[2], dbname=argv[3])
    cur = db.cursor()
    db.execute("SELECT * FROM states ORDER BY states.id ASC")
    q_rows = db.fetchall()
    for rows in q_rows:
        print(rows)
    cur.close()
    db.close()
