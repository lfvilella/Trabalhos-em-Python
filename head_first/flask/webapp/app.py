from flask import Flask, render_template, request

app = Flask(__name__)


def search_letters(phrase, letters='aeiou'):
    return set(letters).intersection(set(phrase))

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search_letters(phrase, letters))
    return render_template('results.html',
                            the_title='Here are your results:',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_results=result)

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                            the_title='Welcome to Search For Letters on the Web!')

# This run like a security to development:
if __name__ == '__main__':
    app.run(debug=True)