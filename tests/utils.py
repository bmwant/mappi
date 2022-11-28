import contextlib
import threading
import time
from functools import wraps
from pathlib import Path

import uvicorn

from mappi.utils import read_configuration

TESTS_DIR = Path(__file__).parent.resolve()
DATA_DIR = TESTS_DIR / "data"


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
