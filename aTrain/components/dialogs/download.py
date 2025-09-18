from datetime import datetime
from multiprocessing.managers import DictProxy

from nicegui import app, ui
from nicegui.run import tear_down as stop_download
from aTrain.components.dialogs.process import update_timer


def dialog_download(progress: DictProxy):
    global timer, dialog
    state = app.storage.client
    start_time = datetime.now()
    timer = ui.timer(
        interval=0.1, callback=lambda: update_progress(progress, start_time)
    )
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Download").classes("h2")
        ui.separator()
        ui.label("").bind_text(state, "timer")
        progress_bar = ui.linear_progress(show_value=False).props("animation-speed=500")
        progress_bar.bind_value(state, "progress")
        ui.separator()
        btn_stop = ui.button("stop", color="dark").props("unelevated no-caps")
        btn_stop.on_click(stop_download)


def update_progress(progress: DictProxy, start_time: datetime):
    app.storage.client["progress"] = progress["current"] / progress["total"]
    update_timer(start_time)


def close_dialog_download():
    timer.cancel()
    dialog.delete()
