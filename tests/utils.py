import contextlib
import threading
import time
from pathlib import Path
from functools import wraps

import yaml
import uvicorn

from mappi import schema

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


# TODO: just reuse `read_config` function
def read_test_config(filename: str) -> schema.Config:
    filepath = DATA_DIR / filename
    with open(filepath) as f:
        return schema.Config.parse_obj(
            yaml.load(f.read(), Loader=yaml.FullLoader)
        )



def use_config(config_filename):
    config = read_test_config(config_filename)
    def outer_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.config = config
        return wrapper
    return outer_wrapper
