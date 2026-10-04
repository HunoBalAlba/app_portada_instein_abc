"""
Redes sociales y presencia digital del INSTEIN.

Este módulo es la **fuente única de verdad** para:
- URLs de las redes sociales oficiales del instituto.
- Metadatos visuales (icono, color corporativo, nombre).
- Canales de comunicación (WhatsApp Canal, etc.).

Convención de nombres
---------------------
- `URL_*`:     URLs de referencia (una constante por red).
- `URLS_REDES`: dict con todas las URLs indexadas por nombre.
- `REDES_SOCIALES`: lista de `RedSocial` con metadata completa.
- `RedSocial`: TypedDict con la estructura de cada red.

Diferencia con `identidad.py`
-----------------------------
- `identidad.py`   → quién es el instituto (nombre, contacto, dirección).
- `redes.py`       → dónde encontrarlo online (redes sociales).

Nota técnica: COLORES CORPORATIVOS
----------------------------------
Los colores de cada red son **corporativos oficiales** de cada
plataforma y NO cambian con el `color_mode`. Son colores de marca
de terceros, no del proyecto.

Ejemplos:
- Facebook   → `#1877F2` (azul Facebook)
- Instagram  → `#E4405F` (rosa Instagram)
- YouTube    → `#FF0000` (rojo YouTube)
- Discord    → `#5865F2` (blurple Discord)

NOTA: NO reemplazar por tokens de Radix ni por el acento azul marino
del proyecto. Son colores oficiales de cada plataforma.

Nota técnica: `RedSocial` ES `TypedDict`
----------------------------------------
`RedSocial` es un `TypedDict`, NO un `dataclass`. Esto permite que
`rx.foreach` itere sobre `REDES_SOCIALES` sin problemas de tipado
(consistente con `Post`, `Carrera`, etc.).

Los items se construyen con dicts literales:

    {"nombre": "Facebook", "icono": "users", ...}

NO con `RedSocial(nombre=...)`.

Nota técnica: NOMBRES DE ICONOS LUCIDE
--------------------------------------
Los iconos siguen el formato **kebab-case** oficial de Lucide
(https://lucide.dev/icons):

    ✅ message-circle    ❌ message_circle
    ✅ circle-play       ❌ circle_play
    ✅ music-2           ❌ music_2

Nota técnica: ORDEN DE `REDES_SOCIALES`
---------------------------------------
El orden importa: es el orden en que se renderizan en el footer y
en la sección de multimedia. Está ordenado por **relevancia de uso**
en Bolivia:

1. Facebook    → red más usada para comunicación institucional.
2. Instagram   → segunda más usada, contenido visual.
3. TikTok      → fuerte crecimiento entre jóvenes.
4. YouTube     → contenido de largo formato.
5. Telegram    → canal de anuncios.
6. Discord     → comunidad de estudiantes.
"""

from __future__ import annotations

from typing import TypedDict


# ======================================================================
# 1. URLs de referencia (una por red)
# ======================================================================

URL_FACEBOOK: str = "https://www.facebook.com/instein.oficial"
URL_INSTAGRAM: str = "https://www.instagram.com/instein.oficial"
URL_TIKTOK: str = "https://www.tiktok.com/@instein.oficial"
URL_YOUTUBE: str = "https://www.youtube.com/@instein_oficial"
URL_TELEGRAM: str = "https://t.me/instein_oficial"
URL_DISCORD: str = "https://discord.gg/instein"
URL_WHATSAPP_CANAL: str = "https://whatsapp.com/channel/instein"


# ======================================================================
# 2. Dict consolidado de URLs (acceso rápido por nombre)
# ======================================================================

URLS_REDES: dict[str, str] = {
    "Facebook": URL_FACEBOOK,
    "Instagram": URL_INSTAGRAM,
    "TikTok": URL_TIKTOK,
    "YouTube": URL_YOUTUBE,
    "Telegram": URL_TELEGRAM,
    "Discord": URL_DISCORD,
    "WhatsApp Canal": URL_WHATSAPP_CANAL,
}
"""Dict de URLs indexadas por nombre legible.

Útil cuando necesitas la URL pero no la metadata completa:

    url = URLS_REDES["Facebook"]
"""


# ======================================================================
# 3. Modelo: RedSocial
# ======================================================================


class RedSocial(TypedDict):
    """
    Estructura de una red social institucional.

    Attributes:
        nombre: Nombre visible (ej: "Facebook").
        icono: Nombre del icono Lucide en kebab-case.
        url: URL del perfil institucional.
        color: Color corporativo oficial (hex, no cambia con el modo).
        aria_label: Etiqueta accesible para lectores de pantalla.
    """

    nombre: str
    icono: str
    url: str
    color: str
    aria_label: str


# ======================================================================
# 4. Lista completa de redes sociales
# ======================================================================

REDES_SOCIALES: list[RedSocial] = [
    {
        "nombre": "Facebook",
        "icono": "users",
        "url": URL_FACEBOOK,
        "color": "#1877F2",
        "aria_label": "Visitar página de Facebook del INSTEIN",
    },
    {
        "nombre": "Instagram",
        "icono": "camera",
        "url": URL_INSTAGRAM,
        "color": "#E4405F",
        "aria_label": "Visitar perfil de Instagram del INSTEIN",
    },
    {
        "nombre": "TikTok",
        "icono": "music-2",
        "url": URL_TIKTOK,
        "color": "#000000",
        "aria_label": "Visitar perfil de TikTok del INSTEIN",
    },
    {
        "nombre": "YouTube",
        "icono": "circle-play",
        "url": URL_YOUTUBE,
        "color": "#FF0000",
        "aria_label": "Visitar canal de YouTube del INSTEIN",
    },
    {
        "nombre": "Telegram",
        "icono": "send",
        "url": URL_TELEGRAM,
        "color": "#0088cc",
        "aria_label": "Visitar canal de Telegram del INSTEIN",
    },
    {
        "nombre": "Discord",
        "icono": "message-circle",
        "url": URL_DISCORD,
        "color": "#5865F2",
        "aria_label": "Unirse al servidor de Discord del INSTEIN",
    },
]
"""Lista de redes sociales del instituto, ordenada por relevancia.

⚠️ Los colores son corporativos oficiales de cada plataforma y NO
cambian con el `color_mode`.

⚠️ El ORDEN importa: es el orden de renderizado en el footer y en
`seccion_multimedia_institucional`.
"""


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- URLs individuales ---
    "URL_DISCORD",
    "URL_FACEBOOK",
    "URL_INSTAGRAM",
    "URL_TELEGRAM",
    "URL_TIKTOK",
    "URL_WHATSAPP_CANAL",
    "URL_YOUTUBE",
    # --- Dict de URLs ---
    "URLS_REDES",
    # --- Modelo ---
    "RedSocial",
    # --- Lista completa ---
    "REDES_SOCIALES",
]