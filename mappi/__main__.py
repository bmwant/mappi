import uvicorn

from mappi.main import app


def run():
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == "__main__":
    run()