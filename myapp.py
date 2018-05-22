from flask import Flask, session, url_for, flash
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
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class NameForm(FlaskForm):
    name = StringField('What is you name?', validators=[DataRequired()])
    submit = SubmitField('Submit ')


class Role(db.Model):
    __tablename__ = 'roles'  # define the name of table in database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %>' % self.username


# @app.route('/')
# def hello_world():
#    return '<h1>Hello World!</h1>', 200

@app.route('/', methods=['GET', 'POST'])
def index():
    print(datetime.utcnow())
    name = None
    form = NameForm()
    try:
        if form.validate_on_submit():
            old_name = session['name']
            print(old_name)
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name')
            session['name'] = form.name.data
            return redirect(url_for('index'))

        name = session['name']
    except KeyError:
        name = session['name'] = ''
    return render_template('index.html', form=form, name=name)


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
