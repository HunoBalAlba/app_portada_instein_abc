"""
Sección del plan de estudios del detalle de carrera — estilo Neon.com.

Contenido
---------
- `seccion_plan_estudios`: encabezado + selector segmentado de años +
  barra de progreso + grid de materias.

Diseño UX
---------
1. **Encabezado limpio**: icono directo + título + subtítulo.
2. **Selector segmentado** para cambiar de año.
3. **Barra de progreso** con acento azul marino.
4. **Header del año** con icono directo (sin caja).
5. **Hover sutil**: solo cambio de borde.
6. **Sin glow ni translateY**.
7. **Coherencia visual** con el resto del sitio (Neon).

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

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa los componentes compartidos:

- `fila_materia` (de `..tarjeta_carrera`).

Antes se importaba desde `....componentes.carreras.tarjeta_carrera`
(ruta larga). Ahora se importa con ruta relativa corta.
"""

from __future__ import annotations

import reflex as rx

# ======================================================================
# Imports de componentes
# ======================================================================

from ..tarjeta_carrera import (
    fila_materia,
)

# ======================================================================
# Imports de dominio (fachada)
# ======================================================================

from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
    OpcionAnio,
)
from ....dominio.estados.estado_plan_estudios import (
    EstadoPlanEstudios,
)

# ======================================================================
# Imports de infraestructura (fachada)
# ======================================================================

from ....infraestructura import (
    AZUL_MARINO_NEON,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
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
    Encabezado limpio para la sección del plan.

    Estilo Neon.com:
    - Icono directo (sin caja).
    - Título en mayúsculas con acento.
    - Subtítulo en gris.

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

    Usa el acento azul marino para el relleno. Es el único elemento
    decorativo con color dentro del header del año.

    Estilo Neon.com:
    - Barra fina (0.375rem).
    - Relleno azul marino con transición suave.
    - Texto "Año X de Y" arriba.

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
        # ─── Texto de progreso ─────────────────────────────────
        rx.text(
            "Año "
            + anio_actual.to_string()
            + " de "
            + total_anios.to_string(),
            font_size="0.75rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            flex_shrink="0",
            white_space="nowrap",
        ),
        # ─── Barra con acento ──────────────────────────────────
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

    Estilo Neon.com:
    - Encabezado limpio.
    - Tarjeta con borde superior de acento (2px).
    - Hover: solo cambio de borde.
    - Sin glow ni translateY.

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
                size="2",
                variant="surface",
                radius="large",
            ),
            width="100%",
        ),
        # =============================================================
        # 2. Contenido del año seleccionado
        # =============================================================
        rx.box(
            # ─── Barra de progreso ─────────────────────────────
            _barra_progreso_plan(),
            # ─── Header del año ────────────────────────────────
            rx.flex(
                rx.vstack(
                    # ─── Título del año ────────────────────────
                    rx.text(
                        plan_actual["anio"],
                        font_size="1.5rem",
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        line_height="1.15",
                        letter_spacing="-0.02em",
                    ),
                    # ─── Contador de materias ──────────────────
                    rx.flex(
                        rx.icon(
                            "book-open",
                            size=12,
                            color=AZUL_MARINO_NEON,
                        ),
                        rx.text(
                            plan_actual["materias"].length().to_string()
                            + " materias",
                            font_size="0.8125rem",
                            font_weight="600",
                            color=TEXTO_HOME_MAS_SUAVE,
                        ),
                        align="center",
                        gap="0.375rem",
                    ),
                    spacing="1",
                    align="start",
                ),
                # ─── Icono del año (directo, sin caja) ─────────
                rx.icon(
                    "graduation-cap",
                    size=32,
                    color=AZUL_MARINO_NEON,
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
            # ─── Lista de materias ─────────────────────────────
            rx.vstack(
                rx.foreach(plan_actual["materias"], fila_materia),
                gap="0.5rem",
                width="100%",
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
        spacing="4",
        width="100%",
        align="start",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_plan_estudios"]