import reflex as rx
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Kl3l",
                as_="span",
                color=styles.Color.PRIMARY.value,
                weight="medium",
            ),
            rx.text(
                "Crypt",
                as_="span",
                color=styles.Color.SECONDARY.value,
                weight="medium"
            ),
            style=styles.navbar_tittle_style
        ),
        position="sticky",
        bg=styles.Color.NAVBAR.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEAFAULT.value,
        z_index="999",
        top="0"
    )