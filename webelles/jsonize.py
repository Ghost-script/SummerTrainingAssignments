#!/usr/bin/env python

"""
Small script to store logfiles in json data files. 

"""

from json import dump, load
from sys import exit

def convert_log (name, date, log_filename, json_filename):
    """
    Stores in the json_filename the content of log_filename, with the following
    format:

        {logs: [{"name" : "name_1", "date" : "date_1", "content" : "log_1"}, 
                {"name" : "name_x", "date" : "date_x", "content" : "log_x"}]}

    If json_filename doesn't exist it will be created, if it does, the new
    entry will be appended to it. 

    """


    try:
        log_file = open(log_filename)
        
    except:
        exit("Error. File " +  log_filename + " couldn't be oppened.")

    else:
        content = log_file.read()
        log_file.close()

    new_entry = {"name" : name, "date" : date, "content" : content}

    try:
        json_file = open (json_filename, "r")

    except IOError, e:
        print "Json file not present. Making one from scratch"
        loaded_json = {"logs" : [new_entry]}

    else:
        loaded_json = load(json_file)
        json_file.close()
        loaded_json["logs"].append(new_entry)

    try:
        json_file = open(json_filename, "w")

    except IOError, e:
        exit(e)

    else:
        dump(loaded_json, json_file)


if __name__ == "__main__":
    convert_log ("Dgplug Training Session", "28.07", "logs/28-07#dgplug.log", "logstore.json")
