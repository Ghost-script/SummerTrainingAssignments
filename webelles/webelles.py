#!/usr/bin/env python

import flask
from modules.jsonize import load_log
from collections import OrderedDict
import re
from jinja2 import evalcontextfilter, Markup, escape

# Create the application.
APP = flask.Flask(__name__)


loaded_data = OrderedDict(sorted(load_log("logs/logstore.json").items(), key = lambda t: t[0]))

@APP.route('/')
def index():
    """ 
    Loads logstore.json data and renders index.html
    
    """
    return flask.render_template('index.html', logs = loaded_data)


@APP.route('/log/<log_id>')
def log(log_id):
    """
    Displays the log given in the url, loaded from logstore.json.

    """
    
    return flask.render_template('log.html', log_content = loaded_data[log_id]["content"])


if __name__ == '__main__':
    APP.debug=True
    APP.run()
