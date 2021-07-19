import os
from uuid import uuid4

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
    player_id = uuid4()
    session['player_id'] = player_id
    # chessboard = ChessBoard()
    return render_template('game_awaiting_page.html')


@app.route('/join/')
def join_game():
    chessboard_id = request.POST.get('id')
    # chessboard = ChessBoard(chessboard_id)
    # if chessboard is not None:
        # player_id = 0
        # session['player_id'] = uuid4()
        # chessboard.add_second_player(player_id)
        # chessboard.start_game()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    return render_template('register.html')


if __name__ == '__main__':
    print(models.User)
    app.run(debug=True)
