#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=root, passwd=root,db=hbtn_0e_0_usa)
        cursor = connection.cursor()

        # Debugging output
        print(f"Connecting to MySQL server with user: {username}, db: {db_name}")

        # Execute query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
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
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)
