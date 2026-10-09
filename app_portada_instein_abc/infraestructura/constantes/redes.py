

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
        "icono": "circle_play",
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
        "icono": "message_circle",
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