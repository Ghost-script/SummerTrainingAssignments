#!/usr/bin/env python

"""
Reads the database and returns the desired content.

"""

from sqlite3 import connect
from calendar import timegm
from time import strptime



def fetch_database( select_by, start, end, day_for_time, database_name):
    """
    Selects the content from the sqlite database 


    """

    queries = [[],[],[]]

    database = connect(database_name)
    cursor = database.cursor()
    
    if str(select_by) == "all" :
        cursor.execute("""
                SELECT date, time, load_1m, load_5m, load_15m
                FROM load_values""" )

    else:
        sqlite_string = """
            SELECT date, time, load_1m, load_5m, load_15m
            FROM load_values
            WHERE %s BETWEEN :start AND :end
            """ % select_by

        if select_by == "time":
            sqlite_string += "AND date = :day_for_time"

        cursor.execute(sqlite_string, {"start" : str(start),
                                       "end" : str(end),
                                       "day_for_time" : str(day_for_time)})

    for row in cursor.fetchall():
        time2timestamp = int(timegm(strptime(row[0]+row[1], "%Y%m%d%H%M%S")))
        queries[0].append([time2timestamp, row[2]])
        queries[1].append([time2timestamp, row[3]])
        queries[2].append([time2timestamp, row[4]])

    return queries



if __name__ == "__main__":

    print "hola"
