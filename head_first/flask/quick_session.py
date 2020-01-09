from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'IDontKnowMyKey'

@app.route('/setuser/<user>')
def setuser(user:str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser():
    return 'User value is currently set to: ' + session['user']

@app.route('/<arg>')
def test(arg):
    return 'This is your arg: ' + arg

if __name__ == '__main__':
    app.run(debug=True)