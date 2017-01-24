from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if not 'number' in session:
        session['number']=random.randrange(0,101)
        print session['number']
    if not 'result' in session:
        session['result']=-1
        print session['result']
    return render_template("index.html")

@app.route('/formGuess', methods=["POST"])
def formGuess():
    if request.form['guess']=='':
        session.clear()
        return redirect('/')
    session['result']=int(request.form['guess'])
    return redirect('/')


app.run(debug=True)
