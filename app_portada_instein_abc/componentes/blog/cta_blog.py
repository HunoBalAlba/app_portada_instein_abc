"""
CTA final del blog: hacia /carreras o /contacto.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "72rem"
PADDING_LATERAL: str = "1.5rem"


def cta_blog() -> rx.Component:
    """
    CTA final del blog hacia /carreras o /contacto.

    Estilo Neon adaptativo:
    - Botón primario "Ver carreras" con azul marino neon.
    - Botón secundario "Contactar" con borde.
    - Layout responsive (columna → fila).

    Returns:
        Bloque CTA completo.
    """
    return rx.box(
        rx.vstack(
            rx.heading(
                "¿Listo para ser parte de INSTEIN?",
                size="7",
                font_weight="900",
                color=COLOR_TEXTO_PRINCIPAL,
                text_align="center",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "La teoría está en el blog. La práctica te espera en "
                "nuestras aulas.",
                font_size="1rem",
                color=COLOR_TEXTO_CUERPO,
                text_align="center",
                max_width="42rem",
                line_height="1.6",
                margin_top="0.5rem",
            ),
            rx.flex(
                # --- CTA primario ---
                rx.link(
                    rx.icon("graduation-cap", size=18),
                    rx.text("Ver carreras", as_="span", font_weight="700"),
                    href="/carreras",
                    text_decoration="none",
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background=AZUL_MARINO_NEON,
                    color="white",
                    padding="1rem 2rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="1rem",
                    box_shadow=f"0 10px 25px -5px {AZUL_MARINO_NEON}",
                    transition="all 0.2s",
                    _hover={
                        "transform": "translateY(-2px)",
                        "filter": "brightness(1.1)",
                    },
                ),
                # --- CTA secundario ---
                rx.link(
                    rx.icon("message-circle", size=18),
                    rx.text("Contactar", as_="span", font_weight="600"),
                    href="/contacto",
                    text_decoration="none",
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background="transparent",
                    color=COLOR_TEXTO_PRINCIPAL,
                    padding="1rem 2rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="1rem",
                    border=f"1px solid {BORDE_HOME_SUAVE}",
                    transition="all 0.2s",
                    _hover={
                        "transform": "translateY(-2px)",
                        "border_color": AZUL_MARINO_NEON,
                    },
                ),
                gap="0.75rem",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                align="center",
                justify="center",
                margin_top="1.5rem",
            ),
            align="center",
            spacing="2",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=f"4rem {PADDING_LATERAL} 5rem {PADDING_LATERAL}",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["cta_blog"]