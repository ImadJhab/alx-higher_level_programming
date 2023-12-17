#!/usr/bin/python3
"""importing models"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    q_rows = cur.fetchall()
    for rows in q_rows:
        print(rows)
    cur.close()
    con.close()
