from nicegui import app, ui

from aTrain.utils.models import model_languages


def input_language():
    state = app.storage.client
    language_options = model_languages(state["model"]) if state["model"] else []
    default_language = list(language_options.keys())[0] if language_options else None
    with ui.column().classes("gap-2"):
        ui.label("Select Language").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(language_options, value=default_language) as select_language:
            select_language.classes("w-full")
            select_language.props("filled bg-color=gray-100 color=dark")
    select_language.bind_value(state, "language")
    state["select_language"] = select_language


def update_language_options(model: str):
    state = app.storage.client
    select_language: ui.select = state["select_language"]
    new_options = model_languages(model)
    languages = list(new_options.keys())
    new_value = x if (x := select_language.value) in languages else languages[0]
    select_language.set_options(new_options, value=new_value)
