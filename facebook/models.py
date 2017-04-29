# coding: utf-8
from facebook.db import db


class Person(db.Model):
    __tablename__ = 'person'
    username = db.Column(db.String(100))
    facebookId = db.Column('facebookId', db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    gender = db.Column(db.String(60))
