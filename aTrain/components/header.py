from nicegui import ui
from importlib.resources import files
from aTrain.version import __version__

ATRAIN_LOGO = files("aTrain") / "static" / "images" / "logo.svg"
GITHUB_LOGO = files("aTrain") / "static" / "images" / "github.svg"
GITHUB_LINK = "https://github.com/JuergenFleiss/aTrain"


def header():
    with ui.header().classes("bg-white justify-between items-center px-10"):
        with ui.row().classes("items-center"):
            (
                ui.button()
                .props("color=white text-color=black icon=menu flat")
                .classes("lt-md")
            )
            ui.image(ATRAIN_LOGO).props("height=30px width=80px fit=contain")
        with ui.row().classes("items-center"):
            ui.image(GITHUB_LOGO).props("height=25px width=25px fit=contain")
            with ui.link(target=GITHUB_LINK, new_tab=True).classes("text-black"):
                ui.label(f"Version {__version__}")
