#!/usr/bin/python3
"""importing models"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4], ))
    q_rows = cur.fetchall()
    for row in q_rows:
        print(row)
    cur.close()
    con.close()
