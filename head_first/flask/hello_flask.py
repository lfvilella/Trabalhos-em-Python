from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Flask'

@app.route('/search4')
def do_search():
    return str(search_letters('life, the universe, and everything', 'eiru,!'))

def search_letters(phrase, letters='aeiou'):
    """ This function return the specific letters in phrase """
    return set(letters).intersection(set(phrase))

app.run()
