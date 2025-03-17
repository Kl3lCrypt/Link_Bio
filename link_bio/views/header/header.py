import reflex as rx
from link_bio.styles.styles import Size, TextColor, Fonts
from link_bio.component.link_icon import link_icon
from link_bio.component.info_text import info_text
from link_bio.styles.colors import Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/wzfsbA01.svg",
                fallback="KL",
                size="7",
                radius="full",
                variant="soft",
                high_contrast=False,
                bg=Color.BG_AVATAR.value,
                border=f"4px solid gray",
                margin="2px"
            ), 
            rx.vstack(
                rx.heading(
                    "Cristian Domenech"
                ),
                rx.text(
                    "@Kl3lCrypt",
                    margin_top= "0px",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("instagram","https://www.instagram.com/__kl3l__/"),
                    link_icon("twitter","https://x.com/Domenech97"),
                    link_icon("Linkedin","https://www.linkedin.com/in/cristian-delgado-domenech/"),
                    spacing="2"
                ),
                align_items="start",
                spacing="0",
                padding_top=Size.SMALL.value,
            ),
            spacing="3"
        ),
        rx.flex(
            info_text("2", "Años de experiencia"),
            info_text("+4", "Proyectos propios"),
            info_text("100%", "Apasionado"),
            width="100%",
            justify="between"
        ),
        rx.text("""Desarrollador de software con conocimientos en Pentesting y Ethical Hacking desde hace 2 años.
                Actualmente, me dedico a desarrollar proyectos personales y crear contenido educativo en línea. 
                Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenid@s! """,
                color=TextColor.BODY.value,
                font_size=Size.DEAFAULT.value,
                ),
        align_items="start",
        spacing="5"
    )