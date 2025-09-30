import os
from importlib.resources import files
from pathlib import Path

from aTrain_core.globals import ATRAIN_DIR, REQUIRED_MODELS
from aTrain_core.load_resources import get_model
from typer import Option, Typer
from typing_extensions import Annotated
from wakepy import keep

os.environ["NICEGUI_STORAGE_PATH"] = str(Path(ATRAIN_DIR) / "settings")

cli = Typer(help="CLI for aTrain.")


@cli.command()
def init():
    """Download all required model for aTrain."""
    for model in REQUIRED_MODELS:
        get_model(model=model)


@cli.command()
def start(
    native: Annotated[bool, Option(help="Run in a native window")] = True,
    reload: Annotated[bool, Option(help="Reload on code change")] = False,
):
    """Start aTrain."""
    print("Running aTrain")
    from nicegui import ui

    from aTrain.pages import about, archive, faq, models, transcribe  # noqa: F401

    with keep.running():
        ui.run(
            native=native,
            reload=reload,
            title="aTrain",
            favicon=files("aTrain") / "static" / "favicon.ico",
            window_size=(1280, 720) if native else None,
        )
