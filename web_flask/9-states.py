#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Must be listening on 0.0.0.0, port 5000
- Routes:
    - '/states_list' and '/states': display a HTML page
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


@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays a specific message when route is '/states_list'
     or '/states' """
    return render_template('7-states_list.html',
                           states=storage.all("State").values())


@app.route('/states/<id>')
def if_state_id(id):
    """ Displays a specific message when route is '/states/<id>' """
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state
    return render_template('9-states.html',
                           state_obj=state_obj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
