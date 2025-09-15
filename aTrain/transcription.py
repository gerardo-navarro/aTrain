import traceback
from pathlib import Path

from aTrain_core.check_inputs import check_inputs_transcribe
from aTrain_core.globals import REQUIRED_MODELS_DIR
from aTrain_core.transcribe import prepare_transcription, transcribe
from nicegui import app, events, run
from nicegui.run import SubprocessException
from starlette.formparsers import MultiPartParser

from aTrain.components.modals.error import modal_error
from aTrain.components.modals.finished import modal_finished
from aTrain.components.modals.process import modal_process
from aTrain.globals import EVENT_SENDER, FILE_SIZE_LIMIT

MultiPartParser.spool_max_size = FILE_SIZE_LIMIT


async def start_transcription(file: events.UploadEventArguments):
    process_modal = modal_process()
    _, file_id, timestamp = prepare_transcription(Path(file.name))
    state = app.storage.client
    try:
        check_inputs_transcribe(
            file=file.name,
            model=state.get("model"),
            language=state.get("language"),
            device="cpu",
        )
        await run.cpu_bound(
            transcribe,
            audio_file=file.content,
            file_id=file_id,
            model=state.get("model"),
            language=state.get("language"),
            speaker_detection=state.get("speaker_detection"),
            num_speakers=state.get("num_speakers") or "auto-detect",
            device="cpu",  # fixed for testing
            compute_type="int8",  # fixed for testing
            timestamp=timestamp,
            original_audio_filename=file.name,
            initial_prompt=None,  # fixed for testing
            GUI=EVENT_SENDER,
            required_models_dir=REQUIRED_MODELS_DIR,
        )
        process_modal.delete()
        modal_finished()

    except (SubprocessException, ValueError) as e:
        process_modal.delete()
        modal_error(error=str(e), traceback=traceback.format_exc())
