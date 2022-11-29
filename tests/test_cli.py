from unittest.mock import patch

from mappi import cli, config


def test_default_executable_invocation(runner):
    with patch("mappi.cli.run") as run_mock:
        result = runner.invoke(cli.cli)

        assert result.exit_code == 0
        run_mock.assert_called_once_with(config.DEFAULT_CONFIG_FILENAME)
