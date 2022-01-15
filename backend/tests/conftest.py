from pytest import fixture
from fastapi.testclient import TestClient

from api import app


@fixture()
def client():
    yield TestClient(app)
