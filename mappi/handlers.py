import os
from pathlib import Path

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles

from mappi import schema
from mappi.utils import logger


async def text_handler():
    return {"Hello": "mappi"}


async def body_handler():
    return "Hello buddy"


async def json_handler():
    return "Hello json"

def static_factory(filepath: Path):
    stat_result = os.stat(filepath)
    static = StaticFiles()
    logger.debug(f"Creating handler for {filepath}")

    async def static_handler(request: Request):
        return static.file_response(filepath, stat_result=stat_result, scope=request.scope)
    
    return static_handler


def handler_factory(route: schema.Route):
    match route.route_type:
        case schema.RouteType.FILENAME:
            logger.debug(f"Path {route.path}: attaching file handler")
            handler = static_factory(route.filename)
            return handler
        case schema.RouteType.JSON:
            logger.debug("Creating json handler")
            return json_handler
        case schema.RouteType.TEXT:
            logger.debug("Creating text handler")
            return text_handler
        case schema.RouteType.BODY:
            logger.debug("Creating body handler")
            return body_handler
        case _:
            # TODO: should raise on pydantic validation level
            raise ValueError("Improper configuratoin") 
