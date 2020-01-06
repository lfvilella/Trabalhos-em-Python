import datetime
import vsearch_lfvilella
from flask import Flask, render_template, request, escape
import mysql.connector

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
    dbconfig = {'host':'127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))
    
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/viewlog')
def view_the_log():
    contents = []
    with open('basic_db/vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    
    titles = ('Date', 'Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents)
        
        

# This run like a security to development:
if __name__ == '__main__':
    app.run(debug=True)