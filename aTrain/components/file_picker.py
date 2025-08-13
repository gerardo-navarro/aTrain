from nicegui import ui


class CustomUpload(ui.upload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on("added", lambda: self.set_text("1 File Selected"))
        self.file_text = "Select File"

    def pick_files(self):
        self.reset()
        self.file_text = "Select File"
        self.run_method("pickFiles")

    def upload(self):
        self.run_method("upload")

    def set_text(self, text):
        self.file_text = text


def file_picker() -> CustomUpload:
    uploader = CustomUpload().classes("hidden")

    select_button = ui.button(icon="attach_file").props("outline color=grey")
    select_button.bind_text(uploader, "file_text").on_click(uploader.pick_files)

    return uploader
