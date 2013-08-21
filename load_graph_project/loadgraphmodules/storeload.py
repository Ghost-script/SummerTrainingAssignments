#!/usr/bin/env python

"""
Gets the system load and stores it in a sqlite dabatase.
Script to be run every 5 minutes using Crontab. 

"""

from os import getloadavg
from sqlite3 import connect
from time import strftime, gmtime



def get_load():
    """
    Returns the average load data in a dict containing:
        {
            date : day of the data, as 20130819 (%Y%m%d)
            time : time of the data, as 145010 (%H%M%S)
            load_1_minute : load of last minute
            load_5_minutes : load of last 5 minutes
            lad_15_minutes : load of last 15 minutes
        }
    
    """


    load_1m, load_5m, load_15m = getloadavg()

    return {"date" : strftime("%Y%m%d", gmtime()),
            "time" : strftime("%H%M%S", gmtime()),
            "load_1_minute" : load_1m,
            "load_5_minutes" : load_5m,
            "load_15_minutes" : load_15m
           }



def store_in_sqlite(results_dict, sqlite_name):
    """
    Handles all the connection with the database given in sqlite_name. 
    If the database is new, creates a new table named 'load_values' with the 
    following schema:

    |  date  |  time  |  load_1m  |  load_5m  |  load_15m  |  row_id  |
    --------------------------------------------------------------------
    |  BLOB  |  BLOB  |    REAL   |    REAL   |    REAL    |  INTEGER |

    
    Then it stores the content passed in the parameter results_dict, which must
    have the structure of those returned by get_load.

    """


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

    """This script is fired every 5 minutes using the crontab feature"""
    store_in_sqlite(get_load(), "/var/www/html/loadgraph/database/sloads.db")





