#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """
    Connects to the MySQL server and retrieves states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user= "root", passwd= "root", db= "hbtn_0e_0_usa")
        cursor = connection.cursor()
        # Execute query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display results
        for state in states[:5]:
            print(state)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)
