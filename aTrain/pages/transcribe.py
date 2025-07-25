from nicegui import ui

from aTrain.layouts.card_layout import card_layout
from aTrain.components.file_picker import file_picker


@ui.page("/")
def page():
    with card_layout():
        uploader = file_picker()
