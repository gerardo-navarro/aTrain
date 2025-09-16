from aTrain_core.globals import REQUIRED_MODELS, REQUIRED_MODELS_DIR
from nicegui import ui
from typer import Typer, Option
from typing_extensions import Annotated
from aTrain.pages import about, archive, faq, models, transcribe  # noqa: F401
from aTrain.models import start_model_download
from importlib.resources import files

cli = Typer(help="CLI for aTrain.")


@cli.command()
def init():
    """Download all required model for aTrain."""
    for model in REQUIRED_MODELS:
        start_model_download(model=model, models_dir=REQUIRED_MODELS_DIR)


@cli.command()
def start(
    native: Annotated[bool, Option(help="Run in a native window")] = True,
    reload: Annotated[bool, Option(help="Reload on code change")] = False,
):
    """Start aTrain."""
    print("Running aTrain")
    ui.run(
        native=native,
        reload=reload,
        title="aTrain",
        favicon=files("aTrain") / "static" / "favicon.ico",
        window_size=(1280, 720) if native else None,
    )
