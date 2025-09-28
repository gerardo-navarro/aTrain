from nicegui import ui, app

TOOLTIP = "If you specify '0' the app will automatically detect the number of speakers."


def input_num_speakers():
    with ui.column().classes("gap-2") as column:
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("Number of Speakers").classes("font-bold text-dark text-md")
            ui.icon("info_outline", size="sm", color="grey").tooltip(TOOLTIP)
        ui.separator()
        input = ui.number(min=0, value=0)
        input.classes("w-full")
        input.props("filled bg-color=gray-100 color=dark")

    input.bind_value(app.storage.general, "num_speakers")
    column.bind_visibility(app.storage.general, "speaker_detection")
