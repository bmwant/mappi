from http import HTTPStatus

import requests

from tests.utils import use_config


@use_config("status_500.yml")
def test_5xx_responses(test_server, test_client):
    response = requests.get("http://127.0.0.1:5000/")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Internal Server Error" in response.text


@use_config("status_500.yml")
def test_client(test_server, test_client):
    assert True
