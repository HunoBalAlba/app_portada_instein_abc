

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    COLOR_DIVISOR,
    TEXTO_HOME_MAS_SUAVE,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "72rem"
PADDING_LATERAL: str = "1.5rem"


def cta_calendario() -> rx.Component:
    """
    Bloque CTA final hacia /contacto.

    Estilo Neon.com:
    - Enlace simple con flecha.
    - Sin botón grande con glow.
    - Border_top sutil.

    Returns:
        Bloque CTA completo.
    """
    return rx.box(
        rx.flex(
            rx.text(
                "¿Tienes dudas sobre el calendario?",
                font_size="1rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.link(
                rx.text(
                    "Contáctanos",
                    font_size="1rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                ),
                rx.icon("arrow-right", size=16, color=AZUL_MARINO_NEON),
                href="/contacto",
                text_decoration="none",
                display="inline-flex",
                align_items="center",
                gap="0.375rem",
                transition="gap 0.2s",
                _hover={"gap": "0.625rem"},
            ),
            align="center",
            justify="start",
            gap="0.5rem",
            flex_wrap="wrap",
            width="100%",
            padding_top="3rem",
            border_top=f"1px solid {COLOR_DIVISOR}",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=f"4rem {PADDING_LATERAL} 5rem {PADDING_LATERAL}",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["cta_calendario"]