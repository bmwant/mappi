from http import HTTPStatus

import pytest

from tests.utils import use_config

pytestmark = pytest.mark.integration


@use_config("test_default.yml")
def test_base_response(test_server, test_client):
    response = test_client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text == "Simple test response"


@use_config("test_default.yml")
def test_not_found_response(test_server, test_client):
    response = test_client.get("/test_not_found")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text == "No mapping registered for /test_not_found route"


@use_config("test_default.yml")
def test_wrong_method(test_server, test_client):
    response = test_client.post("/")

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert response.text == "Method Not Allowed"
