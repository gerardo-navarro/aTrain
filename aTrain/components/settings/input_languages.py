from nicegui import ui, app
from aTrain.models import model_languages
from aTrain_core.globals import REQUIRED_MODELS


def input_language():
    global input
    language_options = model_languages(REQUIRED_MODELS[1])
    with ui.column():
        ui.label("Select Language").classes("h2 font-bold text-primary")
        ui.separator()
        with ui.select(language_options, value="auto-detect") as input:
            input.classes("w-full").props("outlined")
    input.bind_value(app.storage.client, "language")


def update_language_options(model: str):
    new_options = model_languages(model)
    keys = list(new_options.keys())
    new_value = keys[0] if input.value not in keys else input.value
    input.set_options(new_options, value=new_value)
