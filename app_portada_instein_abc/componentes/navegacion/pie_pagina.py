"""
Pie de página institucional — estilo Neon adaptativo (dark/light).

Estructura
----------
1. **Bloque superior**: brand (logo + tagline + redes) + newsletter.
2. **Sección de feedback**: "¿Te resultó útil?" + Sí/No + Reportar.
3. **Grid de enlaces**: 4 columnas (Plataforma, Institucional,
   Recursos, Contacto).
4. **Barra inferior**: copyright + links legales + estado del servidor.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el color_mode del usuario.

- Fondo: `FONDO_HOME` (light: claro, dark: oscuro).
- Acentos: azul marino neon (`AZUL_MARINO_NEON`) en AMBOS modos.
- Textos: `TEXTO_HOME_PRINCIPAL` / `TEXTO_HOME_SUAVE` / `TEXTO_HOME_MAS_SUAVE`.
- Bordes: `BORDE_HOME_SUAVE` / `BORDE_HOME_MEDIO` / `BORDE_HOME_AZUL`.
- Redes sociales: colores corporativos oficiales (hex fijos),
  porque son colores de marca de terceros y no deben cambiar con
  el tema.
- Estado del servidor: verde semántico con pulse.

Nota técnica: TOGGLE DE COLOR MODE
----------------------------------
El toggle está en la **barra de navegación superior** (arriba a la
derecha) para que sea más visible. El footer NO duplica el toggle.

Nota técnica: `ENLACES_FOOTER` es CONSTANTE
-------------------------------------------
`ENLACES_FOOTER` es una constante de módulo (no una función que
devuelve lista) porque no depende del State. Esto permite:

- Reutilizar la constante en tests.
- Evitar reconstruir la lista en cada render del footer.

Nota técnica: SEMÁNTICA HTML5
-----------------------------
El footer se renderiza con `role="contentinfo"` en el componente
raíz para que lectores de pantalla lo identifiquen correctamente.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...componentes.base.primitivos import (
    enlace_navegacion,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_MEDIO,
    RADIO_PASTILLA,
)
from ...infraestructura.constantes.identidad import (
    ANIO_COPYRIGHT,
    DESCRIPCION_INSTITUCIONAL,
    EMAIL_CONTACTO,
    NOMBRE_INSTITUTO,
    REDES_SOCIALES,
    RedSocial,
    TELEFONO_PRINCIPAL,
    WHATSAPP_URL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_FOOTER: str = "72rem"
"""Ancho máximo del contenido del footer."""

PADDING_LATERAL_FOOTER: str = "1.5rem"
"""Padding lateral del footer."""

COLOR_VERDE_ACTIVO: str = "#22c55e"
"""Color del punto verde semántico (activo). Mismo en ambos modos."""

RUTA_REPORTAR_PROBLEMA: str = "/contacto"
"""Ruta del enlace "Reportar un problema"."""


# ======================================================================
# Tipos para la estructura de enlaces
# ======================================================================


class ItemEnlaceFooter(TypedDict):
    """Item individual de enlace del footer."""

    etiqueta: str
    ruta: str
    externo: bool


class ColumnaFooter(TypedDict):
    """Columna de enlaces del footer."""

    titulo: str
    items: list[ItemEnlaceFooter]


# ======================================================================
# Estructura de los enlaces del footer (constante de módulo)
# ======================================================================

ENLACES_FOOTER: list[ColumnaFooter] = [
    {
        "titulo": "Plataforma",
        "items": [
            {"etiqueta": "Inicio", "ruta": "/", "externo": False},
            {"etiqueta": "Carreras", "ruta": "/carreras", "externo": False},
            {"etiqueta": "Contacto", "ruta": "/contacto", "externo": False},
        ],
    },
    {
        "titulo": "Institucional",
        "items": [
            {
                "etiqueta": "Sobre nosotros",
                "ruta": "/sobre-nosotros",
                "externo": False,
            },
            {
                "etiqueta": "Preguntas frecuentes",
                "ruta": "/faq",
                "externo": False,
            },
            {
                "etiqueta": "Calendario académico",
                "ruta": "/calendario",
                "externo": False,
            },
        ],
    },
    {
        "titulo": "Recursos",
        "items": [
            {"etiqueta": "Blog", "ruta": "/blog", "externo": False},
            {
                "etiqueta": "Guía de admisión",
                "ruta": "/admision",
                "externo": False,
            },
            {
                "etiqueta": "Becas y reconocimientos",
                "ruta": "/becas",
                "externo": False,
            },
        ],
    },
    {
        "titulo": "Contacto",
        "items": [
            {"etiqueta": "WhatsApp", "ruta": WHATSAPP_URL, "externo": True},
            {
                "etiqueta": f"Tel: {TELEFONO_PRINCIPAL}",
                "ruta": f"tel:+591{TELEFONO_PRINCIPAL}",
                "externo": True,
            },
            {
                "etiqueta": EMAIL_CONTACTO,
                "ruta": f"mailto:{EMAIL_CONTACTO}",
                "externo": True,
            },
        ],
    },
]


# ======================================================================
# Brand block (logo + tagline + redes sociales)
# ======================================================================


def _logo_institucional_footer() -> rx.Component:
    """
    Logo textual del instituto con badge de gradiente azul marino.

    ✅ ADAPTATIVO: el texto "INSTEIN" y el subtítulo cambian según el modo.
    """
    return rx.flex(
        # --- Badge "I" con gradiente azul marino ---
        rx.box(
            rx.text(
                "I",
                font_size="1.125rem",
                font_weight="900",
                color="white",
                line_height="1",
            ),
            height="2.25rem",
            width="2.25rem",
            border_radius=RADIO_MEDIO,
            background=(
                f"linear-gradient(135deg, {AZUL_MARINO_NEON} 0%, "
                f"#1a237e 100%)"
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            box_shadow=f"0 0 20px {AZUL_MARINO_NEON}80",
            flex_shrink="0",
        ),
        # --- Texto INSTEIN + subtítulo ---
        rx.vstack(
            rx.text(
                NOMBRE_INSTITUTO,
                font_size="0.9375rem",
                font_weight="900",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="0.1em",
                line_height="1.1",
            ),
            rx.text(
                "Instituto Técnico Integrado",
                font_size="0.6875rem",
                font_weight="500",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.2",
            ),
            spacing="0",
            align="start",
        ),
        align="center",
        gap="0.75rem",
    )


def _red_social_boton(red: RedSocial) -> rx.Component:
    """
    Botón de red social con el color corporativo oficial.

    ⚠️ Los colores de marca de las redes NO cambian con el modo
    (son colores oficiales de cada plataforma).

    Args:
        red: `RedSocial` con `nombre`, `icono`, `url`, `color`.
    """
    return rx.link(
        rx.icon(red["icono"], size=16, color="white"),
        href=red["url"],
        is_external=True,
        text_decoration="none",
        height="2rem",
        width="2rem",
        border_radius=RADIO_MEDIO,
        background=red["color"],
        display="flex",
        align_items="center",
        justify_content="center",
        transition="all 0.2s",
        aria_label=f"Visitar {red['nombre']}",
        _hover={
            "transform": "translateY(-2px)",
            "filter": "brightness(1.15)",
        },
    )


def _brand_block() -> rx.Component:
    """
    Bloque de marca con logo + descripción + redes sociales.

    ✅ ADAPTATIVO: la descripción cambia de color según el modo.
    """
    return rx.vstack(
        _logo_institucional_footer(),
        rx.text(
            DESCRIPCION_INSTITUCIONAL,
            font_size="0.8125rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            max_width="20rem",
        ),
        rx.flex(
            *[_red_social_boton(red) for red in REDES_SOCIALES],
            gap="0.5rem",
            flex_wrap="wrap",
            margin_top="0.25rem",
        ),
        align="start",
        spacing="3",
        width="100%",
        max_width="22rem",
    )


# ======================================================================
# Newsletter
# ======================================================================


def _newsletter() -> rx.Component:
    """
    Bloque de newsletter con input de email + botón suscribir.

    ✅ ADAPTATIVO: input, textos y botón cambian según el modo.

    Nota: en una implementación real, el input dispararía un evento
    al backend para guardar el email. Por ahora es solo UI.
    """
    return rx.vstack(
        rx.text(
            "Recibe novedades",
            font_size="0.875rem",
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.2",
        ),
        rx.text(
            "Noticias, fechas de inscripción y eventos del instituto.",
            font_size="0.75rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.4",
        ),
        rx.flex(
            rx.input(
                placeholder="tu@email.com",
                type="email",
                size="2",
                width="100%",
                flex="1",
                min_width="0",
                background=FONDO_AZUL_MUY_SUAVE,
                border=f"1px solid {BORDE_HOME_MEDIO}",
                color=TEXTO_HOME_PRINCIPAL,
                _placeholder={"color": TEXTO_HOME_MAS_SUAVE},
                _focus={
                    "border_color": BORDE_HOME_AZUL,
                    "box_shadow": f"0 0 0 1px {AZUL_MARINO_NEON}",
                },
            ),
            rx.button(
                rx.icon("send", size=14),
                rx.text("Suscribir", as_="span"),
                size="2",
                cursor="pointer",
                flex_shrink="0",
                background=AZUL_MARINO_NEON,
                color="white",
                border_radius=RADIO_MEDIO,
                box_shadow=f"0 4px 12px -2px {AZUL_MARINO_NEON}40",
                transition="all 0.2s",
                _hover={
                    "transform": "translateY(-1px)",
                    "box_shadow": f"0 6px 16px -2px {AZUL_MARINO_NEON}cc",
                },
            ),
            gap="0.5rem",
            width="100%",
            align="center",
        ),
        align="start",
        spacing="2",
        width="100%",
        max_width="22rem",
    )


# ======================================================================
# Sección de feedback ("¿Te resultó útil?")
# ======================================================================


def _seccion_feedback() -> rx.Component:
    """
    Sección con pregunta de feedback y botones Sí/No + reportar.

    ✅ ADAPTATIVO: textos, link y borde cambian según el modo.

    UX:
    - Pregunta con texto destacado.
    - Botones semánticos: verde para Sí, rojo para No.
    - Link "Reportar un problema" con glassmorphism adaptativo.
    - Borde inferior sutil que separa del grid de enlaces.

    Nota: los botones Sí/No usan colores semánticos (verde/rojo),
    NO el azul marino, porque representan estados del sistema.
    """
    return rx.flex(
        rx.text(
            "¿Te resultó útil esta página?",
            font_weight="600",
            font_size="0.875rem",
            color=TEXTO_HOME_PRINCIPAL,
        ),
        rx.flex(
            rx.button(
                rx.icon("thumbs-up", size=14),
                rx.text("Sí", as_="span"),
                size="1",
                variant="soft",
                color_scheme="green",
                cursor="pointer",
            ),
            rx.button(
                rx.icon("thumbs-down", size=14),
                rx.text("No", as_="span"),
                size="1",
                variant="soft",
                color_scheme="red",
                cursor="pointer",
            ),
            enlace_navegacion(
                RUTA_REPORTAR_PROBLEMA,
                rx.icon("message-square-warning", size=14),
                rx.text("Reportar un problema", as_="span"),
                display="inline-flex",
                align_items="center",
                gap="0.4rem",
                padding="0.375rem 0.75rem",
                border_radius=RADIO_MEDIO,
                background=FONDO_AZUL_MUY_SUAVE,
                border=f"1px solid {BORDE_HOME_SUAVE}",
                color=TEXTO_HOME_SUAVE,
                font_size="0.75rem",
                font_weight="600",
                transition="all 0.2s",
                _hover={
                    "background": FONDO_AZUL_MUY_SUAVE,
                    "border_color": BORDE_HOME_MEDIO,
                    "color": TEXTO_HOME_PRINCIPAL,
                },
            ),
            gap="0.5rem",
            align="center",
            wrap="wrap",
        ),
        direction="column",
        gap="0.75rem",
        padding="2rem 0",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        width="100%",
    )


# ======================================================================
# Columna individual de enlaces
# ======================================================================


def _columna_enlaces(columna: ColumnaFooter) -> rx.Component:
    """
    Renderiza una columna del footer con su título y sus enlaces.

    ✅ ADAPTATIVO: los textos y el hover cambian según el modo.

    Args:
        columna: `ColumnaFooter` con `titulo` e `items`.
    """
    return rx.vstack(
        # --- Título de la columna ---
        rx.text(
            columna["titulo"],
            font_size="0.75rem",
            font_weight="700",
            text_transform="uppercase",
            letter_spacing="0.1em",
            color=TEXTO_HOME_MAS_SUAVE,
            margin_bottom="0.5rem",
        ),
        # --- Enlaces ---
        rx.vstack(
            *[
                enlace_navegacion(
                    item["ruta"],
                    item["etiqueta"],
                    externo=item["externo"],
                    font_size="0.875rem",
                    color=TEXTO_HOME_SUAVE,
                    transition="color 0.2s",
                    _hover={"color": AZUL_MARINO_NEON},
                )
                for item in columna["items"]
            ],
            gap="0.5rem",
            align="start",
            width="100%",
        ),
        align="start",
        spacing="1",
        width="100%",
    )


# ======================================================================
# Barra inferior con copyright y estado
# ======================================================================


def _enlace_legal(etiqueta: str, ruta: str) -> rx.Component:
    """
    Enlace legal pequeño en la barra inferior (adaptativo).

    Args:
        etiqueta: Texto visible.
        ruta: URL de destino.
    """
    return enlace_navegacion(
        ruta,
        etiqueta,
        font_size="0.75rem",
        color=TEXTO_HOME_MAS_SUAVE,
        transition="color 0.2s",
        _hover={"color": AZUL_MARINO_NEON},
    )


def _indicador_estado_servidor() -> rx.Component:
    """
    Indicador visual de estado del servidor (punto verde pulsante).

    ✅ ADAPTATIVO: fondo y borde cambian según el modo.

    UX:
    - Punto verde con glow pulsante.
    - Texto "Todos los servicios operativos".
    - Borde + fondo glassmorphism.
    - Animación `borderPulse` (definida en estilos globales).
    """
    return rx.flex(
        rx.box(
            height="0.5rem",
            width="0.5rem",
            border_radius=RADIO_PASTILLA,
            background=COLOR_VERDE_ACTIVO,
            box_shadow=f"0 0 12px {COLOR_VERDE_ACTIVO}",
            animation="pulse 2s ease-in-out infinite",
        ),
        rx.text(
            "Todos los servicios operativos",
            font_size="0.75rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        align="center",
        gap="0.5rem",
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        border=f"1px solid {BORDE_HOME_SUAVE}",
        background="rgba(34, 197, 94, 0.08)",
        animation="borderPulse 2.5s ease-in-out infinite",
    )


def _barra_inferior() -> rx.Component:
    """
    Barra inferior del footer con copyright, links legales y estado
    del servidor.

    ✅ ADAPTATIVO: textos, borde y fondo del indicador cambian según
    el modo.

    UX:
    - Copyright + links legales a la izquierda.
    - Estado del servidor a la derecha.

    Nota: el toggle de color mode está en la barra de navegación
    superior (arriba a la derecha) para que sea más visible.
    """
    return rx.flex(
        # ==========================================================
        # Copyright + links legales (izquierda)
        # ==========================================================
        rx.flex(
            rx.text(
                f"© {ANIO_COPYRIGHT} {NOMBRE_INSTITUTO} · "
                f"Todos los derechos reservados",
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
        # ==========================================================
        # Estado del servidor (derecha)
        # ==========================================================
        _indicador_estado_servidor(),
        # ==========================================================
        # Layout de la barra inferior
        # ==========================================================
        align="center",
        justify="between",
        width="100%",
        padding_top="2rem",
        wrap="wrap",
        gap="1rem",
    )


# ======================================================================
# Bloque superior: brand + newsletter
# ======================================================================


def _bloque_superior() -> rx.Component:
    """
    Bloque superior del footer: brand block + newsletter.

    En desktop se muestran lado a lado; en móvil se apilan.

    ✅ ADAPTATIVO: el borde inferior cambia según el modo.

    Nota: `direction` en `rx.flex` de Radix Themes acepta listas de
    breakpoints directamente (a diferencia de `align`/`justify`).
    Aquí usamos lista para mayor limpieza.
    """
    return rx.flex(
        _brand_block(),
        _newsletter(),
        direction=rx.breakpoints(initial="column", md="row"),
        justify="between",
        align="start",
        gap="2rem",
        width="100%",
        padding="3rem 0",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
    )


# ======================================================================
# Footer completo
# ======================================================================


def pie_pagina_institucional() -> rx.Component:
    """
    Footer institucional completo — estilo Neon adaptativo.

    Contiene:
    - Bloque superior: brand (logo + tagline + redes) + newsletter.
    - Sección de feedback ("¿Te resultó útil?").
    - Grid de enlaces por columnas.
    - Barra inferior con copyright + legales + estado del servidor.

    ✅ ADAPTATIVO: fondo, textos y bordes respetan el color_mode.

    El toggle de color mode está en la barra de navegación superior.

    Returns:
        Componente `rx.box` con `role="contentinfo"`.
    """
    return rx.box(
        rx.vstack(
            # ==========================================================
            # Bloque superior: brand + newsletter
            # ==========================================================
            _bloque_superior(),
            # ==========================================================
            # Sección de feedback
            # ==========================================================
            _seccion_feedback(),
            # ==========================================================
            # Grid de columnas de enlaces
            # ==========================================================
            rx.grid(
                *[_columna_enlaces(col) for col in ENLACES_FOOTER],
                columns=rx.breakpoints(initial="1", sm="2", lg="4"),
                spacing="6",
                width="100%",
                padding="3rem 0",
            ),
            # ==========================================================
            # Barra inferior
            # ==========================================================
            _barra_inferior(),
            spacing="0",
            width="100%",
        ),
        # ==============================================================
        # Estilos del contenedor principal
        # ==============================================================
        width="100%",
        padding=f"0 {PADDING_LATERAL_FOOTER}",
        max_width=ANCHO_MAXIMO_FOOTER,
        margin="0 auto",
        border_top=f"1px solid {BORDE_HOME_SUAVE}",
        background=FONDO_HOME,
        # ==============================================================
        # Semántica HTML5
        # ==============================================================
        role="contentinfo",
        aria_label="Información del sitio",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ENLACES_FOOTER",
    "ColumnaFooter",
    "ItemEnlaceFooter",
    "pie_pagina_institucional",
]