from email.errors import MessageError
import os
import dotenv

from pymongo import MongoClient
from flask import Flask, redirect
from flask import render_template, request
from utils.user import insert_user, login_user

dotenv.load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')

app = Flask(__name__, template_folder='templates')
cluster = MongoClient(MONGO_URL)

main_db = cluster['main']
tasks = main_db['tasks']
users = main_db['users']


@app.route('/')
def index():
    return redirect('/register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logged_in = login_user(request.form['username'], request.form['password'])

        if type(logged_in) == str:
            print(logged_in)
            return render_template('login.html', error=True, message=logged_in)

        else:
            print(logged_in)
            return redirect('/explore')


    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        inserted = insert_user(request.form['username'], request.form['password'])

        if inserted is True:
            return redirect('/explore')

        else:
            return render_template('register.html', error=True)

    return render_template('register.html')


@app.route('/explore')
def explore():
    return render_template('explore.html', explore="active")


@app.route('/planner')
def planner():
    return render_template('planner.html', explore="active")


@app.route('/learn')
def learn():
    return render_template('learn.html', explore="active")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
