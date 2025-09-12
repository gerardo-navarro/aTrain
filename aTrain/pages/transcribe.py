from nicegui import ui, events, app

from aTrain.components.settings.file_picker import file_picker
from aTrain.components.settings.input_model import input_model
from aTrain.components.settings.input_languages import input_language
from aTrain.layouts.card_layout import card_layout


@ui.page("/")
def page():
    with card_layout():
        with ui.element("div").classes(
            "w-full h-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        ):
            uploader = file_picker()
            input_model()
            input_language()
            input_diarize = ui.switch("Speaker Detection")
            input_speakers = ui.number("Number of Speakers", min=0, value=0)
        ui.separator()
        with ui.row():
            with ui.column():
                ui.label("Advanced Settings")
                ui.link("Help needed?", "/faq")
            ui.button("upload", on_click=uploader.upload)

    # EVENT HANDLERS
    input_speakers.bind_visibility(input_diarize, "value")
    uploader.on_upload(handle_upload)


def handle_upload(file: events.UploadEventArguments):
    model = app.storage.client.get("model")
    language = app.storage.client.get("language")
    print(file.name, model, language)
