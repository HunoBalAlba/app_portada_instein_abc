"""
Post destacado (featured) del blog con imagen real.

Estructura
----------
- `_imagen_destacada`:  bloque de imagen grande con overlay + badge.
- `_cta_leer_articulo`: botón CTA "Leer artículo".
- `post_destacado`:     card completa con layout 2 columnas.

Sistema de color
----------------
- Acentos: `AZUL_MARINO_NEON`.
- Overlays sobre imagen: `rgba` intencionales.
- Badge "DESTACADO": `rgba(0,0,0,0.5)` sobre cualquier imagen.

Nota técnica: TIPADO ESTRICTO CON `Post`
----------------------------------------
Todas las funciones que reciben un post están tipadas como `Post`
(el `TypedDict` de `dominio.modelos.blog`), NO como `dict` genérico.

Esto es CRÍTICO para Reflex: si el tipo es `dict` genérico, los
campos internos se infieren como `str | int | bool` y props como
`rx.image(alt=str)` fallan.

Nota técnica: NAVEGACIÓN
------------------------
La card destacada ya NO abre un diálogo modal. Ahora es un enlace
directo a la página de detalle `/blog/{id}`, donde el post se muestra
completo con scroll natural de página.
"""

from __future__ import annotations

import reflex as rx

from ...dominio.estados.estado_blog import EstadoBlog
from ...dominio.modelos.blog import Post
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
)

from .helpers_categoria import badge_categoria, fondo_categoria
from .meta_info import meta_info_post


# ======================================================================
# Constantes locales
# ======================================================================

ALTURA_IMAGEN_DESTACADA: list[str] = ["14rem", "16rem", "18rem"]
ANCHO_IMAGEN_DESTACADA: list[str] = ["100%", "100%", "40%"]
RUTA_IMAGENES_BLOG: str = "/blog/"


# ======================================================================
# Badge "DESTACADO"
# ======================================================================


def _badge_destacado() -> rx.Component:
    """
    Badge "DESTACADO" flotante sobre la imagen.

    Usa `rgba(0,0,0,0.5)` con blur intencional para garantizar
    legibilidad sobre cualquier imagen de fondo.
    """
    return rx.flex(
        rx.icon("star", size=12, color="white", fill="white"),
        rx.text(
            "DESTACADO",
            font_size="0.625rem",
            font_weight="800",
            color="white",
            letter_spacing="0.15em",
        ),
        align="center",
        gap="0.375rem",
        padding="0.375rem 0.75rem",
        border_radius=RADIO_PASTILLA,
        background="rgba(0,0,0,0.5)",
        backdrop_filter="blur(8px)",
        border="1px solid rgba(255,255,255,0.2)",
        position="absolute",
        top="1rem",
        left="1rem",
        z_index="3",
        width="fit-content",
    )


# ======================================================================
# Bloque de imagen destacada
# ======================================================================


def _imagen_destacada(post: Post) -> rx.Component:
    """
    Bloque de imagen grande del post destacado.

    Args:
        post: `Post` destacado. Tipado estricto (no `dict`) para que
            Reflex sepa que `post["titulo"]` y `post["imagen"]` son
            `str` y los acepte en `rx.image`.
    """
    return rx.box(
        # CAPA 1: Fondo de fallback (color de la categoría)
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=fondo_categoria(post["categoria"]),
            z_index="0",
        ),
        # CAPA 2: Imagen real
        rx.image(
            src=f"{RUTA_IMAGENES_BLOG}{post['imagen']}",
            alt=post["titulo"],
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
            z_index="1",
            transition="transform 0.5s cubic-bezier(0.4, 0, 0.2, 1)",
        ),
        # CAPA 3: Overlay sutil
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=(
                "linear-gradient(180deg, "
                "rgba(0,0,0,0.25) 0%, "
                "rgba(0,0,0,0.05) 40%, "
                "rgba(0,0,0,0.4) 100%)"
            ),
            z_index="2",
            pointer_events="none",
        ),
        # CAPA 4: Badge
        _badge_destacado(),
        # Contenedor principal
        position="relative",
        height=ALTURA_IMAGEN_DESTACADA,
        width=ANCHO_IMAGEN_DESTACADA,
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        background=COLOR_FONDO_SUAVE,
        flex_shrink="0",
    )


# ======================================================================
# CTA "Leer artículo"
# ======================================================================


def _cta_leer_articulo() -> rx.Component:
    """
    Botón CTA "Leer artículo" con flecha animada en hover.

    La flecha lleva la clase `arrow-destacado`, que la card padre
    anima al recibir hover.
    """
    return rx.flex(
        rx.text("Leer artículo", as_="span", font_weight="700"),
        rx.icon(
            "arrow-right",
            size=16,
            class_name="arrow-destacado",
            transition="transform 0.2s",
        ),
        align="center",
        gap="0.5rem",
        background=AZUL_MARINO_NEON,
        color="white",
        padding="0.75rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.875rem",
        margin_top="0.5rem",
        box_shadow=f"0 10px 25px -5px {AZUL_MARINO_NEON}",
        transition="all 0.2s",
        cursor="pointer",
    )


# ======================================================================
# Post destacado completo
# ======================================================================


def post_destacado() -> rx.Component:
    """
    Post destacado con layout de dos columnas que enlaza al detalle.

    Estructura:
    - Columna izquierda (40%): imagen grande con overlay y badge.
    - Columna derecha (60%): badge de categoría + título + extracto
      + meta + CTA "Leer artículo".

    La card completa es un enlace a `/blog/{id}` (no un diálogo).
    """
    post = EstadoBlog.post_destacado

    card_destacada = rx.box(
        rx.flex(
            _imagen_destacada(post),
            rx.vstack(
                badge_categoria(post["categoria"]),
                rx.heading(
                    post["titulo"],
                    size="7",
                    font_weight="800",
                    color=COLOR_TEXTO_PRINCIPAL,
                    line_height="1.2",
                    letter_spacing="-0.02em",
                ),
                rx.text(
                    post["extracto"],
                    font_size="0.9375rem",
                    color=COLOR_TEXTO_CUERPO,
                    line_height="1.7",
                ),
                meta_info_post(post),
                _cta_leer_articulo(),
                align="start",
                spacing="3",
                flex="1",
                min_width="0",
            ),
            direction=rx.breakpoints(initial="column", md="row"),
            gap="2rem",
            align="center",
            width="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {BORDE_HOME_SUAVE}",
        width="100%",
        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        cursor="pointer",
        _hover={
            "border_color": AZUL_MARINO_NEON,
            "box_shadow": f"0 20px 40px -10px {AZUL_MARINO_NEON}",
            "& img": {"transform": "scale(1.05)"},
            "& .arrow-destacado": {"transform": "translateX(4px)"},
        },
    )

    return rx.link(
        card_destacada,
        href=f"/blog/{post['id']}",
        text_decoration="none",
        width="100%",
        display="block",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["post_destacado"]