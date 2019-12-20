import datetime
import vsearch_lfvilella
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = (request.form['phrase']).lower()
    letters = request.form['letters']
    result = str(vsearch_lfvilella.search_letters(phrase, letters))
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
        print(datetime.datetime.utcnow().isoformat(),
            req.form,
            req.remote_addr,
            req.user_agent,
            res, file=log, sep=' | ')

@app.route('/viewlog')
def view_the_log():
    with open('basic_db/vsearch.log') as log:
        contents = log.read() # .read() return all file
    return escape(contents)
        
        

# This run like a security to development:
if __name__ == '__main__':
    app.run(debug=True)