from nicegui import ui
from aTrain.layouts.base_layout import base_layout


@ui.page("/archive")
def page():
    with base_layout():
        ui.label("Lorem Ipsum")
