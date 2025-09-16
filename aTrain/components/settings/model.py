from nicegui import app, ui
from aTrain.models import read_transcription_models
from aTrain_core.globals import REQUIRED_MODELS
from aTrain.components.settings.language import update_language_options


def input_model():
    models = read_transcription_models()

    with ui.column().classes("gap-2"):
        ui.label("Select Model").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(models, value=REQUIRED_MODELS[1]).classes("w-full") as input:
            input.classes("w-full")
            input.props("filled bg-color=gray-100 color=dark")

    input.bind_value(app.storage.client, "model")
    input.on_value_change(lambda: update_language_options(input.value))
