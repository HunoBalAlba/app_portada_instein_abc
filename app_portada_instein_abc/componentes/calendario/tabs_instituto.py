"""
Tab 1: Actividades del instituto (timeline con filtros) — estilo Neon.com.

Diseño UX
---------
1. **Timeline vertical** con línea conectora.
2. **Card por evento** con fecha destacada.
3. **Badge por tipo** con color semántico.
4. **Hover sutil** (solo borde).
5. **Sin glow excesivo** (coherente con el sitio).
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base import (
    badge_icono_texto,
    estado_vacio,
)
from ...dominio.estados.estado_calendario import (
    EstadoCalendario,
)
from ...dominio.modelos.calendario import (
    ProximoEvento,
)
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)

from .filtros import barra_filtros
from .helpers import color_por_tipo_evento


# ======================================================================
# Badge de tipo de evento
# ======================================================================


def _badge_tipo_evento(tipo: str) -> rx.Component:
    """
    Badge con el tipo de evento.

    Delega en `badge_icono_texto` del paquete base.
    """
    info = color_por_tipo_evento(tipo)

    return badge_icono_texto(
        info["etiqueta"],
        icono=info["icono"],
        color_scheme=info["color"],
        tamano="sm",
    )


# ======================================================================
# Card de evento
# ======================================================================


def _card_evento(evento: ProximoEvento) -> rx.Component:
    """
    Card individual de evento del instituto.

    Estructura:
    ┌──────────────────────────────────────────┐
    │  [ABR]         Título del evento         │
    │   05           Descripción...            │
    │  2026          [Taller] · Campus         │
    └──────────────────────────────────────────┘

    Args:
        evento: `ProximoEvento` con `mes`, `dia`, `anio`, `titulo`,
            `descripcion`, `tipo`, `lugar`.
    """
    info = color_por_tipo_evento(evento["tipo"])

    return rx.flex(
        # ==========================================================
        # Columna izquierda: fecha (día + mes + año)
        # ==========================================================
        rx.box(
            rx.vstack(
                rx.text(
                    evento["mes"],
                    font_size="0.625rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    text_transform="uppercase",
                    letter_spacing="0.1em",
                ),
                rx.text(
                    evento["dia"],
                    font_size="1.75rem",
                    font_weight="800",
                    color=TEXTO_HOME_PRINCIPAL,
                    line_height="1",
                    letter_spacing="-0.03em",
                    font_family="JetBrains Mono",
                ),
                rx.text(
                    evento["anio"],
                    font_size="0.625rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                align="center",
                spacing="0",
            ),
            height="6rem",
            width="6rem",
            border_radius=RADIO_EXTRA_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            border_top=f"2px solid {AZUL_MARINO_NEON}",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        # ==========================================================
        # Columna derecha: contenido
        # ==========================================================
        rx.vstack(
            # ─── Badge de tipo + lugar ─────────────────────────
            rx.flex(
                _badge_tipo_evento(evento["tipo"]),
                rx.text(
                    evento["lugar"],
                    font_size="0.6875rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                align="center",
                gap="0.5rem",
                flex_wrap="wrap",
            ),
            # ─── Título ────────────────────────────────────────
            rx.heading(
                evento["titulo"],
                as_="h3",
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
            ),
            # ─── Descripción ───────────────────────────────────
            rx.text(
                evento["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
            ),
            align="start",
            spacing="2",
            flex="1",
            min_width="0",
        ),
        align="start",
        gap="1.5rem",
        width="100%",
    )


# ======================================================================
# Item del timeline
# ======================================================================


def _item_timeline(evento: ProximoEvento, indice, total) -> rx.Component:
    """
    Item del timeline de actividades del instituto.

    ⚠️ `indice` y `total` son Vars reactivos porque vienen de un
    `rx.foreach`. Por eso usamos `rx.cond` en lugar de `if/not`.
    """
    es_ultimo = indice == (total - 1)

    return rx.flex(
        # ==========================================================
        # Indicador (círculo + línea conectora)
        # ==========================================================
        rx.vstack(
            rx.box(
                height="1rem",
                width="1rem",
                border_radius=RADIO_PASTILLA,
                background=AZUL_MARINO_NEON,
                border=f"3px solid {COLOR_FONDO_CARTA}",
                box_shadow=f"0 0 0 2px {BORDE_HOME_AZUL}",
                flex_shrink="0",
            ),
            rx.cond(
                es_ultimo,
                rx.fragment(),
                rx.box(
                    width="2px",
                    background=COLOR_DIVISOR,
                    flex="1",
                    min_height="2rem",
                ),
            ),
            align="center",
            spacing="0",
            height="100%",
            padding_top="1.5rem",
            flex_shrink="0",
        ),
        # ==========================================================
        # Card del evento
        # ==========================================================
        rx.box(
            _card_evento(evento),
            padding="1.25rem",
            border_radius=RADIO_EXTRA_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            width="100%",
            margin_bottom=rx.cond(es_ultimo, "0", "1rem"),
            transition="all 0.2s",
            _hover={
                "border_color": AZUL_MARINO_NEON,
            },
        ),
        align="start",
        gap="1rem",
        width="100%",
    )


# ======================================================================
# Estado vacío
# ======================================================================


def _estado_vacio_filtros() -> rx.Component:
    """Estado vacío cuando los filtros no devuelven resultados."""
    return estado_vacio(
        titulo="No hay eventos con esos filtros",
        mensaje="Prueba ajustando los filtros o limpiando la búsqueda.",
        icono="search-x",
        tamano_icono=48,
        boton_accion_etiqueta="Limpiar filtros",
        boton_accion_icono="rotate-ccw",
        boton_accion_on_click=EstadoCalendario.limpiar_filtros,
        boton_accion_color_scheme="crimson",
    )


# ======================================================================
# Tab completo
# ======================================================================


def tab_actividades_instituto() -> rx.Component:
    """
    Contenido del tab 'Actividades del instituto' con filtros.

    Estructura:
    1. Barra de filtros.
    2. Timeline o estado vacío (según haya resultados).
    """
    return rx.vstack(
        # ==========================================================
        # Barra de filtros
        # ==========================================================
        barra_filtros(),
        # ==========================================================
        # Timeline o estado vacío
        # ==========================================================
        rx.cond(
            EstadoCalendario.hay_resultados,
            rx.vstack(
                rx.foreach(
                    EstadoCalendario.eventos_filtrados,
                    lambda evento, idx: _item_timeline(
                        evento,
                        idx,
                        EstadoCalendario.eventos_filtrados.length(),
                    ),
                ),
                spacing="0",
                width="100%",
            ),
            _estado_vacio_filtros(),
        ),
        spacing="0",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["tab_actividades_instituto"]