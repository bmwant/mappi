from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from mappi import schema

TESTS_DIR = Path(__file__).parent.resolve()
DATA_DIR = TESTS_DIR / "data"


@pytest.fixture
def make_read_config():
    with patch("mappi.__main__.read_configuration") as read_mock:

        def _read_config(config_filename):
            filepath = DATA_DIR / config_filename
            with open(filepath) as f:
                config = schema.Config.parse_obj(
                    yaml.load(f.read(), Loader=yaml.FullLoader)
                )
                read_mock.return_value = config
                return read_mock

        return _read_config
