from flask import Flask
from flask import redirect
from flask import make_response
from flask import abort
# from flask.ext.script import Manager # old version
from flask_script import Manager
from flask import render_template
from flask_bootstraps import Bootstrap
from flask_moment import Moment
from datetime import datetime
import time

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# @app.route('/')
# def hello_world():
#    return '<h1>Hello World!</h1>', 200

@app.route('/')
def index():
    print(datetime.utcnow())
    dtime = datetime.utcnow()
    un_time = time.mktime(dtime.timetuple())
    print(un_time)
    return render_template('index.html', current_time=dtime)


@app.route('/redirect')
def redirects():
    return redirect('http://www.example.com')


@app.route('/user/<string:name>')
def welcome(name):
    # abort(404)
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
