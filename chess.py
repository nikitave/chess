import os

from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

import game.models as models

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://greg:f1jyr2atj0g@localhost/chess'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=['POST'])
def create_game():
    return render_template('game_awaiting_page.html')


@app.route('/join/')
def join_game():
    pass


@app.route('/register/', methods=['GET', 'POST'])
def register():
    # if request.method == 'POST':
        # form = 
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
