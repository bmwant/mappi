from pathlib import Path

import click
import uvicorn

from mappi.server import create_app
from mappi.utils import logger, read_configuration

CURRENT_DIR = Path(__file__).parent.resolve()


@click.group(invoke_without_command=True)
@click.version_option(message="mappi, version %(version)s")
@click.pass_context
@click.option("-c", "--config", is_flag=True, default=False)
def cli(ctx, config):
    config_filepath = CURRENT_DIR / "mappi.yml"
    if ctx.invoked_subcommand is None:
        run(config_filepath)


def run(config_filepath: Path):
    config = read_configuration(config_filepath)
    app = create_app(config.routes)
    PORT = 5000
    logger.debug(f"Running on port {PORT}")
    server_config = uvicorn.Config(
        app, port=PORT, log_level="info", server_header=False
    )
    server = uvicorn.Server(server_config)
    server.run()


if __name__ == "__main__":
    cli()
