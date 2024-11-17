import reflex as rx
def seccion()->rx.Component:
    return rx.vstack(
        rx.heading(
            rx.text.span("Saison",color=rx.color("amber",7)),
            "Haz que cada temporada sea inolvidable. Encuentra los productos perfectos para cada ocasión y recíbelos justo cuando los necesitas. Sin esperas, sin complicaciones.",
            rx.text.quote("Saison",color=rx.color("gold",9))),
            rx.link(
                rx.button(rx.icon(tag="airplay"),"Regístrate",),
                href="https://forms.gle/jFs3bNxdqgDeWuuv8",
                is_external=True,
                margin_top="3em",
            ),
            padding_top="8em",
            align="center",
            height="800px"
    )