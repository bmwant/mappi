from enum import Enum

from pydantic import BaseModel, ValidationError, root_validator
from typing import Optional


from pydantic import BaseModel, Field

    
class RouteType(str, Enum):
    BODY = 'body'
    JSON = 'json_data'  # TODO: update to just json
    TEXT = 'text'
    FILENAME = "filename"


class Route(BaseModel):
    path: str
    # TODO: add fields from enum dynamically
    body: Optional[str]
    json_data: Optional[str]
    text: Optional[str]
    filename: Optional[str]   
    route_type: Optional[RouteType]

    @root_validator(pre=True)
    def check_route_type_present(cls, values):
        present_counter: int = 0
        route_type = None
        for r_type in RouteType:
            if r_type.value in values:
                route_type = r_type
                present_counter += 1
        
        if present_counter == 0:
            raise ValueError("Path type should be specified")
    
        if present_counter > 1:
            raise ValueError("Found more than one path type")
        
        # Finally set `route_type` field
        values["route_type"] = route_type
        return values


class Config(BaseModel):
    # TODO: add server config here
    routes: list[Route]
