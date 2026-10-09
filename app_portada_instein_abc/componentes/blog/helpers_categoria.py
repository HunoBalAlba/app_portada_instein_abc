

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    BORDE_HOME_SUAVE,
    COLOR_FONDO_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_PASTILLA,
)


# ======================================================================
# Badge de categoría
# ======================================================================


def _badge_ui(color: str, icono: str, etiqueta: str) -> rx.Component:
    """
    Construye el componente del badge con valores fijos.

    Args:
        color: Nombre del scheme Radix (blue, violet, green, ...).
        icono: Nombre del icono Lucide (kebab-case).
        etiqueta: Texto visible del badge.

    Returns:
        Badge pill con icono + texto.
    """
    return rx.flex(
        rx.icon(icono, size=12, color=rx.color(color, 11)),
        rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=rx.color(color, 11),
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        align="center",
        gap="0.25rem",
        padding="0.25rem 0.625rem",
        border_radius=RADIO_PASTILLA,
        background=rx.color(color, 3),
        border=f"1px solid {rx.color(color, 7)}",
        width="fit-content",
    )


def badge_categoria(clave) -> rx.Component:
    """
    Badge con el nombre de la categoría del post.

    Args:
        clave: Clave de categoría (str estático o `Var` reactivo).

    Returns:
        Componente del badge resuelto vía `rx.match`.
    """
    return rx.match(
        clave,
        ("tecnologia", _badge_ui("blue", "cpu", "Tecnología")),
        ("contaduria", _badge_ui("violet", "calculator", "Contaduría")),
        ("empleabilidad", _badge_ui("green", "trending-up", "Empleabilidad")),
        ("institucional", _badge_ui("crimson", "landmark", "Institucional")),
        ("estudiantes", _badge_ui("orange", "graduation-cap", "Estudiantes")),
        ("tutoriales", _badge_ui("cyan", "book-open", "Tutoriales")),
        _badge_ui("gray", "list", "Todas"),
    )


# ======================================================================
# Icono grande de categoría (placeholder de imagen)
# ======================================================================


def icono_categoria(clave) -> rx.Component:
    """
    Icono grande de la categoría (placeholder de imagen).

    Args:
        clave: Clave de categoría (str o `Var`).

    Returns:
        Icono grande con color según la categoría.
    """
    return rx.match(
        clave,
        ("tecnologia", rx.icon("cpu", size=40, color=rx.color("blue", 11))),
        ("contaduria", rx.icon("calculator", size=40, color=rx.color("violet", 11))),
        ("empleabilidad", rx.icon("trending-up", size=40, color=rx.color("green", 11))),
        ("institucional", rx.icon("landmark", size=40, color=rx.color("crimson", 11))),
        ("estudiantes", rx.icon("graduation-cap", size=40, color=rx.color("orange", 11))),
        ("tutoriales", rx.icon("book-open", size=40, color=rx.color("cyan", 11))),
        rx.icon("list", size=40, color=rx.color("gray", 11)),
    )


# ======================================================================
# Fondo y borde de categoría
# ======================================================================


def fondo_categoria(clave) -> rx.Var:
    """
    Fondo suave del placeholder de imagen.

    Args:
        clave: Clave de categoría (str o `Var`).

    Returns:
        Var con el color de fondo adaptativo.
    """
    return rx.match(
        clave,
        ("tecnologia", rx.color("blue", 3)),
        ("contaduria", rx.color("violet", 3)),
        ("empleabilidad", rx.color("green", 3)),
        ("institucional", rx.color("crimson", 3)),
        ("estudiantes", rx.color("orange", 3)),
        ("tutoriales", rx.color("cyan", 3)),
        COLOR_FONDO_SUAVE,
    )


def borde_categoria(clave) -> rx.Var:
    """
    Borde del placeholder de imagen.

    Args:
        clave: Clave de categoría (str o `Var`).

    Returns:
        Var con el borde adaptativo.
    """
    return rx.match(
        clave,
        ("tecnologia", f"1px solid {rx.color('blue', 7)}"),
        ("contaduria", f"1px solid {rx.color('violet', 7)}"),
        ("empleabilidad", f"1px solid {rx.color('green', 7)}"),
        ("institucional", f"1px solid {rx.color('crimson', 7)}"),
        ("estudiantes", f"1px solid {rx.color('orange', 7)}"),
        ("tutoriales", f"1px solid {rx.color('cyan', 7)}"),
        f"1px solid {BORDE_HOME_SUAVE}",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "badge_categoria",
    "borde_categoria",
    "fondo_categoria",
    "icono_categoria",
]