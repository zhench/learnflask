from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<int:name>')
def welcome(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
