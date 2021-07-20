from passlib.hash import argon2

from models import db, User, Player, Game, Move


def sign_up(username: str, email: str, password: str, image: str):          # TODO change image type hint
    pass


def sign_in(login: str, password: str):
    username, email = None, None
    if '@' in login:
        email = login
    else:
        username = login
    pass
