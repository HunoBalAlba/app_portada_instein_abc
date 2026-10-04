"""
Vista de detalle de una carrera específica
(ruta dinámica "/carrera/[carrera_id]").

Estructura:
- Encabezado sticky con breadcrumb, botón de regreso y progreso.
- Hero con contenedor orbital (imagen + iconos orbitando).
- Hero con información textual: nombre, lema, badges, CTA.
- Pestañas (Tabs) con las 3 secciones principales del detalle.
- Sección de preguntas frecuentes (fuera de las tabs).
- Botón flotante "volver arriba".
- Pie de página institucional.

Sistema de color
----------------
✅ ACENTO ÚNICO: azul marino neon.

Nota técnica: ACORDEÓN FAQ UNIFICADO
------------------------------------
La sección de preguntas frecuentes delega en `acordeon_faq` con
variante `"light"`.

⚠️ IMPORTANTE: los items del acordeón vienen como `Var` reactiva
(`carrera_seleccionada["preguntas_frecuentes"]`), NO como lista
estática de Python.

Nota técnica: VALIDACIÓN DE RUTA
--------------------------------
El decorador `@rx.page` incluye
`on_load=EstadoInstitucional.redirigir_si_carrera_invalida`.
"""

from __future__ import annotations

import reflex as rx

