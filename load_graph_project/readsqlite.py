#!/usr/bin/env python

"""
Reads the database and returns the desired content.

"""

from sqlite3 import *

def fetch_by_date(start_date, end_date, database_name):

    queries = []

    database = connect(database_name)
    cursor = database.cursor()
    cursor.execute("""
        SELECT load_1m, load_5m, load_15m FROM load_values
        WHERE date BETWEEN :start_date AND :end_date
        """, {"start_date" : str(start_date), "end_date" : str(end_date)})

    for row in cursor.fetchall():
        queries.append({"1m" : row[0], "5m" : row[1], "15m" : row[2]})

    return queries


if __name__ == "__main__":

    print fetch_by_date(20130819, 20130819, "loads.db")
