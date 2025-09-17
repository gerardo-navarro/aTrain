from nicegui import ui

from aTrain.components.settings.file import input_file
from aTrain.components.settings.language import input_language
from aTrain.components.settings.model import input_model
from aTrain.components.settings.speaker_count import input_num_speakers
from aTrain.components.settings.speaker_detection import input_speaker_detection
from aTrain.components.settings.advanced import advanced_settings
from aTrain.layouts.base import base_layout
from aTrain.utils.transcription import start_transcription


@ui.page("/")
def page():
    with base_layout():
        with ui.element("div").classes(
            "w-full h-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10"
        ):
            file = input_file()
            input_model()
            input_language()
            input_speaker_detection()
            input_num_speakers()
        ui.separator().classes("mt-4")
        with ui.row().classes("w-full justify-between items-center"):
            settings_btn = ui.button("Advanced Settings", color="gray-100")
            settings_btn.props("size=0.8rem unelevated no-caps icon=settings")
            start_btn = ui.button("Start", on_click=file.upload, color="dark")
            start_btn.props("no-caps unelevated")

    file.on_upload(start_transcription)
    settings_btn.on_click(advanced_settings)
