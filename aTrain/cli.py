import typer
from aTrain_core.globals import REQUIRED_MODELS, REQUIRED_MODELS_DIR
from nicegui import ui

import aTrain.app  # noqa: F401
from aTrain.models import start_model_download

cli = typer.Typer(help="CLI for aTrain.")


@cli.command()
def init():
    """Download all required model for aTrain."""
    for model in REQUIRED_MODELS:
        start_model_download(model=model, models_dir=REQUIRED_MODELS_DIR)


@cli.command()
def start():
    """Start aTrain in native mode."""
    print("Running aTrain in native mode")
    ui.run(native=True, reload=False)


@cli.command()
def dev():
    """Start aTrain in web mode."""
    print("Running aTrain in web mode")
    ui.run(native=False, reload=False)
