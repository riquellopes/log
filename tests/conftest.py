import pytest
import logging
from facebook.api import app as _app
from facebook.api import db


@pytest.fixture(scope='session')
def app(request):
    ctx = _app.app_context()
    ctx.app.config['TESTING'] = True
    ctx.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    ctx.push()

    logging.disable(logging.CRITICAL)

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture(scope='session', autouse=True)
def build_db(app):
    db.create_all()


@pytest.fixture(scope='function', autouse=True)
def rollback(app, request):
    def fin():
        db.session.rollback()
    request.addfinalizer(fin)


@pytest.fixture(scope='session')
def test_client(app):
    return app.test_client()
