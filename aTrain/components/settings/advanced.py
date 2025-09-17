from nicegui import ui, app
from aTrain_core.check_inputs import ComputeType
from torch import cuda


def advanced_settings(open: bool):
    with ui.dialog(value=open) as dialog, ui.card() as card:
        dialog.props("persistent position=right full-height").classes("[&>*]:p-0")
        card.props("square").classes("w-72 xl:w-96 p-6 gap-6")
        ui.label("Advanced Settings").classes("text-lg text-dark font-bold")
        settings_gpu()
        settings_compute_type()
        settings_initial_prompt()
        btn_ok = ui.button("Ok", color="dark").props("unelevated no-caps")
        btn_ok.on_click(dialog.delete)


def settings_gpu():
    tooltip = "GPU acceleration is only available on cuda-enabled NVIDIA GPUs"
    with ui.column().classes("w-full gap-2"):
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("GPU acceleration").classes("font-bold text-dark")
            ui.icon("info_outline", size="sm", color="grey").tooltip(tooltip)
        ui.separator()
        if cuda.is_available():
            switch_gpu = ui.switch("GPU", value=True).props("color=dark")
        else:
            switch_gpu = ui.switch("GPU", value=False).props("color=dark disable")
    switch_gpu.bind_value(app.storage.client, "GPU")
    switch_gpu.on_value_change(set_compute_options)


def settings_compute_type():
    global select_compute
    tooltip = "Int8 is the only option on CPU"
    with ui.column().classes("w-full gap-2"):
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("Compute Type").classes("font-bold text-dark")
            ui.icon("info_outline", size="sm", color="grey").tooltip(tooltip)
        ui.separator()
        select_compute = ui.select(options=[])
        select_compute.props("filled bg-color=gray-100 color=dark").classes("w-full")
        set_compute_options()
    select_compute.bind_value(app.storage.client, "compute_type")


def settings_initial_prompt():
    with ui.column().classes("w-full gap-2"):
        ui.label("Initial Prompt").classes("font-bold text-dark")
        ui.separator()
        textarea = ui.textarea(placeholder="Type here...")
        textarea.props("color=dark autogrow clearable").classes("w-full")
    textarea.bind_value(app.storage.client, "initial_prompt")


def set_compute_options():
    if app.storage.client["GPU"]:
        options = [x.value for x in ComputeType]
    else:
        options = [ComputeType.INT8.value]
    select_compute.set_options(options, value=ComputeType.INT8.value)
