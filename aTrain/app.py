import os

import webview
from flask import Flask
from wakepy import keep


from .api import api
from .globals import EVENT_SENDER
from .models import stop_all_downloads
from .routes import routes
from .transcription import stop_all_transcriptions

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(api)


def run_app() -> None:
    """A function that creates creates the application window and runs the app."""
    window = webview.create_window("aTrain", app, maximized=True)
    window.events.closed += teardown
    with keep.running():
        webview.start()
    # We need to hard exit here, since certain download threads will never stop for some reason.
    os._exit(0)


def teardown() -> None:
    """A function that is invoked when the application window closes and which terminates all processes that are still running."""
    EVENT_SENDER.end_stream()
    stop_all_transcriptions()
    stop_all_downloads()
