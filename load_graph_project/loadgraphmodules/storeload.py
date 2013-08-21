#!/usr/bin/env python

"""
Gets the system load and stores it in a sqlite dabatase.
Script to be run every 5 minutes using Crontab. 

"""

from os import getloadavg
from sqlite3 import *
from time import strftime, gmtime
from os.path import realpath, join
def get_load():
    
    load_1m, load_5m, load_15m = getloadavg()

    return {"date" : strftime("%Y%m%d", gmtime()),
            "time" : strftime("%H%M%S", gmtime()),
            "load_1_minute" : load_1m,
            "load_5_minutes" : load_5m,
            "load_15_minutes" : load_15m}


def store_in_sqlite(results_dict, sqlite_name):

    print sqlite_name
    database = connect(sqlite_name)
    db_cursor = database.cursor()

    db_cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS load_values (
                date BLOB NOT NULL,
                time BLOB NOT NULL,
                load_1m REAL NOT NULL,
                load_5m REAL NOT NULL,
                load_15m REAL NOT NULL,
                row_id INTEGER PRIMARY KEY AUTOINCREMENT
                )
            """)

    db_cursor.execute(
            """
            INSERT INTO load_values (
                date, time, load_1m, load_5m, load_15m
                )
            values (?, ?, ?, ?, ?);

            """, (results_dict["date"],
                  results_dict["time"],
                  results_dict["load_1_minute"],
                  results_dict["load_5_minutes"],
                  results_dict["load_15_minutes"])
            )

    database.commit()
    database.close()

if __name__ == "__main__":
    store_in_sqlite(get_load(), "/var/www/html/loadgraph/database/sloads.db")





