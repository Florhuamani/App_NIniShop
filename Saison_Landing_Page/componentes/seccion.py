import reflex as rx
def seccion()->rx.Component:
    return rx.vstack(
        rx.container(
            rx.hstack(
                rx.heading(
                    rx.text.strong(
                        "No te pierdas nada, ¡Descarga nuestra aplicación ahora!",
                        color=("gray",10),
                        font_size="1.5em",
                        text_align="center",
                        margin_bottom="1em"
                    ),
                    rx.hstack(
                    rx.text.span(
                        "Haz que cada temporada sea inolvidable. Encuentra los productos perfectos para cada ocasión y recíbelos justo cuando los necesitas. Sin esperas, sin complicaciones",
                        color=("black",10),
                        font_size="1.2em",
                        align="left",
                        widht="60%",
                        margin_right="2em")),
                    ),
           
            rx.image(src="https://storage.googleapis.com/a1aa/image/gZMiFsAAIK4GLxeJv6WexQYvikbGZgbLbSf0nWpGNYhAcDonA.jpg",
                     widht=200,
                     height=200,
                     align="center"),
            ),
            
            
            rx.vstack(
                rx.link(
                rx.button(rx.icon(tag="pen"),"Regístrate",),
                href="https://forms.gle/jFs3bNxdqgDeWuuv8",
                is_external=False,
                margin_top="5em",
                padding="5em",
                justify="center",
                position="absolute",
                top="50%",
                left="40%"
            ),
            align_items="center"            )

        ),
        
            padding_top="5em",
            align="center",
            text_align="start",
            height="500px",
            background="#f5edeb"
    )
