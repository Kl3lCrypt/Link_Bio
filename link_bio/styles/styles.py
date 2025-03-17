from enum import Enum
import reflex as rx
from .colors import Color,TextColor
from .fonts import Fonts


#Constantes
MAX_WIDTH="560px"


#Sizes
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEAFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    LBIG="3em"
    XBIG="4em"
    XLBIG="8em"

#STYLES

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Fonts.DEFAULT.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEAFAULT.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "_hover": {
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
    rx.heading: {
        "font_size": Size.BIG.value,
        "color": TextColor.HEADER.value,
        "font_family":Fonts.TITTLE.value,
    }
}



navbar_tittle_style = dict(
    font_family=Fonts.LOGO.value,
    font_size=Size.LARGE.value,
)


tittle_style = dict(
    width="100%",
    padding_top=Size.DEAFAULT.value,
)

button_tittle_style= dict(
    font_size="16px",
    color=TextColor.HEADER.value,
    font_family= Fonts.TITTLE.value,
)

button_body_style= dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    font_family=Fonts.DEFAULT.value
)
