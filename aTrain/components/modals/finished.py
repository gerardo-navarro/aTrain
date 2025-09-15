from nicegui import ui, app
from aTrain.components.modals.process import close_modal_process


def modal_finished():
    close_modal_process()
    state = app.storage.client
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Finished")
        ui.label("").bind_text_from(state, "timer", lambda x: f"We transcribed in {x}")
        ui.button("Exit").on_click(dialog.delete)
