"""
Widgets atómicos del explorador de carreras.

Contenido
---------
- `contenedor_animacion_orbital`: fondo espacial con partículas +
  imagen central (el "Sol" del sistema orbital).
- `cuadro_resumen_multimedia`:   contenedor orbital + etiquetas +
  CTA al detalle.
- `pastilla_carrera_destacada`:  pastilla seleccionable para cambiar
  la carrera destacada.
- `selector_carrera_destacada`:  fila completa de pastillas con
  encabezado y contador.
- `bloque_texto_carrera_destacada`: título + lema + CTA del home.

Sistema de color
----------------
✅ ACENTO ÚNICO: `AZUL_MARINO_NEON` para todos los elementos.
✅ ADAPTATIVO: fondos, textos y bordes cambian con el `color_mode`.

Nota técnica: ORIGEN
--------------------
Este archivo reemplaza la antigua implementación monolítica que
convivía con `tarjetas_carrera.py`. Se extrajo a `widgets.py` dentro
de `explorador/` para mantener la cohesión temática.

Los helpers `color_carrera_adaptativo()` y
`color_suave_carrera_adaptativo()` fueron ELIMINADOS. Aquí usamos
directamente `AZUL_MARINO_NEON` y `FONDO_AZUL_SUAVE`.
"""

from __future__ import annotations

import random

import reflex as rx

from ....componentes.base.primitivos import (
    contenedor_clicable,
    enlace_navegacion,
)
from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ....dominio.modelos.carrera import Carrera
from ....infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
)
from ....infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

# Estrellas decorativas del fondo orbital.
CANTIDAD_ESTRELLAS: int = 80
SEMILLA_ESTRELLAS: int = 42

# Líneas de fuga radiales.
ANGULOS_LINEAS_FUGA: list[float] = [i * 22.5 for i in range(16)]
ANCHO_LINEA_FUGA: str = "150%"

# Imagen central orbital.
TAMANO_IMAGEN_ORBITAL: str = "8rem"

# Anillos tipo Saturno.
ANCHO_ANILLO_INTERIOR: str = "2.4rem"
ALTO_ANILLO_INTERIOR: str = "0.6rem"
ANCHO_ANILLO_EXTERIOR: str = "3.0rem"
ALTO_ANILLO_EXTERIOR: str = "0.9rem"


# ======================================================================
# Estrellas de fondo
# ======================================================================


def _generar_estrellas(
    cantidad: int = CANTIDAD_ESTRELLAS,
    semilla: int = SEMILLA_ESTRELLAS,
) -> list[dict]:
    """
    Genera posiciones aleatorias reproducibles para las estrellas.

    Returns:
        Lista de dicts con `x`, `y`, `tamano`, `opacidad`, `delay`.
    """
    rng = random.Random(semilla)
    return [
        {
            "x": rng.uniform(0, 100),
            "y": rng.uniform(0, 100),
            "tamano": rng.uniform(1, 3),
            "opacidad": rng.uniform(0.3, 0.9),
            "delay": rng.uniform(0, 3),
        }
        for _ in range(cantidad)
    ]


ESTRELLAS_FONDO = _generar_estrellas()
"""Estrellas precalculadas (constante de módulo)."""


def _estrella_fondo(estrella: dict) -> rx.Component:
    """
    Renderiza una estrella individual del fondo.

    Usa `COLOR_TEXTO_PRINCIPAL` (gray-12) para visibilidad en ambos
    modos (oscuro en light, claro en dark).
    """
    return rx.box(
        position="absolute",
        left=f"{estrella['x']}%",
        top=f"{estrella['y']}%",
        width=f"{estrella['tamano']}px",
        height=f"{estrella['tamano']}px",
        background=COLOR_TEXTO_PRINCIPAL,
        border_radius=RADIO_PASTILLA,
        opacity=f"{estrella['opacidad']}",
        animation=(
            f"flotar_estrella {2 + estrella['delay']}s "
            f"ease-in-out {estrella['delay']}s infinite"
        ),
        z_index="0",
        pointer_events="none",
    )


# ======================================================================
# Líneas de fuga radiales
# ======================================================================


def _linea_fuga(angulo: float) -> rx.Component:
    """
    Renderiza una línea de fuga radial desde el centro del contenedor.

    En light mode usa un gris neutro; en dark mode usa el acento.
    """
    return rx.box(
        position="absolute",
        top="50%",
        left="50%",
        width=ANCHO_LINEA_FUGA,
        height="1px",
        background=rx.color_mode_cond(
            light=COLOR_TEXTO_SECUNDARIO,
            dark=AZUL_MARINO_NEON,
        ),
        opacity=rx.color_mode_cond(light="0.15", dark="0.25"),
        transform_origin="0 50%",
        transform=f"translate(0, -50%) rotate({angulo}deg)",
        z_index="1",
        pointer_events="none",
    )


