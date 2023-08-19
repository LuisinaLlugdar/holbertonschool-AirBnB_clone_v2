#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Must be listening on 0.0.0.0, port 5000
- Routes:
    - '/cities_by_states': display a HTML page
- Option strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(self):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Displays a specific message when route is '/cities_by_states' """
    return render_template('8-cities_by_states.html',
                           states=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
