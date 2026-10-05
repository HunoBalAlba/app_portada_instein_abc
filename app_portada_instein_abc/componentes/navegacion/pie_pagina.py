"""
Pie de página institucional — estilo Neon.com (reingeniería UX).

Filosofía
---------
El footer NO es una repetición del header. Es el **último punto de
contacto** con el usuario. Debe:

1. **Acceso rápido** a acciones clave (WhatsApp, ubicación, admisión).
2. **Captar leads** (newsletter con propuesta de valor).
3. **Navegación secundaria** (enlaces con iconos descriptivos).
4. **Cerrar con CTA** (empujar a la acción).

Estructura
----------
1. **Acceso rápido** (3 tarjetas: WhatsApp, Ubicación, Admisión).
2. **Newsletter + Enlaces** (2 columnas).
3. **Feedback discreto** ("¿Te resultó útil?").
4. **Barra inferior** (copyright + legales + redes).

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: `spacing` en `rx.grid` NO acepta unidades CSS
----------------------------------------------------------
`spacing` en `rx.grid` y `rx.flex` de Radix Themes es un prop
CERRADO que acepta solo:

- `"0"`, `"1"`, `"2"`, ..., `"9"` (valores discretos).
- `rx.breakpoints(initial="2", lg="4")` (breakpoints con esos
  mismos valores).

❌ NO acepta unidades CSS como `"3rem"`, `"4rem"`.
❌ NO acepta listas `["3rem", "4rem", "6rem"]`.

Para separación CSS personalizada, usar `gap` (prop abierto)
en lugar de `spacing`.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...componentes.base.primitivos import (
    enlace_navegacion,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    COLOR_DIVISOR,
    FONDO_HOME,
    FONDO_HOME_CARD,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_GRANDE,
    RADIO_MEDIO,
)
from ...infraestructura.constantes.identidad import (
    ANIO_COPYRIGHT,
    EMAIL_CONTACTO,
    NOMBRE_INSTITUTO,
    REDES_SOCIALES,
    RedSocial,
    TELEFONO_PRINCIPAL,
    UBICACION_FISICA,
    WHATSAPP_URL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_FOOTER: str = "80rem"
PADDING_LATERAL_FOOTER: str = "1.5rem"

RUTA_REPORTAR_PROBLEMA: str = "/contacto"


# ======================================================================
# Tipos
# ======================================================================


class ItemEnlaceFooter(TypedDict):
    """Item individual de enlace del footer."""

    etiqueta: str
    ruta: str
    icono: str
    externo: bool


class ColumnaFooter(TypedDict):
    """Columna de enlaces del footer."""

    titulo: str
    items: list[ItemEnlaceFooter]


class AccionRapida(TypedDict):
    """Acción de acceso rápido."""

    icono: str
    titulo: str
    descripcion: str
    ruta: str
    externo: bool


# ======================================================================
# Datos: acciones rápidas
# ======================================================================

ACCIONES_RAPIDAS: list[AccionRapida] = [
    {
        "icono": "message-circle",
        "titulo": "WhatsApp",
        "descripcion": "Respuesta en minutos",
        "ruta": WHATSAPP_URL,
        "externo": True,
    },
    {
        "icono": "map-pin",
        "titulo": "Ubicación",
        "descripcion": UBICACION_FISICA,
        "ruta": "/contacto",
        "externo": False,
    },
    {
        "icono": "graduation-cap",
        "titulo": "Admisión",
        "descripcion": "Inscripciones abiertas",
        "ruta": "/admision",
        "externo": False,
    },
]


# ======================================================================
# Datos: enlaces del footer (con iconos)
# ======================================================================

ENLACES_FOOTER: list[ColumnaFooter] = [
    {
        "titulo": "Plataforma",
        "items": [
            {
                "etiqueta": "Inicio",
                "ruta": "/",
                "icono": "home",
                "externo": False,
            },
            {
                "etiqueta": "Carreras",
                "ruta": "/carreras",
                "icono": "graduation-cap",
                "externo": False,
            },
            {
                "etiqueta": "Contacto",
                "ruta": "/contacto",
                "icono": "map-pin",
                "externo": False,
            },
        ],
    },
    {
        "titulo": "Institucional",
        "items": [
            {
                "etiqueta": "Sobre nosotros",
                "ruta": "/sobre-nosotros",
                "icono": "users",
                "externo": False,
            },
            {
                "etiqueta": "Preguntas frecuentes",
                "ruta": "/faq",
                "icono": "circle-help",
                "externo": False,
            },
            {
                "etiqueta": "Calendario académico",
                "ruta": "/calendario",
                "icono": "calendar",
                "externo": False,
            },
        ],
    },
    {
        "titulo": "Recursos",
        "items": [
            {
                "etiqueta": "Blog",
                "ruta": "/blog",
                "icono": "newspaper",
                "externo": False,
            },
            {
                "etiqueta": "Guía de admisión",
                "ruta": "/admision",
                "icono": "book-open",
                "externo": False,
            },
            {
                "etiqueta": "Becas",
                "ruta": "/becas",
                "icono": "trophy",
                "externo": False,
            },
        ],
    },
    {
        "titulo": "Contacto",
        "items": [
            {
                "etiqueta": "WhatsApp",
                "ruta": WHATSAPP_URL,
                "icono": "message-circle",
                "externo": True,
            },
            {
                "etiqueta": f"Tel: {TELEFONO_PRINCIPAL}",
                "ruta": f"tel:+591{TELEFONO_PRINCIPAL}",
                "icono": "phone",
                "externo": True,
            },
            {
                "etiqueta": EMAIL_CONTACTO,
                "ruta": f"mailto:{EMAIL_CONTACTO}",
                "icono": "mail",
                "externo": True,
            },
        ],
    },
]


# ======================================================================
# Bloque: Acciones rápidas
# ======================================================================


def _tarjeta_accion_rapida(accion: AccionRapida) -> rx.Component:
    """
    Tarjeta de acción rápida (WhatsApp, Ubicación, Admisión).

    Estructura:
    - Icono pequeño.
    - Título grande.
    - Descripción corta.

    Estilo:
    - Fondo plano (`FONDO_HOME_CARD`).
    - Borde sutil.
    - Hover: borde azul.

    Args:
        accion: `AccionRapida` con `icono`, `titulo`, `descripcion`,
            `ruta`, `externo`.

    Returns:
        Tarjeta clicable con la acción.
    """
    return enlace_navegacion(
        accion["ruta"],
        rx.box(
            rx.vstack(
                # ─── Icono ───────────────────────────────────────
                rx.icon(
                    accion["icono"],
                    size=20,
                    color=AZUL_MARINO_NEON,
                ),
                # ─── Título ──────────────────────────────────────
                rx.text(
                    accion["titulo"],
                    font_size="0.9375rem",
                    font_weight="700",
                    color=TEXTO_HOME_PRINCIPAL,
                    line_height="1.3",
                ),
                # ─── Descripción ─────────────────────────────────
                rx.text(
                    accion["descripcion"],
                    font_size="0.75rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                    line_height="1.4",
                ),
                align="start",
                spacing="1",
                width="100%",
            ),
            padding="1.25rem",
            border_radius=RADIO_GRANDE,
            background=FONDO_HOME_CARD,
            border=f"1px solid {BORDE_HOME_SUAVE}",
            width="100%",
            height="100%",
            transition="all 0.2s",
            _hover={
                "border_color": AZUL_MARINO_NEON,
                "transform": "translateY(-2px)",
            },
        ),
        externo=accion["externo"],
        text_decoration="none",
        width="100%",
        height="100%",
    )


def _bloque_acceso_rapido() -> rx.Component:
    """
    Bloque de 3 tarjetas de acceso rápido.

    Layout:
    - Móvil:    1 columna.
    - Tablet:   3 columnas.
    - Desktop:  3 columnas.
    """
    return rx.vstack(
        rx.text(
            "Acceso rápido",
            font_size="0.75rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            letter_spacing="0.15em",
            text_transform="uppercase",
            margin_bottom="1.5rem",
        ),
        rx.grid(
            *[_tarjeta_accion_rapida(a) for a in ACCIONES_RAPIDAS],
            columns=rx.breakpoints(initial="1", sm="3", lg="3"),
            spacing="3",
            width="100%",
        ),
        align="start",
        spacing="0",
        width="100%",
        margin_bottom="4rem",
    )


# ======================================================================
# Bloque: Newsletter
# ======================================================================


def _newsletter() -> rx.Component:
    """
    Bloque de newsletter con propuesta de valor.
    """
    return rx.vstack(
        rx.text(
            "Recibe fechas de inscripción antes que nadie",
            font_size="1.125rem",
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.3",
            letter_spacing="-0.01em",
        ),
        rx.text(
            "Te avisamos cuando se abran las inscripciones y "
            "publicamos nuevos artículos. Sin spam.",
            font_size="0.8125rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.5",
        ),
        rx.flex(
            rx.input(
                placeholder="tu@email.com",
                type="email",
                size="2",
                width="100%",
                flex="1",
                min_width="0",
                background="transparent",
                border=f"1px solid {BORDE_HOME_MEDIO}",
                color=TEXTO_HOME_PRINCIPAL,
                border_radius=RADIO_MEDIO,
                _placeholder={"color": TEXTO_HOME_MAS_SUAVE},
                _focus={
                    "border_color": AZUL_MARINO_NEON,
                    "box_shadow": f"0 0 0 1px {AZUL_MARINO_NEON}",
                },
            ),
            rx.button(
                rx.icon("arrow-right", size=14),
                size="2",
                cursor="pointer",
                flex_shrink="0",
                background=AZUL_MARINO_NEON,
                color="white",
                border_radius=RADIO_MEDIO,
                transition="all 0.2s",
                _hover={"filter": "brightness(1.1)"},
            ),
            gap="0.5rem",
            width="100%",
            align="center",
            margin_top="0.5rem",
        ),
        align="start",
        spacing="3",
        width="100%",
    )


# ======================================================================
# Bloque: Columna individual de enlaces
# ======================================================================


def _columna_enlaces(columna: ColumnaFooter) -> rx.Component:
    """
    Renderiza una columna del footer con su título y sus enlaces.

    Cada enlace lleva un icono descriptivo.
    """
    return rx.vstack(
        # ─── Título de la columna ───────────────────────────────
        rx.text(
            columna["titulo"],
            font_size="0.75rem",
            font_weight="700",
            text_transform="uppercase",
            letter_spacing="0.1em",
            color=TEXTO_HOME_MAS_SUAVE,
            margin_bottom="1rem",
        ),
        # ─── Enlaces con iconos ─────────────────────────────────
        rx.vstack(
            *[
                enlace_navegacion(
                    item["ruta"],
                    rx.flex(
                        rx.icon(
                            item["icono"],
                            size=14,
                            color=TEXTO_HOME_MAS_SUAVE,
                            flex_shrink="0",
                        ),
                        rx.text(
                            item["etiqueta"],
                            font_size="0.875rem",
                            color=TEXTO_HOME_SUAVE,
                            line_height="1.4",
                        ),
                        align="center",
                        gap="0.625rem",
                    ),
                    externo=item["externo"],
                    transition="color 0.2s",
                    _hover={"color": AZUL_MARINO_NEON},
                )
                for item in columna["items"]
            ],
            gap="0.75rem",
            align="start",
            width="100%",
        ),
        align="start",
        spacing="0",
        width="100%",
    )


def _grid_enlaces() -> rx.Component:
    """
    Grid de 4 columnas con los enlaces del footer.

    ⚠️ `spacing` es prop cerrado (solo "0"-"9" o
    `rx.breakpoints(...)` con esos valores). NO acepta unidades CSS.
    """
    return rx.grid(
        *[_columna_enlaces(col) for col in ENLACES_FOOTER],
        columns=rx.breakpoints(initial="2", sm="2", lg="4"),
        spacing=rx.breakpoints(initial="4", lg="6"),
        width="100%",
    )


# ======================================================================
# Bloque: Newsletter + Enlaces (2 columnas)
# ======================================================================


def _bloque_newsletter_enlaces() -> rx.Component:
    """
    Bloque de newsletter (izquierda) + enlaces (derecha).

    Layout:
    - Desktop: newsletter 30% / enlaces 70%.
    - Tablet/Móvil: stack vertical.
    """
    return rx.flex(
        # ─── Newsletter (30%) ───────────────────────────────────
        rx.box(
            _newsletter(),
            width=rx.breakpoints(
                initial="100%",
                lg="30%",
            ),
            flex_shrink="0",
        ),
        # ─── Enlaces (70%) ──────────────────────────────────────
        rx.box(
            _grid_enlaces(),
            width=rx.breakpoints(
                initial="100%",
                lg="70%",
            ),
            flex_shrink="0",
        ),
        # ─── Layout responsive ──────────────────────────────────
        direction=rx.breakpoints(
            initial="column",
            lg="row",
        ),
        align="start",
        justify="between",
        gap="4rem",
        width="100%",
        padding_y="4rem",
        border_top=f"1px solid {COLOR_DIVISOR}",
        border_bottom=f"1px solid {COLOR_DIVISOR}",
    )


# ======================================================================
# Bloque: Feedback discreto
# ======================================================================


def _bloque_feedback() -> rx.Component:
    """
    Bloque de feedback discreto ("¿Te resultó útil?").
    """
    return rx.flex(
        rx.text(
            "¿Te resultó útil esta página?",
            font_size="0.8125rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.flex(
            rx.button(
                rx.icon("thumbs-up", size=12),
                rx.text("Sí", as_="span"),
                size="1",
                variant="soft",
                color_scheme="green",
                cursor="pointer",
            ),
            rx.button(
                rx.icon("thumbs-down", size=12),
                rx.text("No", as_="span"),
                size="1",
                variant="soft",
                color_scheme="red",
                cursor="pointer",
            ),
            gap="0.5rem",
            align="center",
        ),
        enlace_navegacion(
            RUTA_REPORTAR_PROBLEMA,
            rx.text(
                "Reportar un problema",
                font_size="0.75rem",
                font_weight="600",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.icon(
                "arrow-up-right",
                size=12,
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            display="inline-flex",
            align_items="center",
            gap="0.375rem",
            text_decoration="none",
            transition="color 0.2s",
            _hover={"color": AZUL_MARINO_NEON},
        ),
        align="center",
        justify="start",
        gap="1.5rem",
        flex_wrap="wrap",
        padding_y="2rem",
        width="100%",
    )


# ======================================================================
# Bloque: Redes sociales
# ======================================================================


def _boton_red_social(red: RedSocial) -> rx.Component:
    """
    Botón de red social (outline, sin fondo de color).
    """
    return rx.link(
        rx.icon(
            red["icono"],
            size=16,
            color=red["color"],
        ),
        href=red["url"],
        is_external=True,
        text_decoration="none",
        height="2.25rem",
        width="2.25rem",
        border_radius=RADIO_MEDIO,
        background="transparent",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        display="flex",
        align_items="center",
        justify_content="center",
        transition="all 0.2s",
        aria_label=f"Visitar {red['nombre']}",
        _hover={
            "border_color": red["color"],
            "background": f"{red['color']}10",
        },
    )


def _fila_redes_sociales() -> rx.Component:
    """
    Fila con todas las redes sociales del instituto.
    """
    return rx.flex(
        rx.text(
            "SÍGUENOS",
            font_size="0.6875rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            letter_spacing="0.15em",
            text_transform="uppercase",
            flex_shrink="0",
        ),
        rx.flex(
            *[_boton_red_social(red) for red in REDES_SOCIALES],
            gap="0.5rem",
            flex_wrap="wrap",
            align="center",
        ),
        align="center",
        gap="1.5rem",
        flex_wrap="wrap",
        width="100%",
    )


# ======================================================================
# Bloque: Barra inferior (copyright)
# ======================================================================


def _enlace_legal(etiqueta: str, ruta: str) -> rx.Component:
    """Enlace legal pequeño en la barra inferior."""
    return enlace_navegacion(
        ruta,
        etiqueta,
        font_size="0.75rem",
        color=TEXTO_HOME_MAS_SUAVE,
        transition="color 0.2s",
        _hover={"color": AZUL_MARINO_NEON},
    )


def _barra_inferior() -> rx.Component:
    """
    Barra inferior con copyright + links legales + redes.
    """
    return rx.flex(
        # ─── Copyright + links legales ──────────────────────────
        rx.flex(
            rx.text(
                f"© {ANIO_COPYRIGHT} {NOMBRE_INSTITUTO}",
                font_size="0.75rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.text(
                "·",
                font_size="0.75rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            _enlace_legal("Términos", "/terminos"),
            rx.text(
                "·",
                font_size="0.75rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            _enlace_legal("Privacidad", "/privacidad"),
            align="center",
            gap="0.5rem",
            flex_wrap="wrap",
        ),
        # ─── Redes sociales (derecha) ───────────────────────────
        _fila_redes_sociales(),
        align="center",
        justify="between",
        width="100%",
        padding_top="2rem",
        padding_bottom="1rem",
        wrap="wrap",
        gap="1rem",
    )


# ======================================================================
# Footer completo
# ======================================================================


def pie_pagina_institucional() -> rx.Component:
    """
    Footer institucional completo — estilo Neon.com.

    Estructura:
    1. **Acceso rápido** (3 tarjetas).
    2. **Newsletter + Enlaces** (2 columnas).
    3. **Feedback discreto**.
    4. **Barra inferior**.
    """
    return rx.box(
        rx.vstack(
            # 1. Acceso rápido
            _bloque_acceso_rapido(),
            # 2. Newsletter + Enlaces
            _bloque_newsletter_enlaces(),
            # 3. Feedback discreto
            _bloque_feedback(),
            # 4. Barra inferior
            _barra_inferior(),
            spacing="0",
            width="100%",
        ),
        width="100%",
        padding=f"4rem {PADDING_LATERAL_FOOTER} 0 {PADDING_LATERAL_FOOTER}",
        max_width=ANCHO_MAXIMO_FOOTER,
        margin="0 auto",
        background=FONDO_HOME,
        role="contentinfo",
        aria_label="Información del sitio",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ACCIONES_RAPIDAS",
    "ENLACES_FOOTER",
    "ColumnaFooter",
    "ItemEnlaceFooter",
    "pie_pagina_institucional",
]