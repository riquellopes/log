# coding: utf-8
import pytest
import responses
import json
from .factories import PersonFactory


@pytest.fixture
def user_one():
    return PersonFactory.create()


@pytest.fixture
def list_of_user():
    return [PersonFactory.create(facebookId=f) for f in range(1, 3)]


@responses.activate
def test_should_get_status_201_when_information_about_user_are_saved(test_client, app):
    data = {
        "username": "henrique",
        "id": 1,
        "name": "Henrique Lopes",
        "gender": "male"
    }

    url = app.config['GRAPH_FB'].format(1)
    responses.add(responses.GET, url,
                  body=json.dumps(data),
                  status=200,
                  content_type="application/json")

    response = test_client.post("/v1/person", data=json.dumps({"facebookId": 1}), content_type='application/json')
    assert response.status_code == 201


def test_should_get_status_204_when_information_about_are_removed(test_client, user_one):
    response = test_client.delete("/v1/person/{}".format(user_one.facebookId))
    assert response.status_code == 204


def test_service_person_should_get_all_users(test_client, user_one):
    response = test_client.get("/v1/person")
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 1


def test_when_param_limit_exist_response_should_be_a_specific_size(test_client, list_of_user):
    response = test_client.get("/v1/person?limit=2")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 2