from ..componentes.base.acordeon_faq import acordeon_faq
from ..componentes.base.primitivos import (
    enlace_navegacion,
)
from ..componentes.carreras import (
    seccion_informacion,
    seccion_perfil_y_campo_laboral,
    seccion_plan_estudios,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..dominio import (
    EstadoInstitucional,
    IconoAnimado,
)
from ..infraestructura import (
    ANCHO_CONTENIDO,
    ANCHO_SECCION,
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    COLOR_ACENTO_BORDE,
    COLOR_ACENTO_FONDO,
    COLOR_ACENTO_SOLIDO,
    COLOR_ACENTO_TEXTO,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    PADDING_LATERAL,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_INFERIOR_PESTANAS = f"0 {PADDING_LATERAL} 6rem {PADDING_LATERAL}"
TAMANO_IMAGEN_ORBITAL = ["10rem", "13rem", "15rem"]
ANCHO_ESPACIADOR_HEADER = "6rem"


# ======================================================================
# Helpers de color (delegan en el acento único)
# ======================================================================


def _color_carrera_actual() -> str:
    """Color principal del acento global."""
    return AZUL_MARINO_NEON


def _color_suave_carrera_actual() -> rx.Var:
    """Color suave de fondo del acento global."""
    return FONDO_AZUL_SUAVE


# ======================================================================
# Triggers de pestañas
# ======================================================================


def _tabs_trigger(texto: str, icono: str, value: str) -> rx.Component:
    """Trigger de pestaña responsive con el acento cuando activo."""
    return rx.tabs.trigger(
        rx.mobile_only(
            rx.hstack(
                rx.heading(texto, size="4"),
                spacing="2",
                align="center",
                width="100%",
            ),
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                rx.icon(icono, size=24),
                rx.heading(texto, size="5"),
                spacing="2",
                align="center",
                width="100%",
            ),
        ),
        value=value,
        color=COLOR_TEXTO_SECUNDARIO,
        _hover={"color": AZUL_MARINO_NEON},
        _selected={
            "color": AZUL_MARINO_NEON,
            "border_color": AZUL_MARINO_NEON,
        },
    )


# ======================================================================
# Encabezado sticky con breadcrumb
# ======================================================================


def _encabezado_fijo_detalle() -> rx.Component:
    """Encabezado sticky con breadcrumb + botón de regreso."""
    nombre_corto = EstadoInstitucional.carrera_seleccionada["nombre_corto"]

    return rx.box(
        rx.flex(
            # --- Botón de regreso ---
            enlace_navegacion(
                "/carreras",
                rx.icon("arrow-left", size=18),
                rx.text("Volver", font_size="0.8125rem", font_weight="600"),
                color=COLOR_TEXTO_PRINCIPAL,
                padding="0.5rem 0.875rem",
                border_radius=RADIO_MEDIO,
                background=COLOR_FONDO_CARTA,
                border=f"1px solid {COLOR_BORDE_SUAVE}",
                display="flex",
                align_items="center",
                gap="0.375rem",
                transition="all 0.2s",
                flex_shrink="0",
                text_decoration="none",
                _hover={
                    "background": COLOR_FONDO_SUAVE,
                    "border_color": AZUL_MARINO_NEON,
                    "transform": "translateX(-2px)",
                },
            ),
            # --- Breadcrumb central ---
            rx.flex(
                rx.text(
                    "Carreras",
                    font_size="0.8125rem",
                    color=COLOR_TEXTO_SECUNDARIO,
                ),
                rx.icon(
                    "chevron-right",
                    size=14,
                    color=COLOR_TEXTO_SECUNDARIO,
                ),
                rx.text(
                    nombre_corto,
                    font_size="0.8125rem",
                    font_weight="600",
                    color=COLOR_TEXTO_PRINCIPAL,
                ),
                align="center",
                gap="0.375rem",
                display=["none", "none", "flex", "flex"],
            ),
            # --- Espaciador ---
            rx.box(width=ANCHO_ESPACIADOR_HEADER, flex_shrink="0"),
            align="center",
            justify="between",
            width="100%",
        ),
        align="center",
        justify="center",
        width="100%",
        padding="0.75rem 1.5rem",
        background=rx.color("gray", 1, alpha=True),
        backdrop_filter="blur(12px)",
        border_bottom=f"1px solid {COLOR_BORDE_SUAVE}",
        position="sticky",
        top="0",
        z_index="50",
    )


# ======================================================================
# Anillos tipo Saturno
# ======================================================================


def _anillos_saturno(color: str | rx.Var) -> rx.Component:
    """Dibuja los anillos característicos de Saturno."""
    return rx.box(
        rx.box(
            position="absolute",
            top="50%",
            left="50%",
            width="1.8rem",
            height="0.45rem",
            border=f"2px solid {color}",
            border_radius=RADIO_PASTILLA,
            transform="translate(-50%, -50%)",
            opacity="0.8",
        ),
        rx.box(
            position="absolute",
            top="50%",
            left="50%",
            width="2.2rem",
            height="0.65rem",
            border=f"1.5px solid {color}",
            border_radius=RADIO_PASTILLA,
            transform="translate(-50%, -50%)",
            opacity="0.4",
        ),
        position="absolute",
        top="50%",
        left="50%",
        width="0",
        height="0",
        z_index="5",
        pointer_events="none",
    )


# ======================================================================
# Icono orbital
# ======================================================================


def _icono_orbital(icono_animado: IconoAnimado) -> rx.Component:
    """Renderiza un icono orbitando alrededor de la imagen central."""
    periodo = icono_animado["periodo"]
    keyframe_orbita = icono_animado["keyframe_orbita"]
    desfase = icono_animado["desfase_temporal"]
    color_icono = icono_animado["color"]
    tiene_anillos = icono_animado["tiene_anillos"]

    return rx.box(
        rx.box(
            rx.cond(
                tiene_anillos,
                _anillos_saturno(color_icono),
                rx.fragment(),
            ),
            rx.icon(
                icono_animado["nombre"],
                size=18,
                color="white",
            ),
            padding="0.5rem",
            border_radius="0.625rem",
            background=color_icono,
            box_shadow=f"0 6px 16px -4px {color_icono}",
            display="flex",
            align_items="center",
            justify_content="center",
            position="relative",
        ),
        position="absolute",
        top="50%",
        left="50%",
        transform_origin="center center",
        animation=f"{keyframe_orbita} {periodo}s linear {desfase}s infinite",
        z_index="20",
    )


# ======================================================================
# Contenedor orbital
# ======================================================================


def _contenedor_orbital_imagen() -> rx.Component:
    """Contenedor cuadrado con imagen central + iconos orbitales."""
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.box(
        # --- Anillo decorativo exterior ---
        rx.box(
            position="absolute",
            top="5%",
            left="5%",
            right="5%",
            bottom="5%",
            border=rx.color_mode_cond(
                light=f"1px dashed {AZUL_MARINO_NEON}33",
                dark=f"1px dashed {AZUL_MARINO_NEON}55",
            ),
            border_radius=RADIO_PASTILLA,
            z_index="0",
        ),
        # --- Halo radial ---
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=rx.color_mode_cond(
                light=(
                    f"radial-gradient(circle at 50% 50%, "
                    f"{AZUL_MARINO_NEON}33 0%, transparent 60%)"
                ),
                dark=(
                    f"radial-gradient(circle at 50% 50%, "
                    f"{AZUL_MARINO_NEON}44 0%, transparent 60%)"
                ),
            ),
            border_radius=RADIO_PASTILLA,
            filter="blur(20px)",
            z_index="1",
        ),
        # --- Iconos orbitales ---
        rx.box(
            rx.foreach(
                carrera["iconos_animados"],
                _icono_orbital,
            ),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="5",
        ),
        # --- Imagen central ---
        rx.box(
            rx.image(
                src=f"/{carrera['imagen_archivo']}",
                alt=carrera["nombre"],
                width="100%",
                height="100%",
                object_fit="cover",
                border_radius=RADIO_PASTILLA,
            ),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            width=TAMANO_IMAGEN_ORBITAL,
            height=TAMANO_IMAGEN_ORBITAL,
            border_radius=RADIO_PASTILLA,
            border=f"3px solid {AZUL_MARINO_NEON}",
            box_shadow=f"0 15px 30px -8px {AZUL_MARINO_NEON}",
            overflow="hidden",
            z_index="10",
            animation="pulso_central 3s ease-in-out infinite",
        ),
        position="relative",
        width="100%",
        max_width="20rem",
        aspect_ratio="1",
        margin="0 auto",
        display="flex",
        align_items="center",
        justify_content="center",
        overflow="visible",
    )


