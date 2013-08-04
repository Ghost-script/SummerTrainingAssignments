#!/usr/bin/env python

"""
Small script to store logfiles in json data files. 

"""

from json import dump, load
from sys import exit
from requests import get
from argparse import ArgumentParser

def convert_log (name, date, log_filename, json_filename, url=False):
    """
    Stores in the json_filename the content of log_filename, with the following
    format:

        {logs: [{"name" : "name_1", "date" : "date_1", "content" : "log_1"}, 
                {"name" : "name_x", "date" : "date_x", "content" : "log_x"}]}

    If json_filename doesn't exist it will be created, if it does, the new
    entry will be appended to it. 

    """
    
    
    if url:
        content = fetch_from_url(log_filename)
   
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
        print "Json file not present. Making one from scratch"
        loaded_json = {"logs" : {"log_%s" %date : new_entry}}

    else:
        loaded_json = load(json_file)
        json_file.close()
        loaded_json["log_%s" %date] = new_entry

    try:
        json_file = open(json_filename, "w")

    except IOError, e:
        exit(e)

    else:
        dump(loaded_json, json_file)


def fetch_from_url (url):
    print url
    r = get(url)

    if r.status_code == 200:
        return r.text

    else:
        exit ("Error: Server returns %s -- %s" % (r.status_code, r.reason))


def load_log (date, json_filename):
    try:
        json_file = open(json_filename)

    except IOError:
        exit ("Error. Json file '%s' not found" % json_filename)

    else:
        return load(json_file)["logs"][date]


def fetch_from_arnauorriols(init_day, end_day, month, json_file):
    
    month = ("%.2i" %month)

    for x in range(init_day, end_day):
        x = ("%.2i" %x)

        convert_log("test", "%s.%s" %(x, month), "http://arnauorriols.com/~ServerAdmin/irclogs/2013/" + x + "." + month + "/%23dgplug.log", json_file, True)


if __name__ == "__main__":
    args = ArgumentParser(description="Converts log files into json databases")
    args.add_argument("name", help="Name of the log")
    args.add_argument("date", help="Date of the log")
    args.add_argument("path", help="Path/url of the log")
    args.add_argument("-u", "--url", help="Indicates path is http url", action="store_true")
    args.add_argument("-j", "--jsonFile", help="Specifies Json file's path and name. Default: ./logstore.json", default="./logstore.json")
    
    parsed = args.parse_args()

    if parsed.url:
        convert_log(parsed.name, parsed.date, parsed.path, parsed.jsonFile, True)

    else:
        convert_log(parsed.name, parsed.date, parsed.path, parsed.jsonFile, False)



