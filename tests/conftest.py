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

TESTS_DIR = Path(__file__).parent.resolve()
DATA_DIR = TESTS_DIR / "data"


def read_test_config(filename: str) -> schema.Config:
    filepath = DATA_DIR / filename
    with open(filepath) as f:
        return schema.Config.parse_obj(
            yaml.load(f.read(), Loader=yaml.FullLoader)
        )


@pytest.fixture
def make_read_config():
    with patch("mappi.__main__.read_configuration") as read_mock:

        def _read_config(config_filename):
            config = read_test_config(config_filename)
            read_mock.return_value = config
            return read_mock

        return _read_config


class TestServer(uvicorn.Server):
    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()


#TODO: add free port as a fixture
@pytest.fixture(scope="function")
def run_server():
    def _make_server(config: schema.Config):
        app = create_app(config.routes)
        server_config = uvicorn.Config(app, port=5000, log_level="info")
        server = TestServer(server_config)
        logger.debug("About to start a server in a thread")
        with server.run_in_thread():
            yield

    return _make_server


@pytest.fixture(scope="function")
def test_server():
    config = read_test_config("status_500.yml")
    app = create_app(config.routes)
    server_config = uvicorn.Config(app, port=5000, log_level="info")
    server = TestServer(server_config)
    logger.debug("About to start a server in a thread")
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
