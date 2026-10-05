"""
Tab 2: Fechas importantes de Bolivia y el mundo — estilo Neon.com.

Diseño UX
---------
1. **Leyenda arriba** (colores por tipo).
2. **Agrupación por mes**.
3. **Cards compactas** con día destacado.
4. **Hover sutil** (solo borde).
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base import (
    badge_icono_texto,
)
from ...dominio.modelos.calendario import (
    FECHAS_IMPORTANTES,
    TIPOS_FECHA,
    FechaImportante,
)
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    RADIO_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)

from .helpers import color_por_tipo_fecha


# ======================================================================
# Leyenda
# ======================================================================


def _leyenda_fechas() -> rx.Component:
    """Leyenda con los tipos de fecha importante."""
    return rx.flex(
        *[
            rx.flex(
                rx.box(
                    height="0.75rem",
                    width="0.75rem",
                    border_radius=RADIO_PASTILLA,
                    background=rx.color(info["color"], 9),
                    flex_shrink="0",
                ),
                rx.text(
                    info["etiqueta"],
                    font_size="0.75rem",
                    font_weight="600",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                align="center",
                gap="0.375rem",
            )
            for info in TIPOS_FECHA.values()
        ],
        gap="1rem",
        flex_wrap="wrap",
        margin_bottom="2rem",
    )


# ======================================================================
# Badge de tipo de fecha
# ======================================================================


def _badge_tipo_fecha(tipo: str) -> rx.Component:
    """Badge con el tipo de fecha importante."""
    info = color_por_tipo_fecha(tipo)

    return badge_icono_texto(
        info["etiqueta"],
        icono=info["icono"],
        color_scheme=info["color"],
        tamano="sm",
    )


# ======================================================================
# Card de fecha importante
# ======================================================================


def _card_fecha_importante(fecha: FechaImportante) -> rx.Component:
    """
    Card individual de fecha importante.

    Estructura:
    ┌──────────────────────────────────────┐
    │  [DÍA]     [Feriado nacional]        │
    │    01      Año Nuevo                 │
    └──────────────────────────────────────┘

    Args:
        fecha: `FechaImportante` con `mes`, `dia`, `titulo`, `tipo`.
    """
    info = color_por_tipo_fecha(fecha["tipo"])

    return rx.flex(
        # ==========================================================
        # Columna izquierda: día
        # ==========================================================
        rx.box(
            rx.vstack(
                rx.text(
                    "DÍA",
                    font_size="0.5625rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    text_transform="uppercase",
                    letter_spacing="0.1em",
                ),
                rx.text(
                    fecha["dia"],
                    font_size="1.5rem",
                    font_weight="800",
                    color=TEXTO_HOME_PRINCIPAL,
                    line_height="1",
                    letter_spacing="-0.03em",
                    font_family="JetBrains Mono",
                ),
                align="center",
                spacing="0",
            ),
            height="4.5rem",
            width="4.5rem",
            border_radius=RADIO_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            border_top=f"2px solid {AZUL_MARINO_NEON}",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        # ==========================================================
        # Columna derecha: título + tipo
        # ==========================================================
        rx.vstack(
            _badge_tipo_fecha(fecha["tipo"]),
            rx.text(
                fecha["titulo"],
                font_size="0.9375rem",
                font_weight="600",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.4",
            ),
            align="start",
            spacing="1",
            flex="1",
            min_width="0",
        ),
        align="center",
        gap="1rem",
        width="100%",
        padding="1rem",
        border_radius=RADIO_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        transition="all 0.2s",
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


# ======================================================================
# Grupo por mes
# ======================================================================


def _grupo_mes(mes: str, fechas: list[FechaImportante]) -> rx.Component:
    """
    Grupo de fechas de un mismo mes.

    Args:
        mes: Nombre del mes (ej: "ENERO").
        fechas: Lista de fechas del mes.
    """
    return rx.box(
        # ==========================================================
        # Encabezado del mes
        # ==========================================================
        rx.flex(
            rx.text(
                mes,
                font_size="0.875rem",
                font_weight="800",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.1em",
                text_transform="uppercase",
            ),
            rx.box(
                flex="1",
                height="1px",
                background=COLOR_DIVISOR,
            ),
            rx.text(
                str(len(fechas)),
                font_size="0.75rem",
                font_weight="700",
                color=TEXTO_HOME_MAS_SUAVE,
                padding="0.125rem 0.5rem",
                border_radius=RADIO_PASTILLA,
                background=rx.color_mode_cond(
                    light="rgba(59, 91, 219, 0.08)",
                    dark="rgba(59, 91, 219, 0.15)",
                ),
                border=f"1px solid {BORDE_HOME_AZUL}",
            ),
            align="center",
            gap="0.75rem",
            width="100%",
            margin_bottom="1rem",
        ),
        # ==========================================================
        # Grid de fechas del mes
        # ==========================================================
        rx.grid(
            *[_card_fecha_importante(f) for f in fechas],
            columns=rx.breakpoints(initial="1", sm="2"),
            spacing="3",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )


# ======================================================================
# Tab completo
# ======================================================================


def tab_fechas_importantes() -> rx.Component:
    """
    Contenido del tab 'Fechas importantes'.

    Agrupa las fechas por mes (orden cronológico), mostrando cada mes
    como un bloque con su grid de fechas.
    """
    # Agrupamos por mes manteniendo el orden de aparición
    meses_ordenados: list[str] = []
    fechas_por_mes: dict[str, list[FechaImportante]] = {}

    for fecha in FECHAS_IMPORTANTES:
        mes = fecha["mes"]
        if mes not in fechas_por_mes:
            meses_ordenados.append(mes)
            fechas_por_mes[mes] = []
        fechas_por_mes[mes].append(fecha)

    return rx.vstack(
        _leyenda_fechas(),
        *[
            _grupo_mes(mes, fechas_por_mes[mes])
            for mes in meses_ordenados
        ],
        spacing="0",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["tab_fechas_importantes"]