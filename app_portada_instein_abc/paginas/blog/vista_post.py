

from __future__ import annotations

import reflex as rx

from ...componentes.base import enlace_navegacion
from ...componentes.blog import meta_info_post
from ...componentes.blog.helpers_categoria import (
    badge_categoria,
    fondo_categoria,
)
from ...componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ...dominio import (
    EstadoBlog,
    Post,
)
from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    PADDING_LATERAL,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_LECTURA: str = "65ch"
ANCHO_CONTENIDO: str = "64rem"


# ======================================================================
# Hero editorial del post
# ======================================================================


def _hero_post() -> rx.Component:
    """Hero del artículo: imagen de fondo + badge + título + meta."""
    post = EstadoBlog.post_seleccionado

    return rx.box(
        # CAPA 1: Fondo de fallback
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
            src=f"/blog/{post['imagen']}",
            alt=post["titulo"],
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
            z_index="1",
        ),
        # CAPA 3: Overlay
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=(
                "linear-gradient(180deg, "
                "rgba(0,0,0,0.35) 0%, "
                "rgba(0,0,0,0.15) 40%, "
                "rgba(0,0,0,0.85) 100%)"
            ),
            z_index="2",
            pointer_events="none",
        ),
        # CAPA 4: Contenido
        rx.vstack(
            rx.vstack(
                rx.box(
                    badge_categoria(post["categoria"]),
                    background="rgba(255,255,255,0.92)",
                    backdrop_filter="blur(8px)",
                    border_radius=RADIO_PASTILLA,
                    padding="0.125rem",
                    width="fit-content",
                ),
                rx.heading(
                    post["titulo"],
                    as_="h1",
                    font_size=["1.75rem", "2.5rem", "3rem"],
                    font_weight="700",
                    color="white",
                    line_height="1.15",
                    letter_spacing="-0.02em",
                    text_shadow="0 2px 16px rgba(0,0,0,0.6)",
                    max_width="48rem",
                ),
                rx.box(
                    meta_info_post(post),
                    css={
                        "& *": {
                            "color": "rgba(255,255,255,0.85) !important"
                        },
                    },
                ),
                spacing="4",
                align="start",
                width="100%",
                max_width=ANCHO_CONTENIDO,
                margin="0 auto",
            ),
            justify="end",
            align="start",
            width="100%",
            padding=[
                "6rem 1.25rem 2rem 1.25rem",
                "8rem 1.5rem 2.5rem 1.5rem",
                "10rem 1.5rem 3rem 1.5rem",
            ],
            min_height=["20rem", "24rem", "28rem"],
            position="relative",
            z_index="3",
        ),
        position="relative",
        width="100%",
        overflow="hidden",
    )


# ======================================================================
# Botón "Volver al blog"
# ======================================================================


