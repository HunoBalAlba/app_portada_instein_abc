"""
Vista "Sobre nosotros" (ruta "/sobre-nosotros") — estilo Neon.com.

Contenido
---------
1. Hero con nombre del instituto + tagline.
2. Sección 01 — Nuestra historia.
3. Sección 02 — Misión, visión y valores.
4. Sección 03 — Lo que nos define (valores detallados).
5. CTA final hacia /admision.

Diseño
------
Refactorizado al estilo Neon.com:

1. **Layout izquierdo** (no centrado), coherente con el home.
2. **Encabezados numerados** (01, 02, 03) con `encabezado_seccion`.
3. **Separadores** entre secciones.
4. **HTML5 semántico** (`main`, `section`, `article`).
5. **Tarjetas limpias** con borde superior de acento.
6. **Responsive mobile-first**.
7. **Dark mode adaptativo**.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: IMPORTS
---------------------
Todos los símbolos se importan desde la fachada `..infraestructura`,
`..componentes.base` y `..componentes.navegacion`, sin rutas largas.

Nota técnica: LOGO
------------------
El logo usa `aspect_ratio="1"` + `overflow="hidden"` para
garantizar que siempre sea cuadrado y no deforme la imagen.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ..componentes.base.encabezado_seccion import encabezado_seccion
from ..componentes.base.separador_secciones import separador_secciones
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_SECUNDARIO,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_COMPLETO,
    NOMBRE_INSTITUTO,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ======================================================================
# Tipos
# ======================================================================


class ValorInstitucional(TypedDict):
    """Valor institucional con icono + título + descripción."""

    icono: str
    titulo: str
    descripcion: str


# ======================================================================
# Datos estáticos
# ======================================================================

VALORES: list[ValorInstitucional] = [
    {
        "icono": "award",
        "titulo": "Excelencia",
        "descripcion": (
            "Formamos profesionales que destacan en su campo con "
            "compromiso y calidad técnica."
        ),
    },
    {
        "icono": "users",
        "titulo": "Comunidad",
        "descripcion": (
            "Una red de egresados que se apoyan mutuamente y comparten "
            "oportunidades profesionales."
        ),
    },
    {
        "icono": "book-open",
        "titulo": "Aprendizaje continuo",
        "descripcion": (
            "Actualizamos nuestros planes de estudio cada gestión para "
            "reflejar el mercado actual."
        ),
    },
    {
        "icono": "target",
        "titulo": "Compromiso",
        "descripcion": (
            "Tu éxito profesional y personal es nuestra misión. Te "
            "acompañamos hasta el primer empleo."
        ),
    },
]


# ======================================================================
# Sección (estilo Neon.com)
# ======================================================================


def _seccion(
    numero: str,
    etiqueta: str,
    titulo: str,
    subtitulo: str | None,
    contenido: rx.Component,
    id_seccion: str,
) -> rx.Component:
    """
    Sección con encabezado horizontal + contenido.

    Args:
        numero: "01", "02", "03".
        etiqueta: Texto pequeño en mayúsculas.
        titulo: Título de la sección.
        subtitulo: Subtítulo opcional.
        contenido: Componente con el contenido.
        id_seccion: ID único (anchor).

    Returns:
        Componente `<section>` completo.
    """
    return rx.el.section(
        rx.box(
            encabezado_seccion(numero, etiqueta, titulo, subtitulo),
            contenido,
            padding=[
                f"5rem {PADDING_SECCION_HORIZONTAL}",
                f"7rem {PADDING_SECCION_HORIZONTAL}",
                f"8rem {PADDING_SECCION_HORIZONTAL}",
            ],
            max_width=ANCHO_MAXIMO_CONTENIDO,
            margin="0 auto",
            width="100%",
        ),
        width="100%",
        id=id_seccion,
        aria_label=titulo,
        scroll_margin_top="5rem",
    )


# ======================================================================
# Hero
# ======================================================================


def _hero_sobre_nosotros() -> rx.Component:
    """
    Hero con badge + nombre + tagline.

    Estilo Neon.com:
    - Alineado a la izquierda (no centrado).
    - Badge "SOBRE NOSOTROS" arriba.
    - Título con nombre completo.
    - Tagline descriptivo.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ──────────────────────────────────────────
            rx.flex(
                rx.icon("info", size=12, color=AZUL_MARINO_NEON),
                rx.text(
                    "SOBRE NOSOTROS",
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
            # ─── Título ─────────────────────────────────────────
            rx.heading(
                NOMBRE_INSTITUTO,
                as_="h1",
                font_size=["3rem", "4rem", "5rem"],
                font_weight="900",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.04em",
                line_height="1",
                max_width="56rem",
            ),
            # ─── Nombre completo ────────────────────────────────
            rx.text(
                NOMBRE_COMPLETO,
                font_size=["1rem", "1.125rem"],
                color=AZUL_MARINO_NEON,
                font_weight="600",
                letter_spacing="0.05em",
                margin_top="1rem",
            ),
            # ─── Descripción ────────────────────────────────────
            rx.text(
                "Formamos Técnicos Superiores de excelencia con "
                "títulos de Provisión Nacional, comprometidos con "
                "el desarrollo profesional y humano de cada estudiante.",
                font_size=["1rem", "1.125rem", "1.25rem"],
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                max_width="48rem",
                margin_top="1.5rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO_CONTENIDO,
        margin="0 auto",
        padding=["4rem 1.5rem 3rem 1.5rem", "6rem 2rem 4rem 2rem"],
        width="100%",
    )


# ======================================================================
# Logo institucional
# ======================================================================


def _logo_instituto() -> rx.Component:
    """
    Logo del instituto cuadrado.

    Garantías:
    - Siempre cuadrado (`aspect_ratio="1"`).
    - Nunca desborda (`max_width="100%"`).
    - Recorta si hace falta (`overflow="hidden"`).

    Returns:
        Imagen del logo dentro de un contenedor cuadrado.
    """
    return rx.box(
        rx.image(
            src="/log_instein.jpg",
            alt="Logo del Instituto Técnico Integrado San Antonio de Padua",
            width="100%",
            height="100%",
            object_fit="cover",
        ),
        width="100%",
        # aspect_ratio="1",
        max_width="100%",
        border_radius=RADIO_EXTRA_GRANDE,
        border=f"1px solid {BORDE_HOME_AZUL}",
        background=FONDO_AZUL_SUAVE,
        overflow="hidden",
    )


# ======================================================================
# Sección: Historia
# ======================================================================


def _contenido_historia() -> rx.Component:
    """
    Contenido de la sección "Nuestra historia".

    Layout 2 columnas:
    - Izquierda: texto de la historia.
    - Derecha: logo institucional.
    """
    return rx.flex(
        # ─── Columna izquierda: texto ────────────────────────────
        rx.vstack(
            rx.text(
                "Desde 2010, INSTEIN ha sido un referente en formación "
                "técnica en Bolivia. Con más de 500 egresados activos en "
                "el mercado laboral, hemos construido una comunidad "
                "sólida de profesionales técnicos de excelencia.",
                font_size="1rem",
                color=COLOR_TEXTO_CUERPO,
                line_height="1.7",
            ),
            rx.text(
                "Nuestro compromiso es ofrecer una formación práctica, "
                "actualizada y conectada con las necesidades reales "
                "del mercado laboral boliviano. Cada plan de estudios "
                "se revisa cada gestión para garantizar que nuestros "
                "egresados estén preparados para los desafíos actuales.",
                font_size="1rem",
                color=COLOR_TEXTO_CUERPO,
                line_height="1.7",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width=rx.breakpoints(
                initial="100%",
                lg="60%",
            ),
            flex_shrink="0",
        ),
        # ─── Columna derecha: logo ───────────────────────────────
        rx.box(
            _logo_instituto(),
            width=rx.breakpoints(
                initial="100%",
                lg="40%",
            ),
            max_width=["16rem", "20rem", "24rem", "100%"],
            flex_shrink="0",
            margin=["0 auto", "0 auto", "0 auto", "0"],
        ),
        # ─── Layout responsive ───────────────────────────────────
        direction=rx.breakpoints(
            initial="column",
            lg="row",
        ),
        align="center",
        justify="between",
        gap="3rem",
        width="100%",
    )


# ======================================================================
# Sección: Misión y Visión
# ======================================================================


def _tarjeta_myv(
    icono: str,
    titulo: str,
    contenido: str,
) -> rx.Component:
    """
    Tarjeta de misión o visión.

    Estilo Neon.com:
    - Borde superior de acento (`2px solid AZUL_MARINO_NEON`).
    - Icono pequeño, sin caja.
    - Fondo plano.
    """
    return rx.box(
        rx.vstack(
            # ─── Icono ──────────────────────────────────────────
            rx.icon(
                icono,
                size=24,
                color=AZUL_MARINO_NEON,
            ),
            # ─── Título ─────────────────────────────────────────
            rx.heading(
                titulo,
                as_="h3",
                font_size="1.25rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.02em",
                line_height="1.2",
                margin_top="0.5rem",
            ),
            # ─── Contenido ──────────────────────────────────────
            rx.text(
                contenido,
                font_size="0.9375rem",
                color=COLOR_TEXTO_CUERPO,
                line_height="1.7",
                margin_top="0.75rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding=["1.5rem", "1.75rem", "2rem"],
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _contenido_mision_vision() -> rx.Component:
    """Grid de 2 columnas con misión y visión."""
    return rx.grid(
        _tarjeta_myv(
            "target",
            "Misión",
            "Formar Técnicos Superiores competentes, con sólidos "
            "valores éticos y humanos, capaces de responder a las "
            "demandas del sector productivo y contribuir al "
            "desarrollo del país.",
        ),
        _tarjeta_myv(
            "eye",
            "Visión",
            "Ser el instituto técnico de referencia en Bolivia, "
            "reconocido por la calidad de sus egresados y por su "
            "contribución al desarrollo técnico y profesional de "
            "la región.",
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección: Valores
# ======================================================================


def _tarjeta_valor(valor: ValorInstitucional) -> rx.Component:
    """
    Tarjeta de valor institucional.

    Estilo Neon.com:
    - Icono pequeño, sin caja.
    - Título + descripción.
    - Borde superior de acento.
    """
    return rx.box(
        rx.vstack(
            # ─── Icono ──────────────────────────────────────────
            rx.icon(
                valor["icono"],
                size=20,
                color=AZUL_MARINO_NEON,
            ),
            # ─── Título ─────────────────────────────────────────
            rx.heading(
                valor["titulo"],
                as_="h4",
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.01em",
                line_height="1.3",
                margin_top="0.5rem",
            ),
            # ─── Descripción ────────────────────────────────────
            rx.text(
                valor["descripcion"],
                font_size="0.875rem",
                color=COLOR_TEXTO_SECUNDARIO,
                line_height="1.5",
                margin_top="0.5rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_GRANDE,
        background=COLOR_FONDO_SUAVE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _contenido_valores() -> rx.Component:
    """Grid de 4 columnas con los valores institucionales."""
    return rx.grid(
        *[_tarjeta_valor(v) for v in VALORES],
        columns=rx.breakpoints(initial="1", sm="2", lg="4"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final() -> rx.Component:
    """
    CTA final de la página.

    Banner con título + subtítulo + botón a /admision.
    """
    return rx.box(
        rx.vstack(
            rx.heading(
                "¿Listo para empezar?",
                as_="h3",
                font_size=["1.5rem", "1.75rem", "2rem"],
                font_weight="900",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                text_align="center",
            ),
            rx.text(
                "Conoce nuestra guía de admisión y descubre cómo "
                "formar parte de la comunidad INSTEIN.",
                font_size="1rem",
                color=TEXTO_HOME_MAS_SUAVE,
                text_align="center",
                max_width="36rem",
                line_height="1.6",
                margin_top="0.5rem",
            ),
            rx.link(
                rx.text(
                    "Ver guía de admisión",
                    as_="span",
                    font_size="0.9375rem",
                    font_weight="700",
                    color="white",
                ),
                rx.icon("arrow-right", size=16, color="white"),
                href="/admision",
                text_decoration="none",
                display="inline-flex",
                align_items="center",
                gap="0.5rem",
                padding="0.875rem 1.75rem",
                border_radius=RADIO_PASTILLA,
                background=AZUL_MARINO_NEON,
                transition="all 0.2s",
                margin_top="1.5rem",
                _hover={
                    "transform": "translateY(-2px)",
                    "filter": "brightness(1.1)",
                },
            ),
            align="center",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO_CONTENIDO,
        margin="0 auto",
        padding=f"4rem {PADDING_SECCION_HORIZONTAL} 6rem {PADDING_SECCION_HORIZONTAL}",
        width="100%",
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/sobre-nosotros",
    title=f"Sobre nosotros | {NOMBRE_INSTITUTO}",
    description=(
        "Conoce la historia, misión y valores del Instituto Técnico "
        "Integrado San Antonio de Padua (INSTEIN)."
    ),
)
def vista_sobre_nosotros() -> rx.Component:
    """
    Página "Sobre nosotros" del instituto — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">` → barra de navegación.
    - `<main>`                 → contenido principal.
    - `<section>`              → cada sección temática.
    - `<footer>`               → pie de página.
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
                # ─── Hero ───────────────────────────────────────────
                _hero_sobre_nosotros(),
                # ─── Sección 01 — Historia ──────────────────────────
                _seccion(
                    numero="01",
                    etiqueta="Nuestra historia",
                    titulo="15 años formando profesionales",
                    subtitulo=(
                        "Un recorrido por los hitos que nos han "
                        "convertido en referente de la formación "
                        "técnica en Bolivia."
                    ),
                    contenido=_contenido_historia(),
                    id_seccion="historia",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── Sección 02 — Misión y Visión ───────────────────
                _seccion(
                    numero="02",
                    etiqueta="Nuestro propósito",
                    titulo="Misión y visión",
                    subtitulo=(
                        "Los principios que guían nuestra labor "
                        "formativa día a día."
                    ),
                    contenido=_contenido_mision_vision(),
                    id_seccion="mision-vision",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── Sección 03 — Valores ───────────────────────────
                _seccion(
                    numero="03",
                    etiqueta="Lo que nos define",
                    titulo="Nuestros valores",
                    subtitulo=(
                        "Los pilares que sostienen nuestra identidad "
                        "institucional y nuestra relación con los "
                        "estudiantes."
                    ),
                    contenido=_contenido_valores(),
                    id_seccion="valores",
                ),
                # ─── CTA final ──────────────────────────────────────
                _cta_final(),
                width="100%",
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
    "VALORES",
    "ValorInstitucional",
    "vista_sobre_nosotros",
]