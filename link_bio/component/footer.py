import reflex as rx
from link_bio.styles.styles import Size, TextColor, Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/picsvg_download.svg",
            height=Size.XBIG.value,
            width=Size.XLBIG.value,
            border=f"1px solid {Color.FAV.value}",
        ),
        rx.link(
            "© 2025-2026 Kl3lCrypt by KL3Labs . Todos los derechos reservados",
            href="https://github.com/Kl3lCrypt",
            is_external=True,
            font_size=Size.MEDIUM.value,
            align="center",
            white_space="nowrap",
            overflow="hidden",
            text_overflow="ellipsis",  # 🔹 Recorta con '...'
            max_width="80vw",  # 🔹 Limita el ancho al 80% del viewport
        ),
        rx.text(
            "Building software from Spain to the World",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important",
        ),
        align="center",
        padding_bottom= Size.XBIG.value,
        color=TextColor.FOOTER.value,
    )