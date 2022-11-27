import contextlib
import time
import threading
from pathlib import Path
from unittest.mock import patch

import pytest
import uvicorn
import yaml

from mappi import schema
from mappi.server import create_app
from mappi.utils import logger
from tests.utils import TestServer, read_test_config


@pytest.fixture
def make_read_config():
    with patch("mappi.__main__.read_configuration") as read_mock:

        def _read_config(config_filename):
            config = read_test_config(config_filename)
            read_mock.return_value = config
            return read_mock

        return _read_config


# TODO: add free port as a fixture
# TODO: redirect server log to a file
@pytest.fixture(scope="function")
def test_server(request):
    if not hasattr(request.function, "config"):
        raise RuntimeError(
            f"Unittest {request.function.__name__} that uses server needs `use_config` decorator"
        )
    config = request.function.config
    app = create_app(config.routes)
    server_config = uvicorn.Config(app, port=5000, log_level="info")
    server = TestServer(server_config)
    with server.run_in_thread():
        yield


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: mark tests that require mappi server to be running",
    )


def pytest_addoption(parser):
    parser.addoption(
        "--integration",
        action="store_true",
        help="run the tests that require mappi server running",
    )


def pytest_runtest_setup(item):
    if "integration" in item.keywords and not item.config.getoption("--integration"):
        pytest.skip("need --integration option to run this test")
