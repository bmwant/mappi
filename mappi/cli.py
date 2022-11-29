from pathlib import Path

import click
import uvicorn

from mappi import config
from mappi.server import create_app
from mappi.utils import logger, read_configuration


@click.group(invoke_without_command=True)
@click.version_option(message="mappi, version %(version)s")
@click.pass_context
@click.option(
    "-c",
    "--config",
    "config_filepath",
    type=click.Path(exists=True),
    default=config.DEFAULT_CONFIG_FILENAME,
)
def cli(ctx, config_filepath):
    if ctx.invoked_subcommand is None:
        run(config_filepath)


@cli.command(name="config", short_help="Generate sample configuration")
@click.option("--full", is_flag=True, default=False)
def generate_config(full: bool):
    config_filepath = config.DATA_DIR / "config-basic.yml"
    if full:
        config_filepath = config.DATA_DIR / "config-full.yml"
    with open(config_filepath) as f:
        print(f.read())


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
