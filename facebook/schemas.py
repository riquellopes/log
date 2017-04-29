# coding: utf-8
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields
from facebook.models import Person
from facebook.db import db


class PersonSchema(ModelSchema):

    class Meta:
        model = Person
        sqla_session = db.session


class PersonFormSchema(Schema):
    facebookId = fields.Int(required=True)
