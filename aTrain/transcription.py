import traceback
from pathlib import Path
from concurrent.futures.process import BrokenProcessPool
from aTrain_core.check_inputs import check_inputs_transcribe
from aTrain_core.globals import REQUIRED_MODELS_DIR
from aTrain_core.transcribe import prepare_transcription, transcribe
from nicegui import app, events, run
from nicegui.run import SubprocessException, setup as setup_process_pool
from starlette.formparsers import MultiPartParser
from multiprocessing import Manager
from aTrain.components.dialogs.error import dialog_error
from aTrain.components.dialogs.finished import dialog_finished
from aTrain.components.dialogs.process import dialog_process, close_dialog_process
from aTrain.globals import FILE_SIZE_LIMIT

MultiPartParser.spool_max_size = FILE_SIZE_LIMIT


async def start_transcription(file: events.UploadEventArguments):
    with Manager() as manager:
        progress = manager.dict({"task": "Prepare", "current": 0, "total": 999999})
        dialog_process(progress)
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
                progress=progress,
                required_models_dir=REQUIRED_MODELS_DIR,
            )
            dialog_finished()

        except (SubprocessException, ValueError) as e:
            dialog_error(error=str(e), traceback=traceback.format_exc())

        except BrokenProcessPool:
            close_dialog_process()
            setup_process_pool()
