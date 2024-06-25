#!/usr/bin/python3
"""
Script that lists all cities on args state from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    connection = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cursor = connection.cursor()
    # Execute query to retrieve states
    cursor.execute("""SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s""", (sys.argv[4], ))
    state = cursor.fetchall()
    # Display results
    x = list(y[0] for y in state)
    print(*x, sep=", ")

    # Close the cursor and connection
    cursor.close()
    connection.close()
