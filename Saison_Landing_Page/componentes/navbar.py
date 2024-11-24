import reflex as rx

def navbar()->rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.heading("Saison",size="8",weight="bold"),
         
        ),
        rx.hstack(
            rx.link("Inicio",href="/#",size="3",weight="bold"),
            rx.link("Iniciar Sesión",href="/#",size="3",weight="bold"),
            justify="end",
            spacing="5"
            ),
            justify="between",
            align_items="center",
            padding="1em",
            width="100%",
            bg=rx.color("brown",3)
        
    )