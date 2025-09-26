from aTrain_core.check_inputs import ComputeType
from nicegui import ElementFilter, app, ui
from torch import cuda


def advanced_settings(open: bool):
    with ui.dialog(value=open) as dialog, ui.card() as card:
        dialog.props("position=right full-height").classes("[&>*]:p-0")
        card.props("square").classes("w-72 xl:w-96 p-6 gap-6")
        ui.label("Advanced Settings").classes("text-lg text-dark font-bold")
        input_gpu()
        input_compute_type()
        input_initial_prompt()
        btn = ui.button("Ok", color="dark").props("unelevated no-caps")
        btn.on_click(dialog.close)
        dialog.on("hide", dialog.delete)


def input_gpu():
    tooltip = "GPU acceleration is only available on cuda-enabled NVIDIA GPUs"
    with ui.column().classes("w-full gap-2"):
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("GPU acceleration").classes("font-bold text-dark")
            ui.icon("info_outline", size="sm", color="grey").tooltip(tooltip)
        ui.separator()
        if cuda.is_available():
            switch = ui.switch("GPU", value=True).props("color=dark")
        else:
            switch = ui.switch("GPU", value=False).props("color=dark disable")
    switch.bind_value(app.storage.client, "GPU")
    switch.on_value_change(set_compute_options)


def input_compute_type():
    tooltip = "Int8 is the only option on CPU"
    with ui.column().classes("w-full gap-2"):
        with ui.row(align_items="center").classes("w-full justify-between"):
            ui.label("Compute Type").classes("font-bold text-dark")
            ui.icon("info_outline", size="sm", color="grey").tooltip(tooltip)
        ui.separator()
        select = ui.select(options=[]).mark("select_compute")
        select.props("filled bg-color=gray-100 color=dark").classes("w-full")
    select.bind_value(app.storage.client, "compute_type")
    set_compute_options()


def input_initial_prompt():
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
    for select in ElementFilter(marker="select_compute", kind=ui.select):
        select.set_options(options, value=ComputeType.INT8.value)
