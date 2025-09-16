from nicegui import ui

from aTrain.components.settings.file import input_file
from aTrain.components.settings.language import input_language
from aTrain.components.settings.model import input_model
from aTrain.components.settings.speaker_count import input_num_speakers
from aTrain.components.settings.speaker_detection import input_speaker_detection
from aTrain.layouts.card_layout import card_layout
from aTrain.transcription import start_transcription


@ui.page("/")
def page():
    with card_layout():
        with ui.element("div").classes(
            "w-full h-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10"
        ):
            file = input_file()
            input_model()
            input_language()
            input_speaker_detection()
            input_num_speakers()
        ui.separator()
        with ui.row().classes("w-full justify-between items-center"):
            with ui.column():
                ui.label("Advanced Settings")
                ui.link("Help needed?", "/faq")
            ui.button("Start", on_click=file.upload)

    file.on_upload(start_transcription)
