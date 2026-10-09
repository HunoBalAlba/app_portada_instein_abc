

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ..componentes.base import (
    enlace_navegacion,
    separador_secciones,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "72rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ======================================================================
# Tipos
# ======================================================================


class EnlaceSugerido(TypedDict):
    """Enlace sugerido en la página 404."""

    icono: str
    etiqueta: str
    ruta: str
    origen_excluido: str


# ======================================================================
# Estado de la vista 404
# ======================================================================


class Estado404(rx.State):
    """Estado de la vista 404."""

    @rx.var
    def origen(self) -> str:
        """
        Origen del error, leído desde el query param `origen`.

        Returns:
            "blog", "carrera" o "" (genérico).
        """
        return self.router.page.params.get("origen", "")

    @rx.var
    def mensaje_contextual(self) -> str:
        """
        Mensaje descriptivo según el origen.

        Returns:
            Mensaje contextualizado.
        """
        origen = self.router.page.params.get("origen", "")
        if origen == "blog":
            return (
                "El artículo que buscas no existe o fue movido. "
                "Puedes volver al blog o explorar otras secciones."
            )
        if origen == "carrera":
            return (
                "La carrera que buscas no existe o fue movida. "
                "Puedes ver todas las carreras disponibles o volver "
                "al inicio."
            )
        return (
            "Lo sentimos, el recurso que buscas no existe o fue "
            "movido. Puedes volver al inicio o explorar nuestro blog."
        )


# ======================================================================
# Hero con el número 404
# ======================================================================


def _hero_404() -> rx.Component:
    """
    Hero de la página 404.

    Estilo Neon.com:
    - Layout izquierdo (no centrado).
    - Badge "ERROR 404" arriba.
    - Número 404 dominante con acento azul marino.
    - Mensaje contextual.
    - CTAs duales (volver al inicio + volver al navegador).
    """
    return rx.vstack(
        # ─── Badge ─────────────────────────────────────────────
        rx.flex(
            rx.icon("alert-circle", size=12, color=AZUL_MARINO_NEON),
            rx.text(
                "ERROR 404",
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
        # ─── Número 404 dominante ──────────────────────────────
        rx.text(
            "404",
            font_size=["6rem", "8rem", "10rem"],
            font_weight="900",
            line_height="0.9",
            letter_spacing="-0.06em",
            color=AZUL_MARINO_NEON,
            font_family="JetBrains Mono",
            aria_hidden="true",
            margin_bottom="2rem",
        ),
        # ─── Título con énfasis bicolor ────────────────────────
        rx.heading(
            rx.text.span("Página "),
            rx.text.span(
                "no encontrada",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            as_="h1",
            font_size=["1.75rem", "2rem", "2.25rem"],
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
            letter_spacing="-0.03em",
            line_height="1.15",
            max_width="48rem",
        ),
        # ─── Descripción ───────────────────────────────────────
        rx.text(
            Estado404.mensaje_contextual,
            font_size=["1rem", "1.0625rem"],
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            max_width="42rem",
            margin_top="1rem",
        ),
        # ─── CTAs ──────────────────────────────────────────────
        _ctas_adaptados_por_origen(),
        align="start",
        spacing="0",
        width="100%",
    )


# ======================================================================
# CTAs
# ======================================================================


def _cta_primario() -> rx.Component:
    """
    CTA primario "Volver al inicio".

    Estilo Neon.com:
    - Fondo azul marino.
    - Sin glow.
    - Hover sutil.
    """
    return enlace_navegacion(
        "/",
        rx.text("Volver al inicio", as_="span", font_weight="600"),
        rx.icon("home", size=16, color="white"),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background=AZUL_MARINO_NEON,
        color="white",
        padding="0.875rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        transition="all 0.2s",
        text_decoration="none",
        width="fit-content",
        _hover={
            "filter": "brightness(1.1)",
        },
    )


def _cta_volver_navegador() -> rx.Component:
    """
    CTA secundario "Volver".

    Ejecuta `history.back()` en el navegador para volver a la
    página anterior.
    """
    return rx.box(
        rx.text("Volver", as_="span", font_weight="600"),
        rx.icon("arrow-left", size=16, color=TEXTO_HOME_PRINCIPAL),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        padding="0.875rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        cursor="pointer",
        width="fit-content",
        on_click=rx.call_script("history.back()"),
        _hover={
            "border_color": BORDE_HOME_AZUL,
            "background": rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.05)",
                dark="rgba(59, 91, 219, 0.1)",
            ),
        },
    )


def _cta_secundario_blog() -> rx.Component:
    """CTA secundario "Ver blog"."""
    return enlace_navegacion(
        "/blog",
        rx.text("Ver blog", as_="span", font_weight="600"),
        rx.icon("newspaper", size=16, color=TEXTO_HOME_PRINCIPAL),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        padding="0.875rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        text_decoration="none",
        width="fit-content",
        _hover={
            "border_color": BORDE_HOME_AZUL,
            "background": rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.05)",
                dark="rgba(59, 91, 219, 0.1)",
            ),
        },
    )


