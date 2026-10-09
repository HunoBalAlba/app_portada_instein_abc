

from __future__ import annotations

import reflex as rx

from app_portada_instein_abc.infraestructura import (
    AZUL_MARINO_NEON,
    TEXTO_HOME_SUAVE,
)


# ======================================================================
# Constantes locales
# ======================================================================

TAMANO_ICONO: int = 16
"""Tamaño en px de los iconos de las viñetas."""

MARGEN_TOP_ICONO: str = "0.125rem"
"""Alineación óptica del icono con la primera línea de texto."""

COLOR_ICONO: str = AZUL_MARINO_NEON
"""Color único de los iconos (azul marino neon)."""


# ======================================================================
# Helper genérico
# ======================================================================


def _vineta(elemento: str, icono: str) -> rx.Component:
    """
    Viñeta genérica: icono a la izquierda + texto a la derecha.

    Args:
        elemento: Texto de la viñeta.
        icono: Nombre del icono Lucide (kebab-case).

    Returns:
        Fila con icono + texto.
    """
    return rx.flex(
        rx.icon(
            icono,
            size=TAMANO_ICONO,
            color=COLOR_ICONO,
            margin_top=MARGEN_TOP_ICONO,
            flex_shrink="0",
        ),
        rx.text(
            elemento,
            color=TEXTO_HOME_SUAVE,
            line_height="1.6",
        ),
        gap="0.75rem",
        align="start",
    )


# ======================================================================
# Viñetas específicas del dominio
# ======================================================================


def vineta_perfil_profesional(elemento: str) -> rx.Component:
    """
    Viñeta con icono de check para el perfil profesional.

    Args:
        elemento: Texto de la habilidad o competencia.

    Returns:
        Fila con icono `check` + texto.
    """
    return _vineta(elemento, "check")


def vineta_campo_laboral(elemento: str) -> rx.Component:
    """
    Viñeta con icono de maletín para el campo laboral.

    Args:
        elemento: Texto de la salida laboral.

    Returns:
        Fila con icono `briefcase-business` + texto.
    """
    return _vineta(elemento, "briefcase-business")


def vineta_requisito(elemento: str) -> rx.Component:
    """
    Viñeta con icono de check para listas de requisitos.

    Args:
        elemento: Texto del requisito.

    Returns:
        Fila con icono `check` + texto.
    """
    return _vineta(elemento, "check")


def vineta_beneficio(elemento: str) -> rx.Component:
    """
    Viñeta con icono de estrella para listas de beneficios.

    Args:
        elemento: Texto del beneficio.

    Returns:
        Fila con icono `star` + texto.
    """
    return _vineta(elemento, "star")


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "TAMANO_ICONO",
    "COLOR_ICONO",
    "MARGEN_TOP_ICONO",
    "vineta_beneficio",
    "vineta_campo_laboral",
    "vineta_perfil_profesional",
    "vineta_requisito",
]