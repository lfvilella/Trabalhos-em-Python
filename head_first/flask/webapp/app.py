import datetime
from flask import Flask, render_template, request, escape

app = Flask(__name__)


def search_letters(phrase, letters='aeiou'):
    return set(letters).intersection(set(phrase))

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search_letters(phrase, letters))
    log_request(request, result)
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

def log_request(req:'flask_request', res:str) -> None:
    with open('basic_db/vsearch.log', 'a') as log:
        print(datetime.datetime.utcnow().isoformat(), req, req.form, res, file=log)

@app.route('/viewlog')
def view_the_log():
    with open('basic_db/vsearch.log') as log:
        contents = log.read() # .read() return all file
    return escape(contents)
        
        

# This run like a security to development:
if __name__ == '__main__':
    app.run(debug=True)