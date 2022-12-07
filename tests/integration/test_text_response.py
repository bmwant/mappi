from http import HTTPStatus  # noqa: F401

import pytest

from tests.utils import use_config  # noqa: F401

pytestmark = pytest.mark.integration


@use_config("test_status_5xx.yml")
def test_text_response(test_server, test_client):
    response = test_client.get("/test_500")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Internal Server Error" in response.text
