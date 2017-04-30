# coding: utf-8
import os

GRAPH_FB = "http://graph.facebook.com/{}"
DEBUG = True
SECRET_KEY = 'ldeyrweuy11yu2333uy3iu'
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
