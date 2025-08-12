from nicegui import ui


class CustomUpload(ui.upload):
    def remove_files(self):
        self.run_method("removeQueuedFiles")

    def pick_files(self):
        self.run_method("pickFiles")

    def upload(self):
        self.run_method("upload")

    def reset(self):
        self.run_method("reset")


def file_picker() -> CustomUpload:
    data = {"file_text": "No file selected"}

    uploader = CustomUpload().classes("hidden")
    uploader.on("added", lambda: data.update(file_text="1 file selected"))
    uploader.on("removed", lambda: data.update(file_text="No file selected"))

    with ui.row().classes("gap-0 items-center"):
        select_button = ui.button("Select File")
        with ui.element("div") as div:
            div.classes("border border-rounded w-32 h-8 overflow-hidden")
            ui.label().props("outlined readonly").bind_text(data, "file_text")

    select_button.on_click(uploader.remove_files)
    select_button.on_click(uploader.pick_files)

    return uploader
