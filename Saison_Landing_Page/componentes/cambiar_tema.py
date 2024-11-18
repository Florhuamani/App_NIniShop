import reflex as rx
from reflex.style import set_color_mode,color_mode,toggle_color_mode

def cambiar_tema()->rx.Component:
    return rx.hstack(
        rx.button(rx.icon(tag="moon", size=25),on_click=toggle_color_mode,variant="surface"),
        justify="end",
    )