# ======================================================================
# Badge informativo
# ======================================================================


def _badge_info(
    icono: str,
    texto: str,
    color: str | rx.Var,
    fondo_suave: bool = True,
) -> rx.Component:
    """Badge informativo con icono + texto y borde con el acento."""
    return rx.flex(
        rx.icon(icono, size=12, color=color),
        rx.text(
            texto,
            font_size="0.75rem",
            font_weight="600",
            color=COLOR_TEXTO_PRINCIPAL,
            white_space="nowrap",
        ),
        align="center",
        gap="0.375rem",
        padding="0.375rem 0.75rem",
        border_radius=RADIO_PASTILLA,
        background=COLOR_FONDO_SUAVE if fondo_suave else "transparent",
        border=f"1px solid {color}",
    )


# ======================================================================
# Hero de carrera
# ======================================================================


def _hero_carrera() -> rx.Component:
    """Bloque de presentación principal."""
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.flex(
        # --- Columna izquierda: contenedor orbital ---
        rx.box(
            _contenedor_orbital_imagen(),
            width=["100%", "100%", "100%", "40%"],
            flex_shrink="0",
        ),
        # --- Columna derecha: información textual ---
        rx.vstack(
            # --- Badge de categoría ---
            rx.flex(
                rx.icon("award", size=12, color="white"),
                rx.text(
                    "TÉCNICO SUPERIOR",
                    font_size="0.625rem",
                    font_weight="800",
                    color="white",
                    letter_spacing="0.1em",
                ),
                align="center",
                gap="0.375rem",
                background=AZUL_MARINO_NEON,
                padding="0.375rem 0.75rem",
                border_radius=RADIO_PASTILLA,
                width="fit-content",
                box_shadow=f"0 4px 12px -2px {AZUL_MARINO_NEON}",
            ),
            # --- Nombre ---
            rx.heading(
                carrera["nombre"],
                size="8",
                font_weight="800",
                color=COLOR_TEXTO_PRINCIPAL,
                line_height="1.1",
                text_align="left",
                letter_spacing="-0.025em",
            ),
            # --- Lema ---
            rx.text(
                carrera["lema"],
                font_size="1rem",
                color=COLOR_TEXTO_CUERPO,
                line_height="1.6",
                max_width="36rem",
            ),
            # --- Badges ---
            rx.flex(
                _badge_info("clock", carrera["duracion"], AZUL_MARINO_NEON),
                _badge_info(
                    "building-2", carrera["modalidad"], AZUL_MARINO_NEON
                ),
                wrap="wrap",
                gap="0.5rem",
                margin_top="0.5rem",
            ),
            align="start",
            spacing="4",
            width=["100%", "100%", "100%", "60%"],
        ),
        width="100%",
        justify="center",
        align="center",
        gap=["2rem", "2.5rem", "3rem", "3rem"],
        padding=[
            "2rem 1.5rem",
            "2.5rem 1.5rem",
            "3rem 1.5rem",
            "3rem 1.5rem",
        ],
        flex_direction=rx.breakpoints(initial="column", lg="row"),
    )


# ======================================================================
# Sección: PREGUNTAS FRECUENTES
# ======================================================================


