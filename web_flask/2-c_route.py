#!/usr/bin/python3
"""A minimal Flask application looks something like this"""
from pickle import TRUE
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """main path to the flask application"""
    return 'Hello HBNB!!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """path to hbnb in the flask application"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cis(text):
    """url section with a variable as part of their path"""
    return '%s' % 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run()
