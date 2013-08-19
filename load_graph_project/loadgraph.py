#!/usr/bin/env python


from flask import Flask, request
from urlparse import parse_qs
from loadgraphmodules.readsqlite import fetch_by_hours

app = Flask(__name__)

@app.route('/')
def index():

    value_type = request.args.get("vtype")
    sort_by = request.args.get("selectby")
    start_ref = request.args.get("start")
    end_ref = request.args.get("end")

    plot_data = manage_query(parse_qs(request.query_string, keep_blank_values = True))

    return render_template("index.html", plot_data = plot_data)


def manage_query(query_string_dict):

    return fetch_database(query_string_dict["selectby"], query_string_dict["start"], query_string_dict["end"], "/var/www/html/loadplot/loads.db")

if __name__ == '__main__':
    app.run()
