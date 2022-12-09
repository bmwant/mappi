from unittest.mock import ANY, MagicMock, patch

from mappi import cli, config
from tests import utils


def test_default_executable_invocation(runner):
    config_mock = MagicMock()
    updated_config_mock = MagicMock()
    with (
        patch("mappi.cli.run") as run_mock,
        patch("mappi.cli.read_configuration", return_value=config_mock) as read_mock,
        patch(
            "mappi.cli.update_configuration", return_value=updated_config_mock
        ) as update_mock,
    ):
        result = runner.invoke(cli.cli)

        assert result.exit_code == 0
        read_mock.assert_called_once_with(config.MAPPI_CONFIG_FILENAME)
        update_mock.assert_called_once_with(
            config=config_mock, port=config.DEFAULT_PORT
        )
        run_mock.assert_called_once_with(updated_config_mock)


def test_port_override(runner):
    port: int = 5959
    with (
        patch("mappi.cli.run") as run_mock,
        patch("mappi.cli.update_configuration") as update_mock,
    ):
        result = runner.invoke(cli.cli, ["--port", f"{port}"])

        assert result.exit_code == 0
        update_mock.assert_called_once_with(config=ANY, port=port)
        run_mock.assert_called_once()


def test_config_override(runner):
    config_filepath = runner.path / "custom-config.yml"
    with open(config_filepath, "w") as f:
        f.write(utils.SAMPLE_CONFIG_YAML)

    with (
        patch("mappi.cli.run") as run_mock,
        patch("mappi.cli.read_configuration") as read_mock,
    ):
        result = runner.invoke(cli.cli, ["--config", f"{config_filepath}"])

        assert result.exit_code == 0
        read_mock.assert_called_once_with(str(config_filepath))
        run_mock.assert_called_once()
