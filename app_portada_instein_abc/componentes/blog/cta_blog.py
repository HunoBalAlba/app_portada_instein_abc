

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
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

    Estilo Neon.com:
    - CTA primario "Ver carreras" (azul marino).
    - CTA secundario "Contactar" (outline).
    - Sin glow.
    - Sin translateY.

    Returns:
        Bloque CTA completo.
    """
    return rx.box(
        rx.vstack(
            rx.heading(
                "¿Listo para ser parte de INSTEIN?",
                as_="h2",
                font_size=["1.5rem", "1.75rem", "2rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                text_align="center",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "La teoría está en el blog. La práctica te espera en "
                "nuestras aulas.",
                font_size="1rem",
                color=TEXTO_HOME_MAS_SUAVE,
                text_align="center",
                max_width="42rem",
                line_height="1.6",
                margin_top="0.5rem",
            ),
            rx.flex(
                # ─── CTA primario ──────────────────────────────
                rx.link(
                    rx.icon("graduation-cap", size=18, color="white"),
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
                    transition="all 0.2s",
                    _hover={"filter": "brightness(1.1)"},
                ),
                # ─── CTA secundario ────────────────────────────
                rx.link(
                    rx.icon("message-circle", size=18),
                    rx.text("Contactar", as_="span", font_weight="600"),
                    href="/contacto",
                    text_decoration="none",
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background="transparent",
                    color=TEXTO_HOME_PRINCIPAL,
                    padding="1rem 2rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="1rem",
                    border=f"1px solid {BORDE_HOME_MEDIO}",
                    transition="all 0.2s",
                    _hover={
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