from nicegui import app, ui
from nicegui.events import ValueChangeEventArguments


def input_speaker_count():
    with ui.column().classes("gap-2") as column:
        ui.label("Number of Speakers").classes("font-bold text-dark text-md")
        ui.separator()
        input = ui.number(min=0, placeholder="Detect automatically")
        input.classes("w-full")
        input.props("filled bg-color=gray-100 color=dark")

    input.on_value_change(lambda args: check_value(input, args))
    input.bind_value(app.storage.general, "speaker_count")
    column.bind_visibility(app.storage.general, "speaker_detection")


def check_value(input: ui.number, args: ValueChangeEventArguments):
    if args.value == 0.0:
        input.set_value(None)
        input.update()
