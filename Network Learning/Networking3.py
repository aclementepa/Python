from flask import Flask, abort, redirect, url_for
from flask.helpers import url_for
app = Flask(__name__)

# runs a website on localhost:5000


def hello_world():
    return 'Hello Tutorialspoint'

# @app.route('/')
# def index(): pass

@app.route('/')
def index():
    return redirect(url_for('login'))

# @app.route('/login')
# def login(): pass

@app.route('/login')
def login():
    abort(401)

@app.route('/user/')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('index', _external=True))
    print(url_for('login'))
    # print(url_for('login', next='/'))
    # print(url_for('profile', username='Tutorials Point'))

# if __name__ == '__main__':
#     app.run()