def _boton_volver() -> rx.Component:
    """Botón para volver a la lista de posts."""
    return enlace_navegacion(
        "/blog",
        rx.icon("arrow-left", size=16),
        rx.text("Volver al blog", as_="span", font_weight="600"),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        padding="0.5rem 1rem",
        border_radius=RADIO_MEDIO,
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        border=f"1px solid {BORDE_HOME_MEDIO}",
        font_size="0.875rem",
        text_decoration="none",
        transition="all 0.2s",
        width="fit-content",
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


# ======================================================================
# Cuerpo del artículo
# ======================================================================


def _cuerpo_post() -> rx.Component:
    """Cuerpo del artículo con lead + separador + contenido."""
    post = EstadoBlog.post_seleccionado

    return rx.vstack(
        rx.box(
            rx.text(
                post["extracto"],
                font_size=["1rem", "1.0625rem", "1.125rem"],
                font_weight="500",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.75",
                font_style="italic",
            ),
            padding_left="1.25rem",
            border_left=f"4px solid {AZUL_MARINO_NEON}",
            width="100%",
        ),
        rx.box(
            height="1px",
            width="100%",
            background=COLOR_DIVISOR,
            margin_y="1.5rem",
        ),
        rx.box(
            rx.text(
                post["contenido"],
                font_size=["1rem", "1.0625rem", "1.125rem"],
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.85",
                white_space="pre-line",
                max_width=ANCHO_LECTURA,
            ),
            width="100%",
        ),
        spacing="0",
        align="start",
        width="100%",
    )


# ======================================================================
# Navegación entre posts
# ======================================================================


def _tarjeta_navegacion_post(
    post: Post | rx.Var,
    direccion: str,
) -> rx.Component:
    """Tarjeta de navegación a un post adyacente."""
    es_anterior = direccion == "anterior"

    icono = "arrow-left" if es_anterior else "arrow-right"
    etiqueta = "Anterior" if es_anterior else "Siguiente"
    alineacion_texto = "start" if es_anterior else "end"
    justify_contenido = "start" if es_anterior else "end"

    bloque_texto = rx.vstack(
        rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        rx.text(
            post["titulo"],
            font_size="0.875rem",
            font_weight="600",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.3",
            max_width="18rem",
        ),
        spacing="0",
        align=alineacion_texto,
        flex="1",
        min_width="0",
    )

    icono_componente = rx.icon(
        icono, size=16, color=TEXTO_HOME_MAS_SUAVE
    )

    if es_anterior:
        contenido_interno = [icono_componente, bloque_texto]
    else:
        contenido_interno = [bloque_texto, icono_componente]

    return enlace_navegacion(
        f"/blog/{post['id']}",
        *contenido_interno,
        display="flex",
        align_items="center",
        gap="0.75rem",
        padding="1rem",
        border_radius=RADIO_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        text_decoration="none",
        flex="1",
        justify=justify_contenido,
        transition="all 0.2s",
        height="100%",
        min_width="0",
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


def _navegacion_posts() -> rx.Component:
    """
    Navegación al post anterior y siguiente.

    ⚠️ Usamos los flags `hay_post_anterior` y `hay_post_siguiente`.
    """
    hay_anterior = EstadoBlog.hay_post_anterior
    hay_siguiente = EstadoBlog.hay_post_siguiente

    return rx.cond(
        hay_anterior | hay_siguiente,
        rx.box(
            rx.text(
                "Continúa leyendo",
                font_size="0.75rem",
                font_weight="700",
                color=TEXTO_HOME_MAS_SUAVE,
                text_transform="uppercase",
                letter_spacing="0.075em",
                margin_bottom="1rem",
            ),
            rx.flex(
                rx.cond(
                    hay_anterior,
                    _tarjeta_navegacion_post(
                        EstadoBlog.post_anterior,
                        "anterior",
                    ),
                    rx.fragment(),
                ),
                rx.cond(
                    hay_siguiente,
                    _tarjeta_navegacion_post(
                        EstadoBlog.post_siguiente,
                        "siguiente",
                    ),
                    rx.fragment(),
                ),
                gap="1rem",
                width="100%",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                align="stretch",
            ),
            width="100%",
            margin_top="3rem",
        ),
        rx.fragment(),
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final_post() -> rx.Component:
    """
    Bloque CTA al final del artículo.

    Estilo Neon.com:
    - Sin glow.
    - Sin translateY.
    """
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Te resultó útil este artículo?",
                font_size="0.75rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.1em",
                text_transform="uppercase",
            ),
            rx.heading(
                "Hablemos de tu futuro profesional",
                as_="h2",
                font_size=["1.25rem", "1.5rem", "1.75rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                text_align="center",
                line_height="1.2",
            ),
            rx.text(
                "Nuestro equipo de admisiones está disponible para "
                "resolver tus dudas y ayudarte a elegir la carrera "
                "adecuada.",
                font_size="0.9375rem",
                color=TEXTO_HOME_MAS_SUAVE,
                text_align="center",
                max_width="36rem",
                line_height="1.6",
            ),
            rx.flex(
                enlace_navegacion(
                    "/contacto",
                    rx.icon("message-circle", size=18, color="white"),
                    rx.text("Consultar", as_="span", font_weight="700"),
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background=AZUL_MARINO_NEON,
                    color="white",
                    padding="0.875rem 1.75rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    transition="all 0.2s",
                    text_decoration="none",
                    _hover={"filter": "brightness(1.1)"},
                ),
                enlace_navegacion(
                    "/blog",
                    rx.icon("arrow-left", size=18),
                    rx.text(
                        "Ver más artículos",
                        as_="span",
                        font_weight="600",
                    ),
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background="transparent",
                    color=TEXTO_HOME_PRINCIPAL,
                    padding="0.875rem 1.75rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    border=f"1px solid {BORDE_HOME_MEDIO}",
                    transition="all 0.2s",
                    text_decoration="none",
                    _hover={
                        "border_color": AZUL_MARINO_NEON,
                    },
                ),
                gap="0.75rem",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                align="center",
                justify="center",
                margin_top="1.5rem",
                width="100%",
            ),
            align="center",
            spacing="3",
            width="100%",
        ),
        padding="2.5rem 1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background="transparent",
        border=f"1px solid {BORDE_HOME_AZUL}",
        width="100%",
        margin_top="3rem",
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/blog/[post_id]",
    title=f"Artículo | {NOMBRE_INSTITUTO}",
    on_load=EstadoBlog.redirigir_si_post_invalido,
)
def vista_post() -> rx.Component:
    """Página de detalle del artículo."""
    return rx.box(
        rx.vstack(
            rx.box(
                barra_navegacion_superior(),
                width="100%",
                role="banner",
                aria_label="Navegación principal",
            ),
            rx.el.main(
                _hero_post(),
                rx.box(
                    rx.vstack(
                        _boton_volver(),
                        _cuerpo_post(),
                        _navegacion_posts(),
                        _cta_final_post(),
                        spacing="6",
                        width="100%",
                        align="start",
                    ),
                    max_width=ANCHO_CONTENIDO,
                    margin="0 auto",
                    padding=f"2.5rem {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
                    width="100%",
                ),
                width="100%",
                aria_label="Artículo del blog",
            ),
            rx.box(
                pie_pagina_institucional(),
                width="100%",
                role="contentinfo",
                aria_label="Información del sitio",
            ),
            align="center",
            min_height="100vh",
            width="100%",
            spacing="0",
            background=FONDO_HOME,
        ),
        width="100%",
        background=FONDO_HOME,
        lang="es",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_post"]