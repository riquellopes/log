# coding: utf-8
# from factory import RelatedFactory, lazy_attribute
import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory
from facebook.models import Person
from facebook.db import db


class PersonFactory(Factory):
    class Meta:
        model = Person
        sqlalchemy_session = db.session

    facebookId = 10
    username = factory.Faker('user_name')
    name = factory.Faker('name')
    gender = "male"
