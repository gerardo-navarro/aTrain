from nicegui import ui
from aTrain.layouts.card_layout import card_layout
from aTrain.archive import load_faqs


@ui.page("/faq")
def page():
    faqs = load_faqs()
    with card_layout():
        ui.label("Frequently Asked Questions").classes("text-lg text-dark font-bold")
        ui.separator()
        with ui.column().classes("gap-3 w-full"):
            for faq in faqs:
                with ui.expansion(faq["question"], group="faq") as expansion:
                    expansion.classes("w-full").props("dense")
                    ui.label(faq["answer"]).classes("font-light")
