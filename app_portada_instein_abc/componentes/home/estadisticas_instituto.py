

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    COLOR_DIVISOR,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "80rem"

# Padding del bloque completo
PADDING_BLOQUE: str = "6rem 2rem"

# Altura del gráfico
ALTO_GRAFICO: int = 320

# Espaciado entre stats
GAP_ENTRE_STATS: str = "3rem"


# ======================================================================
# Tipos
# ======================================================================


class Estadistica(TypedDict):
    """Estructura de una estadística individual."""

    valor: str
    sufijo: str
    etiqueta: str


class ItemGrafico(TypedDict):
    """Item individual del gráfico de barras."""

    carrera: str
    egresados: int


# ======================================================================
# Datos estáticos
# ======================================================================

ESTADISTICAS: list[Estadistica] = [
    {
        "valor": "5",
        "sufijo": "",
        "etiqueta": "Carreras Técnicas",
    },
    {
        "valor": "15",
        "sufijo": "+",
        "etiqueta": "Años de Experiencia",
    },
    {
        "valor": "500",
        "sufijo": "+",
        "etiqueta": "Egresados",
    },
    {
        "valor": "100",
        "sufijo": "%",
        "etiqueta": "Empleabilidad",
    },
]

DATA_EGRESADOS: list[ItemGrafico] = [
    {"carrera": "Sistemas", "egresados": 234},
    {"carrera": "Contaduría", "egresados": 198},
    {"carrera": "Electrónica", "egresados": 178},
    {"carrera": "Secretariado", "egresados": 156},
    {"carrera": "Comercio Int.", "egresados": 145},
]


# ======================================================================
# Stat individual (columna sin card)
# ======================================================================


def _stat_item(
    stat: Estadistica,
    es_ultimo: bool = False,
) -> rx.Component:
    """
    Columna de una estadística individual.

    Estilo Neon.com:
    - Número grande (`4rem`, `900`).
    - Sufijo (`+`, `%`) en azul marino.
    - Etiqueta uppercase, tamaño pequeño, color secundario.
    - Divisor vertical a la izquierda (excepto la primera).

    Args:
        stat: Diccionario con `valor`, `sufijo`, `etiqueta`.
        es_ultimo: Ignorado (reservado para futura lógica de
            divisores condicionales).

    Returns:
        Columna con la estadística.
    """
    return rx.box(
        rx.vstack(
            # ─── Número + sufijo ────────────────────────────────
            rx.flex(
                rx.text(
                    stat["valor"],
                    font_size=["3rem", "3.5rem", "4rem"],
                    font_weight="900",
                    color=TEXTO_HOME_PRINCIPAL,
                    line_height="1",
                    letter_spacing="-0.05em",
                ),
                rx.cond(
                    stat["sufijo"],
                    rx.text(
                        stat["sufijo"],
                        font_size=["1.75rem", "2rem", "2.5rem"],
                        font_weight="800",
                        color=AZUL_MARINO_NEON,
                        line_height="1",
                        margin_left="0.125rem",
                    ),
                ),
                align="start",
                gap="0",
                flex_wrap="nowrap",
            ),
            # ─── Etiqueta ───────────────────────────────────────
            rx.text(
                stat["etiqueta"],
                font_size="0.75rem",
                font_weight="600",
                letter_spacing="0.1em",
                text_transform="uppercase",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.4",
                margin_top="0.75rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        padding_left=["0", "0", "2rem"],
        padding_y="1rem",
        border_left=rx.breakpoints(
            initial="none",
            sm="none",
            lg=f"1px solid {COLOR_DIVISOR}",
        ),
        width="100%",
    )


# ======================================================================
# Grid de stats
# ======================================================================


def _grid_stats() -> rx.Component:
    """
    Grid de las 4 estadísticas con divisor vertical.

    Layout:
    - Móvil:    2 columnas.
    - Tablet:   2 columnas.
    - Desktop:  4 columnas.
    """
    return rx.grid(
        *[_stat_item(s) for s in ESTADISTICAS],
        columns=rx.breakpoints(initial="2", sm="2", lg="4"),
        spacing="4",
        width="100%",
    )


# ======================================================================
# Gráfico de barras horizontales
# ======================================================================


def _grafico_egresados() -> rx.Component:
    """
    Gráfico de barras horizontales con egresados por carrera.

    Estilo Neon.com:
    - Sin borde exterior.
    - Sin fondo de card.
    - Título limpio arriba.
    - Barras en azul marino sólido.
    - Ejes sin línea, solo labels.

    Usa Recharts con `layout="vertical"`.
    """
    return rx.vstack(
        # ─── Encabezado del gráfico ─────────────────────────────
        rx.vstack(
            rx.text(
                "Egresados por carrera",
                font_size=["1.125rem", "1.25rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.2",
            ),
            rx.text(
                "Distribución histórica de egresados en las 5 carreras "
                "técnicas del instituto.",
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.5",
                max_width="48rem",
            ),
            spacing="1",
            align="start",
        ),
        # ─── Gráfico Recharts ───────────────────────────────────
        rx.box(
            rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="egresados",
                    stroke=AZUL_MARINO_NEON,
                    fill=AZUL_MARINO_NEON,
                    radius=[0, 6, 6, 0],
                ),
                rx.recharts.x_axis(
                    type_="number",
                    stroke=TEXTO_HOME_MAS_SUAVE,
                    tick_line=False,
                    axis_line=False,
                ),
                rx.recharts.y_axis(
                    data_key="carrera",
                    type_="category",
                    width=120,
                    stroke=TEXTO_HOME_MAS_SUAVE,
                    tick_line=False,
                    axis_line=False,
                ),
                rx.recharts.cartesian_grid(
                    stroke_dasharray="3 3",
                    horizontal=False,
                    vertical=True,
                    stroke=rx.color_mode_cond(
                        light="rgba(15, 23, 42, 0.06)",
                        dark="rgba(255, 255, 255, 0.05)",
                    ),
                ),
                rx.recharts.tooltip(),
                data=DATA_EGRESADOS,
                layout="vertical",
                margin={"top": 10, "right": 20, "left": 10, "bottom": 10},
                width="100%",
                height=ALTO_GRAFICO,
            ),
            width="100%",
            padding_y="1rem",
        ),
        spacing="4",
        align="start",
        width="100%",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_estadisticas() -> rx.Component:
    """
    Bloque completo con las estadísticas del instituto.

    Estructura (estilo Neon.com):
    1. Grid de 4 stats con divisor vertical (sin cards).
    2. Separador horizontal sutil.
    3. Gráfico de barras desnudo.

    Layout responsive:
    - Desktop: 4 columnas de stats + gráfico full width.
    - Tablet:  2 columnas de stats + gráfico full width.
    - Móvil:   2 columnas de stats + gráfico full width.

    Returns:
        Componente `rx.box` con el bloque completo.
    """
    return rx.box(
        rx.vstack(
            # ─── Grid de stats ──────────────────────────────────
            _grid_stats(),
            # ─── Separador ──────────────────────────────────────
            rx.box(
                height="1px",
                width="100%",
                background=COLOR_DIVISOR,
                margin_y="3rem",
            ),
            # ─── Gráfico ────────────────────────────────────────
            _grafico_egresados(),
            spacing="0",
            width="100%",
        ),
        width="100%",
        max_width=ANCHO_MAXIMO_CONTENIDO,
        margin="0 auto",
        padding=PADDING_BLOQUE,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "DATA_EGRESADOS",
    "ESTADISTICAS",
    "Estadistica",
    "ItemGrafico",
    "seccion_estadisticas",
]