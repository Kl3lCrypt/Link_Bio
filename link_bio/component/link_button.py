import reflex as rx
import link_bio.styles.styles as styles

def link_button(tittle: str, body: str, image_icon: str ,url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=image_icon,
                    height=styles.Size.BIG.value,
                    width=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    ),
                rx.vstack(
                    rx.text(tittle, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing="1",
                    margin="0px !important",
                ),
                align="center"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )