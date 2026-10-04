"""
Datos institucionales del INSTEIN.

Este módulo es la **fuente única de verdad** para:
- Nombre y razón social del instituto.
- Teléfonos y canales de contacto.
- Dirección física y ubicación.
- Redes sociales oficiales.
- Descripción institucional.
- Año de copyright.

Nada de esto debe duplicarse en otros módulos. Si un componente
necesita un dato institucional, se importa desde aquí.

Convención de nombres
---------------------
- `NOMBRE_*`          → nombre(s) del instituto.
- `TELEFONO_*`        → teléfonos de contacto.
- `EMAIL_*`           → direcciones de correo.
- `DIRECCION`, `UBICACION_FISICA`, `HORARIO_ATENCION` → datos de sede.
- `URL_*`             → URLs (WhatsApp, GitHub, etc.).
- `ANIO_COPYRIGHT`    → año actual del copyright.
- `ENTIDAD_COPYRIGHT` → entidad legal del copyright.
- `DESCRIPCION_INSTITUCIONAL` → descripción larga del instituto.

Nota técnica: FORMATO DE TELÉFONOS
----------------------------------
Los teléfonos se almacenan SIN el prefijo internacional (`+591`), en
formato local (8 dígitos). Cuando se necesite el prefijo:

- Para llamadas: `f"tel:+591{TELEFONO_PRINCIPAL}"`.
- Para WhatsApp: `WHATSAPP_URL` ya incluye el prefijo.

Nota técnica: `RedSocial` ES `TypedDict`
----------------------------------------
`RedSocial` es un `TypedDict`, no un `dataclass`. Esto permite que
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
"""

from __future__ import annotations

from typing import TypedDict


# ======================================================================
# 1. Identidad institucional
# ======================================================================

NOMBRE_INSTITUTO: str = "INSTEIN"
"""Nombre corto del instituto (usado en logos y headers)."""

NOMBRE_COMPLETO: str = (
    "INSTITUTO TÉCNICO INTEGRADO SAN ANTONIO DE PADUA"
)
"""Razón social completa del instituto."""

SIGLAS: str = "INSTEIN"
"""Siglas oficiales (alias de `NOMBRE_INSTITUTO`)."""

ANIO_COPYRIGHT: str = "2026"
"""Año del copyright (como `str` para formateo directo)."""

ENTIDAD_COPYRIGHT: str = (
    "INSTEIN - Instituto Técnico Integrado San Antonio de Padua"
)
"""Entidad legal del copyright (para footers y metadatos)."""

DESCRIPCION_INSTITUCIONAL: str = (
    "Formación técnica de excelencia con títulos de Provisión Nacional. "
    "5 carreras, equipamiento moderno y docentes especializados."
)
"""Descripción corta del instituto (para footers y meta description)."""


# ======================================================================
# 2. Contacto
# ======================================================================

TELEFONO_PRINCIPAL: str = "71282993"
"""Teléfono principal de contacto (formato local, sin +591)."""

TELEFONO_SECUNDARIO: str = "79104232"
"""Teléfono alterno de contacto (formato local, sin +591)."""

EMAIL_CONTACTO: str = "contacto@instein.edu.bo"
"""Correo electrónico principal de contacto."""

WHATSAPP_URL: str = f"https://wa.me/591{TELEFONO_PRINCIPAL}"
"""URL de WhatsApp con el teléfono principal (incluye +591)."""


# ======================================================================
# 3. Ubicación
# ======================================================================

DIRECCION: str = "Calle Jorge Carrasco entre 3 y 4"
"""Dirección de la calle (sin referencia de galería)."""

UBICACION_FISICA: str = "Galería FLOR DE ORO 1er. piso"
"""Referencia física dentro del edificio."""

DIRECCION_COMPLETA: str = f"{DIRECCION}, {UBICACION_FISICA}"
"""Dirección + referencia combinadas (para footers y contacto)."""

HORARIO_ATENCION: str = "Lunes a Viernes: 08:30 - 18:30"
"""Horario de atención al público."""


