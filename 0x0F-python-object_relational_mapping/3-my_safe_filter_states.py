#!/usr/bin/python3
"""
Script that lists a named on args states from the database
safe from MySQL injection
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
    state = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (state, ))
    states = cursor.fetchall()
    # Display results
    for x in states:
        print(x)

    # Close the cursor and connection
    cursor.close()
    connection.close()
