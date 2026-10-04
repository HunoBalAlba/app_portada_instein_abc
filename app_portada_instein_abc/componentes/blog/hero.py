"""
Hero del Blog Institucional.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_ACENTO_FONDO,
    COLOR_ACENTO_TEXTO,
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


def hero_blog() -> rx.Component:
    """
    Hero del blog con badge + título + subtítulo.

    Estilo Neon adaptativo:
    - Badge "BLOG INSTITUCIONAL" con acento.
    - Título grande con span coloreado.
    - Subtítulo descriptivo.

    Returns:
        Componente con el hero completo.
    """
    return rx.vstack(
        # ==========================================================
        # Badge
        # ==========================================================
        rx.flex(
            rx.icon("newspaper", size=12, color=AZUL_MARINO_NEON),
            rx.text(
                "BLOG INSTITUCIONAL",
                font_size="0.75rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.05em",
            ),
            align="center",
            gap="0.5rem",
            padding="0.5rem 1rem",
            border_radius=RADIO_PASTILLA,
            background=COLOR_ACENTO_FONDO,
            border=f"1px solid {BORDE_HOME_AZUL}",
            width="fit-content",
            margin_bottom="1rem",
        ),
        # ==========================================================
        # Título
        # ==========================================================
        rx.heading(
            "Ideas, guías y ",
            rx.text.span("novedades", color=AZUL_MARINO_NEON),
            " del mundo técnico",
            size="9",
            font_weight="900",
            color=COLOR_TEXTO_PRINCIPAL,
            text_align="center",
            letter_spacing="-0.03em",
            line_height="1.1",
        ),
        # ==========================================================
        # Subtítulo
        # ==========================================================
        rx.text(
            "Artículos sobre tecnología, contaduría, empleabilidad, "
            "tutoriales y vida institucional. Aprende algo nuevo cada "
            "semana.",
            font_size="1rem",
            color=COLOR_TEXTO_CUERPO,
            text_align="center",
            max_width="48rem",
            line_height="1.7",
            margin_top="0.5rem",
        ),
        align="center",
        spacing="3",
        padding=f"5rem {PADDING_LATERAL} 3rem {PADDING_LATERAL}",
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["hero_blog"]