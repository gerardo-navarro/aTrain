from pathlib import Path

from aTrain_core.globals import REQUIRED_MODELS_DIR
from aTrain_core.transcribe import prepare_transcription, transcribe
from aTrain_core.check_inputs import check_inputs_transcribe
from nicegui import app, events, run, ui
from nicegui.run import SubprocessException

from aTrain.globals import EVENT_SENDER, FILE_SIZE_LIMIT
from starlette.formparsers import MultiPartParser

MultiPartParser.spool_max_size = FILE_SIZE_LIMIT


async def start_transcription(file: events.UploadEventArguments):
    _, file_id, timestamp = prepare_transcription(Path(file.name))
    settings = app.storage.client
    try:
        check_inputs_transcribe(
            file=file.name,
            model=settings.get("model"),
            language=settings.get("language"),
            device="cpu",
        )
        ui.notify("running")
        await run.cpu_bound(
            transcribe,
            audio_file=file.content,
            file_id=file_id,
            model=settings.get("model"),
            language=settings.get("language"),
            speaker_detection=settings.get("speaker_detection"),
            num_speakers=settings.get("num_speakers") or "auto-detect",
            device="cpu",  # fixed for testing
            compute_type="int8",  # fixed for testing
            timestamp=timestamp,
            original_audio_filename=file.name,
            initial_prompt=None,  # fixed for testing
            GUI=EVENT_SENDER,
            required_models_dir=REQUIRED_MODELS_DIR,
        )
        ui.notify("Success")
    except (SubprocessException, ValueError) as e:
        ui.notify(e)
