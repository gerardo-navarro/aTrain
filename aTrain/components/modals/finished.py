from nicegui import ui, app


def modal_finished():
    state = app.storage.client
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Finished")
        ui.label("").bind_text_from(state, "timer", lambda x: f"We transcribed in {x}")
        ui.button("Exit").on_click(dialog.delete)
