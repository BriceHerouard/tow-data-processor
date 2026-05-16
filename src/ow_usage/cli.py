import typer

app = typer.Typer(help="Old World Unit Usage CLI")


@app.callback()
def main() -> None:
    """Entry point for the CLI."""


if __name__ == "__main__":
    app()