def _cta_secundario_carreras() -> rx.Component:
    """CTA secundario "Ver carreras"."""
    return enlace_navegacion(
        "/carreras",
        rx.text("Ver carreras", as_="span", font_weight="600"),
        rx.icon("graduation-cap", size=16, color=TEXTO_HOME_PRINCIPAL),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        padding="0.875rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        text_decoration="none",
        width="fit-content",
        _hover={
            "border_color": BORDE_HOME_AZUL,
            "background": rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.05)",
                dark="rgba(59, 91, 219, 0.1)",
            ),
        },
    )


def _ctas_adaptados_por_origen() -> rx.Component:
    """
    Fila de CTAs.

    Estructura:
    - CTA primario: "Volver al inicio" (siempre).
    - CTA secundario: "Volver" (history.back).
    - CTA terciario: según origen ("Ver blog" / "Ver carreras").

    En móvil se apilan.
    """
    return rx.flex(
        _cta_primario(),
        _cta_volver_navegador(),
        rx.cond(
            Estado404.origen == "carrera",
            _cta_secundario_carreras(),
            rx.cond(
                Estado404.origen == "blog",
                _cta_secundario_blog(),
                rx.fragment(),
            ),
        ),
        gap="0.75rem",
        direction=rx.breakpoints(initial="column", sm="row"),
        align="start",
        justify="start",
        flex_wrap="wrap",
        margin_top="2.5rem",
        width="100%",
    )


# ======================================================================
# Enlaces sugeridos
# ======================================================================

ENLACES_404: list[EnlaceSugerido] = [
    {
        "icono": "graduation-cap",
        "etiqueta": "Carreras",
        "ruta": "/carreras",
        "origen_excluido": "carrera",
    },
    {
        "icono": "calendar",
        "etiqueta": "Calendario",
        "ruta": "/calendario",
        "origen_excluido": "",
    },
    {
        "icono": "book-open",
        "etiqueta": "Admisión",
        "ruta": "/admision",
        "origen_excluido": "",
    },
    {
        "icono": "trophy",
        "etiqueta": "Becas",
        "ruta": "/becas",
        "origen_excluido": "",
    },
    {
        "icono": "map-pin",
        "etiqueta": "Contacto",
        "ruta": "/contacto",
        "origen_excluido": "",
    },
    {
        "icono": "newspaper",
        "etiqueta": "Blog",
        "ruta": "/blog",
        "origen_excluido": "blog",
    },
]


