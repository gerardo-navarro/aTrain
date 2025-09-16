from nicegui import ui
from aTrain.components.dialogs.process import close_dialog_process


def dialog_error(error: str, traceback: str):
    close_dialog_process()
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Error")
        ui.label(error)
        ui.label("Traceback")
        ui.label(traceback)
        ui.button("Exit").on_click(dialog.delete)
