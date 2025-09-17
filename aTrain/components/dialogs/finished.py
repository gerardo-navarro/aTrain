from nicegui import ui, app


def dialog_finished():
    state = app.storage.client
    with ui.dialog(value=True).props("persistent"), ui.card():
        ui.label("Finished")
        ui.label("").bind_text_from(state, "timer", lambda x: f"We transcribed in {x}")
        btn_exit = ui.button("Exit", color="dark").props("unelevated no-caps")
        btn_exit.on_click(ui.navigate.reload)
