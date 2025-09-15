from nicegui import ui
from aTrain.components.modals.process import close_modal_process


def modal_error(error: str, traceback: str):
    close_modal_process()
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Error")
        ui.label(error)
        ui.label("Traceback")
        ui.label(traceback)
        ui.button("Exit").on_click(dialog.delete)
