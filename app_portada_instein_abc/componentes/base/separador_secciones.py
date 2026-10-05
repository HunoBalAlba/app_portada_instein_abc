"""
Separador horizontal sutil entre secciones (estilo Neon.com).

Componente reutilizable por todas las vistas que necesitan
marcar visualmente el cambio de sección con una línea fina.

Uso:
    from ..componentes.base.separador_secciones import separador_secciones

    ...
    separador_secciones()
    ...
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import COLOR_DIVISOR


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_DEFECTO: str = "80rem"
PADDING_X_DEFECTO: str = "1.5rem"


# ======================================================================
# Componente
# ======================================================================


def separador_secciones(
    ancho_maximo: str = ANCHO_MAXIMO_DEFECTO,
    padding_x: str = PADDING_X_DEFECTO,
) -> rx.Component:
    """
    Línea horizontal sutil entre secciones.

    Estilo Neon.com: separador fino que marca el cambio de sección
    sin gritar. Ancho máximo consistente con las secciones.

    Args:
        ancho_maximo: Ancho máximo del contenedor (default "80rem").
        padding_x: Padding lateral (default "1.5rem").

    Returns:
        Componente `rx.box` con una línea de 1px de alto.
    """
    return rx.box(
        rx.box(
            height="1px",
            width="100%",
            background=COLOR_DIVISOR,
        ),
        max_width=ancho_maximo,
        margin="0 auto",
        padding_x=padding_x,
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["separador_secciones"]