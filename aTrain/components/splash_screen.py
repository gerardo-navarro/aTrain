import importlib
import sys
from importlib.resources import files

from nicegui import run, ui

ATRAIN_LOGO = files("aTrain") / "static" / "images" / "logo.svg"


async def splash_screen():
    if "torch" not in sys.modules.keys():
        with ui.column() as splash:
            ui.image(ATRAIN_LOGO).props("height=30px width=80px fit=contain")
            ui.spinner("dots", size="3em")
        await run.io_bound(importlib.import_module, name="torch")
        await run.io_bound(importlib.import_module, name="aTrain_core.transcribe")
        splash.delete()
