import os
from pathlib import Path
from typing import List

import uvicorn
import yaml

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from mappi import schema


CURRENT_DIR = Path(__file__).parent.resolve()


def _create_app(routes: List[schema.Route]):
    app = FastAPI()
    for route in routes:
        handler = handler_factory(route.route_type)
        app.router.add_api_route(route.path, handler)
    return app


async def handler():
    return {"Hello": "mappi"}


async def body_handler():
    return "Hello buddy"


async def json_handler():
    return "Hello json"


def handler_factory(route_type: schema.RouteType):
    filepath = CURRENT_DIR / "mappi.yml"
    stat_result = os.stat(filepath)
    static = StaticFiles()

    def static_handler(request: Request):
        return static.file_response(filepath, stat_result=stat_result, scope=request.scope)
    
    
    match route_type:
        case schema.RouteType.FILENAME:
            return static_handler
        case schema.RouteType.JSON:
            return json_handler
        case schema.RouteType.TEXT:
            return handler
        case schema.RouteType.BODY:
            return body_handler
        case _:
            # TODO: should raise on pydantic validation level
            raise ValueError("Improper configuratoin") 


def read_configuration() -> schema.Config:
    filename = CURRENT_DIR / "mappi.yml"
    with open(filename) as f:
        return schema.Config.parse_obj(
            yaml.load(f.read(), Loader=yaml.FullLoader)
        )
        

def run():
    config = read_configuration()
    app = _create_app(config.routes)
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == "__main__":
    run()
