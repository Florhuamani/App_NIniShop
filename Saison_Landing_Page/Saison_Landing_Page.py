import reflex as rx

from .componentes.navbar import navbar
from .componentes.seccion import seccion
from .componentes.cambiar_tema import cambiar_tema

def index()->rx.Component:
    return rx.box(
        navbar(),
        cambiar_tema(),
        seccion(),
    )
app=rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
app.add_page(index)