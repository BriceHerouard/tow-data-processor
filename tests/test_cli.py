from typer.testing import CliRunner

from ow_usage.cli import app


def test_cli_help_smoke() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Old World Unit Usage CLI" in result.stdout
