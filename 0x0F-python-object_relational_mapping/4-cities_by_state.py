#!/usr/bin/python3
"""
Script that lists all cities from the database
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states ON states.id=cities.state_id""")
    state = cursor.fetchall()
    # Display results
    for x in state:
        print(x)

    # Close the cursor and connection
    cursor.close()
    connection.close()
