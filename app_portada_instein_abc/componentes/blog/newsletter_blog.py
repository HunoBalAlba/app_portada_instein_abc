"""
Bloque de newsletter inline al pie del blog.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_ACENTO_FONDO,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
)


def newsletter_blog() -> rx.Component:
    """
    Bloque de newsletter inline al pie del blog.

    Estilo Neon adaptativo:
    - Icono de mail centrado.
    - Título + subtítulo.
    - Input de email + botón "Suscribirme".

    Returns:
        Bloque de newsletter completo.
    """
    return rx.box(
        rx.vstack(
            rx.icon("mail", size=32, color=AZUL_MARINO_NEON),
            rx.heading(
                "Recibe los nuevos artículos",
                size="5",
                font_weight="800",
                color=COLOR_TEXTO_PRINCIPAL,
                text_align="center",
            ),
            rx.text(
                "Suscríbete a nuestro newsletter y recibe las novedades "
                "del blog directamente en tu correo.",
                font_size="0.875rem",
                color=COLOR_TEXTO_SECUNDARIO,
                text_align="center",
                max_width="32rem",
                line_height="1.6",
            ),
            rx.flex(
                rx.input(
                    placeholder="tu@email.com",
                    type="email",
                    size="3",
                    width="100%",
                    flex="1",
                    min_width="0",
                ),
                rx.button(
                    rx.icon("send", size=16),
                    rx.text("Suscribirme", as_="span", font_weight="700"),
                    size="3",
                    variant="solid",
                    color_scheme="crimson",
                    cursor="pointer",
                    flex_shrink="0",
                ),
                gap="0.5rem",
                width="100%",
                max_width="32rem",
                align="center",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                margin_top="0.5rem",
            ),
            align="center",
            spacing="2",
            width="100%",
        ),
        padding="2.5rem 1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_ACENTO_FONDO,
        border=f"1px solid {BORDE_HOME_AZUL}",
        width="100%",
        margin_top="3rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["newsletter_blog"]