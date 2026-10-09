

from __future__ import annotations

from typing import Any, Callable

import reflex as rx

from ...dominio.estados.estado_calendario import (
    EstadoCalendario,
)
from ...dominio.modelos.calendario import (
    OPCIONES_CARRERA,
    OPCIONES_ORDEN,
    OPCIONES_TIPO_EVENTO,
)
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes del módulo
# ======================================================================

BIMESTRES_FILTRO: list[dict] = [
    {"valor": "0", "etiqueta": "Todos", "icono": "layers"},
    {"valor": "1", "etiqueta": "I Bimestre", "icono": "circle-1"},
    {"valor": "2", "etiqueta": "II Bimestre", "icono": "circle-2"},
    {"valor": "3", "etiqueta": "III Bimestre", "icono": "circle-3"},
    {"valor": "4", "etiqueta": "IV Bimestre", "icono": "circle-4"},
]
"""Opciones del filtro por bimestre (como strings)."""


# ======================================================================
# Item de opción (dentro del popover)
# ======================================================================


def _item_opcion(
    etiqueta: str,
    icono: str,
    valor: Any,
    activo: Any,
    handler: Callable,
) -> rx.Component:
    """
    Item de opción dentro del popover.

    Estilo Neon.com:
    - Icono + etiqueta + check (si activo).
    - Hover: fondo tintado.
    - Activo: fondo azul marino suave + check visible.

    Args:
        etiqueta: Texto visible de la opción.
        icono: Nombre del icono Lucide.
        valor: Valor que se pasa al handler al hacer clic.
        activo: Var/Bool que indica si está activa.
        handler: Event handler que recibe `valor`.

    Returns:
        Fila clicable con icono + etiqueta + check.
    """
    return rx.box(
        rx.flex(
            rx.icon(
                icono,
                size=14,
                color=rx.cond(activo, AZUL_MARINO_NEON, TEXTO_HOME_MAS_SUAVE),
                flex_shrink="0",
            ),
            rx.text(
                etiqueta,
                font_size="0.8125rem",
                font_weight=rx.cond(activo, "700", "500"),
                color=rx.cond(activo, AZUL_MARINO_NEON, TEXTO_HOME_PRINCIPAL),
                flex="1",
                min_width="0",
                white_space="nowrap",
                overflow="hidden",
                text_overflow="ellipsis",
            ),
            rx.cond(
                activo,
                rx.icon(
                    "check",
                    size=14,
                    color=AZUL_MARINO_NEON,
                    flex_shrink="0",
                ),
                rx.fragment(),
            ),
            align="center",
            gap="0.625rem",
            width="100%",
        ),
        padding="0.5rem 0.75rem",
        border_radius=RADIO_MEDIO,
        cursor="pointer",
        transition="all 0.15s",
        on_click=handler(valor),
        background=rx.cond(
            activo,
            rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.08)",
                dark="rgba(59, 91, 219, 0.15)",
            ),
            "transparent",
        ),
        _hover={
            "background": rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.05)",
                dark="rgba(59, 91, 219, 0.1)",
            ),
        },
    )

def _buscador_eventos() -> rx.Component:
    """
    Buscador inline (sin popover).

    El input se muestra directamente en la barra de filtros.
    Es lo más simple y funcional.
    """
    hay_texto = EstadoCalendario.texto_busqueda != ""

    return rx.box(
        rx.flex(
            rx.icon(
                "search",
                size=16,
                color=AZUL_MARINO_NEON,
                flex_shrink="0",
            ),
            rx.input(
                placeholder="Buscar evento por nombre o lugar...",
                value=EstadoCalendario.texto_busqueda,
                on_change=EstadoCalendario.actualizar_busqueda,
                variant="soft",
                size="2",
                width="100%",
                border="none",
                background="transparent",
                _focus={"box_shadow": "none", "outline": "none"},
            ),
            rx.cond(
                hay_texto,
                rx.box(
                    rx.icon("x", size=16, color=TEXTO_HOME_MAS_SUAVE),
                    padding="0.25rem",
                    border_radius=RADIO_MEDIO,
                    cursor="pointer",
                    on_click=EstadoCalendario.actualizar_busqueda(""),
                    transition="all 0.2s",
                    _hover={"background": COLOR_FONDO_CARTA},
                ),
                rx.fragment(),
            ),
            align="center",
            gap="0.5rem",
            width="100%",
        ),
        width="100%",
        padding="0.5rem 0.875rem",
        border_radius=RADIO_GRANDE,
        border=rx.cond(
            hay_texto,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {COLOR_BORDE_SUAVE}",
        ),
        background="transparent",
        transition="all 0.2s",
        _focus_within={"border_color": AZUL_MARINO_NEON},
    )


