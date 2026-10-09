

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "72rem"
PADDING_LATERAL: str = "1.5rem"


def hero_blog() -> rx.Component:
    """
    Hero del blog con badge + título + subtítulo.

    Estilo Neon.com:
    - Layout alineado a la izquierda.
    - Badge "BLOG INSTITUCIONAL" con icono.
    - Título con énfasis bicolor.
    - Subtítulo descriptivo.
    - Peso tipográfico 700.

    Returns:
        Componente con el hero completo.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ─────────────────────────────────────────
            rx.flex(
                rx.icon("newspaper", size=12, color=AZUL_MARINO_NEON),
                rx.text(
                    "BLOG INSTITUCIONAL",
                    font_size="0.6875rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    letter_spacing="0.15em",
                    text_transform="uppercase",
                ),
                align="center",
                gap="0.5rem",
                margin_bottom="1.5rem",
            ),
            # ─── Título con énfasis bicolor ────────────────────
            rx.heading(
                rx.text.span("Ideas, guías y "),
                rx.text.span(
                    "novedades",
                    color=AZUL_MARINO_NEON,
                ),
                rx.text.span(" del mundo técnico"),
                as_="h1",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                max_width="48rem",
            ),
            # ─── Subtítulo ─────────────────────────────────────
            rx.text(
                "Artículos sobre tecnología, contaduría, empleabilidad, "
                "tutoriales y vida institucional. Aprende algo nuevo "
                "cada semana.",
                font_size=["1rem", "1.125rem"],
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                max_width="48rem",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=[
            f"4rem {PADDING_LATERAL} 3rem {PADDING_LATERAL}",
            f"6rem {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
        ],
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["hero_blog"]