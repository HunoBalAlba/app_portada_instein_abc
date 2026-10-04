"""
Sección del plan de estudios del detalle de carrera.

Contenido
---------
- `seccion_plan_estudios`: encabezado + selector segmentado de años +
  barra de progreso + grid de materias.

Sistema de color
----------------
✅ ACENTO ÚNICO: `AZUL_MARINO_NEON` para la barra de progreso y el
   borde superior de las tarjetas.
✅ ADAPTATIVO: fondos, textos y bordes respetan el `color_mode`.

Nota técnica: `EstadoPlanEstudios` ESTÁ EN `dominio/estados/`
-------------------------------------------------------------
El estado del selector segmentado vive en
`dominio.estados.estado_plan_estudios.EstadoPlanEstudios`.

Este módulo SOLO contiene la UI.

Nota técnica: BARRA DE PROGRESO CON VARS
----------------------------------------
La barra de progreso usa una Var calculada:
    porcentaje = (anio_actual * 100 / total_anios).to_string() + "%"

Esto funciona porque `anio_actual` y `total_anios` son Vars reactivos
y Reflex serializa la operación como JS del lado del cliente.

Nota técnica: `rx.foreach` + `lambda`
-------------------------------------
Se usa `rx.foreach(items, lambda x, i: ...)` para tener acceso al
índice. El `lambda` NO se ejecuta en Python: Reflex lo compila como
una operación de frontend.
"""

from __future__ import annotations

import reflex as rx

