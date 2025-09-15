from nicegui import ui


def modal_error(error: str, traceback: str):
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Error")
        ui.label(error)
        ui.label("Traceback")
        ui.label(traceback)
        ui.button("Exit").on_click(dialog.delete)
