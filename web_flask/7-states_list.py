#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Must be listening on 0.0.0.0, port 5000
- Routes:
    - '/states_list': display a HTML page
- Option strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage():
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()

@app.route("/states_list>", strict_slashes=False)
def states_list():
    """ Displays a specific message when route is '/states_list' """
    return render_template("7-states_list.html",
                           states=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
