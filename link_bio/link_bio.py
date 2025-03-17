import reflex as rx
from link_bio.component.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.component.footer import footer
from link_bio.styles import styles
from link_bio.styles.styles import Size


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index) 

