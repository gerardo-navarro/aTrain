from nicegui import ui, app
from datetime import datetime


def dialog_process():
    global timer, dialog
    state = app.storage.client
    start_time = datetime.now()
    timer = ui.timer(interval=1, callback=lambda: update_timer(start_time))
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Process").classes("h2")
        ui.separator()
        ui.label("").bind_text(state, "timer")


def close_dialog_process():
    timer.cancel()
    dialog.delete()


def update_timer(start_time: datetime):
    state = app.storage.client
    timedelta = datetime.now() - start_time
    total_seconds = int(timedelta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    state["timer"] = f"{hours:02}:{minutes:02}:{seconds:02}"
