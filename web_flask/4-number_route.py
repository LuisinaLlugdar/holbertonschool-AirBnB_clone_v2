#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Must be listening on 0.0.0.0, port 5000
- Routes:
    - '/': display “Hello HBNB!”
    - '/hbnb': display "HBNB"
    - '/c/<text>': display “C ” followed by the value of
    the text variable (replace underscore _ symbols with a space )
    - '/python/<text>': display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space ).
    The default value of text is “is cool”
    - '/number/<n>': display “n is a number” only if n is an integer
- Option strict_slashes=False in route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays a specific message when route is '/' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays a specific message when route is '/hbnb' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Displays a specific message when route is '/c/<text>' """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays a specific message when route is '/python'
    and a different one when the route is '/python/<text>'
    """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def integer_n(n):
    """ Displays a specific message when route is '/number/<n>' """
    if type(n) is int:
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
