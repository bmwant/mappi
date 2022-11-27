from pathlib import Path
from typing import List

import uvicorn
import yaml
from fastapi import FastAPI

from mappi import schema
from mappi.handlers import handler_factory
from mappi.utils import logger

CURRENT_DIR = Path(__file__).parent.resolve()


def _create_app(routes: List[schema.Route]):
    app = FastAPI()
    for route in routes:
        handler = handler_factory(route)
        app.router.add_api_route(route.path, handler)
    return app


def read_configuration() -> schema.Config:
    filename = CURRENT_DIR / "mappi.yml"
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))


def run():
    config = read_configuration()
    app = _create_app(config.routes)
    PORT = 5000
    logger.debug(f"Running on port {PORT}")
    server_config = uvicorn.Config(app, port=PORT, log_level="info")
    server = uvicorn.Server(server_config)
    server.run()


if __name__ == "__main__":
    run()
