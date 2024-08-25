#!/usr/bin/python3
"""Script that starts a flask web app and display Hello HBNB"""

from flask import Flask

# Instantiate a flask app
app = Flask(__name__)


# define the hbnb route
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HNBN!"""
    return 'Hello HBNB!'


# run if main on port 5000 on any host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
