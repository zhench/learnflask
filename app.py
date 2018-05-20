from flask import Flask
from flask import redirect
from flask import make_response
from flask import abort

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#    return '<h1>Hello World!</h1>', 200

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '44')
    return response


@app.route('/redirect')
def redirects():
    return redirect('http://www.example.com')


@app.route('/user/<int:name>')
def welcome(name):
    # abort(404)
    return '<h1>Hello %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
