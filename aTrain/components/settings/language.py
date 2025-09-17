from aTrain_core.globals import REQUIRED_MODELS
from nicegui import app, ui

from aTrain.utils.models import model_languages, read_transcription_models


def input_language():
    global input
    models = read_transcription_models()
    default_model = REQUIRED_MODELS[1]
    language_options = model_languages(default_model) if default_model in models else []
    default_language = "auto-detect" if language_options else None
    with ui.column().classes("gap-2"):
        ui.label("Select Language").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(language_options, value=default_language) as input:
            input.classes("w-full")
            input.props("filled bg-color=gray-100 color=dark")
    input.bind_value(app.storage.client, "language")


def update_language_options(model: str):
    new_options = model_languages(model)
    languages = list(new_options.keys())
    new_value = input.value if input.value in languages else languages[0]
    input.set_options(new_options, value=new_value)
