#!/usr/bin/env python

import flask
from modules.jsonize import load_log
from collections import OrderedDict
from jinja2 import evalcontextfilter, Markup, escape
from os.path import dirname, join

# Create the application.
APP = flask.Flask(__name__)

# dirname(__file__) is needed to make the full path needed when deployed
loaded_data = OrderedDict(sorted(load_log(join(dirname(__file__),
                                               "logs/logstore.json")
                                         ).items(), key = lambda t: t[0]))


@APP.route('/')
def index():
    """ 
    renders index.html, passing the loaded json data as logs variable.
    
    """
    return flask.render_template('index.html', logs = loaded_data)


@APP.route('/log/<log_id>')
def log(log_id):
    """
    Displays the content of the log specified in the url.

    """
    
    return flask.render_template('log.html',
                                 log_content = loaded_data[log_id]["content"])


if __name__ == '__main__':
    APP.debug=True
    APP.run()
