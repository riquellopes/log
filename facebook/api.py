# coding: utf-8
from flask_restful import Api
from facebook import app as application
from facebook.db import db
from facebook.resources import PersonResource


def setup_app():
    db.init_app(application)
    api = Api(application, prefix="/v1")

    api.add_resource(PersonResource, '/person', '/person/<int:person_id>')

    return application


app = setup_app()


@app.before_request
def berore():
    db.create_all()
