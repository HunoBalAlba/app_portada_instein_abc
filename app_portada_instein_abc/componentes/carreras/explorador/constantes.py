"""
Constantes compartidas del explorador de carrera.

Layout, tamaños y opciones de navegación del explorador.

Nota técnica: SCOPE
-------------------
Este módulo SOLO contiene constantes del **explorador** (buscador,
panel flotante, contenido, widgets). No contiene constantes globales
del proyecto — esas viven en `infraestructura.constantes`.
"""

from __future__ import annotations

from ....infraestructura.constantes.dimensiones import (
    PADDING_LATERAL,
)


# ======================================================================
# Layout
# ======================================================================

ANCHO_MAXIMO_BUSCADOR: str = "48rem"
"""Ancho máximo del input de búsqueda."""

PADDING_EXPLORADOR: str = f"2rem {PADDING_LATERAL}"
"""Padding del contenedor principal del explorador."""

PADDING_INFERIOR_GRID: str = "0 auto 3rem auto"
"""Margen inferior del grid de imágenes."""

PADDING_PANEL_FLOTANTE: str = "1.5rem"
"""Padding interno del panel flotante."""

ALTO_MINIMO_CONTENIDO: str = "20rem"
"""Altura mínima del área de contenido dinámico (para evitar saltos)."""


# ======================================================================
# Tamaños
# ======================================================================

TAMANO_BOTON_FLOTANTE: str = "3.5rem"
"""Tamaño del botón flotante del panel de selección."""

TAMANO_ICONO_OPCION: int = 22
"""Tamaño del icono en los botones de opción del explorador (px)."""

TAMANO_ICONO_ESTADO_VACIO: int = 48
"""Tamaño del icono del estado vacío (px)."""

ALTO_BANNER_CARD: str = "5rem"
"""Altura del banner (imagen superior) en las cards del explorador."""

ALTO_BANNER_CARD_GRANDE: str = "7rem"
"""Altura del banner en las cards destacadas del buscador."""


# ======================================================================
# Opciones del explorador
# ======================================================================

OPCIONES_EXPLORADOR: list[tuple[str, str, str]] = [
    ("info", "Información", "info"),
    ("book-open", "Plan", "plan"),
    ("user-check", "Perfil", "perfil"),
    ("briefcase", "Campo", "campo"),
    ("help-circle", "FAQ", "faq"),
]
"""Tuplas `(icono, etiqueta, id_seccion)` de las 5 secciones."""


# ======================================================================
# Ancho del panel flotante (responsive)
# ======================================================================

ANCHO_PANEL_FLOTANTE: list[str] = [
    "calc(100% - 4rem)",
    "calc(100% - 4rem)",
    "22rem",
    "26rem",
]
"""Ancho del panel flotante en cada breakpoint."""

POSICION_PANEL_FLOTANTE: str = "6rem"
"""Distancia desde abajo para el panel flotante."""


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ALTO_BANNER_CARD",
    "ALTO_BANNER_CARD_GRANDE",
    "ALTO_MINIMO_CONTENIDO",
    "ANCHO_MAXIMO_BUSCADOR",
    "ANCHO_PANEL_FLOTANTE",
    "OPCIONES_EXPLORADOR",
    "PADDING_EXPLORADOR",
    "PADDING_INFERIOR_GRID",
    "PADDING_PANEL_FLOTANTE",
    "POSICION_PANEL_FLOTANTE",
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_ICONO_OPCION",
]