from nicegui import ui


def sidebar():
    with ui.left_drawer().classes("bg-gray-100"):
        nav_button(icon="🎧", text="Transcribe", path="/")
        nav_button(icon="💾", text="Archive", path="/archive")
        nav_button(icon="🧮", text="Models", path="/models")
        nav_button(icon="📖", text="FAQ", path="/faq")
        ui.separator()
        nav_button(icon="💡", text="About", path="/about")


def nav_button(icon: str, text: str, path: str):
    is_current_page = ui.context.client.page.path == path
    button_color = "gray-200" if is_current_page else "white"
    button_props = "text-color=black align=left flat no-caps"
    button_classes = "w-full rounded-lg"
    with ui.link(target=path).classes("w-full"):
        with ui.button(color=button_color).props(button_props).classes(button_classes):
            ui.label(icon).classes("text-base font-medium mr-4")
            ui.label(text).classes("text-base font-medium")
