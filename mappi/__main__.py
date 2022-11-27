from pathlib import Path

import uvicorn
import yaml

from mappi import schema
from mappi.server import create_app
from mappi.utils import logger

CURRENT_DIR = Path(__file__).parent.resolve()


def read_configuration() -> schema.Config:
    filename = CURRENT_DIR / "mappi.yml"
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))


def run():
    config = read_configuration()
    app = create_app(config.routes)
    PORT = 5000
    logger.debug(f"Running on port {PORT}")
    server_config = uvicorn.Config(
        app, port=PORT, log_level="info", server_header=False
    )
    server = uvicorn.Server(server_config)
    server.run()


if __name__ == "__main__":
    run()
