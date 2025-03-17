import reflex as rx
from enum import Enum

class Color(Enum):
    PRIMARY = "#0288D1" # Azul claro brillante, para botones y enlaces principales
    SECONDARY ="#81D4FA" # Azul más suave para elementos secundarios
    BACKGROUND = "#1A1A1A"  # Fondo oscuro, para un modo oscuro
    CONTENT = "#1E3A8A"  # Azul más oscuro, para barra de navegación y botones
    NAVBAR= "#212B36"
    FAV = "gray"  # Azul brillante para resaltar detalles
    BG_AVATAR="#B3E5FC"

class TextColor(Enum):
    HEADER = "#FFFFFF"  # Blanco suave para los encabezados
    BODY = "#E0E0E0"  # Gris claro para el texto del cuerpo
    FOOTER = "#BDBDBD"  # Gris aún más suave para el pie de página
