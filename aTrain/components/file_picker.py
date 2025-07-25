from nicegui import ui


def file_picker() -> ui.upload:
    data = {"file_text": "No file selected"}

    uploader = ui.upload().classes("hidden")
    uploader.on("added", lambda e: data.update(file_text=e.args[0]["__key"]))
    uploader.on("removed", lambda: data.update(file_text="No file selected"))

    with ui.row().classes("gap-0 items-center"):
        select_button = ui.button("Select File")
        div_classes = "border border-rounded w-32 h-8 overflow-hidden"
        with ui.element("div").classes(div_classes):
            ui.label().props("outlined readonly").bind_text(data, "file_text")

    select_button.on_click(lambda: uploader.run_method("removeQueuedFiles"))
    select_button.on_click(lambda: uploader.run_method("pickFiles"))

    return uploader
