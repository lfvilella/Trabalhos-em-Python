from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Flask'

def search_letters(phrase, letters='aeiou'):
    return set(letters).intersection(set(phrase))

@app.route('/search4')
def do_search():
    return str(search_letters('life, the universe, and everything', 'eiru,!'))

@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                            the_title='Welcome to Search For Letters on the Web!')


app.run()