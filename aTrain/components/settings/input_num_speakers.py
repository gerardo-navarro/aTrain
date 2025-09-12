from nicegui import ui, app


def input_num_speakers():
    with ui.column() as column:
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("Number of Speakers").classes("h2 font-bold text-primary")
            ui.icon("help_outline", size="sm", color="grey").tooltip(
                "If you specify '0' the app will automatically detect the number of speakers."
            )

        ui.separator()
        input = ui.number(min=0, value=0).classes("w-full")
    input.bind_value(app.storage.client, "num_speakers")
    column.bind_visibility(app.storage.client, "speaker_detection")
