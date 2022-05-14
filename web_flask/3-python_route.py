#!/usr/bin/python3
"""
Script starts a Flask web application
- listening on 0.0.0.0,
- port 5000
Routes:
>> `/` : display “Hello HBNB!”
>> `/hbnb` : display “HBNB”
    - The default value of <text> is “is cool”
>> `/c/<text>` : display “C ”
>> `/python/(<text>)` : display “Python ”
 (replace underscore _ symbols with a space )
- Route definition option: strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return('C {}'.format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text_py>', strict_slashes=False)
def python_route(text_py='is cool'):
    return('Python {}'.format(text_py.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
