from contextlib import contextmanager
from nicegui import ui
from aTrain.components.header import header


@contextmanager
def base_layout():
    ui.query("body").classes("bg-slate-200")
    header()
    yield
