from nicegui import ui


def advanced_settings():
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Advanced Settings")
        btn_ok = ui.button("Ok", color="dark").props("unelevated no-caps")
        btn_ok.on_click(dialog.delete)