# ======================================================================
# Anillos tipo Saturno
# ======================================================================


def _anillos_saturno(color: str | rx.Var) -> rx.Component:
    """
    Dibuja los anillos característicos de Saturno alrededor del icono.

    Args:
        color: Color del anillo (hex o Var adaptativa).
    """
    return rx.box(
        rx.box(
            position="absolute",
            top="50%",
            left="50%",
            width=ANCHO_ANILLO_INTERIOR,
            height=ALTO_ANILLO_INTERIOR,
            border=f"2px solid {color}",
            border_radius=RADIO_PASTILLA,
            transform="translate(-50%, -50%)",
            opacity="0.8",
        ),
        rx.box(
            position="absolute",
            top="50%",
            left="50%",
            width=ANCHO_ANILLO_EXTERIOR,
            height=ALTO_ANILLO_EXTERIOR,
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


def _icono_orbital(icono_animado: dict) -> rx.Component:
    """
    Renderiza un icono con su trayectoria elíptica kepleriana.

    Args:
        icono_animado: `IconoAnimado` con `periodo`, `keyframe_orbita`,
            `desfase_temporal`, `color`, `tiene_anillos`, `nombre`.
    """
    return rx.box(
        rx.box(
            rx.cond(
                icono_animado["tiene_anillos"],
                _anillos_saturno(icono_animado["color"]),
                rx.fragment(),
            ),
            rx.icon(icono_animado["nombre"], size=24, color="white"),
            padding="0.75rem",
            border_radius=RADIO_GRANDE,
            background=icono_animado["color"],
            box_shadow=f"0 8px 20px -5px {icono_animado['color']}",
            display="flex",
            align_items="center",
            justify_content="center",
            position="relative",
        ),
        position="absolute",
        top="50%",
        left="50%",
        transform_origin="center center",
        animation=(
            f"{icono_animado['keyframe_orbita']} "
            f"{icono_animado['periodo']}s linear "
            f"{icono_animado['desfase_temporal']}s infinite"
        ),
        z_index="20",
    )


# ======================================================================
# Contenedor orbital completo
# ======================================================================


def contenedor_animacion_orbital(carrera: Carrera) -> rx.Component:
    """
    Contenedor con fondo espacial + iconos orbitando + imagen central.

    Capas (de fondo a frente):
    - z_index=-1: Fondo base (gradiente adaptativo).
    - z_index=0:  Estrellas.
    - z_index=1:  Líneas de fuga.
    - z_index=2:  Halo radial.
    - z_index=10: Imagen central.
    - z_index=20: Iconos orbitando.

    Args:
        carrera: `Carrera` con `iconos_animados`, `imagen_archivo`,
            `nombre`.
    """
    return rx.box(
        # ==============================================================
        # CAPA 1: Fondo espacial
        # ==============================================================
        rx.box(
            rx.box(
                *[_estrella_fondo(e) for e in ESTRELLAS_FONDO],
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                z_index="0",
                pointer_events="none",
            ),
            rx.box(
                *[_linea_fuga(a) for a in ANGULOS_LINEAS_FUGA],
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                z_index="1",
                pointer_events="none",
            ),
            rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background=rx.color_mode_cond(
                    light=(
                        f"radial-gradient(circle at 50% 50%, "
                        f"{AZUL_MARINO_NEON}33 0%, transparent 70%)"
                    ),
                    dark=(
                        f"radial-gradient(circle at 50% 50%, "
                        f"{AZUL_MARINO_NEON}44 0%, transparent 70%)"
                    ),
                ),
                z_index="2",
                pointer_events="none",
            ),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=rx.color_mode_cond(
                light="linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)",
                dark="linear-gradient(135deg, #0b0914 0%, #05040a 100%)",
            ),
            z_index="-1",
        ),
        # ==============================================================
        # CAPA 2: Iconos orbitales
        # ==============================================================
        rx.box(
            rx.foreach(carrera["iconos_animados"], _icono_orbital),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="20",
        ),
        # ==============================================================
        # CAPA 3: Imagen central
        # ==============================================================
        rx.box(
            rx.image(
                src="/" + carrera["imagen_archivo"],
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
            border=f"4px solid {AZUL_MARINO_NEON}",
            box_shadow=f"0 20px 40px -10px {AZUL_MARINO_NEON}",
            overflow="hidden",
            z_index="10",
            animation="pulso_central 3s ease-in-out infinite",
        ),
        # ==============================================================
        # CONTENEDOR PRINCIPAL
        # ==============================================================
        position="relative",
        width="100%",
        height="100%",
        display="flex",
        align_items="center",
        justify_content="center",
        overflow="hidden",
    )


# ======================================================================
# Etiqueta superpuesta
# ======================================================================


def _etiqueta_superpuesta(
    contenido: rx.Component,
    posicion: dict,
) -> rx.Component:
    """
    Etiqueta flotante sobre la imagen orbital.

    Usa `rgba(0,0,0,0.4)` intencional para garantizar legibilidad
    sobre cualquier imagen de fondo, independientemente del modo.

    Args:
        contenido: Contenido interno de la etiqueta.
        posicion: Dict con `top`/`left` o `top`/`right`.
    """
    return rx.box(
        contenido,
        position="absolute",
        z_index="30",
        background="rgba(0,0,0,0.4)",
        backdrop_filter="blur(12px)",
        border_radius=RADIO_PASTILLA,
        padding="0.25rem 0.625rem",
        border="1px solid rgba(255,255,255,0.15)",
        **posicion,
    )


# ======================================================================
# Cuadro de resumen multimedia
# ======================================================================


def cuadro_resumen_multimedia() -> rx.Component:
    """
    Tarjeta principal con:
    - Contenedor orbital de fondo.
    - Etiquetas superpuestas (RESUMEN, duración).
    - Footer con nombre corto + botón de detalle.

    UX:
    - Etiqueta "RESUMEN" con punto rojo semántico.
    - Botón de detalle en blanco con sombra.
    """
    carrera = EstadoInstitucional.carrera_destacada

    return rx.box(
        contenedor_animacion_orbital(carrera),
        # ==========================================================
        # Etiqueta superior izquierda: RESUMEN
        # ==========================================================
        _etiqueta_superpuesta(
            rx.flex(
                rx.box(
                    height="0.375rem",
                    width="0.375rem",
                    border_radius=RADIO_PASTILLA,
                    background=rx.color("red", 9),
                ),
                rx.text("RESUMEN", size="1", color="white"),
                align="center",
                gap="0.375rem",
            ),
            posicion={"top": "1rem", "left": "1rem"},
        ),
        # ==========================================================
        # Etiqueta superior derecha: duración
        # ==========================================================
        _etiqueta_superpuesta(
            rx.text(carrera["duracion"], size="1", color="white"),
            posicion={"top": "1rem", "right": "1rem"},
        ),
        # ==========================================================
        # Footer: nombre corto + botón
        # ==========================================================
        rx.flex(
            rx.box(
                rx.text(
                    "TÉCNICO SUPERIOR EN",
                    size="1",
                    color="rgba(255,255,255,0.75)",
                ),
                rx.heading(carrera["nombre_corto"], size="6", color="white"),
            ),
            enlace_navegacion(
                EstadoInstitucional.url_detalle_carrera_destacada,
                rx.icon(
                    "image_upscale",
                    size=20,
                    color=AZUL_MARINO_NEON,
                    margin_left="0.125rem",
                ),
                height="2.75rem",
                width="2.75rem",
                border_radius=RADIO_PASTILLA,
                background="white",
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow="0 10px 25px -5px rgba(0,0,0,0.4)",
                flex_shrink="0",
            ),
            position="absolute",
            bottom="0",
            left="0",
            right="0",
            z_index="30",
            align="end",
            justify="between",
            padding="1rem",
            background="linear-gradient(to top, rgba(0,0,0,0.7), transparent)",
        ),
        # ==========================================================
        # Contenedor principal
        # ==========================================================
        position="relative",
        width="100%",
        height="18rem",
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        border=f"2px solid {AZUL_MARINO_NEON}",
        box_shadow=f"0 20px 40px -10px {AZUL_MARINO_NEON}",
    )


# ======================================================================
# Pastilla de carrera destacada
# ======================================================================


def pastilla_carrera_destacada(carrera: Carrera) -> rx.Component:
    """
    Pastilla seleccionable para elegir la carrera destacada.

    UX:
    - Activa: fondo sólido del acento + icono blanco.
    - Inactiva: fondo transparente + icono del acento.
    """
    esta_activa = EstadoInstitucional.id_carrera_destacada == carrera["id"]

    return contenedor_clicable(
        rx.box(
            rx.icon(
                carrera["icono"],
                size=26,
                color=rx.cond(esta_activa, "white", AZUL_MARINO_NEON),
            ),
            padding="0.75rem",
            background=rx.cond(esta_activa, AZUL_MARINO_NEON, "transparent"),
            border=f"1px solid {AZUL_MARINO_NEON}",
            border_radius=RADIO_GRANDE,
            box_shadow=rx.cond(
                esta_activa,
                f"0 10px 25px -5px {AZUL_MARINO_NEON}",
                "none",
            ),
            transition="all 0.2s",
            display="flex",
        ),
        rx.text(
            carrera["nombre_corto"],
            size="1",
            color=rx.cond(esta_activa, AZUL_MARINO_NEON, COLOR_TEXTO_SECUNDARIO),
            margin_top="0.375rem",
        ),
        al_hacer_clic=lambda: EstadoInstitucional.seleccionar_carrera_destacada(
            carrera["id"]
        ),
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        flex_shrink="0",
    )


# ======================================================================
# Bloque de texto de la carrera destacada
# ======================================================================


def bloque_texto_carrera_destacada() -> rx.Component:
    """
    Texto descriptivo de la carrera destacada con badge "CARRERA
    DESTACADA".

    UX:
    - Badge con fondo sólido del acento.
    - Título + lema en neutros.
    - CTA "Explorar Carreras" con fondo del acento.
    """
    carrera = EstadoInstitucional.carrera_destacada

    return rx.box(
        # ==========================================================
        # Badge "CARRERA DESTACADA"
        # ==========================================================
        rx.flex(
            rx.icon("star", size=12, color="white"),
            rx.text(
                "CARRERA DESTACADA",
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
            margin_bottom="1rem",
        ),
        # ==========================================================
        # Título
        # ==========================================================
        rx.heading(
            carrera["nombre"],
            size="8",
            color=COLOR_TEXTO_PRINCIPAL,
        ),
        # ==========================================================
        # Lema
        # ==========================================================
        rx.text(
            carrera["lema"],
            font_size="1rem",
            color=COLOR_TEXTO_SECUNDARIO,
            margin_top="0.5rem",
        ),
        # ==========================================================
        # CTA "Explorar Carreras"
        # ==========================================================
        enlace_navegacion(
            "/carreras",
            rx.text(
                "Explorar Carreras",
                as_="span",
                font_size="0.875rem",
                font_weight="700",
            ),
            rx.icon("layout-grid", size=16),
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_top="1.5rem",
            background=AZUL_MARINO_NEON,
            color="white",
            padding="0.75rem 1.5rem",
            border_radius=RADIO_PASTILLA,
            width="fit-content",
            box_shadow=f"0 10px 25px -5px {AZUL_MARINO_NEON}",
            transition="all 0.2s",
            _hover={
                "transform": "translateY(-2px)",
                "filter": "brightness(1.1)",
            },
        ),
        padding="1.5rem 1.5rem 1rem 1.5rem",
    )


# ======================================================================
# Selector completo de carrera destacada
# ======================================================================


def selector_carrera_destacada() -> rx.Component:
    """
    Bloque con encabezado "Elige una carrera" + contador + fila de
    pastillas selectoras.
    """
    return rx.box(
        # ==========================================================
        # Encabezado
        # ==========================================================
        rx.flex(
            rx.text(
                "Elige una carrera",
                color_scheme="gray",
                size="1",
                text_transform="uppercase",
                font_weight="600",
                letter_spacing="0.05em",
            ),
            rx.text(
                (EstadoInstitucional.id_carrera_destacada + 1).to_string()
                + " / "
                + EstadoInstitucional.carreras.length().to_string(),
                color_scheme="gray",
                size="1",
                font_weight="600",
            ),
            align="center",
            justify="between",
            padding="0 1.5rem",
            margin_bottom="1.75rem",
        ),
        # ==========================================================
        # Fila de pastillas
        # ==========================================================
        rx.vstack(
            rx.box(
                rx.flex(
                    rx.foreach(
                        EstadoInstitucional.carreras,
                        pastilla_carrera_destacada,
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    direction="row",
                ),
                width="100%",
                max_width="30em",
            ),
            align="center",
            justify="center",
        ),
        align="center",
        justify="center",
        padding_top="1rem",
        padding_bottom="1rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "bloque_texto_carrera_destacada",
    "contenedor_animacion_orbital",
    "cuadro_resumen_multimedia",
    "pastilla_carrera_destacada",
    "selector_carrera_destacada",
]