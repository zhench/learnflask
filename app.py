from flask import Flask
from flask import redirect
from flask import make_response
from flask import abort
# from flask.ext.script import Manager # old version
from flask_script import Manager
from flask import render_template
from flask_bootstraps import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap=Bootstrap(app)


# @app.route('/')
# def hello_world():
#    return '<h1>Hello World!</h1>', 200

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect')
def redirects():
    return redirect('http://www.example.com')


@app.route('/user/<string:name>')
def welcome(name):
    # abort(404)
    return render_template('user.html', name=name)


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
