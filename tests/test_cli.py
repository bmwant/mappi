from unittest.mock import MagicMock, patch

from mappi import cli, config


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
