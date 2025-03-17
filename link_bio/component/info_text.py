import reflex as rx
from link_bio.styles import styles

def info_text(tittle: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            tittle, font_weight="bold", text_align="center", color=styles.Color.PRIMARY.value, as_="span"
        ),
        f" {body}", 
        font_size=styles.Size.MEDIUM.value,
        color= styles.TextColor.BODY.value
    )


