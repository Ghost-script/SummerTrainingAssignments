#!/usr/bin/env python


from flask import Flask, request, render_template
from urlparse import parse_qs
from loadgraphmodules.readsqlite import fetch_database
from re import split
app = Flask(__name__)

@app.route('/')
def index():


    try:
        
        plot_data = manage_query(parse_qs(request.query_string, keep_blank_values = True))
        return render_template("index.html", plot_data = plot_data )

    except KeyError:
        print "Key Eerro, query string = %s" % request.query_string
        return render_template("index.html", plot_data = None)

def manage_query(query_string_dict):
    print query_string_dict
    start = "".join(split("\.+|/+|-+|:+|'+", query_string_dict["start"][0]))
    end = "".join(split("\.+|/+|-+|:+|'+", query_string_dict["end"][0]))
    print start, end, query_string_dict["day_for_time"][0]
    if not "day_for_time" in query_string_dict:
        print "no day for time in query"
        query_string_dict["day_for_time"] = ""

    else:

        day_for_time = "".join(split("\.+|/+|-+|:+|'+", query_string_dict["day_for_time"][0]))
    return fetch_database(query_string_dict["selectby"][0],start, end, day_for_time, "/var/www/html/loadgraph/database/sloads.db")

if __name__ == '__main__':
    app.debug=True
    app.run()
