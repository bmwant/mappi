import uvicorn

from mappi.main import app


if __name__ == "__main__":
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()