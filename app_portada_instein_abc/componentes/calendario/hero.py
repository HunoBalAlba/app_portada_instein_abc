"""
Hero + grid de info rápida del Calendario Académico — estilo Neon.com.

Contenido
---------
- `hero_calendario`:      hero con badge + título + subtítulo.
- `grid_info_rapida`:     grid con 4 tarjetas de resumen.

Diseño UX
---------
1. **Layout izquierdo** (coherente con el resto del sitio).
2. **Badge con punto verde pulsante** (comunicado "activo").
3. **Título con énfasis bicolor** (patrón Neon).
4. **Peso tipográfico** 700 (no 900).
5. **Cards con icono directo** (sin caja) + borde superior de acento.
6. **Hover sutil**: solo cambio de borde.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    FONDO_AZUL_SUAVE,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Tipos
# ======================================================================


class InfoRapida(TypedDict):
    """Tarjeta de info rápida del hero."""

    icono: str
    titulo: str
    valor: str
    descripcion: str
    color: str


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "80rem"
PADDING_LATERAL: str = "1.5rem"

# Color verde para el punto pulsante del badge.
COLOR_VERDE_ACTIVO: str = "#22c55e"


# ======================================================================
# Datos estáticos
# ======================================================================

INFO_RAPIDA: list[InfoRapida] = [
    {
        "icono": "calendar-check",
        "titulo": "Inscripciones",
        "valor": "Abiertas todo el año",
        "descripcion": "No hay fecha límite. Inscríbete cuando quieras.",
        "color": "green",
    },
    {
        "icono": "play-circle",
        "titulo": "Inicio de clases",
        "valor": "Primer lunes de cada mes",
        "descripcion": "Ingreso escalonado según tu fecha de inscripción.",
        "color": "blue",
    },
    {
        "icono": "clock",
        "titulo": "Duración",
        "valor": "3 años · 6 semestres",
        "descripcion": "Título de Técnico Superior en Provisión Nacional.",
        "color": "violet",
    },
    {
        "icono": "building-2",
        "titulo": "Modalidad",
        "valor": "Presencial · 3 turnos",
        "descripcion": "Mañana, tarde y noche. Elige el que mejor te convenga.",
        "color": "orange",
    },
]


# ======================================================================
# Hero
# ======================================================================


def hero_calendario() -> rx.Component:
    """
    Hero del calendario con título + subtítulo + badge.

    Estilo Neon.com:
    - Layout alineado a la izquierda.
    - Badge con punto verde pulsante.
    - Título con énfasis bicolor.
    - Subtítulo descriptivo.
    - Peso tipográfico 700.

    Returns:
        Hero completo.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ─────────────────────────────────────────
            rx.flex(
                rx.box(
                    height="0.5rem",
                    width="0.5rem",
                    border_radius=RADIO_PASTILLA,
                    background=COLOR_VERDE_ACTIVO,
                    animation="pulse 2s ease-in-out infinite",
                    flex_shrink="0",
                ),
                rx.text(
                    "INSCRIPCIONES ABIERTAS TODO EL AÑO",
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
                rx.text.span("Calendario "),
                rx.text.span(
                    "Académico",
                    color=AZUL_MARINO_NEON,
                ),
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
                "Todas las actividades del instituto y las fechas "
                "importantes de Bolivia en un solo lugar. En INSTEIN "
                "puedes inscribirte en cualquier momento del año.",
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
# Cards de info rápida
# ======================================================================


def _card_info_rapida(item: InfoRapida) -> rx.Component:
    """
    Card con info rápida (inscripciones, inicio, duración, modalidad).

    Estilo Neon.com:
    - Icono directo (sin caja).
    - Borde superior de acento.
    - Hover: solo cambio de borde.

    Args:
        item: `InfoRapida` con `icono`, `titulo`, `valor`,
            `descripcion`, `color`.
    """
    return rx.box(
        rx.vstack(
            # ─── Icono (directo, sin caja) ──────────────────────
            rx.icon(
                item["icono"],
                size=22,
                color=AZUL_MARINO_NEON,
                flex_shrink="0",
            ),
            # ─── Etiqueta del dato ──────────────────────────────
            rx.text(
                item["titulo"],
                font_size="0.6875rem",
                font_weight="700",
                color=TEXTO_HOME_MAS_SUAVE,
                text_transform="uppercase",
                letter_spacing="0.15em",
                margin_top="0.75rem",
            ),
            # ─── Valor principal ────────────────────────────────
            rx.text(
                item["valor"],
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
                margin_top="0.375rem",
            ),
            # ─── Descripción ────────────────────────────────────
            rx.text(
                item["descripcion"],
                font_size="0.8125rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.5",
                margin_top="0.5rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        background=COLOR_FONDO_CARTA,
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def grid_info_rapida() -> rx.Component:
    """
    Grid con las 4 cards de info rápida.

    Estilo Neon.com:
    - Grid responsive (1 → 2 → 4 columnas).
    - Alineado con el padding del hero.
    """
    return rx.box(
        rx.grid(
            *[_card_info_rapida(item) for item in INFO_RAPIDA],
            columns=rx.breakpoints(initial="1", sm="2", lg="4"),
            spacing="4",
            width="100%",
            align_items="stretch",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=f"0 {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "INFO_RAPIDA",
    "InfoRapida",
    "grid_info_rapida",
    "hero_calendario",
]