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


if __name__ == '__main__':
    app.run()
