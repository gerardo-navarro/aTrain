from datetime import datetime
from multiprocessing.managers import DictProxy

from nicegui import app, ui
from nicegui.run import tear_down as stop_transcription


def dialog_process(progress: DictProxy):
    global timer, dialog
    state = app.storage.client
    start_time = datetime.now()
    timer = ui.timer(interval=1, callback=lambda: update_progress(progress, start_time))
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Process").classes("h2")
        ui.separator()
        ui.label("").bind_text(state, "timer")
        ui.separator()
        ui.label("").bind_text(state, "task")
        progress_bar = ui.linear_progress(show_value=False).props("animation-speed=500")
        progress_bar.bind_value(state, "progress")
        ui.separator()
        btn_stop = ui.button("stop", color="dark").props("unelevated no-caps")
        btn_stop.on_click(stop_transcription)


def update_progress(progress: DictProxy, start_time: datetime):
    state = app.storage.client
    state["progress"] = progress["current"] / progress["total"]
    state["task"] = progress["task"]
    update_timer(start_time)


def update_timer(start_time: datetime):
    state = app.storage.client
    timedelta = datetime.now() - start_time
    total_seconds = int(timedelta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    state["timer"] = f"{hours:02}:{minutes:02}:{seconds:02}"


def close_dialog_process():
    timer.cancel()
    dialog.delete()
