import logging
from pathlib import Path

import yaml

from mappi import schema

logging.disable(level=logging.CRITICAL)

# if config.DEBUG:
if True:
    logging.disable(logging.NOTSET)
    logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger(__package__)


def read_configuration(filename: Path) -> schema.Config:
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))
