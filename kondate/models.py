from kondate import db
from sqlalchemy import Column, Integer, String

class Menu(db.Model):
    __tablename__ = 'kondate'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))


def init():
    db.create_all()