def _seccion_preguntas_frecuentes() -> rx.Component:
    """Sección completa con las preguntas frecuentes de la carrera."""
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.vstack(
        # --- Encabezado ---
        rx.flex(
            rx.box(
                rx.icon("circle-help", size=20, color=AZUL_MARINO_NEON),
                padding="0.625rem",
                border_radius=RADIO_MEDIO,
                background=FONDO_AZUL_SUAVE,
                border=f"1px solid {AZUL_MARINO_NEON}",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    "Preguntas frecuentes",
                    font_size="0.9375rem",
                    font_weight="800",
                    color=COLOR_TEXTO_PRINCIPAL,
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                    line_height="1.2",
                ),
                rx.text(
                    "Respuestas a las dudas más comunes de esta carrera.",
                    font_size="0.75rem",
                    color=COLOR_TEXTO_SECUNDARIO,
                    line_height="1.4",
                ),
                spacing="1",
                align="start",
                flex="1",
                min_width="0",
            ),
            # Contador
            rx.box(
                rx.text(
                    carrera["preguntas_frecuentes"].length().to_string(),
                    font_size="0.6875rem",
                    font_weight="700",
                    color=COLOR_TEXTO_SECUNDARIO,
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                ),
                padding="0.25rem 0.625rem",
                border_radius=RADIO_PASTILLA,
                background=COLOR_FONDO_SUAVE,
                border=f"1px solid {AZUL_MARINO_NEON}",
                flex_shrink="0",
            ),
            align="center",
            gap="0.75rem",
            width="100%",
            margin_bottom="1.5rem",
            flex_wrap="wrap",
        ),
        # --- Acordeón ---
        acordeon_faq(
            items=carrera["preguntas_frecuentes"],
            variante="light",
            icono="circle-help",
            color_acento=AZUL_MARINO_NEON,
            tamano_texto_pregunta="0.9375rem",
            tamano_texto_respuesta="0.875rem",
            padding_cabecera="1.125rem 1.25rem",
            padding_respuesta="0 1.25rem 1.25rem 3.5rem",
        ),
        spacing="0",
        width="100%",
        max_width=ANCHO_SECCION,
        margin="0 auto",
        padding=f"0 {PADDING_LATERAL}",
    )


# ======================================================================
# Pestañas
# ======================================================================


def _pestanas_secciones_detalle() -> rx.Component:
    """Sistema de pestañas con `rx.tabs.root`."""
    return rx.tabs.root(
        rx.tabs.list(
            _tabs_trigger("Info", "info", value="info"),
            _tabs_trigger("Plan", "book-open-text", value="plan"),
            _tabs_trigger("Perfil", "target", value="perfil"),
            width="100%",
            gap="0.25rem",
            padding="0.375rem",
            border_radius=RADIO_EXTRA_GRANDE,
        ),
        rx.tabs.content(
            seccion_informacion(),
            margin_top="1.5rem",
            value="info",
        ),
        rx.tabs.content(
            seccion_plan_estudios(),
            margin_top="1.5rem",
            value="plan",
        ),
        rx.tabs.content(
            seccion_perfil_y_campo_laboral(),
            margin_top="1.5rem",
            value="perfil",
        ),
        default_value="info",
        width="100%",
    )


# ======================================================================
# Botón flotante
# ======================================================================


def _boton_volver_arriba() -> rx.Component:
    """Botón flotante para volver al inicio de la página."""
    return rx.box(
        rx.icon(
            "arrow-up",
            size=20,
            color="white",
        ),
        position="fixed",
        bottom="2rem",
        right="2rem",
        height="3rem",
        width="3rem",
        border_radius=RADIO_PASTILLA,
        background=AZUL_MARINO_NEON,
        box_shadow=f"0 10px 30px -8px {AZUL_MARINO_NEON}",
        display=["none", "flex"],
        align_items="center",
        justify_content="center",
        cursor="pointer",
        z_index="40",
        transition="all 0.25s cubic-bezier(0.4, 0, 0.2, 1)",
        on_click=rx.call_script(
            "window.scrollTo({top: 0, behavior: 'smooth'})"
        ),
        _hover={
            "transform": "translateY(-3px)",
            "box_shadow": f"0 15px 40px -8px {AZUL_MARINO_NEON}",
        },
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/carrera/[carrera_id]",
    title=f"Detalle de Carrera | {NOMBRE_INSTITUTO}",
    on_load=EstadoInstitucional.redirigir_si_carrera_invalida,
)
def vista_detalle_carrera() -> rx.Component:
    """
    Página de detalle con:
    - Encabezado sticky con breadcrumb.
    - Hero con contenedor orbital + info textual.
    - Pestañas (Info, Plan, Perfil).
    - Sección de preguntas frecuentes.
    - Botón flotante "volver arriba".
    - Pie de página institucional.

    El `on_load` redirige a `/404?origen=carrera` si el `carrera_id`
    de la URL no existe o no es válido.
    """
    return rx.vstack(
        barra_navegacion_superior(),
        rx.box(
            _encabezado_fijo_detalle(),
            _hero_carrera(),
            rx.box(
                _pestanas_secciones_detalle(),
                padding=PADDING_INFERIOR_PESTANAS,
                max_width=ANCHO_CONTENIDO,
                margin="0 auto",
                width="100%",
            ),
            _seccion_preguntas_frecuentes(),
            _boton_volver_arriba(),
            padding_bottom="3rem",
            width="100%",
        ),
        pie_pagina_institucional(),
        align="center",
        min_height="100vh",
        width="100%",
        spacing="0",
        background=FONDO_HOME,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_detalle_carrera"]