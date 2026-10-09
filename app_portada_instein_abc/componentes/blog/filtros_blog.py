

from __future__ import annotations

import reflex as rx

from ...dominio.estados.estado_blog import EstadoBlog
from ...dominio.modelos.blog import Categoria
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_BORDE_SUAVE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Pill de categoría
# ======================================================================


def _pill_categoria(cat: Categoria) -> rx.Component:
    """
    Pill individual de categoría.

    Estilo Neon.com:
    - Activa: fondo azul marino + texto blanco.
    - Inactiva: fondo plano + borde sutil.
    - Hover: solo cambio de borde (sin glow, sin translateY).

    Args:
        cat: `Categoria` con `valor`, `etiqueta`, `icono`, `color`.
    """
    activo: rx.Var = EstadoBlog.categoria_activa == cat["valor"]

    return rx.box(
        rx.flex(
            rx.icon(
                cat["icono"],
                size=14,
                color=rx.cond(
                    activo,
                    "white",
                    AZUL_MARINO_NEON,
                ),
            ),
            rx.text(
                cat["etiqueta"],
                font_size="0.8125rem",
                font_weight="600",
                color=rx.cond(
                    activo,
                    "white",
                    TEXTO_HOME_PRINCIPAL,
                ),
                white_space="nowrap",
            ),
            align="center",
            gap="0.375rem",
        ),
        padding="0.5rem 1rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            activo,
            AZUL_MARINO_NEON,
            "transparent",
        ),
        border=rx.cond(
            activo,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {BORDE_HOME_MEDIO}",
        ),
        cursor="pointer",
        transition="all 0.2s",
        on_click=EstadoBlog.seleccionar_categoria(cat["valor"]),
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


# ======================================================================
# Buscador
# ======================================================================


def _buscador_blog() -> rx.Component:
    """Input de búsqueda de posts."""
    return rx.box(
        rx.flex(
            rx.icon("search", size=16, color=TEXTO_HOME_MAS_SUAVE),
            rx.input(
                placeholder="Buscar artículo por título, autor...",
                value=EstadoBlog.texto_busqueda,
                on_change=EstadoBlog.actualizar_busqueda,
                variant="soft",
                size="2",
                width="100%",
                border="none",
                background="transparent",
                _focus={"box_shadow": "none", "outline": "none"},
            ),
            rx.cond(
                EstadoBlog.texto_busqueda != "",
                rx.box(
                    rx.icon("x", size=16, color=TEXTO_HOME_MAS_SUAVE),
                    padding="0.25rem",
                    border_radius=RADIO_MEDIO,
                    cursor="pointer",
                    on_click=EstadoBlog.actualizar_busqueda(""),
                    _hover={"background": "transparent"},
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
        background="transparent",
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        transition="all 0.2s",
        _focus_within={"border_color": AZUL_MARINO_NEON},
    )


# ======================================================================
# Barra de filtros completa
# ======================================================================


def barra_filtros() -> rx.Component:
    """
    Barra con el buscador y las categorías como pills.

    Estructura:
    - Input de búsqueda.
    - Fila de pills de categorías.
    - Contador de resultados + botón limpiar filtros.

    Estilo Neon.com:
    - Pills con solo fondo + borde.
    - Sin glow.
    """
    from ...dominio.modelos.blog import CATEGORIAS

    return rx.vstack(
        # ==========================================================
        # Buscador
        # ==========================================================
        _buscador_blog(),
        # ==========================================================
        # Pills de categorías
        # ==========================================================
        rx.flex(
            *[_pill_categoria(cat) for cat in CATEGORIAS],
            gap="0.5rem",
            flex_wrap="wrap",
            width="100%",
        ),
        # ==========================================================
        # Contador + limpiar
        # ==========================================================
        rx.flex(
            rx.flex(
                rx.text(
                    "Artículos:",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                rx.text(
                    EstadoBlog.contador_resultados,
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
                EstadoBlog.hay_filtros_activos,
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
                    on_click=EstadoBlog.limpiar_filtros,
                    _hover={
                        "border_color": AZUL_MARINO_NEON,
                    },
                ),
                rx.fragment(),
            ),
            align="center",
            justify="between",
            width="100%",
            flex_wrap="wrap",
            gap="0.5rem",
        ),
        spacing="4",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["barra_filtros"]