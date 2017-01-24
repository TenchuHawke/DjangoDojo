from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    try:
        session['count']+=1
    except KeyError:
        session['count']=1
    return render_template("index.html")

@app.route('/button', methods=['POST'])
def button():
    print request.form
    if request.form['Ninja'] == "Ninja":
        session['count'] += 1
    return redirect('/')

@app.route('/button2', methods=['POST'])
def button2():
    print request.form
    if request.form['StartOver'] == "StartOver":
        session['count'] = 0
    return redirect('/')
app.run(debug=True)
