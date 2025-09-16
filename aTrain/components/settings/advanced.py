from nicegui import ui


def advanced_settings():
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Advanced Settings")
        ui.button("Ok").on_click(dialog.delete)
