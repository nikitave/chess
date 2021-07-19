from chess import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100))
    image = db.Column(db.String(200), nullable=False, default='default.jpg')

    def __repr__(self):
        return f'User(username={self.username}, email={self.email}, image_path={self.image_path})'


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    players = db.relationship('Player', backref='game')
    moves = db.relationship('Move', backref='game')

    def __repr__(self):
        return f'Game(player_1_id={self.player_1_id}, player_2_id={self.player_2_id}, moves={self.moves})'


class Player(db.Model):
    """Helper model for game being able to have 2 players"""
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.ForeignKey('game.id'), nullable=False)


class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.ForeignKey('game.id'), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    coords = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'Move(game_id={self.game_id}, index={self.index}, coords={self.coords})'
