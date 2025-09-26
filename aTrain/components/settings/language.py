from nicegui import ElementFilter, app, ui

from aTrain.utils.models import model_languages


def input_language():
    state = app.storage.client
    language_options = model_languages(state["model"]) if state["model"] else []
    default_language = list(language_options.keys())[0] if language_options else None
    with ui.column().classes("gap-2"):
        ui.label("Select Language").classes("font-bold text-dark text-md")
        ui.separator()
        with ui.select(language_options, value=default_language) as select:
            select.classes("w-full").props("filled bg-color=gray-100 color=dark")
            select.mark("select_language").bind_value(state, "language")


def update_language_options(model: str):
    new_options = model_languages(model)
    languages = list(new_options.keys())
    for select in ElementFilter(marker="select_language", kind=ui.select):
        new_value = select.value if select.value in languages else languages[0]
        select.set_options(new_options, value=new_value)
