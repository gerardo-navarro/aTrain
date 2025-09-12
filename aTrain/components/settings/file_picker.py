from nicegui import ui


class CustomUpload(ui.upload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on("added", self.set_added)
        self.set_select()

    def pick_files(self):
        self.reset()
        self.set_select()
        self.run_method("pickFiles")

    def upload(self):
        self.run_method("upload")

    def set_added(self):
        self.file_text = "1 File Added"
        self.file_icon = "file_present"

    def set_select(self):
        self.file_text = "Select File"
        self.file_icon = "attach_file"


def file_picker() -> CustomUpload:
    uploader = CustomUpload().classes("hidden")

    with ui.column():
        ui.label("Select file").classes("h2 font-bold text-primary")
        ui.separator()
        select_button = ui.button().props("outline color=grey").classes("w-full h-full")

    select_button.bind_text(uploader, "file_text")
    select_button.bind_icon(uploader, "file_icon")
    select_button.on_click(uploader.pick_files)

    return uploader
