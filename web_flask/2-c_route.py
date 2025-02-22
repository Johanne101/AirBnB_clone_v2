#!/usr/bin/python3
"""
Script starts a Flask web application
- listening on 0.0.0.0,
- port 5000
Routes:
>> `/` : display “Hello HBNB!”
>> `/hbnb` : display “HBNB”
>> `/c/<text>` : display “C ”
- Route definition option: strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def redirect():
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return('C {}'.format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
