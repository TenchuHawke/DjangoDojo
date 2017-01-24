from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name="bob")


@app.route('/sucess')
def success():
    return render_template('sucess.html')
app.run(debug=True)
