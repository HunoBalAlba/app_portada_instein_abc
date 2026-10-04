"""
Barra de filtros del blog: búsqueda + pills de categoría + contador.
"""

from __future__ import annotations

import reflex as rx

from ...dominio.estados.estado_blog import EstadoBlog
from ...dominio.modelos.blog import Categoria
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    COLOR_ACENTO_FONDO,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_SECUNDARIO,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
)


# ======================================================================
# Pill de categoría
# ======================================================================


def _pill_categoria(cat: Categoria) -> rx.Component:
    """
    Pill individual de categoría.

    UX:
    - Activa: fondo del color de la categoría + texto blanco.
    - Inactiva: fondo neutro + texto secundario.

    Args:
        cat: `Categoria` con `valor`, `etiqueta`, `icono`, `color`.
    """
    activo: rx.Var = EstadoBlog.categoria_activa == cat["valor"]
    color_scheme = cat["color"]

    return rx.box(
        rx.flex(
            rx.icon(
                cat["icono"],
                size=14,
                color=rx.cond(activo, "white", COLOR_TEXTO_SECUNDARIO),
            ),
            rx.text(
                cat["etiqueta"],
                font_size="0.8125rem",
                font_weight="600",
                color=rx.cond(activo, "white", COLOR_TEXTO_CUERPO),
                white_space="nowrap",
            ),
            align="center",
            gap="0.375rem",
        ),
        padding="0.5rem 1rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            activo,
            rx.color(color_scheme, 9),
            COLOR_FONDO_SUAVE,
        ),
        border=rx.cond(
            activo,
            f"1px solid {rx.color(color_scheme, 9)}",
            f"1px solid {BORDE_HOME_SUAVE}",
        ),
        cursor="pointer",
        transition="all 0.2s cubic-bezier(0.4, 0, 0.2, 1)",
        on_click=EstadoBlog.seleccionar_categoria(cat["valor"]),
        box_shadow=rx.cond(
            activo,
            f"0 4px 12px -2px {rx.color(color_scheme, 9)}",
            "none",
        ),
        _hover={
            "transform": "translateY(-1px)",
            "background": rx.cond(
                activo,
                rx.color(color_scheme, 9),
                COLOR_FONDO_CARTA,
            ),
        },
    )


# ======================================================================
# Buscador
# ======================================================================


def _buscador_blog() -> rx.Component:
    """Input de búsqueda de posts."""
    return rx.box(
        rx.flex(
            rx.icon("search", size=16, color=COLOR_TEXTO_SECUNDARIO),
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
                    rx.icon("x", size=16, color=COLOR_TEXTO_SECUNDARIO),
                    padding="0.25rem",
                    border_radius=RADIO_MEDIO,
                    cursor="pointer",
                    on_click=EstadoBlog.actualizar_busqueda(""),
                    _hover={"background": COLOR_FONDO_SUAVE},
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
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {BORDE_HOME_SUAVE}",
        transition="all 0.2s",
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
    """
    # Import aquí para evitar ciclo con EstadoBlog
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
                    color=COLOR_TEXTO_SECUNDARIO,
                ),
                rx.text(
                    EstadoBlog.contador_resultados,
                    font_size="0.8125rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    padding="0.125rem 0.5rem",
                    background=COLOR_ACENTO_FONDO,
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
                            color=COLOR_TEXTO_SECUNDARIO,
                        ),
                        rx.text(
                            "Limpiar filtros",
                            font_size="0.75rem",
                            font_weight="600",
                            color=COLOR_TEXTO_CUERPO,
                        ),
                        align="center",
                        gap="0.375rem",
                    ),
                    padding="0.375rem 0.75rem",
                    border_radius=RADIO_MEDIO,
                    background=COLOR_FONDO_SUAVE,
                    border=f"1px solid {BORDE_HOME_SUAVE}",
                    cursor="pointer",
                    transition="all 0.2s",
                    on_click=EstadoBlog.limpiar_filtros,
                    _hover={
                        "background": COLOR_FONDO_CARTA,
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