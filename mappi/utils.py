import logging
from pathlib import Path

import yaml

from mappi import config, schema

# logging.disable(level=logging.CRITICAL)

# unicorn_access_logger = logging.getLogger("uvicorn.access")
# unicorn_error_logger = logging.getLogger("uvicorn.error")
# unicorn_access_logger.disabled = True
# unicorn_error_logger.disabled = True

# if config.DEBUG:
# if True:
#     logging.disable(logging.NOTSET)
#     logging.basicConfig(level=logging.DEBUG)


logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__package__)


def read_configuration(filename: Path) -> schema.Config:
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))
