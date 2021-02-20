from flask import Flask, render_template, request
from logic.chessboard import ChessBoard
# from logic.figures import King

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/', methods=['POST'])
def create_game():
    print('CREATE')
    chessboard = ChessBoard()
    return render_template('game_awaiting_page.html', chessboard_id=chessboard.id)


@app.route('/join/')
def join_game():
    chessboard_id = request.POST.get('id')
    chessboard = ChessBoard(chessboard_id)
    if chessboard is not None:              #
        chessboard.add_second_player()      # then start game
