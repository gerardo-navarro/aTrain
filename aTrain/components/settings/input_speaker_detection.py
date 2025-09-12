from nicegui import ui, app


def input_speaker_detection():
    with ui.column():
        ui.label("Speaker Detection").classes("h2 font-bold text-primary")
        ui.separator()
        input = ui.switch("Speaker Detection")
    input.bind_value(app.storage.client, "speaker_detection")
