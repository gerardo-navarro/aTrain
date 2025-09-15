from nicegui import ui


def modal_process():
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Process")
    return dialog
