from nicegui import ui
from aTrain.layouts.base_layout import base_layout


@ui.page("/models")
def page():
    with base_layout():
        ui.label("Lorem Ipsum")