def _item_resultado_busqueda(evento: dict) -> rx.Component:
    """
    Item individual de resultado dentro del buscador.

    Al hacer clic:
    1. Aplica el título del evento como texto de búsqueda.
    2. Cierra el popover (rx.popover.close).

    Estilo Neon.com:
    - Fila compacta con icono + título.
    - Hover: fondo tintado.
    - Clic: cierra el popover.

    Args:
        evento: `ProximoEvento` con `titulo`, `mes`, `dia`, `tipo`.

    Returns:
        Fila clicable con el evento.
    """
    return rx.popover.close(
        rx.box(
            rx.flex(
                # ─── Icono del tipo ─────────────────────────────
                rx.icon(
                    "calendar",
                    size=14,
                    color=AZUL_MARINO_NEON,
                    flex_shrink="0",
                ),
                # ─── Información del evento ─────────────────────
                rx.vstack(
                    rx.text(
                        evento["titulo"],
                        font_size="0.8125rem",
                        font_weight="600",
                        color=TEXTO_HOME_PRINCIPAL,
                        line_height="1.3",
                        white_space="nowrap",
                        overflow="hidden",
                        text_overflow="ellipsis",
                        width="100%",
                    ),
                    rx.text(
                        evento["mes"] + " " + evento["dia"],
                        font_size="0.6875rem",
                        color=TEXTO_HOME_MAS_SUAVE,
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                    ),
                    spacing="0",
                    align="start",
                    flex="1",
                    min_width="0",
                ),
                # ─── Chevron indicador ──────────────────────────
                rx.icon(
                    "arrow-right",
                    size=14,
                    color=TEXTO_HOME_MAS_SUAVE,
                    flex_shrink="0",
                ),
                align="center",
                gap="0.625rem",
                width="100%",
            ),
            padding="0.5rem 0.75rem",
            border_radius=RADIO_MEDIO,
            cursor="pointer",
            transition="all 0.15s",
            on_click=EstadoCalendario.actualizar_busqueda(evento["titulo"]),
            _hover={
                "background": rx.color_mode_cond(
                    light="rgba(59, 91, 219, 0.06)",
                    dark="rgba(59, 91, 219, 0.12)",
                ),
            },
        ),
    )

# ======================================================================
# Selector de ordenamiento (popover)
# ======================================================================


