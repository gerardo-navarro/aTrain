import os
from aTrain_core.globals import ATRAIN_DIR
from aTrain_core.GUI_integration import EventSender

MODELS_DIR = os.path.join(ATRAIN_DIR, "models")
RUNNING_DOWNLOADS = []
RUNNING_TRANSCRIPTIONS = []
EVENT_SENDER = EventSender()
FILE_SIZE_LIMIT = 1024 * 1024 * 1024 * 10  # 10 GB file size limit
