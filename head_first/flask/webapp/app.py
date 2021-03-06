import datetime
import vsearch_lfvilella
from flask import Flask, render_template, request, escape, session, copy_current_request_context
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread

app = Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB',}

app.secret_key = 'ThatKeyShouldBeHard'

@app.route('/search4', methods=['POST'])
def do_search():

    @copy_current_request_context
    def log_request(req:'flask_request', res:str):
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)"""

                cursor.execute(_SQL, (req.form['phrase'],
                                    req.form['letters'],
                                    req.remote_addr,
                                    req.user_agent.browser,
                                    res, ))
        except ConnectionError as err:
            print('Is your database on? Error:', str(err))
        except CredentialsError as err:
            print('Is your credentials right? Error:', str(err))
        except SQLError as err:
            print('Is your query correct? Error:', str(err))
        except Exception as err:
            print('Something went wrong:', str(err))
        return 'Error'

    phrase = (request.form['phrase']).lower()
    letters = request.form['letters']
    result = str(vsearch_lfvilella.search_letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, result))
        t.start()

    except Exception as error:
        print('Loggin failed with this error:', str(error))

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

@app.route('/viewlog')
@check_logged_in
def view_the_log():
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select ts, phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        
        titles = ('Date', 'Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results',)
        return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents)
    except ConnectionError as err:
        print('Is your database on? Error:', str(err))
    except CredentialsError as err:
        print('Is your credentials right? Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'
        
@app.route('/viewreports')
@check_logged_in
def view_the_reports():
    count_request = """select count(*) from log"""
    count_letters = """select count(letters) as 'count', letters 
                        from log 
                        group by letters 
                        order by count desc 
                        limit 1"""
    count_ip = """select distinct ip from log"""
    count_browser = """select browser_string, count(browser_string) as 'count' 
                        from log 
                        group by browser_string 
                        order by count desc 
                        limit 1"""

    dados = [
        {'title': 'Requests', 'value': run_sql(count_request)},
        {'title': 'Letters', 'value': run_sql(count_letters)},
        {'title': 'Ip', 'value': run_sql(count_ip)},
        {'title': 'Browser', 'value': run_sql(count_browser)},
    ]

    return render_template('viewreports.html', dados=dados)

def run_sql(command:str):
    with UseDatabase(app.config['dbconfig']) as cursor:
        cursor.execute(command)
        return cursor.fetchone()

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'

# This run like a security to development:
if __name__ == '__main__':
    app.run(debug=True)