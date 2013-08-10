#!/usr/bin/env python

"""
jsonize module. Stores logs into a json file and retrieves them for further use

"""

from json import dump, load
from sys import exit
from requests import get
from argparse import ArgumentParser
from datetime import date
from formattools import format2date

def convert_log (name, date, log_filename, json_filename, url = False,
                 server_loaded = False):
    """
    Stores in the json_filename the content of log_filename, with the following
    format:

        {"logs" : {"log_id1" : {"name" : "name_1", "date" : "date_1",
                                "content" : "log_1"}, 
                   "log_idx" : {"name" : "name_x", "date" : "date_x",
                                "content" : "log_x"}
                  }
        }

    If json_filename doesn't exist it will be created, if it does, the new
    entry will be appended to it. 

    If url == True, log_filename is an url which will be passed as argument
    to fetch_from_url, which will fetch the log (plain text) using requests.
    The url have to point to a log (or any plain-text) file.

    If server_loaded == True, log_filename is an already open file, such as
    a fileStorage object in request.files.

    It's important to match the format of the date for all entries. To achieve
    this, the module formattools is provided. It's recommended to apply
    formattools.format2date function to the variable date before passing it to
    this function.

    """
 
    if url:
        content = fetch_from_url(log_filename)

    elif server_loaded:
        content = log_filename.read()

    else:
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
        print "Json file not found. Making one from scratch"
        loaded_json = {"logs" : {"log_%s" %date : new_entry}}

    else:
        loaded_json = load(json_file)
        json_file.close()
        loaded_json["logs"]["log_%s" %date] = new_entry

    try:
        json_file = open(json_filename, "w")

    except IOError, e:
        exit(e)

    else:
        dump(loaded_json, json_file)


def fetch_from_url (url):
    """
    Uses requests to get the log text from the url given as parameter.
    The url have to point to a plain-text file, such as: 
    "http.example.com/mylog.log"

    Returns the text of the log.

    """

    print "Retrieving '%s'..." % url,

    r = get(url)

    if r.status_code == 200:
        print "  --  DONE"
        return r.text

    else:
        exit ("Error: Server returns %s -- %s" % (r.status_code, r.reason))


def load_log (json_filename, log_id = None):
    """
    Loads the json_filename Json file and returns the value of the key "logs",
    which should contain all logs stored in it. This value is a dictionary the
    keys of which are the logs id, and it's values the corresponent log info.

    If log_id specified, only returns the specified log information.

    """

    try:
        json_file = open(json_filename)

    except IOError:
        exit ("Error. Json file '%s' not found" % json_filename)

    else:
        if log_id:
            return load(json_file)["logs"][log_id]

        else:
            return load(json_file)["logs"]


def fetch_from_arnauorriols(init_day, end_day, month, json_file):
    """
    Fetches all the logs of #dgplug channel stored in 
    "http://www.arnauorriols.com/irclogs/2013" between the days "init_day"
    and "end_day" of the given "month". 
    
    Stores these logs in the json file "json_file".

    """

    for x in range(int(init_day), int(end_day)):
        
        full_date = date(2013, int(month), x)
        formated_date = format2date(x, month)
        convert_log("#dgplug - %s" %full_date.strftime("%a, %d of %B"),
                    formated_date,
                    "http://arnauorriols.com/~ServerAdmin/irclogs/2013/" + 
                    formated_date + "/%23dgplug.log", json_file, True)


if __name__ == "__main__":

    args = ArgumentParser(description="Converts log files into json databases")
    
    args.add_argument("name", help = "Name of the log")
    args.add_argument("date", help = "Date of the log")
    args.add_argument("path", help = "Path/url of the log")
    args.add_argument("-u", "--url", help = "Indicates path is http url",
                      action = "store_true")
    args.add_argument("-j", "--jsonFile", help = "Specifies Json file's path"
                      "and name. Default: ./logstore.json",
                      default = "./logstore.json")
    
    parsed = args.parse_args()

    if parsed.url:
        convert_log(parsed.name, parsed.date, parsed.path, parsed.jsonFile,
                    True)

    else:
        convert_log(parsed.name, parsed.date, parsed.path, parsed.jsonFile,
                    False)



