from pathlib import Path

import uvicorn
import yaml

from fastapi import FastAPI, APIRouter


CURRENT_DIR = Path(__file__).parent.resolve()


def _create_routes():
    router = APIRouter()
    return router


def _create_app(routes):
    app = FastAPI()
    for route in routes:
        handler = handler_factory()
        app.router.add_api_route(route["path"], handler)
    return app
    

def handler_factory():
    def handler():
        return "response"
    return handler


def read_configuration():
    filename = CURRENT_DIR / "mappi.yml"
    routes = []
    with open(filename) as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
        routes = conf["routes"]

    return routes
        

def run():
    routes = read_configuration()
    app = _create_app(routes)
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == "__main__":
    run()
