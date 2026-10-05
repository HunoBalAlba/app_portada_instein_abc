"""
Hero de la página de carreras — carrusel de banners destacados.

Estructura
----------
- Grid de perspectiva de fondo.
- Carrusel con auto-avance (via `rx.moment`).
- Flechas de navegación izquierda/derecha.
- Indicadores de posición (dots).
- Miniaturas clicables.
- Barra de progreso del auto-avance.

Sistema de color
----------------
✅ ACENTO ÚNICO: `AZUL_MARINO_NEON` para todas las carreras.
✅ ADAPTATIVO: fondo, textos y bordes respetan el `color_mode`.

Nota técnica: AUTO-AVANCE CON `rx.moment`
-----------------------------------------
El auto-avance del carrusel se implementa con `rx.moment(interval=5000)`,
que internamente usa `setInterval` de JS en el cliente.

Ventajas sobre `while True` en Python:
- Cero fugas de memoria (1 intervalo por página activa).
- Cero CPU del servidor (el timer vive en el navegador).
- Cancelación automática al desmontar el componente.
"""

from __future__ import annotations

import reflex as rx

from ...dominio import (
    CarreraConEtiqueta,
    EstadoInstitucional,
)
from ...infraestructura import (
    ANCHO_CONTENIDO,
    ANCHO_SECCION,
    AZUL_MARINO_NEON,
    COLOR_ACENTO_BORDE,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    SOMBRA_CAJA,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_GRID_PERSPECTIVA: str = "200%"
ANGULOS_GRID: list[float] = [i * 45 for i in range(8)]
TAMANO_ICONO_FLECHA: int = 22
PADDING_HERO: str = "3rem 3rem 2rem 3rem"
INTERVALO_AUTO_AVANCE_MS: int = 5000
INTERVALO_AUTO_AVANCE_SEG: float = INTERVALO_AUTO_AVANCE_MS / 1000
KEYFRAME_BARRA_PROGRESO: str = "progreso_carrusel"
ALTURA_BARRA_PROGRESO: str = "0.25rem"


# ======================================================================
# Grid de perspectiva de fondo
# ======================================================================


def _grid_perspectiva() -> rx.Component:
    """Grid de líneas radiales que simulan perspectiva."""
    return rx.box(
        *[
            rx.box(
                position="absolute",
                top="50%",
                left="50%",
                width=ANCHO_GRID_PERSPECTIVA,
                height="1px",
                background=rx.color("accent", 6),
                opacity=rx.color_mode_cond(light="0.06", dark="0.12"),
                transform_origin="0 50%",
                transform=f"translate(0, -50%) rotate({angulo}deg)",
            )
            for angulo in ANGULOS_GRID
        ],
        position="absolute",
        top="0",
        left="0",
        right="0",
        bottom="0",
        overflow="hidden",
        z_index="0",
        pointer_events="none",
    )


# ======================================================================
# Barra de progreso del auto-avance
# ======================================================================


def _barra_progreso_auto_avance() -> rx.Component:
    """Barra de progreso animada que se llena durante el intervalo."""
    return rx.box(
        rx.box(
            height="100%",
            background=AZUL_MARINO_NEON,
            border_radius=RADIO_PASTILLA,
            animation=(
                f"{KEYFRAME_BARRA_PROGRESO} "
                f"{INTERVALO_AUTO_AVANCE_SEG}s linear infinite"
            ),
            transform_origin="left center",
        ),
        position="absolute",
        bottom="0",
        left="0",
        right="0",
        height=ALTURA_BARRA_PROGRESO,
        background="rgba(0,0,0,0.3)",
        backdrop_filter="blur(4px)",
        overflow="hidden",
        z_index="3",
        pointer_events="none",
    )


# ======================================================================
# Banner individual
# ======================================================================


def _banner_carrera(item: CarreraConEtiqueta) -> rx.Component:
    """Banner horizontal grande con imagen + overlay + info."""
    carrera = item["carrera"]
    etiqueta = item["etiqueta"]

    return rx.link(
        rx.box(
            # Imagen de fondo
            rx.box(
                rx.image(
                    src="/" + carrera["imagen_banner"],
                    alt=carrera["nombre"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    position="absolute",
                    top="0",
                    left="0",
                    z_index="0",
                ),
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background=(
                    "linear-gradient(to top, rgba(0,0,0,0.85) 0%, "
                    "rgba(0,0,0,0.2) 60%, rgba(0,0,0,0.4) 100%)"
                ),
                z_index="1",
            ),
            _barra_progreso_auto_avance(),
            rx.vstack(
                rx.box(
                    rx.text(
                        etiqueta,
                        font_size="0.75rem",
                        font_weight="600",
                        color="white",
                    ),
                    padding="0.375rem 0.75rem",
                    background="rgba(0,0,0,0.6)",
                    backdrop_filter="blur(8px)",
                    border_radius=RADIO_MEDIO,
                    width="fit-content",
                ),
                rx.box(flex="1"),
                rx.heading(
                    carrera["nombre"],
                    font_size=["1.25rem", "1.5rem", "1.75rem"],
                    font_weight="800",
                    color="white",
                    line_height="1.2",
                    max_width="90%",
                ),
                rx.flex(
                    rx.box(
                        rx.image(
                            src="/" + carrera["imagen_archivo"],
                            alt=carrera["nombre"],
                            width="100%",
                            height="100%",
                            object_fit="cover",
                            border_radius=RADIO_PASTILLA,
                        ),
                        width="3rem",
                        height="3rem",
                        border_radius=RADIO_PASTILLA,
                        overflow="hidden",
                        border="2px solid rgba(255,255,255,0.4)",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text(
                            carrera["nombre_corto"],
                            font_size="0.875rem",
                            font_weight="600",
                            color="white",
                        ),
                        rx.text(
                            carrera["duracion"] + " · Técnico Superior",
                            font_size="0.75rem",
                            color="rgba(255,255,255,0.75)",
                        ),
                        align="start",
                        spacing="0",
                        flex="1",
                    ),
                    rx.box(
                        rx.text(
                            "Ver detalle",
                            font_size="0.75rem",
                            font_weight="600",
                            color="white",
                        ),
                        padding="0.5rem 0.875rem",
                        border_radius=RADIO_MEDIO,
                        background="rgba(0,0,0,0.6)",
                        backdrop_filter="blur(8px)",
                        border="1px solid rgba(255,255,255,0.25)",
                        flex_shrink="0",
                    ),
                    align="center",
                    gap="0.75rem",
                    width="100%",
                    margin_top="1rem",
                ),
                align="start",
                justify="between",
                spacing="2",
                width="100%",
                height="100%",
                padding="1.25rem",
                padding_bottom="1.5rem",
                position="relative",
                z_index="2",
            ),
            position="relative",
            height="20rem",
            border_radius=RADIO_GRANDE,
            overflow="hidden",
            transition="all 0.3s",
            _hover={
                "transform": "translateY(-4px)",
                "box_shadow": f"0 20px 40px -10px {AZUL_MARINO_NEON}",
            },
        ),
        href=f"/carrera/{carrera['id']}",
        text_decoration="none",
        width="100%",
    )


# ======================================================================
# Flechas de navegación
# ======================================================================


def _flecha_navegacion(direccion: str) -> rx.Component:
    """Flecha circular para navegar el carrusel."""
    if direccion == "izquierda":
        icono = "chevron-left"
        evento = EstadoInstitucional.anterior_carrusel
        posicion = {"left": "-1.5rem"}
    else:
        icono = "chevron-right"
        evento = EstadoInstitucional.siguiente_carrusel
        posicion = {"right": "-1.5rem"}

    return rx.box(
        rx.icon(
            icono,
            size=TAMANO_ICONO_FLECHA,
            color=COLOR_TEXTO_PRINCIPAL,
        ),
        position="absolute",
        top="50%",
        transform="translateY(-50%)",
        height="2.75rem",
        width="2.75rem",
        border_radius=RADIO_PASTILLA,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        box_shadow=SOMBRA_CAJA,
        display="flex",
        align_items="center",
        justify_content="center",
        cursor="pointer",
        z_index="10",
        transition="all 0.2s",
        on_click=evento,
        _hover={
            "transform": "translateY(-50%) scale(1.1)",
            "box_shadow": "0 8px 20px -4px rgba(0,0,0,0.2)",
            "border_color": COLOR_ACENTO_BORDE,
        },
        **posicion,
    )


# ======================================================================
# Dots indicadores
# ======================================================================


def _dot_indicador(item: CarreraConEtiqueta, idx: int) -> rx.Component:
    """Dot individual del carrusel."""
    esta_activo = EstadoInstitucional.indice_carrusel == idx

    return rx.box(
        height="0.5rem",
        width=rx.cond(esta_activo, "1.5rem", "0.5rem"),
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            esta_activo,
            AZUL_MARINO_NEON,
            COLOR_BORDE_SUAVE,
        ),
        cursor="pointer",
        transition="all 0.3s",
        on_click=lambda: EstadoInstitucional.ir_a_banner(idx),
    )


def _indicadores_dots() -> rx.Component:
    """Fila de dots que indican la posición actual."""
    return rx.flex(
        rx.foreach(
            EstadoInstitucional.carreras_destacadas_con_etiquetas,
            _dot_indicador,
        ),
        gap="0.375rem",
        justify="center",
        align="center",
        margin_top="1.5rem",
        width="100%",
    )


# ======================================================================
# Miniaturas de carreras
# ======================================================================


def _miniatura_carrera(
    item: CarreraConEtiqueta,
    idx: int,
) -> rx.Component:
    """Miniatura individual de carrera."""
    esta_activa = EstadoInstitucional.indice_carrusel == idx
    carrera = item["carrera"]

    return rx.box(
        rx.text(
            carrera["nombre_corto"],
            font_size="0.75rem",
            font_weight="600",
            color=rx.cond(
                esta_activa,
                AZUL_MARINO_NEON,
                COLOR_TEXTO_SECUNDARIO,
            ),
            white_space="nowrap",
        ),
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            esta_activa,
            COLOR_FONDO_SUAVE,
            COLOR_FONDO_CARTA,
        ),
        border=rx.cond(
            esta_activa,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {COLOR_BORDE_SUAVE}",
        ),
        cursor="pointer",
        transition="all 0.2s",
        on_click=lambda: EstadoInstitucional.ir_a_banner(idx),
        _hover={
            "transform": "translateY(-2px)",
            "border_color": AZUL_MARINO_NEON,
            "box_shadow": "0 8px 20px -8px rgba(0, 0, 0, 0.15)",
        },
    )


