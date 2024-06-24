#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa thier name provided form args
"""

import MySQLdb
import sys


def list_Mstates(username, password, db_name, state_name):
    """
    Connects to the MySQL server and retrieves specified states from database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user="root", passwd="root",
                                     db="hbtn_0e_0_usa")
        cursor = connection.cursor()
        # Execute query to retrieve states
        query = "SELECT * FROM states WHERE name = %s ORDER BY id asc"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        # Display results
        for state in states:
            print(state)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_Mstates(username, password, db_name, state_name)
