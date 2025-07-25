from contextlib import contextmanager
from nicegui import ui
from aTrain.components.header import header
from aTrain.components.footer import footer
from aTrain.components.sidebar import sidebar


@contextmanager
def base_layout():
    ui.query("body").classes("bg-gray-100")
    header()
    sidebar()
    yield
    footer()
