import reflex as rx
def seccion()->rx.Component:
    return rx.vstack(
        rx.container(
            rx.hstack(
                rx.heading(
            rx.text.span("Haz que cada temporada sea inolvidable. Encuentra los productos perfectos para cada ocasión y recíbelos justo cuando los necesitas. Sin esperas, sin complicaciones.",color=rx.color("black",10)),
            ),
            rx.image(src="https://images.unsplash.com/photo-1672839825620-19bcea184fcc?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                     widht=200,
                     height=200,
                     align="end"),
            ),
            
            rx.vstack(
                rx.link(
                rx.button(rx.icon(tag="pen"),"Regístrate",),
                href="https://forms.gle/jFs3bNxdqgDeWuuv8",
                is_external=False,
                margin_top="5em",
                padding="5em",
                justify="center",
                position="relative"
            ),
        
            )

        ),
        
            padding_top="5em",
            align="start",
            text_align="start",
            height="500px",
            background="#f1f7fe"
    )
