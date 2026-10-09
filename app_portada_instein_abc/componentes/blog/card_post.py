

from __future__ import annotations

import reflex as rx

from ...componentes.base.estado_vacio import (
    estado_vacio as _estado_vacio_unificado,
)
from ...dominio.estados.estado_blog import EstadoBlog
from ...dominio.modelos.blog import Post
from ...infraestructura import (
    AZUL_MARINO_NEON,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    RADIO_EXTRA_GRANDE,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)

from .helpers_categoria import (
    badge_categoria,
    fondo_categoria,
    icono_categoria,
)
from .meta_info import meta_info_post


# ======================================================================
# Constantes locales
# ======================================================================

ALTURA_IMAGEN_CARD: str = "11rem"
RUTA_IMAGENES_BLOG: str = "/blog/"


# ======================================================================
# Bloque de imagen con overlay de categoría
# ======================================================================


def _imagen_post(post: Post) -> rx.Component:
    """
    Bloque de imagen del post con fallback + imagen real + overlay.

    Args:
        post: `Post` (TypedDict). Tipado estricto para que Reflex
            sepa que `post["titulo"]` y `post["imagen"]` son `str`.
    """
    return rx.box(
        # Capa 1: fondo con icono de categoría (fallback)
        rx.box(
            rx.flex(
                icono_categoria(post["categoria"]),
                align="center",
                justify="center",
                width="100%",
                height="100%",
            ),
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=fondo_categoria(post["categoria"]),
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="0",
        ),
        # Capa 2: imagen real
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
            transition="transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
            _group_hover={"transform": "scale(1.05)"},
        ),
        # Capa 3: overlay sutil (respetando color de categoría)
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=rx.match(
                post["categoria"],
                (
                    "tecnologia",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(37, 99, 235, 0.15) 100%)",
                ),
                (
                    "contaduria",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(124, 58, 237, 0.15) 100%)",
                ),
                (
                    "empleabilidad",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(22, 163, 74, 0.15) 100%)",
                ),
                (
                    "institucional",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(196, 30, 58, 0.15) 100%)",
                ),
                (
                    "estudiantes",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(234, 88, 12, 0.15) 100%)",
                ),
                (
                    "tutoriales",
                    "linear-gradient(180deg, transparent 60%, "
                    "rgba(8, 145, 178, 0.15) 100%)",
                ),
                "transparent",
            ),
            z_index="2",
            pointer_events="none",
        ),
        # Contenedor
        position="relative",
        width="100%",
        height=ALTURA_IMAGEN_CARD,
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        background=COLOR_FONDO_CARTA,
    )


# ======================================================================
# CTA "Leer artículo"
# ======================================================================


def _cta_leer_articulo() -> rx.Component:
    """
    CTA "Leer artículo" con flecha animada en hover.

    La flecha lleva la clase `arrow-leer` que la card padre anima
    en hover (`& .arrow-leer`).
    """
    return rx.flex(
        rx.text("Leer artículo", as_="span", font_weight="700"),
        rx.icon(
            "arrow-right",
            size=14,
            class_name="arrow-leer",
            transition="transform 0.2s",
        ),
        align="center",
        gap="0.375rem",
        color=AZUL_MARINO_NEON,
        font_size="0.8125rem",
        margin_top="0.5rem",
        transition="all 0.2s",
    )


# ======================================================================
# Card individual de post
# ======================================================================


def card_post(post: Post) -> rx.Component:
    """
    Card individual de post que enlaza a la página de detalle.

    Estilo Neon.com:
    - Imagen con zoom sutil en hover.
    - Borde de acento en hover.
    - **Sin translateY** (solo borde).
    - **Sin glow**.
    - CTA "Leer artículo" con flecha animada.

    Args:
        post: `Post` (TypedDict). Tipado estricto.
    """
    card = rx.box(
        rx.vstack(
            _imagen_post(post),
            badge_categoria(post["categoria"]),
            rx.heading(
                post["titulo"],
                as_="h3",
                font_size="1.0625rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
            ),
            rx.text(
                post["extracto"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
            ),
            meta_info_post(post),
            _cta_leer_articulo(),
            align="start",
            spacing="2",
            width="100%",
            height="100%",
        ),
        padding="1.25rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        cursor="pointer",
        _hover={
            "border_color": AZUL_MARINO_NEON,
            "& .arrow-leer": {"transform": "translateX(4px)"},
        },
        class_name="card-post",
    )

    return rx.link(
        card,
        href=f"/blog/{post['id']}",
        text_decoration="none",
        width="100%",
        height="100%",
        display="block",
    )


# ======================================================================
# Grid de posts
# ======================================================================


def grid_posts() -> rx.Component:
    """Grid responsive con los posts paginados."""
    return rx.grid(
        rx.foreach(
            EstadoBlog.posts_paginados,
            card_post,
        ),
        columns=rx.breakpoints(initial="1", sm="2", lg="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Estado vacío
# ======================================================================


def estado_vacio() -> rx.Component:
    """
    Estado vacío cuando los filtros no devuelven resultados.

    Delega en `componentes.base.estado_vacio`.
    """
    return _estado_vacio_unificado(
        titulo="No hay artículos con esos filtros",
        mensaje=(
            "Prueba ajustando la búsqueda o seleccionando otra "
            "categoría."
        ),
        icono="search-x",
        tamano_icono=48,
        boton_accion_etiqueta="Limpiar filtros",
        boton_accion_icono="rotate-ccw",
        boton_accion_on_click=EstadoBlog.limpiar_filtros,
        boton_accion_color_scheme="indigo",
    )


# ======================================================================
# Botón "Cargar más"
# ======================================================================


def boton_cargar_mas() -> rx.Component:
    """
    Botón 'Cargar más' (solo se muestra si hay más posts).

    Estilo Neon.com:
    - Botón outline con indigo (no crimson).
    - Hover sutil (solo cambio de borde).
    """
    return rx.cond(
        EstadoBlog.hay_mas_posts,
        rx.flex(
            rx.button(
                rx.icon("plus", size=16),
                rx.text(
                    "Cargar más artículos",
                    as_="span",
                    font_weight="700",
                ),
                on_click=EstadoBlog.cargar_mas_posts,
                size="3",
                variant="outline",
                color_scheme="indigo",
                cursor="pointer",
                transition="all 0.2s",
            ),
            justify="center",
            width="100%",
            margin_top="2rem",
        ),
        rx.fragment(),
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "boton_cargar_mas",
    "card_post",
    "estado_vacio",
    "grid_posts",
]