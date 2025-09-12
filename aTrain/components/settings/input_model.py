from nicegui import app, ui
from aTrain.models import read_transcription_models
from aTrain_core.globals import REQUIRED_MODELS
from aTrain.components.settings.input_languages import update_language_options


def input_model():
    models = read_transcription_models()

    with ui.column():
        ui.label("Select Model").classes("h2 font-bold text-primary")
        ui.separator()
        with ui.select(models, value=REQUIRED_MODELS[1]).classes("w-full") as input:
            input.classes("w-full").props("outlined")

    input.bind_value(app.storage.client, "model")
    input.on_value_change(lambda: update_language_options(input.value))
