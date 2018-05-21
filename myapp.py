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
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is you name?', validators=[DataRequired()])
    submit = SubmitField('Submit ')


# @app.route('/')
# def hello_world():
#    return '<h1>Hello World!</h1>', 200

@app.route('/',methods=['GET','POST'])
def index():
    print(datetime.utcnow())
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('index.html', form=form,name=name )


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
