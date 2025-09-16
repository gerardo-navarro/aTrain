from nicegui import ui
from aTrain.layouts.base import base_layout


@ui.page("/about")
def page():
    with base_layout():
        ui.label("Lorem Ipsum")
