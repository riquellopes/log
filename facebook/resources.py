# coding: utf-8
import http
import requests
import json
from flask import current_app as app, Response, request
from flask_restful import Resource
from webargs.flaskparser import use_args
from facebook.schemas import PersonSchema
from facebook.db import db
from facebook.models import Person


class PersonResource(Resource):

    @use_args(PersonSchema(strict=True), locations=("json",))
    def post(self, args):
        app.logger.info("Init method post /v1/person/")
        person = args
        try:
            response = requests.get(app.config['GRAPH_FB'].format(person.facebookId))
            json = response.json()
            app.logger.info("Facebook response - json:{}".format(str(json)))

            person.username = json['username']
            person.name = json['name']
            person.gender = json['gender']

            db.session.add(person)
            db.session.commit()
        except Exception:
            app.logger.exception("Error to process information.")
            return "", http.HTTPStatus.BAD_REQUEST
        return "", http.HTTPStatus.CREATED

    def delete(self, person_id):
        app.logger.info("Init method delete /v1/person/{}.".format(person_id))
        try:
            Person.query.get(person_id).query.delete()
            db.session.commit()
        except Exception:
            app.logger.exception("Error to delete person.")
            return "", http.HTTPStatus.BAD_REQUEST
        return "", http.HTTPStatus.OK

    def get(self):
        app.logger.info("Init method get /v1/person")

        limit = request.args.get('limit', None)
        p = Person.query.filter()
        if limit is not None:
            p = p.limit(limit)

        return Response(
            json.dumps([PersonSchema().dump(i).data for i in p], indent=2), mimetype='application/json')
