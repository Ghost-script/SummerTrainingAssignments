#!/usr/bin/env python

# import sqlite3
import flask
from modules.jsonize import load_log, convert_log
from modules.formattools import format2date
from ordereddict import OrderedDict
from os.path import dirname, join
from werkzeug import secure_filename
from werkzeug.contrib.cache import SimpleCache


# Configuration
DATABASE = join(dirname(__file__), "database/webelles.db")
DEBUG = True
SECRET_KEY = "thisisasecretkey"
USERNAME = "JCaselles"
PASSWORD = "thisisapassword"

# Create the application.
APP = flask.Flask(__name__)
APP.config.from_object(__name__) # Consider using envvar() in the future

# Create cache instance
cache = SimpleCache(default_timeout = 3000)


"""
def connect_db():
    return sqlite3.connect(APP.config["DATABASE"])

"""



@APP.route("/login", methods = ["GET", "POST"])
def login():
    """

    """

    error = None

    if flask.request.method == "POST":
        if flask.request.form["username"] != APP.config["USERNAME"]:
            error = "Invalid username"
 
        elif flask.request.form["password"] != APP.config["PASSWORD"]:
            error = "Invalid password"

        else:
            flask.session["logged_in"] = True
            return flask.redirect(flask.url_for("index"))

    return flask.render_template("login.html", error = error)



@APP.route("/logout")
def logout():
    """

    """

    flask.session.pop("logged_in", None)
    return flask.redirect(flask.url_for("index"))



@APP.route('/')
def index():
    """ 
    renders index.html, passing the loaded json data as logs variable.
    
    """
    
    if not cache.get("data"):
        cache.set("data",
                  OrderedDict(sorted(load_log(join(dirname(__file__),
                                                   "logs/logstore.json")
                                             ).items(), key = lambda t: t[0])))

    return flask.render_template('index.html', logs = cache.get("data"))



@APP.route('/log/<log_id>')
def log(log_id):
    """
    Displays the content of the log specified in the url.

    """

    return flask.render_template('log.html',
                            log_content = cache.get("data")[log_id]["content"])



@APP.route('/uploadlog', methods = ["GET", "POST"] )
def upload_log():
    """

    """

    error = None

    if flask.request.method == "POST":
        file_uploaded = flask.request.files["filepath"]

        if file_uploaded.content_type == "text/plain":
            formated_date = format2date(flask.request.form["date_day"],
                                        flask.request.form["date_month"])

            convert_log(flask.request.form["title"],
                        formated_date, file_uploaded,
                        join(dirname(__file__), "logs/logstore.json"),
                        server_loaded = True
                        )

            cache.set("data",
                      OrderedDict(sorted(load_log(join(dirname(__file__),
                                                       "logs/logstore.json")
                                                 ).items(),
                                         key = lambda t: t[0])))

            return flask.redirect(flask.url_for("index"))

        else:
            error = "File uploaded is not accepted. It has to be a .log or" \
                    " plain text file"

    return flask.render_template('upload_log.html', error = error)



if __name__ == '__main__':
    APP.run()