def _selector_orden() -> rx.Component:
    """
    Selector de ordenamiento como popover con lista de opciones.

    Estilo Neon.com:
    - Trigger muestra la opción activa.
    - Popover con lista de opciones (con check en activo).
    - Cada opción cierra el popover al hacer clic.

    Returns:
        Popover con trigger + contenido.
    """
    # Etiqueta de la opción activa
    etiqueta_activa = _resolver_etiqueta_activa(
        EstadoCalendario.orden_activo, OPCIONES_ORDEN
    )

    return rx.popover.root(
        # ─── Trigger ───────────────────────────────────────────
        rx.popover.trigger(
            rx.box(
                rx.flex(
                    rx.icon(
                        "arrow-up-down",
                        size=14,
                        color=AZUL_MARINO_NEON,
                        flex_shrink="0",
                    ),
                    rx.text(
                        "Ordenar: ",
                        font_size="0.8125rem",
                        font_weight="500",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    rx.text(
                        etiqueta_activa,
                        font_size="0.8125rem",
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        flex="1",
                        min_width="0",
                        white_space="nowrap",
                        overflow="hidden",
                        text_overflow="ellipsis",
                    ),
                    rx.icon(
                        "chevron-down",
                        size=14,
                        color=TEXTO_HOME_MAS_SUAVE,
                        flex_shrink="0",
                    ),
                    align="center",
                    gap="0.375rem",
                    width="100%",
                ),
                padding="0.5rem 0.875rem",
                border_radius=RADIO_GRANDE,
                border=f"1px solid {COLOR_BORDE_SUAVE}",
                background="transparent",
                cursor="pointer",
                transition="all 0.2s",
                width="100%",
                _hover={"border_color": AZUL_MARINO_NEON},
            ),
        ),
        # ─── Contenido del popover ─────────────────────────────
        rx.popover.content(
            rx.vstack(
                # ─── Encabezado ────────────────────────────────
                rx.flex(
                    rx.text(
                        "Ordenar por",
                        font_size="0.6875rem",
                        font_weight="700",
                        color=TEXTO_HOME_MAS_SUAVE,
                        text_transform="uppercase",
                        letter_spacing="0.1em",
                    ),
                    rx.text(
                        f"({len(OPCIONES_ORDEN)})",
                        font_size="0.6875rem",
                        font_weight="500",
                        color=TEXTO_HOME_MAS_SUAVE,
                        opacity="0.7",
                    ),
                    align="center",
                    gap="0.375rem",
                    width="100%",
                    padding_bottom="0.5rem",
                    border_bottom=f"1px solid {COLOR_DIVISOR}",
                ),
                # ─── Lista de opciones ─────────────────────────
                rx.vstack(
                    *[
                        rx.popover.close(
                            _item_opcion(
                                opcion["etiqueta"],
                                "arrow-up-down",
                                opcion["valor"],
                                EstadoCalendario.orden_activo
                                == opcion["valor"],
                                EstadoCalendario.cambiar_orden,
                            )
                        )
                        for opcion in OPCIONES_ORDEN
                    ],
                    spacing="0",
                    width="100%",
                    max_height="20rem",
                    overflow_y="auto",
                ),
                spacing="2",
                width="100%",
            ),
            width="320px",
            padding="0.75rem",
            border_radius=RADIO_GRANDE,
        ),
    )


# ======================================================================
# Filtro con popover
# ======================================================================


def _filtro_popover(
    etiqueta_grupo: str,
    valor_actual: Any,
    opciones: list[dict],
    handler: Callable,
    icono_trigger: str = "filter",
) -> rx.Component:
    """
    Filtro como popover con lista de opciones.

    Args:
        etiqueta_grupo: Texto en el trigger (ej: "Carrera").
        valor_actual: Var con el valor actual del filtro.
        opciones: Lista de dicts con `valor`, `etiqueta`, `icono`.
        handler: Event handler que recibe `valor`.
        icono_trigger: Icono del trigger.

    Returns:
        Popover con trigger + contenido. Cada opción cierra el popover.
    """
    etiqueta_activa = _resolver_etiqueta_activa(
        valor_actual, opciones
    )

    return rx.popover.root(
        # ─── Trigger ───────────────────────────────────────────
        rx.popover.trigger(
            rx.box(
                rx.flex(
                    rx.icon(
                        icono_trigger,
                        size=14,
                        color=AZUL_MARINO_NEON,
                        flex_shrink="0",
                    ),
                    rx.text(
                        f"{etiqueta_grupo}: ",
                        font_size="0.8125rem",
                        font_weight="500",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    rx.text(
                        etiqueta_activa,
                        font_size="0.8125rem",
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        flex="1",
                        min_width="0",
                        white_space="nowrap",
                        overflow="hidden",
                        text_overflow="ellipsis",
                    ),
                    rx.icon(
                        "chevron-down",
                        size=14,
                        color=TEXTO_HOME_MAS_SUAVE,
                        flex_shrink="0",
                    ),
                    align="center",
                    gap="0.375rem",
                    width="100%",
                ),
                padding="0.5rem 0.875rem",
                border_radius=RADIO_GRANDE,
                border=f"1px solid {COLOR_BORDE_SUAVE}",
                background="transparent",
                cursor="pointer",
                transition="all 0.2s",
                width="100%",
                _hover={"border_color": AZUL_MARINO_NEON},
            ),
        ),
        # ─── Contenido del popover ─────────────────────────────
        rx.popover.content(
            rx.vstack(
                # ─── Encabezado ────────────────────────────────
                rx.flex(
                    rx.text(
                        etiqueta_grupo,
                        font_size="0.6875rem",
                        font_weight="700",
                        color=TEXTO_HOME_MAS_SUAVE,
                        text_transform="uppercase",
                        letter_spacing="0.1em",
                    ),
                    rx.text(
                        f"({len(opciones)})",
                        font_size="0.6875rem",
                        font_weight="500",
                        color=TEXTO_HOME_MAS_SUAVE,
                        opacity="0.7",
                    ),
                    align="center",
                    gap="0.375rem",
                    width="100%",
                    padding_bottom="0.5rem",
                    border_bottom=f"1px solid {COLOR_DIVISOR}",
                ),
                # ─── Lista de opciones ─────────────────────────
                rx.vstack(
                    *[
                        rx.popover.close(
                            _item_opcion(
                                opcion["etiqueta"],
                                opcion["icono"],
                                opcion["valor"],
                                valor_actual == opcion["valor"],
                                handler,
                            )
                        )
                        for opcion in opciones
                    ],
                    spacing="0",
                    width="100%",
                    max_height="20rem",
                    overflow_y="auto",
                ),
                spacing="2",
                width="100%",
            ),
            width="280px",
            padding="0.75rem",
            border_radius=RADIO_GRANDE,
        ),
    )


def _resolver_etiqueta_activa(
    valor_actual: Any,
    opciones: list[dict],
) -> str:
    """
    Resuelve la etiqueta del valor activo.

    Como `valor_actual` puede ser una Var reactiva, usamos
    `rx.match` para resolver la etiqueta en el cliente.

    Args:
        valor_actual: Var con el valor actual.
        opciones: Lista de opciones con `valor` y `etiqueta`.

    Returns:
        Texto con la etiqueta activa.
    """
    if not opciones:
        return "Ninguno"

    return rx.match(
        valor_actual,
        *[
            (opcion["valor"], opcion["etiqueta"])
            for opcion in opciones
        ],
        opciones[0]["etiqueta"],
    )


# ======================================================================
# Barra de filtros completa
# ======================================================================


def barra_filtros() -> rx.Component:
    """
    Barra de filtros completa con popovers.

    Estructura:
    1. Búsqueda + ordenamiento (grid de 2).
    2. Filtros como popovers en grid de 3:
       - Carrera.
       - Tipo de evento.
       - Bimestre.
    3. Contador + limpiar filtros.
    """
    return rx.vstack(
        
        # ==========================================================
        # 2. Filtros como popovers
        # ==========================================================
        rx.grid(
            _filtro_popover(
                "Carrera",
                EstadoCalendario.filtro_carrera,
                OPCIONES_CARRERA,
                EstadoCalendario.cambiar_filtro_carrera,
                icono_trigger="graduation-cap",
            ),
            _filtro_popover(
                "Tipo",
                EstadoCalendario.filtro_tipo,
                OPCIONES_TIPO_EVENTO,
                EstadoCalendario.cambiar_filtro_tipo,
                icono_trigger="tag",
            ),
            _filtro_popover(
                "Bimestre",
                EstadoCalendario.filtro_bimestre,
                BIMESTRES_FILTRO,
                EstadoCalendario.cambiar_filtro_bimestre,
                icono_trigger="layers",
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="3",
            width="100%",
        ),
        # ==========================================================
                # 1. Búsqueda + ordenamiento
                # ==========================================================
                rx.grid(
                    
                    _selector_orden(),
                    _buscador_eventos(),
                    columns=rx.breakpoints(initial="1", sm="2"),
                    spacing="3",
                    width="100%",
                ),
        # ==========================================================
        # 3. Resultado + limpiar filtros
        # ==========================================================
        rx.flex(
            rx.flex(
                rx.text(
                    "Resultados:",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                rx.text(
                    EstadoCalendario.contador_resultados,
                    font_size="0.8125rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    padding="0.125rem 0.5rem",
                    background=rx.color_mode_cond(
                        light="rgba(59, 91, 219, 0.08)",
                        dark="rgba(59, 91, 219, 0.15)",
                    ),
                    border=f"1px solid {BORDE_HOME_AZUL}",
                    border_radius=RADIO_PASTILLA,
                ),
                align="center",
                gap="0.375rem",
            ),
            rx.cond(
                EstadoCalendario.hay_filtros_activos,
                rx.box(
                    rx.flex(
                        rx.icon(
                            "rotate-ccw",
                            size=14,
                            color=TEXTO_HOME_MAS_SUAVE,
                        ),
                        rx.text(
                            "Limpiar filtros",
                            font_size="0.75rem",
                            font_weight="600",
                            color=TEXTO_HOME_PRINCIPAL,
                        ),
                        align="center",
                        gap="0.375rem",
                    ),
                    padding="0.375rem 0.75rem",
                    border_radius=RADIO_MEDIO,
                    background="transparent",
                    border=f"1px solid {COLOR_BORDE_SUAVE}",
                    cursor="pointer",
                    transition="all 0.2s",
                    on_click=EstadoCalendario.limpiar_filtros,
                    _hover={"border_color": BORDE_HOME_AZUL},
                ),
                rx.fragment(),
            ),
            align="center",
            justify="between",
            width="100%",
            flex_wrap="wrap",
            gap="0.5rem",
            margin_top="0.5rem",
        ),
        spacing="4",
        width="100%",
        margin_bottom="2rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "BIMESTRES_FILTRO",
    "barra_filtros",
]