from ....componentes.carreras.tarjeta_carrera import (
    fila_materia,
)
from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
    OpcionAnio,
)
from ....dominio.estados.estado_plan_estudios import (
    EstadoPlanEstudios,
)
from ....infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    FONDO_AZUL_SUAVE,
)
from ....infraestructura.constantes.dimensiones import (
    ANCHO_SECCION,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    SOMBRA_SUAVE,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_TARJETA: str = "1.5rem"
"""Padding interno de las tarjetas."""

RADIO_TARJETA: str = "1.25rem"
"""Border-radius de las tarjetas."""


# ======================================================================
# Helpers internos
# ======================================================================


def _estilo_tarjeta_detalle() -> dict:
    """
    Estilo común para las tarjetas de detalle.

    Aplica:
    - Fondo neutro.
    - Borde neutro sutil.
    - Borde superior grueso con el acento azul marino.
    - Hover: borde + sombra tintados con el acento.
    """
    return {
        "padding": PADDING_TARJETA,
        "border_radius": RADIO_TARJETA,
        "background": COLOR_FONDO_CARTA,
        "border": f"1px solid {COLOR_BORDE_SUAVE}",
        "border_top": f"4px solid {AZUL_MARINO_NEON}",
        "box_shadow": SOMBRA_SUAVE,
        "width": "100%",
        "height": "100%",
        "transition": "all 0.25s cubic-bezier(0.4, 0, 0.2, 1)",
        "_hover": {
            "border_color": AZUL_MARINO_NEON,
            "box_shadow": f"0 12px 32px -8px {AZUL_MARINO_NEON}",
            "transform": "translateY(-2px)",
        },
    }


def _encabezado_seccion(
    icono: str,
    titulo: str,
    subtitulo: str | None = None,
) -> rx.Component:
    """
    Encabezado consistente para la sección del plan.
    """
    return rx.flex(
        rx.box(
            rx.icon(icono, size=20, color=COLOR_TEXTO_SECUNDARIO),
            padding="0.625rem",
            border_radius=RADIO_MEDIO,
            background=FONDO_AZUL_SUAVE,
            border=f"1px solid {BORDE_HOME_SUAVE}",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(
                titulo,
                font_size="0.9375rem",
                font_weight="800",
                color=COLOR_TEXTO_PRINCIPAL,
                text_transform="uppercase",
                letter_spacing="0.05em",
                line_height="1.2",
            ),
            rx.cond(
                subtitulo is not None,
                rx.text(
                    subtitulo or "",
                    font_size="0.75rem",
                    color=COLOR_TEXTO_SECUNDARIO,
                    line_height="1.4",
                ),
                rx.fragment(),
            ),
            spacing="1",
            align="start",
            flex="1",
            min_width="0",
        ),
        align="center",
        gap="0.75rem",
        width="100%",
        margin_bottom="1.25rem",
        flex_wrap="wrap",
    )


# ======================================================================
# Selector segmentado de años
# ======================================================================


def _opcion_anio_segmento(opcion: OpcionAnio) -> rx.Component:
    """
    Item del selector segmentado de años.

    Args:
        opcion: `OpcionAnio` con `etiqueta` y `valor`.
    """
    return rx.segmented_control.item(
        opcion["etiqueta"],
        value=opcion["valor"],
    )


# ======================================================================
# Barra de progreso del plan
# ======================================================================


def _barra_progreso_plan() -> rx.Component:
    """
    Barra de progreso del plan de estudios.

    Usa el acento para el relleno. Es el único elemento decorativo
    con color dentro del header del año.

    Returns:
        Fila con texto de progreso + barra.
    """
    total_anios = (
        EstadoInstitucional.carrera_seleccionada["plan_estudios"].length()
    )
    anio_actual = EstadoPlanEstudios.indice_anio_actual + 1

    # Cálculo del porcentaje como Var compatible con Reflex.
    porcentaje = (anio_actual * 100 / total_anios).to_string() + "%"

    return rx.flex(
        # --- Texto de progreso ---
        rx.text(
            "Año "
            + anio_actual.to_string()
            + " de "
            + total_anios.to_string(),
            font_size="0.75rem",
            font_weight="700",
            color=COLOR_TEXTO_SECUNDARIO,
            flex_shrink="0",
            white_space="nowrap",
        ),
        # --- Barra con acento ---
        rx.box(
            rx.box(
                width=porcentaje,
                height="100%",
                background=AZUL_MARINO_NEON,
                border_radius=RADIO_PASTILLA,
                transition="width 0.35s cubic-bezier(0.4, 0, 0.2, 1)",
            ),
            height="0.375rem",
            flex="1",
            background=COLOR_DIVISOR,
            border_radius=RADIO_PASTILLA,
            overflow="hidden",
        ),
        align="center",
        gap="0.75rem",
        width="100%",
        margin_bottom="1.5rem",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_plan_estudios() -> rx.Component:
    """
    Sección con el plan de estudios dividido por años.

    Estructura:
    1. Encabezado + selector segmentado de años.
    2. Contenido del año: barra de progreso + header + materias.

    Returns:
        Vstack con los 2 bloques.
    """
    plan_actual = EstadoInstitucional.carrera_seleccionada["plan_estudios"][
        EstadoPlanEstudios.indice_anio_actual
    ]

    return rx.vstack(
        # =============================================================
        # 1. Encabezado + Selector
        # =============================================================
        rx.box(
            _encabezado_seccion(
                "book-open-text",
                "Plan de estudios",
                "Selecciona el año para ver las materias correspondientes.",
            ),
            rx.segmented_control.root(
                rx.foreach(
                    EstadoInstitucional.opciones_anio_plan,
                    _opcion_anio_segmento,
                ),
                on_change=EstadoPlanEstudios.cambiar_anio,
                value=EstadoPlanEstudios.anio_seleccionado,
                width="100%",
                size="3",
                variant="surface",
                radius="large",
            ),
            width="100%",
        ),
        # =============================================================
        # 2. Contenido del año seleccionado
        # =============================================================
        rx.box(
            # --- Barra de progreso ---
            _barra_progreso_plan(),
            # --- Header del año ---
            rx.flex(
                rx.vstack(
                    rx.text(
                        plan_actual["anio"],
                        font_size="1.5rem",
                        font_weight="800",
                        color=COLOR_TEXTO_PRINCIPAL,
                        line_height="1.15",
                        letter_spacing="-0.02em",
                    ),
                    rx.flex(
                        rx.icon(
                            "book-open",
                            size=12,
                            color=COLOR_TEXTO_SECUNDARIO,
                        ),
                        rx.text(
                            plan_actual["materias"].length().to_string()
                            + " materias",
                            font_size="0.8125rem",
                            font_weight="500",
                            color=COLOR_TEXTO_SECUNDARIO,
                        ),
                        align="center",
                        gap="0.375rem",
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.box(
                    rx.icon(
                        "graduation-cap",
                        size=36,
                        color=COLOR_TEXTO_SECUNDARIO,
                    ),
                    padding="0.875rem",
                    border_radius=RADIO_GRANDE,
                    background=COLOR_FONDO_SUAVE,
                    border=f"1px solid {COLOR_BORDE_SUAVE}",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                align="center",
                justify="between",
                width="100%",
                margin_bottom="1.5rem",
                padding_bottom="1.5rem",
                border_bottom=f"1px solid {COLOR_DIVISOR}",
                flex_wrap="wrap",
                gap="1rem",
            ),
            # --- Lista de materias ---
            rx.vstack(
                rx.foreach(plan_actual["materias"], fila_materia),
                gap="0.5rem",
                width="100%",
            ),
            **_estilo_tarjeta_detalle(),
        ),
        spacing="4",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_plan_estudios"]