

from __future__ import annotations

import reflex as rx

from ....componentes.base import (
    tarjeta_dato,
)
from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ....infraestructura import (
    AZUL_MARINO_NEON,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    RADIO_EXTRA_GRANDE,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_TARJETA: str = "1.75rem"
"""Padding interno de las tarjetas."""


# ======================================================================
# Encabezado de sección (limpio, estilo Neon)
# ======================================================================


def _encabezado_seccion(
    icono: str,
    titulo: str,
    subtitulo: str | None = None,
) -> rx.Component:
    """
    Encabezado limpio para la sección de descripción.

    Estilo Neon.com:
    - Icono directo (sin caja).
    - Título en mayúsculas + subtítulo en gris.
    - Alineado a la izquierda.

    Args:
        icono: Nombre del icono Lucide (kebab-case).
        titulo: Título de la sección (mayúsculas).
        subtitulo: Texto opcional debajo del título.

    Returns:
        Fila con icono + título + subtítulo.
    """
    return rx.flex(
        # ─── Icono directo (sin caja) ──────────────────────────
        rx.icon(
            icono,
            size=18,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
        ),
        # ─── Título + subtítulo ────────────────────────────────
        rx.vstack(
            rx.text(
                titulo,
                font_size="0.6875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.15em",
                text_transform="uppercase",
                line_height="1.2",
            ),
            rx.cond(
                subtitulo is not None,
                rx.text(
                    subtitulo or "",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                    line_height="1.5",
                    margin_top="0.25rem",
                ),
                rx.fragment(),
            ),
            spacing="0",
            align="start",
            flex="1",
            min_width="0",
        ),
        align="center",
        gap="0.75rem",
        width="100%",
        margin_bottom="1.5rem",
        flex_wrap="wrap",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_informacion() -> rx.Component:
    """
    Sección de información general de la carrera.

    Estructura:
    1. Tarjeta de descripción con encabezado limpio.
    2. Grid de 4 datos rápidos (duración, título, modalidad, cupos).

    Estilo Neon.com:
    - Tarjeta con fondo plano y borde superior de acento (2px).
    - Hover: solo cambio de borde.
    - Grid de datos con `tarjeta_dato` compartido.
    - Sin glow ni translateY.

    Returns:
        Vstack con los 2 bloques.
    """
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.vstack(
        # =============================================================
        # 1. Descripción
        # =============================================================
        rx.box(
            _encabezado_seccion(
                "info",
                "Descripción de la carrera",
                "Información general y objetivos del programa.",
            ),
            rx.text(
                carrera["descripcion"],
                font_size="0.9375rem",
                line_height="1.75",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            padding=PADDING_TARJETA,
            border_radius=RADIO_EXTRA_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            border_top=f"2px solid {AZUL_MARINO_NEON}",
            width="100%",
            height="100%",
            transition="all 0.2s",
            _hover={"border_color": AZUL_MARINO_NEON},
        ),
        # =============================================================
        # 2. Grid de datos rápidos
        # =============================================================
        rx.grid(
            tarjeta_dato(
                icono="clock",
                etiqueta="Duración",
                valor=carrera["duracion"],
            ),
            tarjeta_dato(
                icono="award",
                etiqueta="Título",
                valor="Técnico Superior",
            ),
            tarjeta_dato(
                icono="building-2",
                etiqueta="Modalidad",
                valor=carrera["modalidad"],
            ),
            tarjeta_dato(
                icono="users",
                etiqueta="Cupos",
                valor=f"{carrera['cupos_disponibles']} disponibles",
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="4"),
            spacing="3",
            width="100%",
            align_items="stretch",
        ),
        spacing="4",
        width="100%",
        align="start",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_informacion"]