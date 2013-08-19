#!/usr/bin/env python

"""
Reads the database and returns the desired content.

"""

from sqlite3 import *

def fetch_database(value_type, select_by, start, end, database_name):

    queries = []


    database = connect(database_name)
    cursor = database.cursor()
    cursor.execute("""
        SELECT select_by, :value_type FROM load_values
        WHERE :select_by BETWEEN :start AND :end
        """, {"value_type" : value_type, "select_by" : select_by, "start" : str(start), "end" : str(end)})

    """
    for row in cursor.fetchall():
        queries.append([row[0], row[1])

    
    return queries
    """

    return cursor.fetchall()

if __name__ == "__main__":

    print fetch_by_date(20130819, 20130819, "loads.db")
