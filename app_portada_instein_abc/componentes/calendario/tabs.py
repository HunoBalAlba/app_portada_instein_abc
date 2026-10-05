"""
Ensamblador de los tabs del Calendario Académico — estilo Neon.com.

Diseño UX
---------
- **Tabs con icono + texto** (más intuitivo).
- **Sin fondo de card** (solo border_bottom sutil).
- **Indicador activo con azul marino**.
- **Contenido con separación clara**.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    BORDE_HOME_SUAVE,
    RADIO_EXTRA_GRANDE,
)

from .tabs_fechas import tab_fechas_importantes
from .tabs_instituto import tab_actividades_instituto


# ======================================================================
# Trigger individual
# ======================================================================


def _tab_trigger(
    texto: str,
    icono: str,
    value: str,
) -> rx.Component:
    """
    Trigger de pestaña con icono + texto.

    Estilo Neon.com:
    - Icono + texto en desktop.
    - Activo: color azul marino + border_bottom.
    - Hover: color azul marino.
    """
    return rx.tabs.trigger(
        # ─── Móvil: solo texto ─────────────────────────────────
        rx.mobile_only(
            rx.text(
                texto,
                font_size="0.875rem",
                font_weight="600",
            ),
        ),
        # ─── Tablet/desktop: icono + texto ─────────────────────
        rx.tablet_and_desktop(
            rx.flex(
                rx.icon(icono, size=16),
                rx.text(
                    texto,
                    font_size="0.875rem",
                    font_weight="600",
                ),
                align="center",
                gap="0.5rem",
            ),
        ),
        value=value,
        padding="0.75rem 1rem",
        color=rx.color("gray", 11),
        transition="all 0.2s",
        _hover={"color": rx.color("indigo", 9)},
        _selected={"color": rx.color("indigo", 9)},
    )


# ======================================================================
# Tabs completas
# ======================================================================


def tabs_calendario() -> rx.Component:
    """
    Tabs con dos pestañas:
    - "Actividades del instituto": timeline con eventos.
    - "Fechas importantes": feriados y días especiales de Bolivia.

    Estilo Neon.com:
    - Lista de triggers con border_bottom sutil.
    - Contenido con margin_top consistente.
    - Sin fondo de card.

    Returns:
        Componente `rx.tabs.root` con las 2 pestañas.
    """
    return rx.tabs.root(
        # ==========================================================
        # Lista de triggers
        # ==========================================================
        rx.tabs.list(
            _tab_trigger(
                "Actividades del instituto",
                "calendar-check",
                value="actividades",
            ),
            _tab_trigger(
                "Fechas importantes",
                "flag",
                value="fechas",
            ),
            width="100%",
            gap="0.25rem",
            border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        ),
        # ==========================================================
        # Contenido: Actividades del instituto
        # ==========================================================
        rx.tabs.content(
            tab_actividades_instituto(),
            margin_top="2rem",
            value="actividades",
        ),
        # ==========================================================
        # Contenido: Fechas importantes
        # ==========================================================
        rx.tabs.content(
            tab_fechas_importantes(),
            margin_top="2rem",
            value="fechas",
        ),
        default_value="actividades",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["tabs_calendario"]