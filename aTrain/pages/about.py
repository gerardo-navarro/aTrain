from nicegui import ui
from aTrain.layouts.card_layout import card_layout


@ui.page("/about")
def page():
    with card_layout():
        ui.label("Lorem Ipsum")
