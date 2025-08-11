from aTrain_core.globals import REQUIRED_MODELS
from nicegui import ui

from aTrain.components.file_picker import file_picker
from aTrain.layouts.card_layout import card_layout
from aTrain.models import model_languages, read_transcription_models

DATA = {}


@ui.page("/")
def page():
    # DATA
    models = read_transcription_models()
    languages = model_languages(REQUIRED_MODELS[1])

    # LAYOUT
    with card_layout():
        with ui.grid(rows=2, columns=3):
            uploader = file_picker()
            input_models = ui.select(models, label="Model", value=REQUIRED_MODELS[1])
            input_langs = ui.select(languages, label="Language", value="auto-detect")
            input_diarize = ui.switch("Speaker Detection")
            input_speakers = ui.number("Number of Speakers", placeholder="auto")
        ui.separator()
        with ui.row():
            with ui.column():
                ui.label("Advanced Settings")
                ui.link("Help needed?", "/faq")
            ui.button("upload", on_click=uploader.upload)

    # EVENT HANDLERS
    input_speakers.bind_visibility(input_diarize, "value")
    input_models.bind_value(DATA, "model")
    input_models.on_value_change(
        lambda e: input_langs.set_options(model_languages(e.value))
    )
    input_langs.bind_value(DATA, "language")
