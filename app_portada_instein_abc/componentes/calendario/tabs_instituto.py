

from __future__ import annotations

import reflex as rx

from ...componentes.base import estado_vacio
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


# ======================================================================
# Badge con colores hex directos
# ======================================================================


def _badge_hex(
    etiqueta: str,
    icono: str,
    color: str,
    fondo: str,
    borde: str,
) -> rx.Component:
    """
    Badge con colores hex directos.

    Esta función recibe strings LITERALES (no Vars). Se usa dentro
    de `rx.match`, donde cada rama tiene colores conocidos en
    tiempo de compilación.

    Args:
        etiqueta: Texto visible (ej: "Seminario").
        icono: Nombre del icono Lucide (kebab-case).
        color: Color del texto e icono (hex).
        fondo: Fondo del badge (hex).
        borde: Color del borde (hex).

    Returns:
        Badge con los colores especificados.
    """
    return rx.flex(
        rx.icon(
            icono,
            size=12,
            color=color,
            flex_shrink="0",
        ),
        rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=color,
            text_transform="uppercase",
            letter_spacing="0.05em",
            white_space="nowrap",
        ),
        align="center",
        gap="0.375rem",
        padding="0.25rem 0.625rem",
        border_radius=RADIO_PASTILLA,
        background=fondo,
        border=f"1px solid {borde}",
        width="fit-content",
    )


# ======================================================================
# Badge por tipo de evento (via rx.match)
# ======================================================================


def _badge_tipo_evento(tipo: str | rx.Var) -> rx.Component:
    """
    Badge con el tipo de evento resuelto dinámicamente.

    Usa `rx.match` para resolver el tipo **en el cliente** porque
    `tipo` es una `Var` reactiva cuando viene de `rx.foreach`.

    Args:
        tipo: Clave del tipo de evento (Var reactiva o str).

    Returns:
        Badge correspondiente al tipo.
    """
    return rx.match(
        tipo,
        # ─── Categorías académicas ─────────────────────────────
        ("taller", _badge_hex(
            "Taller", "wrench",
            "#3b82f6", "#eff6ff", "#bfdbfe",
        )),
        ("taller_tecnico", _badge_hex(
            "Taller técnico", "code",
            "#6366f1", "#eef2ff", "#c7d2fe",
        )),
        ("seminario", _badge_hex(
            "Seminario", "mic",
            "#8b5cf6", "#f5f3ff", "#ddd6fe",
        )),
        ("charla", _badge_hex(
            "Charla", "graduation-cap",
            "#06b6d4", "#ecfeff", "#a5f3fc",
        )),
        # ─── Categorías de evaluación ──────────────────────────
        ("evaluacion", _badge_hex(
            "Evaluación", "clipboard-check",
            "#f59e0b", "#fffbeb", "#fde68a",
        )),
        ("parcial", _badge_hex(
            "Parcial", "file-pen",
            "#f97316", "#fff7ed", "#fed7aa",
        )),
        ("examen_final", _badge_hex(
            "Examen final", "file-check",
            "#dc2626", "#fef2f2", "#fecaca",
        )),
        ("cierre_actas", _badge_hex(
            "Cierre de actas", "file-lock",
            "#7c3aed", "#f5f3ff", "#ddd6fe",
        )),
        ("graduacion", _badge_hex(
            "Graduación", "award",
            "#eab308", "#fefce8", "#fef08a",
        )),
        # ─── Categorías institucionales ────────────────────────
        ("inicio_bimestre", _badge_hex(
            "Inicio de bimestre", "play-circle",
            "#16a34a", "#f0fdf4", "#bbf7d0",
        )),
        ("institucional", _badge_hex(
            "Institucional", "landmark",
            "#dc2626", "#fef2f2", "#fecaca",
        )),
        ("feria", _badge_hex(
            "Feria", "store",
            "#f97316", "#fff7ed", "#fed7aa",
        )),
        ("feriado", _badge_hex(
            "Feriado", "party-popper",
            "#ef4444", "#fef2f2", "#fecaca",
        )),
        # ─── Categorías recreativas ────────────────────────────
        ("deportivo", _badge_hex(
            "Deportivo", "trophy",
            "#22c55e", "#f0fdf4", "#bbf7d0",
        )),
        ("cultural", _badge_hex(
            "Cultural", "music",
            "#ec4899", "#fdf2f8", "#fbcfe8",
        )),
        # ─── Fallback visible ──────────────────────────────────
        _badge_hex(
            "Desconocido", "alert-circle",
            "#6b7280", "#f3f4f6", "#d1d5db",
        ),
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
        evento: `ProximoEvento`.
    """
    return rx.flex(
        # ==========================================================
        # Columna izquierda: fecha
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
    """Item del timeline de actividades del instituto."""
    es_ultimo = indice == (total - 1)

    return rx.flex(
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
        boton_accion_color_scheme="indigo",
    )


# ======================================================================
# Tab completo
# ======================================================================


def tab_actividades_instituto() -> rx.Component:
    """Contenido del tab 'Actividades del instituto' con filtros."""
    return rx.vstack(
        barra_filtros(),
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