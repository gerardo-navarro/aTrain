from aTrain.layouts.base_layout import base_layout
from contextlib import contextmanager
from nicegui import ui


@contextmanager
def card_layout():
    with base_layout():
        with ui.card().classes("w-full h-full bg-white rounded-lg").props("flat"):
            yield
