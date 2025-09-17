from aTrain_core.globals import REQUIRED_MODELS
from nicegui import app, ui

from aTrain.components.settings.language import update_language_options
from aTrain.utils.models import read_transcription_models


def input_model():
    models = read_transcription_models()
    default_model = REQUIRED_MODELS[1]
    active_model = default_model if default_model in models else None
    with ui.column().classes("gap-2"):
        ui.label("Select Model").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(models, value=active_model).classes("w-full") as input:
            input.classes("w-full")
            input.props("filled bg-color=gray-100 color=dark")

    input.bind_value(app.storage.client, "model")
    input.on_value_change(lambda: update_language_options(input.value))
