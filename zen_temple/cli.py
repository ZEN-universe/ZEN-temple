"""Command-line entry point for the ZEN-temple visualization server."""

from .main import parse_arguments_and_run


def create_zen_visualization_cli() -> None:
    """Start ZEN-temple using the command-line arguments."""
    parse_arguments_and_run()


if __name__ == "__main__":
    create_zen_visualization_cli()
