from typing import List

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from mappi import schema
from mappi.handlers import handler_factory


class MappiMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["server"] = "mappi"
        return response


async def add_server_header(request: Request, call_next):
    response = await call_next(request)

    return response


def create_app(routes: List[schema.Route]):
    app = FastAPI()
    for route in routes:
        handler = handler_factory(route)
        app.router.add_api_route(route.path, handler)

    app.add_middleware(MappiMiddleware)

    return app
