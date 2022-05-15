#!/usr/bin/python3
"""A minimal Flask application looks something like this"""
from pickle import TRUE
from flask import Flask
from flask import render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text='is cool'):
    """display default content if variable path is none.
       Otherwise prints the variable
    """
    return '%s' % 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays only integers"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    """displays a template with a integer"""
    return render_template('5-number.html', x=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEven(n):
    """displays a template with a integer depending if is even or not"""
    return render_template('6-number_odd_or_even.html', x=n)


if __name__ == '__main__':
    app.run()
