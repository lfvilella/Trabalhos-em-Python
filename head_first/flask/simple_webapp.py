from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'YouNeverGetTheKey'

@app.route('/')
def hello():
    return "Hello, it's a simple webpage"

@app.route('/page1')
@check_logged_in
def page1():
    return 'This is page1.'

@app.route('/page2')
@check_logged_in
def page2():
    return 'This is page2.'

@app.route('/page3')
@check_logged_in
def page3():
    return 'This is page3.'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'

if __name__ == '__main__':
    app.run(debug=True)