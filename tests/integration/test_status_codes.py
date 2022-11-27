from http import HTTPStatus

import requests


# def test_5xx_responses(make_read_config, run_server):
#     read_config = make_read_config("status_500.yml")
#     config = read_config()
#     run_server(config)
#     breakpoint()
#     response = requests.get("http://127.0.0.1:5000/")
#     assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR


def test_5xx_responses(test_server):
    response = requests.get("http://127.0.0.1:5000/")

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.headers['content-type'] == "text/html; charset=utf-8"
    assert "Internal Server Error" in response.text
