

from __future__ import annotations

import reflex as rx

from ...dominio.modelos.calendario import BIMESTRES_2026
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Tarjeta individual de bimestre
# ======================================================================


def _tarjeta_bimestre(bimestre: dict) -> rx.Component:
    """
    Tarjeta de un bimestre con su info clave.

    Estilo Neon.com:
    - Número grande (I, II, III, IV).
    - Período + rango de fechas.
    - Borde superior de acento.
    - Hover sutil.

    Args:
        bimestre: `BimestreAcademico`.

    Returns:
        Card visual del bimestre.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge del número ───────────────────────────────
            rx.flex(
                rx.text(
                    str(bimestre["numero"]),
                    font_size="0.75rem",
                    font_weight="800",
                    color=AZUL_MARINO_NEON,
                    line_height="1",
                ),
                align="center",
                justify="center",
                height="1.75rem",
                width="1.75rem",
                border_radius=RADIO_PASTILLA,
                background=rx.color_mode_cond(
                    light="rgba(59, 91, 219, 0.08)",
                    dark="rgba(59, 91, 219, 0.15)",
                ),
                border=f"1px solid {BORDE_HOME_AZUL}",
                flex_shrink="0",
            ),
            # ─── Etiqueta ────────────────────────────────────────
            rx.text(
                bimestre["etiqueta"],
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.2",
            ),
            # ─── Período ─────────────────────────────────────────
            rx.text(
                bimestre["periodo"],
                font_size="0.75rem",
                font_weight="600",
                color=AZUL_MARINO_NEON,
                text_transform="uppercase",
                letter_spacing="0.05em",
            ),
            # ─── Rango de fechas ─────────────────────────────────
            rx.vstack(
                rx.flex(
                    rx.icon("play", size=12, color=TEXTO_HOME_MAS_SUAVE),
                    rx.text(
                        f"Inicio: {bimestre['fecha_inicio']}",
                        font_size="0.8125rem",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    align="center",
                    gap="0.375rem",
                ),
                rx.flex(
                    rx.icon("flag", size=12, color=TEXTO_HOME_MAS_SUAVE),
                    rx.text(
                        f"Fin: {bimestre['fecha_fin']}",
                        font_size="0.8125rem",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    align="center",
                    gap="0.375rem",
                ),
                spacing="2",
                align="start",
                margin_top="1rem",
                width="100%",
            ),
            align="start",
            spacing="1",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


# ======================================================================
# Cronograma completo
# ======================================================================


def cronograma_bimestres() -> rx.Component:
    """
    Grid con los 4 bimestres del año académico.

    Returns:
        Grid responsive con las tarjetas de bimestres.
    """
    return rx.grid(
        *[_tarjeta_bimestre(b) for b in BIMESTRES_2026],
        columns=rx.breakpoints(initial="1", sm="2", lg="4"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["cronograma_bimestres"]