#!/usr/bin/python3
""" flask running"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    if not text:
        # If text is empty, return a custom 404 response
        return """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.
         If you entered the URL manually, please check your spelling
         and try again.</p>
        """, 404

    # Replace underscores with spaces
    text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(text_with_spaces)


@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    if not text:
        text_with_spaces = "is cool"
    else:
        text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(text_with_spaces)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
