"""
Sección de carreras en la página de inicio — estilo Neon.com.

Propósito
---------
Comunicar al visitante, en los primeros segundos, qué carreras
ofrece el instituto. Cada tarjeta es un enlace directo al detalle
de esa carrera.

Diseño
------
1. **Grid responsive** de 5 tarjetas con imagen de portada.
2. **Imagen de fondo** + gradiente oscuro para legibilidad.
3. **Nombre corto + icono + CTA** sobre la imagen.
4. **Hover sutil** (zoom leve de la imagen + borde de acento).
5. **Sin glow excesivo** (coherente con el sitio).
6. **Enlace global** al catálogo de carreras.

Técnica de imagen de fondo
--------------------------
Cada tarjeta tiene:
1. `<img>` con `object_fit="cover"` ocupando el 100%.
2. Overlay con gradiente lineal (transparente → negro) para que el
   texto sea legible sin importar la imagen.
3. Contenido (icono + nombre + CTA) encima, con `z_index`.

Sistema de color
----------------
✅ ADAPTATIVO: fondo, textos y bordes respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    FONDO_AZUL_SUAVE,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Tipos
# ======================================================================


class CarreraDestacada(TypedDict):
    """Carrera destacada para el grid del inicio."""

    icono: str
    nombre_corto: str
    nombre_completo: str
    id_carrera: str
    imagen: str


# ======================================================================
# Datos estáticos
# ======================================================================

CARRERAS_DESTACADAS: list[CarreraDestacada] = [
    {
        "icono": "cpu",
        "nombre_corto": "Sistemas",
        "nombre_completo": "Sistemas Informáticos",
        "id_carrera": "0",
        "imagen": "sistemas.png",
    },
    {
        "icono": "calculator",
        "nombre_corto": "Contaduría",
        "nombre_completo": "Contaduría General",
        "id_carrera": "1",
        "imagen": "contaduria.png",
    },
    {
        "icono": "briefcase",
        "nombre_corto": "Secretariado",
        "nombre_completo": "Secretariado Ejecutivo",
        "id_carrera": "2",
        "imagen": "secretariado.png",
    },
    {
        "icono": "globe",
        "nombre_corto": "Comercio Int.",
        "nombre_completo": "Comercio Internacional",
        "id_carrera": "3",
        "imagen": "comercio.png",
    },
    {
        "icono": "zap",
        "nombre_corto": "Electrónica",
        "nombre_completo": "Electrónica",
        "id_carrera": "4",
        "imagen": "electronica.png",
    },
]


# ======================================================================
# Tarjeta individual con imagen
# ======================================================================


def _tarjeta_carrera(carrera: CarreraDestacada) -> rx.Component:
    """
    Tarjeta de carrera con imagen de portada.

    Estructura:
    ┌────────────────────────┐
    │                        │  ← Imagen de fondo (portada)
    │   [gradiente oscuro]   │
    │                        │
    │   🖥️  Sistemas         │  ← Contenido encima
    │   Ver detalle →        │
    └────────────────────────┘

    Estilo Neon.com:
    - Imagen de fondo con `object_fit="cover"`.
    - Gradiente oscuro para legibilidad.
    - Hover: zoom leve de la imagen + borde de acento.
    - Border-radius grande.
    - Aspect ratio fijo (3:4 vertical).

    Args:
        carrera: `CarreraDestacada` con los datos de la carrera.

    Returns:
        Tarjeta clicable (enlace a `/carrera/{id}`).
    """
    return rx.link(
        rx.box(
            # ─── Imagen de fondo ────────────────────────────────
            rx.image(
                src=f"/{carrera['imagen']}",
                alt=carrera["nombre_completo"],
                width="100%",
                height="100%",
                object_fit="cover",
                position="absolute",
                top="0",
                left="0",
                z_index="0",
                transition="transform 0.4s ease",
                class_name="card-carrera-imagen",
            ),
            # ─── Gradiente oscuro para legibilidad ──────────────
            rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background=(
                    "linear-gradient(180deg, "
                    "rgba(0, 0, 0, 0.0) 0%, "
                    "rgba(0, 0, 0, 0.2) 40%, "
                    "rgba(0, 0, 0, 0.75) 100%)"
                ),
                z_index="1",
            ),
            # ─── Contenido sobre la imagen ──────────────────────
            rx.vstack(
                # ─── Icono + CTA arriba (sutil) ─────────────────
                rx.flex(
                    rx.flex(
                        rx.icon(
                            carrera["icono"],
                            size=14,
                            color="white",
                        ),
                        align="center",
                        justify="center",
                        padding="0.5rem",
                        border_radius=RADIO_PASTILLA,
                        background="rgba(255, 255, 255, 0.15)",
                        backdrop_filter="blur(8px)",
                        border="1px solid rgba(255, 255, 255, 0.2)",
                        flex_shrink="0",
                    ),
                    width="100%",
                    justify="start",
                ),
                # ─── Espacio flexible ────────────────────────────
                rx.spacer(),
                # ─── Nombre corto (abajo) ────────────────────────
                rx.vstack(
                    rx.text(
                        carrera["nombre_corto"],
                        font_size="1rem",
                        font_weight="800",
                        color="white",
                        line_height="1.2",
                        letter_spacing="-0.02em",
                        text_shadow="0 2px 8px rgba(0, 0, 0, 0.5)",
                    ),
                    # ─── CTA "Ver detalle →" ─────────────────────
                    rx.flex(
                        rx.text(
                            "Ver detalle",
                            font_size="0.75rem",
                            font_weight="600",
                            color="rgba(255, 255, 255, 0.85)",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=12,
                            color="rgba(255, 255, 255, 0.85)",
                        ),
                        align="center",
                        gap="0.25rem",
                        transition="gap 0.2s, color 0.2s",
                    ),
                    align="start",
                    spacing="1",
                    width="100%",
                ),
                align="start",
                justify="between",
                width="100%",
                height="100%",
                padding="1.25rem",
                position="relative",
                z_index="2",
            ),
            # ─── Estilos base de la tarjeta ─────────────────────
            position="relative",
            width="100%",
            aspect_ratio="3 / 4",
            border_radius=RADIO_EXTRA_GRANDE,
            overflow="hidden",
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            transition="all 0.3s ease",
            cursor="pointer",
            _hover={
                "border_color": AZUL_MARINO_NEON,
                "& .card-carrera-imagen": {
                    "transform": "scale(1.06)",
                },
            },
        ),
        href=f"/carrera/{carrera['id_carrera']}",
        text_decoration="none",
        width="100%",
        display="block",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_carreras_inicio() -> rx.Component:
    """
    Sección completa de carreras destacadas para el inicio.

    Estructura:
    1. Header: badge + título + subtítulo.
    2. Grid de 5 tarjetas con imagen.
    3. CTA "Ver todas las carreras".

    Estilo Neon.com:
    - Layout alineado a la izquierda (header).
    - Grid responsive (1 → 2 → 3 → 5 columnas).
    - Padding vertical consistente con el resto del sitio.

    Returns:
        Componente `<section>` completo.
    """
    return rx.box(
        rx.vstack(
            # ==========================================================
            # Header: badge + título + subtítulo
            # ==========================================================
            rx.vstack(
                # ─── Badge ─────────────────────────────────────────
                rx.flex(
                    rx.icon("graduation-cap", size=12, color=AZUL_MARINO_NEON),
                    rx.text(
                        "CARRERAS TÉCNICAS",
                        font_size="0.6875rem",
                        font_weight="700",
                        color=AZUL_MARINO_NEON,
                        letter_spacing="0.15em",
                        text_transform="uppercase",
                    ),
                    align="center",
                    gap="0.5rem",
                    margin_bottom="1.5rem",
                ),
                # ─── Título con énfasis bicolor ────────────────────
                rx.heading(
                    rx.text.span("5 carreras, "),
                    rx.text.span(
                        "3 años, 1 título",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    as_="h2",
                    font_size=["1.75rem", "2rem", "2.25rem"],
                    font_weight="700",
                    color=TEXTO_HOME_PRINCIPAL,
                    letter_spacing="-0.03em",
                    line_height="1.15",
                    max_width="48rem",
                ),
                # ─── Subtítulo ─────────────────────────────────────
                rx.text(
                    "Elige el programa que impulse tu carrera. Todas "
                    "con título de Técnico Superior en Provisión "
                    "Nacional.",
                    font_size=["1rem", "1.0625rem"],
                    color=TEXTO_HOME_MAS_SUAVE,
                    line_height="1.6",
                    max_width="42rem",
                    margin_top="0.75rem",
                ),
                align="start",
                spacing="0",
                width="100%",
                margin_bottom="3rem",
            ),
            # ==========================================================
            # Grid de tarjetas con imagen
            # ==========================================================
            rx.grid(
                *[_tarjeta_carrera(c) for c in CARRERAS_DESTACADAS],
                columns=rx.breakpoints(
                    initial="1",
                    sm="2",
                    md="3",
                    lg="5",
                ),
                spacing="3",
                width="100%",
            ),
            # ==========================================================
            # CTA "Ver todas las carreras"
            # ==========================================================
            rx.flex(
                rx.link(
                    rx.text(
                        "Ver todas las carreras",
                        font_size="0.9375rem",
                        font_weight="700",
                        color=AZUL_MARINO_NEON,
                    ),
                    rx.icon(
                        "arrow-right",
                        size=16,
                        color=AZUL_MARINO_NEON,
                    ),
                    href="/carreras",
                    text_decoration="none",
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    transition="gap 0.2s",
                    _hover={"gap": "0.75rem"},
                ),
                width="100%",
                justify="start",
                margin_top="2.5rem",
            ),
            spacing="0",
            width="100%",
            align="start",
        ),
        max_width="80rem",
        margin="0 auto",
        padding=[
            "4rem 1.5rem",
            "5rem 1.5rem",
            "6rem 1.5rem",
        ],
        width="100%",
        id="carreras-inicio",
        aria_label="Carreras técnicas del instituto",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "CARRERAS_DESTACADAS",
    "CarreraDestacada",
    "seccion_carreras_inicio",
]