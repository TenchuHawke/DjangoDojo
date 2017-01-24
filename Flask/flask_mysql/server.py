from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'emaildb')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.route('/')
def index():
    query = "SELECT * FROM emails"                           # define your query
    emails = mysql.query_db(query)                           # run query with query_db()
    print emails
    try:
        session['validemail']==False
    except KeyError:
        session['validemail'] = True
    return render_template('index.html')  # pass data to our template


@app.route('/emails', methods=['POST'])
def create():
    if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.form['incEmail']):
        session['validemail']=False
        return redirect('/')
    else:
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO emails (email, created_at, modified_at) VALUES (:incEmail, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {'incEmail': request.form['incEmail']}
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)

    return redirect('/results')


@app.route('/results')
def results():
        query = "SELECT * FROM emails"                           # define your query
        emails = mysql.query_db(query)                           # run query with
        return render_template('result.html', all_emails=emails)
app.run(debug=True)
