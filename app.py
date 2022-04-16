from flask import Flask, redirect
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    return redirect('/explore')

@app.route('/explore')
def index():
    return render_template('explore.html', explore="active")

@app.route('/planner')
def planner():
    return render_template('planner.html', explore="active")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

app.run(port=5000, debug=True)