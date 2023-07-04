from flask import Flask
import os
import pytest
from time import time

from project import create_app
from project.models.db import Model

@pytest.fixture(scope='module')
def timestamp() -> float:
    return time()

@pytest.fixture(scope='module')
def flask_app():
    os.environ['CONFIG_TYPE'] = 'settings.TestingConfig'
    app = create_app()
    return app

@pytest.fixture(scope='module')
def test_client(flask_app: Flask):
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def new_model(timestamp: float) -> Model:
    reef_query = Model(query={'a': 1, 'b': {'$gte': 2}}, limit=5, start=(timestamp - 60*60*24), stop=timestamp, fields={'_id': 0})
    return reef_query