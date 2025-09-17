from nicegui import app, ui

from aTrain.utils.models import model_languages


def input_language():
    global input
    state = app.storage.client
    language_options = model_languages(state["model"]) if state["model"] else []
    default_language = list(language_options.keys())[0] if language_options else None
    with ui.column().classes("gap-2"):
        ui.label("Select Language").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(language_options, value=default_language) as input:
            input.classes("w-full")
            input.props("filled bg-color=gray-100 color=dark")
    input.bind_value(state, "language")


def update_language_options(model: str):
    new_options = model_languages(model)
    languages = list(new_options.keys())
    new_value = input.value if input.value in languages else languages[0]
    input.set_options(new_options, value=new_value)
