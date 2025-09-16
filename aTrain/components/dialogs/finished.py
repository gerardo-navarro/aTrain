from nicegui import ui, app
from aTrain.components.dialogs.process import close_dialog_process


def dialog_finished():
    close_dialog_process()
    state = app.storage.client
    with ui.dialog(value=True).props("persistent"), ui.card():
        ui.label("Finished")
        ui.label("").bind_text_from(state, "timer", lambda x: f"We transcribed in {x}")
        ui.button("Exit").on_click(ui.navigate.reload)
