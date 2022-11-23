import uvicorn


from fastapi import FastAPI, APIRouter


def _create_routes():
    router = APIRouter()
    return router


def _create_app():
    app = FastAPI()
    index = lambda: {"Hello": "World"}
    app.router.add_api_route("/", index)
    return app
    
def run():
    app = _create_app()
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == "__main__":
    run()