import socket
from unittest.mock import patch

import pytest
import uvicorn

from mappi.server import create_app
from mappi.utils import read_configuration
from tests.utils import TestServer


@pytest.fixture
def make_read_config():
    with patch("mappi.__main__.read_configuration") as read_mock:

        def _read_config(config_filename):
            # TODO: check whether we need this fixture separately
            config = read_configuration(config_filename)
            read_mock.return_value = config
            return read_mock

        return _read_config


@pytest.fixture
def free_port():
    sock = socket.socket()
    sock.bind(("", 0))
    yield sock.getsockname()[1]
    sock.close()


# TODO: redirect server log to a file
@pytest.fixture(scope="function")
def test_server(request, free_port):
    test_function = request.function
    if not hasattr(test_function, "config"):
        raise RuntimeError(
            f"Unittest {test_function.__name__} that uses server "
            f"needs `use_config` decorator"
        )

    config = test_function.config
    app = create_app(config.routes)
    server_config = uvicorn.Config(app, port=free_port, log_level="info")
    server = TestServer(server_config)

    # assign a port to a test function, so client knows proper server endpoint
    test_function.port = free_port
    with server.run_in_thread():
        yield


@pytest.fixture(scope="function")
def test_client(request):
    test_function = request.function
    if not hasattr(test_function, "port"):
        raise RuntimeError(
            f"Unittest {test_function.__name__} that uses `test_client` fixture "
            f"has to use `test_server` fixture as well"
        )


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
