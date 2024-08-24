#!/usr/bin/python3
"""Script that starts a flask web app and display defined routes"""

from flask import Flask

# Instantiate a flask app
app = Flask(__name__)


# define the hello hbnb route
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HNBN!"""
    return 'Hello HBNB!'


# define the hbnb route
@app.route("/hbnb", strict_slashes=False)
def view_hbnb():
    """Returns HNBN"""
    return 'HBNB'


# define the display c text route
@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Returns text passed!"""
    return 'C {}'.format(text.replace('_', ' '))


# define the display python txt route
@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text):
    """Returns text passed!"""
    return 'Python {}'.format(text.replace('_', ' '))


# run if main on port 5000 on any host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
