from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.route('/')
def index():
    try:
        session['validemail']==False
    except KeyError:
        session['validemail'] = True

    # check to see if userid is in session, if not then create it
    try:
        session['UserID'] == ""
    except KeyError:
        session['UserID']=""

    return redirect('/wall')
    return render_template('index.html')  # pass data to our template


# @app.route('/login', methods=['POST'])
# def login():
#     if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.form['incEmail']):
#         session['validemail']=False
#         return redirect('/')
#     else:
#         # Write query as a string. Notice how we have multiple values
#         # we want to insert into our query.
#         query = "INSERT INTO wall (email, created_at, modified_at) VALUES (:incEmail, NOW(), NOW())"
#         # We'll then create a dictionary of data from the POST data received.
#         data = {'incEmail': request.form['incEmail']}
#         # Run query, with dictionary values injected into the query.
#         mysql.query_db(query, data)
#
#
#     return redirect('/wall')


@app.route('/wall')
def wall():
        messages_inc = "select messages.id, messages.message, date_format(messages.created_at,'%d %b %y %h:%i %p') as m_created_at,  concat(concat(upper(left(first_name,1)), lower(substring(first_name,2))), concat(upper(left(last_name,1)), lower(substring(last_name,2)))) as message_user from messages join users on users.id = messages.user_id order by messages.id;"
        comments_inc = 'select comments.id as cId, comments.message_id, comments.comment, date_format(comments.created_at,"%d %b %y %h:%i %p") as c_created_at, concat(concat(upper(left(first_name,1)), lower(substring(first_name,2))), concat(upper(left(last_name,1)), lower(substring(last_name,2)))) as comment_user from comments join users on comments.user_id = users.id order by comments.created_at asc;'     # define your query

        mess_inc = mysql.query_db(messages_inc)
        com_inc = mysql.query_db(comments_inc)                           # run query with
        return render_template('wall.html', messages_all=mess_inc, comments_all=com_inc)

@app.route('/add', methods=['POST'])
def add():
        tempId=1
        queryM = 'INSERT INTO messages (message, created_at, modified_at, user_id) values ("{}" , now(), now(), "{}");'.format(request.form['commenttext'], tempId)
        queryC = 'INSERT INTO comments (comment, created_at, modified_at, message_id, user_id) values ("{}" , now(), now(), "{}", "{}");'.format(request.form['commenttext'], request.form['id'], tempId)


        if int(request.form['id'])<0:
            print "Message"
            mysql.query_db(queryM)
        else:
            mysql.query_db(queryC)
            print "Comment"
        return redirect('/wall')


app.run(debug=True)
