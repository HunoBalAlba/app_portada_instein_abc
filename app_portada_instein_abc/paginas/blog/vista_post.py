"""
Vista de detalle de un post del blog
(ruta dinámica "/blog/[post_id]").

Reemplaza el antiguo `dialogos.py`. En vez de un modal, el post se
muestra en una página completa, con:

- Hero editorial con imagen de fondo + título + meta info.
- Cuerpo de lectura con tipografía optimizada (max_width ~65ch).
- Navegación al post anterior / siguiente (si existen).
- CTA al final hacia /contacto.
- Botón "Volver al blog".

Ventajas sobre el diálogo modal
-------------------------------
- URL compartible: `/blog/3` se puede enviar por WhatsApp.
- SEO: Google indexa cada post.
- Scroll natural: sin peleas con flexbox.
- Botón atrás del navegador funciona.
- Mejor lectura larga: patrón Medium/Substack/NYT.

Nota técnica: PATH PARAMS
-------------------------
`post_id` viene como string en `self.router.page.params["post_id"]`.
El State `EstadoBlog` lo resuelve con la var `post_seleccionado`.

Nota técnica: VALIDACIÓN DE RUTA
--------------------------------
El decorador `@rx.page` incluye
`on_load=EstadoBlog.redirigir_si_post_invalido`. Este evento se
ejecuta al cargar la página y redirige a `/404?origen=blog` si el
`post_id` no corresponde a ningún post real.

Nota técnica: FLAGS DE NAVEGACIÓN
---------------------------------
`EstadoBlog.post_anterior` y `EstadoBlog.post_siguiente` SIEMPRE
devuelven un `Post` válido (con fallback al destacado), así que
**no se pueden usar directamente en `rx.cond(...)`** porque siempre
evaluarían a True.

Para decidir si mostrar u ocultar las tarjetas de navegación, se usan
los flags booleanos `hay_post_anterior` y `hay_post_siguiente`:

    ❌ rx.cond(EstadoBlog.post_anterior, ...)    # siempre True
    ✅ rx.cond(EstadoBlog.hay_post_anterior, ...) # correcto
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base.primitivos import (
    enlace_navegacion,
)
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
    COLOR_ACENTO_FONDO,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
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

ANCHO_LECTURA: str = "65ch"
ANCHO_CONTENIDO: str = "64rem"


# ======================================================================
# Hero editorial del post
# ======================================================================


def _hero_post() -> rx.Component:
    """
    Hero del artículo: imagen de fondo con overlay + badge + título
    + meta info.
    """
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
                    box_shadow="0 4px 12px -2px rgba(0,0,0,0.15)",
                    width="fit-content",
                ),
                rx.heading(
                    post["titulo"],
                    size="8",
                    font_weight="900",
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
        background=COLOR_FONDO_CARTA,
        color=COLOR_TEXTO_PRINCIPAL,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        font_size="0.875rem",
        text_decoration="none",
        transition="all 0.2s",
        width="fit-content",
        _hover={
            "background": COLOR_FONDO_SUAVE,
            "border_color": AZUL_MARINO_NEON,
            "transform": "translateX(-2px)",
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
                color=COLOR_TEXTO_PRINCIPAL,
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
                color=COLOR_TEXTO_CUERPO,
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
    """
    Tarjeta de navegación a un post adyacente.

    Args:
        post: Var con el `Post` (post_anterior o post_siguiente).
        direccion: "anterior" o "siguiente".
    """
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
            color=COLOR_TEXTO_SECUNDARIO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        rx.text(
            post["titulo"],
            font_size="0.875rem",
            font_weight="600",
            color=COLOR_TEXTO_PRINCIPAL,
            line_height="1.3",
            max_width="18rem",
        ),
        spacing="0",
        align=alineacion_texto,
        flex="1",
        min_width="0",
    )

    icono_componente = rx.icon(
        icono, size=16, color=COLOR_TEXTO_SECUNDARIO
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
            "transform": "translateY(-2px)",
            "box_shadow": f"0 8px 20px -8px {AZUL_MARINO_NEON}",
        },
    )


def _navegacion_posts() -> rx.Component:
    """
    Navegación al post anterior y siguiente.

    ⚠️ Usamos los flags `hay_post_anterior` y `hay_post_siguiente`
    (bool), NO `post_anterior`/`post_siguiente` (que siempre son
    truthy por el fallback al destacado).
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
                color=COLOR_TEXTO_SECUNDARIO,
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
    """Bloque CTA al final del artículo."""
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
                size="6",
                font_weight="800",
                color=COLOR_TEXTO_PRINCIPAL,
                text_align="center",
                line_height="1.2",
            ),
            rx.text(
                "Nuestro equipo de admisiones está disponible para "
                "resolver tus dudas y ayudarte a elegir la carrera "
                "adecuada.",
                font_size="0.9375rem",
                color=COLOR_TEXTO_SECUNDARIO,
                text_align="center",
                max_width="36rem",
                line_height="1.6",
            ),
            rx.flex(
                enlace_navegacion(
                    "/contacto",
                    rx.icon("message-circle", size=18),
                    rx.text("Consultar", as_="span", font_weight="700"),
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background=AZUL_MARINO_NEON,
                    color="white",
                    padding="0.875rem 1.75rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    box_shadow=f"0 10px 25px -5px {AZUL_MARINO_NEON}",
                    transition="all 0.2s",
                    text_decoration="none",
                    _hover={
                        "transform": "translateY(-2px)",
                        "filter": "brightness(1.1)",
                    },
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
                    color=COLOR_TEXTO_PRINCIPAL,
                    padding="0.875rem 1.75rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    border=f"1px solid {COLOR_BORDE_SUAVE}",
                    transition="all 0.2s",
                    text_decoration="none",
                    _hover={
                        "transform": "translateY(-2px)",
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
        background=COLOR_ACENTO_FONDO,
        border=f"1px solid {AZUL_MARINO_NEON}",
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
    """
    Página de detalle del artículo.

    Estructura:
    1. Barra de navegación.
    2. Hero editorial con imagen + título + meta.
    3. Contenedor con:
       - Botón "Volver al blog".
       - Cuerpo del artículo.
       - Navegación al post anterior / siguiente.
       - CTA final hacia /contacto.
    4. Pie de página.

    El `on_load` (`redirigir_si_post_invalido`) redirige
    automáticamente a `/404?origen=blog` si el `post_id` de la URL
    no corresponde a ningún post real.
    """
    return rx.vstack(
        barra_navegacion_superior(),
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

__all__ = ["vista_post"]