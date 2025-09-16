from nicegui import ui, app
from aTrain.models import model_languages
from aTrain_core.globals import REQUIRED_MODELS


def input_language():
    global input
    language_options = model_languages(REQUIRED_MODELS[1])
    with ui.column().classes("gap-2"):
        ui.label("Select Language").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(language_options, value="auto-detect") as input:
            input.classes("w-full")
            input.props("filled bg-color=bg-gray-100 color=dark")
    input.bind_value(app.storage.client, "language")


def update_language_options(model: str):
    new_options = model_languages(model)
    languages = list(new_options.keys())
    new_value = input.value if input.value in languages else languages[0]
    input.set_options(new_options, value=new_value)
