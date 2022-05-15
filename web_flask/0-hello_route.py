#!/usr/bin/python3
"""A minimal Flask application looks something like this"""
from pickle import TRUE
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """main path to the flask application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
