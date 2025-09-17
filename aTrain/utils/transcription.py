import traceback
from concurrent.futures.process import BrokenProcessPool
from multiprocessing import Manager
from pathlib import Path

from aTrain_core.check_inputs import check_inputs_transcribe
from aTrain_core.globals import REQUIRED_MODELS_DIR
from aTrain_core.transcribe import prepare_transcription, transcribe
from nicegui import app, events, run, ui
from nicegui.run import SubprocessException
from nicegui.run import setup as setup_process_pool
from starlette.formparsers import MultiPartParser

from aTrain.components.dialogs.error import dialog_error
from aTrain.components.dialogs.finished import dialog_finished
from aTrain.components.dialogs.process import close_dialog_process, dialog_process


MultiPartParser.spool_max_size = 1024 * 1024 * 1024 * 10  # 10 GB file size limit


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
                device="GPU" if state.get("GPU") else "cpu",
            )
            await run.cpu_bound(
                transcribe,
                audio_file=file.content,
                file_id=file_id,
                model=state.get("model"),
                language=state.get("language"),
                speaker_detection=state.get("speaker_detection"),
                num_speakers=state.get("num_speakers") or "auto-detect",
                device="GPU" if state.get("GPU") else "cpu",
                compute_type=state.get("compute_type"),
                timestamp=timestamp,
                original_audio_filename=file.name,
                initial_prompt=state.get("initial_prompt") or None,
                progress=progress,
                required_models_dir=REQUIRED_MODELS_DIR,
            )
            dialog_finished()

        except (SubprocessException, ValueError) as e:
            dialog_error(error=str(e), traceback=traceback.format_exc())

        except BrokenProcessPool:
            setup_process_pool()
            close_dialog_process()
            ui.navigate.reload()
