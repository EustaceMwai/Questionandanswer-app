from typing import re

from flask import Flask, render_template, g, request
from database import get_db, init_db_command

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass

    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/question')
def question():
    return render_template('question.html')


@app.route('/answer')
def answer():
    return render_template('answer.html')


@app.route('/ask')
def ask():
    return render_template('ask.html')


@app.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')


@app.route('/users')
def users():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.cli.add_command(init_db_command)