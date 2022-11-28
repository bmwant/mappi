from http import HTTPStatus

from tests.utils import use_config


@use_config("status_5xx.yml")
def test_500_response(test_server, test_client):
    response = test_client.get("/test_500")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Internal Server Error" in response.text


@use_config("status_5xx.yml")
def test_501_response(test_server, test_client):
    response = test_client.get("/test_501")

    assert response.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Not Implemented" in response.text


@use_config("status_5xx.yml")
def test_502_response(test_server, test_client):
    response = test_client.get("/test_502")

    assert response.status_code == HTTPStatus.BAD_GATEWAY
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert "Bad Gateway" in response.text


@use_config("status_5xx.yml")
def test_503_response(test_server, test_client):
    response = test_client.get("/test_503")

    assert response.status_code == HTTPStatus.SERVICE_UNAVAILABLE
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Service Unavailable" in response.text


@use_config("status_5xx.yml")
def test_504_response(test_server, test_client):
    response = test_client.get("/test_504")

    assert response.status_code == HTTPStatus.GATEWAY_TIMEOUT
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert "Gateway Timeout" in response.text
