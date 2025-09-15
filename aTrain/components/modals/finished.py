from nicegui import ui


def modal_finished():
    with ui.dialog(value=True).props("persistent") as dialog, ui.card():
        ui.label("Finished")
        ui.button("Exit").on_click(dialog.delete)
