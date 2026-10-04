"""
Sección de información general de la carrera.

Contenido
---------
- `seccion_informacion`: descripción larga + grid de 4 datos rápidos
  (duración, título, modalidad, cupos) + CTA opcional de contacto.

Sistema de color
----------------
✅ ACENTO ÚNICO: `AZUL_MARINO_NEON` para bordes y decoración.
✅ ADAPTATIVO: todos los textos y fondos respetan el `color_mode`.

Nota técnica: CTA COMENTADO
---------------------------
El CTA de contacto (`_cta_contacto`) está implementado pero COMENTADO
en el ensamblaje final. Se deja el código listo por si se reactiva.

Para activarlo: descomentar la última línea de `seccion_informacion()`.
"""

from __future__ import annotations

import reflex as rx

from ....componentes.base.primitivos import (
    enlace_navegacion,
    tarjeta_dato,
)
from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ....infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    FONDO_AZUL_SUAVE,
)
from ....infraestructura.constantes.dimensiones import (
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
    Encabezado consistente para la sección de descripción.

    Args:
        icono: Nombre del icono Lucide.
        titulo: Título de la sección.
        subtitulo: Texto opcional debajo del título.
    """
    hijos: list[rx.Component] = [
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
    ]

    return rx.flex(
        *hijos,
        align="center",
        gap="0.75rem",
        width="100%",
        margin_bottom="1.25rem",
        flex_wrap="wrap",
    )


# ======================================================================
# CTA de contacto
# ======================================================================


def _cta_contacto() -> rx.Component:
    """
    Bloque CTA de contacto con icono, texto y flecha.

    El fondo usa el acento (decorativo). El texto blanco garantiza
    contraste WCAG en ambos modos.

    Returns:
        Enlace estilizado como tarjeta CTA.
    """
    return enlace_navegacion(
        "/contacto",
        rx.flex(
            # --- Icono grande ---
            rx.box(
                rx.icon("phone-call", size=26, color="white"),
                padding="1rem",
                border_radius=RADIO_GRANDE,
                background="rgba(255,255,255,0.15)",
                border="1px solid rgba(255,255,255,0.2)",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            # --- Texto ---
            rx.vstack(
                rx.flex(
                    rx.text(
                        "¿Interesado en esta carrera?",
                        font_size="1rem",
                        font_weight="800",
                        color="white",
                        line_height="1.3",
                    ),
                    rx.box(
                        rx.flex(
                            rx.box(
                                width="0.375rem",
                                height="0.375rem",
                                border_radius=RADIO_PASTILLA,
                                background=rx.color("green", 8),
                                animation="pulse 2s ease-in-out infinite",
                            ),
                            rx.text(
                                "Inscripciones abiertas",
                                font_size="0.625rem",
                                font_weight="800",
                                color="white",
                                letter_spacing="0.075em",
                            ),
                            align="center",
                            gap="0.375rem",
                        ),
                        padding="0.25rem 0.625rem",
                        border_radius=RADIO_PASTILLA,
                        background="rgba(255,255,255,0.2)",
                    ),
                    align="center",
                    gap="0.5rem",
                    flex_wrap="wrap",
                ),
                rx.text(
                    "Contáctanos para recibir más información y conocer el "
                    "proceso de inscripción.",
                    font_size="0.8125rem",
                    color="rgba(255,255,255,0.9)",
                    line_height="1.5",
                ),
                spacing="2",
                align="start",
                flex="1",
            ),
            # --- Flecha ---
            rx.box(
                rx.icon("arrow-right", size=20, color="white"),
                padding="0.5rem",
                border_radius=RADIO_PASTILLA,
                background="rgba(255,255,255,0.15)",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
                transition="transform 0.2s",
            ),
            align="center",
            gap="1rem",
            width="100%",
        ),
        background=AZUL_MARINO_NEON,
        padding="1.25rem 1.5rem",
        border_radius=RADIO_TARJETA,
        box_shadow=f"0 10px 25px -5px {AZUL_MARINO_NEON}",
        transition="all 0.25s cubic-bezier(0.4, 0, 0.2, 1)",
        text_decoration="none",
        width="100%",
        _hover={
            "transform": "translateY(-3px)",
            "box_shadow": f"0 20px 45px -8px {AZUL_MARINO_NEON}",
        },
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_informacion() -> rx.Component:
    """
    Sección de información general de la carrera.

    Estructura:
    1. Tarjeta de descripción con encabezado.
    2. Grid de 4 datos rápidos (duración, título, modalidad, cupos).
    3. CTA de contacto (comentado por defecto).

    Returns:
        Vstack con los 3 bloques.
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
                color=COLOR_TEXTO_CUERPO,
            ),
            **_estilo_tarjeta_detalle(),
        ),
        # =============================================================
        # 2. Grid de datos rápidos
        # =============================================================
        rx.grid(
            tarjeta_dato(
                icono="clock",
                etiqueta="Duración",
                valor=carrera["duracion"],
                color_icono=COLOR_TEXTO_SECUNDARIO,
            ),
            tarjeta_dato(
                icono="award",
                etiqueta="Título",
                valor="Técnico Superior",
                color_icono=COLOR_TEXTO_SECUNDARIO,
            ),
            tarjeta_dato(
                icono="building-2",
                etiqueta="Modalidad",
                valor=carrera["modalidad"],
                color_icono=COLOR_TEXTO_SECUNDARIO,
            ),
            tarjeta_dato(
                icono="users",
                etiqueta="Cupos",
                valor=(
                    f"{carrera['cupos_disponibles']} disponibles"
                ),
                color_icono=COLOR_TEXTO_SECUNDARIO,
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="4"),
            spacing="3",
            width="100%",
        ),
        # =============================================================
        # 3. CTA de contacto (comentado por defecto)
        # =============================================================
        # _cta_contacto(),
        spacing="4",
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_informacion"]