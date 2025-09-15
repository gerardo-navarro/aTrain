from nicegui import ui, app
from datetime import datetime


def modal_process():
    state = app.storage.client
    start_time = datetime.now()
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Process").classes("h2")
        ui.separator()
        ui.label("").bind_text(state, "timer")
        ui.timer(
            interval=1,
            callback=lambda: state.update({"timer": str(datetime.now() - start_time)}),
        )
    return dialog
