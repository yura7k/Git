from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name = 'Yuriy'
    return render_template('index.html', name=name)

@app.route('/en')
def en():
    return ("Hallo World!!!")