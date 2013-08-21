#!/usr/bin/env python

"""
Reads the database and returns the desired content.

"""

from sqlite3 import connect
from calendar import timegm
from time import strptime



def fetch_database( select_by, start, end, day_for_time, database_name):
    """
    Selects the content from the sqlite database, filtering it with the
    parameters given. 
        
        select_by: column from where to apply the range filter. Can be
                    time or date.

        start, stop: specifies the range to be filtered.

        day_for_time: If select_by == time, specifies the day from with the 
                      time range applies. 

        database_name: The name of the database the be queried


    Returns an array with all the data, with the following structure:
        
        [
            [
                [timestamp1, load_1m1], 
                [timestamp2, load_1m2], 
                [timestampx, load_1mx]
            ],
            [
                [timestamp1, load_5m1], 
                [timestamp2, load_5m2], 
                [timestampx, load_5mx]
            ],
            [
                [timestamp1, load_15m1], 
                [timestamp2, load_15m2], 
                [timestampx, load_15mx]
            ]
        ]

    being timestamp the timestamp in seconds of the date+time data.

    """


    queries = [[],[],[]]

    database = connect(database_name)
    cursor = database.cursor()
    
    if str(select_by) == "all":
        cursor.execute("""
                SELECT date, time, load_1m, load_5m, load_15m
                FROM load_values""")

    else:
        sqlite_string ="""
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
