"""
Vista completa del Calendario Académico (ruta "/calendario").
"""

from __future__ import annotations

import reflex as rx

from ..componentes.calendario import (
    cta_calendario,
    grid_info_rapida,
    hero_calendario,
    tabs_calendario,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    FONDO_HOME,
    NOMBRE_INSTITUTO,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_LATERAL: str = "1.5rem"


# ======================================================================
# Vista
# ======================================================================


@rx.page(
    route="/calendario",
    title=f"Calendario académico | {NOMBRE_INSTITUTO}",
)
def vista_calendario() -> rx.Component:
    """Página del calendario académico del instituto."""
    return rx.vstack(
        barra_navegacion_superior(),
        hero_calendario(),
        grid_info_rapida(),
        rx.box(
            tabs_calendario(),
            max_width="64rem",
            margin="0 auto",
            padding=f"2rem {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
            width="100%",
        ),
        cta_calendario(),
        pie_pagina_institucional(),
        align="center",
        min_height="100vh",
        width="100%",
        spacing="0",
        background=FONDO_HOME,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_calendario"]