import reflex as rx
from link_bio.component.link_button import link_button
from link_bio.component.tittle import tittle


def links() -> rx.Component:
    return rx.vstack(
        tittle("Comunidad"),
        link_button("YouTube","Desarrollo y ciberseguridad!","youtube", "https://www.youtube.com/@Kl3lCrypt"),
        link_button("GitHub", "Poroyectos y desarrollos", "github", "https://github.com/Kl3lCrypt"),
        link_button("Twitch", "Directos casi todas las semanas!", "twitch", "https://www.twitch.tv/kl3lcrypt/"),
        link_button("Email", "Contacto para proyectos!! (kl3lcrypt@gmail.com)","mail-plus", "mailto:kl3lcrypt@gmail.com"),
        width="100%",
        spacing="3"
    )