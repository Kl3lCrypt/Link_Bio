import reflex as rx
from link_bio.styles.styles import Size

def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=image,
            size=20
        ),
        href=url,
        is_external=True,
        margin_top=Size.SMALL.value
    )