def _enlace_sugerido(enlace: EnlaceSugerido) -> rx.Component:
    """
    Enlace individual del bloque "Quizá buscabas".

    Args:
        enlace: `EnlaceSugerido` con `icono`, `etiqueta`, `ruta`.

    Returns:
        Enlace estilizado como chip.
    """
    return enlace_navegacion(
        enlace["ruta"],
        rx.icon(enlace["icono"], size=14, color=AZUL_MARINO_NEON),
        rx.text(
            enlace["etiqueta"],
            font_size="0.875rem",
            font_weight="600",
            color=TEXTO_HOME_PRINCIPAL,
        ),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background="transparent",
        border=f"1px solid {BORDE_HOME_SUAVE}",
        text_decoration="none",
        transition="all 0.2s",
        width="fit-content",
        _hover={
            "border_color": BORDE_HOME_AZUL,
            "background": rx.color_mode_cond(
                light="rgba(59, 91, 219, 0.05)",
                dark="rgba(59, 91, 219, 0.1)",
            ),
        },
    )


def _enlaces_sugeridos(origen: str) -> rx.Component:
    """
    Bloque con enlaces rápidos a las secciones más visitadas.

    Filtra el enlace del origen del error para no sugerir la misma
    sección que acaba de fallar.

    Args:
        origen: "blog", "carrera" o "".
    """
    enlaces_filtrados = [
        item for item in ENLACES_404
        if item["origen_excluido"] != origen
    ]

    return rx.box(
        rx.vstack(
            rx.text(
                "Quizá buscabas",
                font_size="0.6875rem",
                font_weight="700",
                color=TEXTO_HOME_MAS_SUAVE,
                letter_spacing="0.15em",
                text_transform="uppercase",
                margin_bottom="1rem",
            ),
            rx.flex(
                *[_enlace_sugerido(e) for e in enlaces_filtrados],
                gap="0.5rem",
                flex_wrap="wrap",
                align="start",
                width="100%",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        width="100%",
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/404",
    title=f"Página no encontrada | {NOMBRE_INSTITUTO}",
    description=(
        "La página que buscas no existe o fue movida."
    ),
)
def vista_404() -> rx.Component:
    """
    Página de error 404 — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header>`  → barra de navegación.
    - `<main>`    → contenido principal.
    - `<footer>`  → pie de página.

    Se activa cuando:
    - El usuario navega a `/404` directamente.
    - Un `on_load` redirige aquí con `?origen=blog` o
      `?origen=carrera`.
    """
    return rx.box(
        rx.vstack(
            # =============================================================
            # 1. HEADER
            # =============================================================
            rx.box(
                barra_navegacion_superior(),
                width="100%",
                role="banner",
                aria_label="Navegación principal",
            ),
            # =============================================================
            # 2. MAIN
            # =============================================================
            rx.el.main(
                rx.box(
                    rx.vstack(
                        # ─── Hero 404 ───────────────────────────
                        _hero_404(),
                        # ─── Separador ──────────────────────────
                        rx.box(
                            separador_secciones(
                                ancho_maximo=ANCHO_MAXIMO_CONTENIDO,
                            ),
                            padding_top="3rem",
                            padding_bottom="3rem",
                            width="100%",
                        ),
                        # ─── Enlaces sugeridos ──────────────────
                        rx.cond(
                            Estado404.origen == "carrera",
                            _enlaces_sugeridos("carrera"),
                            rx.cond(
                                Estado404.origen == "blog",
                                _enlaces_sugeridos("blog"),
                                _enlaces_sugeridos(""),
                            ),
                        ),
                        spacing="0",
                        width="100%",
                        align="start",
                    ),
                    max_width=ANCHO_MAXIMO_CONTENIDO,
                    margin="0 auto",
                    padding=[
                        f"4rem {PADDING_SECCION_HORIZONTAL} 6rem {PADDING_SECCION_HORIZONTAL}",
                        f"6rem {PADDING_SECCION_HORIZONTAL} 8rem {PADDING_SECCION_HORIZONTAL}",
                    ],
                    width="100%",
                ),
                width="100%",
                aria_label="Contenido principal",
            ),
            # =============================================================
            # 3. FOOTER
            # =============================================================
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

__all__ = [
    "ENLACES_404",
    "EnlaceSugerido",
    "Estado404",
    "vista_404",
]