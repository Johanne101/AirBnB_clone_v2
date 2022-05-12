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
>> `/python/(<text>)` : display “Python ” (replace underscore _ symbols with a space )
>> `/number/<n>` : display “n is a number” only if n is an integer

    - `h1` tag: “Number: n” inside the tag body
>> `/number_template/<n>` : display a HTML page only if n is an integer:
- Route definition option: strict_slashes=False
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_n_route(n):
    return(render_template('5-number.html', n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
