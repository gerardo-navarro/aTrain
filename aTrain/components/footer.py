from nicegui import ui
from importlib.resources import files

BANDAS_LOGO = files("aTrain") / "static" / "images" / "Bandas_Logo.svg"
PAPER_TEXT = "Using aTrain for research? Please cite our paper as per our license:"
PAPER_TITLE = "Take the aTrain. Introducing an interface for the Accessible Transcription of Interviews"
PAPER_LINK = "https://doi.org/10.1016/j.jbef.2024.100891"


def footer():
    with ui.footer(wrap=False).classes("bg-white justify-between items-center p-10"):
        ui.image(BANDAS_LOGO).props("height='50px' width='150px' fit='contain'")
        with ui.column(align_items="end", wrap=True).classes("gap-0"):
            ui.label(PAPER_TEXT).classes("text-black")
            ui.link(PAPER_TITLE, target=PAPER_LINK, new_tab=True)
