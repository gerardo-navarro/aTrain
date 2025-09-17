from nicegui import ui


def dialog_error(error: str, traceback: str):
    with ui.dialog(value=True).props("persistent"), ui.card():
        ui.label("Error")
        ui.label(error)
        ui.label("Traceback")
        ui.label(traceback)
        btn_exit = ui.button("Exit", color="dark").props("unelevated no-caps")
        btn_exit.on_click(ui.navigate.reload)
