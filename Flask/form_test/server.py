from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms

    session['formName'] = request.form['name']
    session['formLoc'] = request.form['location']
    session['formLang'] = request.form['language']
    session['formComment'] = request.form['comment']
    print session['formName']
    print session['formLoc']
    print session['formLang']
    print session['formComment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html", name=session['formName'], location=session['formLoc'], language=session['formLang'], comment=session['formComment'])
    if request.method == 'POST':
        if request.form['submit'] == 'back':
            return redirect('/')
app.run(debug=True)  # run our server