def _miniaturas_carreras() -> rx.Component:
    """Fila de miniaturas clicables debajo del carrusel."""
    return rx.flex(
        rx.foreach(
            EstadoInstitucional.carreras_destacadas_con_etiquetas,
            _miniatura_carrera,
        ),
        gap="0.5rem",
        justify="center",
        align="center",
        flex_wrap="wrap",
        margin_top="1.5rem",
        width="100%",
    )


# ======================================================================
# Auto-avance con rx.moment
# ======================================================================


def _auto_avance_moment() -> rx.Component:
    """
    Componente invisible que dispara `siguiente_carrusel` cada 5 s.

    Usa `rx.moment(interval=...)`, que inyecta un `setInterval` de JS
    en el cliente. Al desmontar el componente, el navegador cancela el
    intervalo automáticamente.
    """
    return rx.moment(
        interval=INTERVALO_AUTO_AVANCE_MS,
        on_change=EstadoInstitucional.siguiente_carrusel,
        display="none",
    )


# ======================================================================
# Carrusel completo
# ======================================================================


def _carrusel_carreras() -> rx.Component:
    """Carrusel de banners + barra de progreso + indicadores."""
    return rx.box(
        _auto_avance_moment(),
        rx.box(
            rx.box(
                _banner_carrera(EstadoInstitucional.item_carrusel_actual),
                key=EstadoInstitucional.indice_carrusel,
                width="100%",
            ),
            _flecha_navegacion("izquierda"),
            _flecha_navegacion("derecha"),
            position="relative",
            width="100%",
            max_width=ANCHO_SECCION,
            margin="0 auto",
        ),
        _indicadores_dots(),
        _miniaturas_carreras(),
        width="100%",
    )


# ======================================================================
# Hero completo
# ======================================================================


def hero_carreras() -> rx.Component:
    """
    Hero de la página de carreras con carrusel.

    El auto-avance vive en `_auto_avance_moment()`, que usa
    `rx.moment(interval=...)` para disparar `siguiente_carrusel` cada
    5 segundos sin mantener una tarea de Python corriendo.
    """
    return rx.box(
        _grid_perspectiva(),
        rx.box(
            _carrusel_carreras(),
            max_width=ANCHO_CONTENIDO,
            margin="0 auto",
            padding=PADDING_HERO,
            position="relative",
            z_index="1",
            width="100%",
        ),
        position="relative",
        width="100%",
        overflow="hidden",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["hero_carreras"]