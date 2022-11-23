from pathlib import Path

import uvicorn
import yaml

from fastapi import FastAPI, APIRouter


CURRENT_DIR = Path(__file__).parent.resolve()


def _create_routes():
    router = APIRouter()
    return router


def _create_app():
    app = FastAPI()
    index = lambda: {"Hello": "World"}
    app.router.add_api_route("/", index)
    return app
    

def read_configuration():
    filename = CURRENT_DIR / "mappi.yml"
    routes = []
    with open(filename) as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
        routes = conf["routes"]

    for route in routes:
        print(route["path"])
        
        
def run():
    read_configuration()
    app = _create_app()
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == "__main__":
    run()