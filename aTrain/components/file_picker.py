from nicegui import ui


class CustomUpload(ui.upload):
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
    uploader.on("added", lambda: uploader.set_text("1 File Selected"))

    select_button = ui.button("Select File", icon="attach_file")
    select_button.props("outline color=grey")
    select_button.bind_text(uploader, "file_text")
    select_button.on_click(uploader.pick_files)

    return uploader