# ======================================================================
# 4. URLs externas
# ======================================================================

GITHUB_URL: str = "https://github.com/tu-usuario/instein"
"""URL del repositorio en GitHub (placeholder)."""


# ======================================================================
# 5. Redes sociales
# ======================================================================

URLS_REDES: dict[str, str] = {
    "TikTok": "https://www.tiktok.com/@instein.oficial",
    "Facebook": "https://www.facebook.com/instein.oficial",
    "Instagram": "https://www.instagram.com/instein.oficial",
    "Telegram": "https://t.me/instein_oficial",
    "Discord": "https://discord.gg/instein",
    "YouTube": "https://www.youtube.com/@instein_oficial",
    "WhatsApp Canal": "https://whatsapp.com/channel/instein",
}
"""URLs de las redes sociales del instituto (referencia)."""


class RedSocial(TypedDict):
    """
    Estructura de una red social institucional.

    Attributes:
        nombre: Nombre visible (ej: "Facebook").
        icono: Nombre del icono Lucide en kebab-case.
        url: URL del perfil institucional.
        color: Color corporativo oficial (hex, no cambia con el modo).
    """

    nombre: str
    icono: str
    url: str
    color: str


REDES_SOCIALES: list[RedSocial] = [
    {
        "nombre": "Facebook",
        "icono": "users",
        "url": URLS_REDES["Facebook"],
        "color": "#1877F2",
    },
    {
        "nombre": "Instagram",
        "icono": "camera",
        "url": URLS_REDES["Instagram"],
        "color": "#E4405F",
    },
    {
        "nombre": "TikTok",
        "icono": "music-2",
        "url": URLS_REDES["TikTok"],
        "color": "#000000",
    },
    {
        "nombre": "YouTube",
        "icono": "circle-play",
        "url": URLS_REDES["YouTube"],
        "color": "#FF0000",
    },
    {
        "nombre": "Telegram",
        "icono": "send",
        "url": URLS_REDES["Telegram"],
        "color": "#0088cc",
    },
    {
        "nombre": "Discord",
        "icono": "message-circle",
        "url": URLS_REDES["Discord"],
        "color": "#5865F2",
    },
]
"""Lista de redes sociales con metadatos visuales.

⚠️ Los colores son corporativos oficiales de cada plataforma y NO
cambian con el `color_mode`. Son colores de marca de terceros.
"""


# ======================================================================
# 6. Datos académicos / legales
# ======================================================================

RESOLUCION_MINISTERIAL: str = "R.M. 0871/2016"
"""Resolución Ministerial que autoriza al instituto."""

DURACION_CARRERA_ANIOS: int = 3
"""Duración estándar de las carreras (años)."""

DURACION_CARRERA_SEMESTRES: int = 6
"""Duración estándar de las carreras (semestres)."""

TITULO_OTORGADO: str = "Técnico Superior en Provisión Nacional"
"""Título otorgado al egresar."""


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Identidad institucional ---
    "ANIO_COPYRIGHT",
    "DESCRIPCION_INSTITUCIONAL",
    "ENTIDAD_COPYRIGHT",
    "NOMBRE_COMPLETO",
    "NOMBRE_INSTITUTO",
    "SIGLAS",
    # --- Contacto ---
    "EMAIL_CONTACTO",
    "TELEFONO_PRINCIPAL",
    "TELEFONO_SECUNDARIO",
    "WHATSAPP_URL",
    # --- Ubicación ---
    "DIRECCION",
    "DIRECCION_COMPLETA",
    "HORARIO_ATENCION",
    "UBICACION_FISICA",
    # --- URLs externas ---
    "GITHUB_URL",
    # --- Redes sociales ---
    "REDES_SOCIALES",
    "RedSocial",
    "URLS_REDES",
    # --- Datos académicos / legales ---
    "DURACION_CARRERA_ANIOS",
    "DURACION_CARRERA_SEMESTRES",
    "RESOLUCION_MINISTERIAL",
    "TITULO_OTORGADO",
]