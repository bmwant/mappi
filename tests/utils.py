import contextlib
import threading
import time
from functools import wraps
from pathlib import Path
from urllib.parse import urljoin

import uvicorn

from mappi.utils import read_configuration

TESTS_DIR = Path(__file__).parent.resolve()
DATA_DIR = TESTS_DIR / "data"
DEFAULT_TIMEOUT = 3


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


def use_config(config_filename: str):
    config_filepath = DATA_DIR / config_filename
    config = read_configuration(config_filepath)

    def outer_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.config = config
        return wrapper

    return outer_wrapper


def update_url(func, new_url):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # url is the first param
        if len(args) > 0:
            args = [urljoin(new_url, args[0])] + list(args[1:])
        # url is a keyword argument
        elif "url" in kwargs:
            kwargs["url"] = urljoin(new_url, kwargs["url"])
        else:
            raise ValueError("URL is missing")
        # set default timeout
        kwargs["timeout"] = DEFAULT_TIMEOUT
        return func(*args, **kwargs)

    return wrapper
