"""
Barra de navegación superior — estilo Neon.com.

Sistema de color
----------------
- Fondo: glassmorphism adaptativo.
- Elemento activo: acento azul marino.
- Toggle de color_mode: a la derecha.
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base.primitivos import (
    enlace_navegacion,
)
from ...dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_BARRA_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_MEDIO,
    RADIO_PASTILLA,
)
from ...infraestructura.constantes.identidad import (
    NOMBRE_INSTITUTO,
    WHATSAPP_URL,
)


# ======================================================================
# Constantes
# ======================================================================

TAMANO_ICONO_MENU: int = 18
TAMANO_ICONO_LOGO: int = 16
ANCHO_MAXIMO_BARRA: str = "80rem"


# ======================================================================
# Elemento del menú
# ======================================================================


def elemento_menu(
    etiqueta: str,
    icono: str,
    ruta: str,
) -> rx.Component:
    """
    Elemento del menú de navegación.

    Estilo Neon.com: solo texto en desktop, iconos solo en móvil.
    """
    esta_activo: rx.Var = (
        EstadoInstitucional.ruta_activa_normalizada == ruta
    )

    color_contenido = rx.cond(
        esta_activo,
        TEXTO_HOME_PRINCIPAL,
        TEXTO_HOME_MAS_SUAVE,
    )

    return enlace_navegacion(
        ruta,
        rx.flex(
            rx.icon(
                icono,
                size=TAMANO_ICONO_MENU,
                color=color_contenido,
            ),
            rx.text(
                etiqueta,
                font_size="0.875rem",
                font_weight=rx.cond(esta_activo, "600", "500"),
                color=color_contenido,
                white_space="nowrap",
                display=["none", "none", "block"],
            ),
            align="center",
            gap="0.5rem",
        ),
        padding="0.5rem 0.75rem",
        border_radius=RADIO_MEDIO,
        background=rx.cond(esta_activo, FONDO_AZUL_SUAVE, "transparent"),
        transition="all 0.2s",
        display="inline-flex",
        align_items="center",
        justify_content="center",
        text_decoration="none",
        _hover={
            "background": FONDO_AZUL_MUY_SUAVE,
        },
    )


# ======================================================================
# Logo
# ======================================================================


def _logo_institucional() -> rx.Component:
    """
    Logo minimalista: badge + texto (solo tablet/desktop).
    """
    return rx.flex(
        rx.box(
            rx.icon(
                "triangle",
                size=TAMANO_ICONO_LOGO,
                color="white",
            ),
            height="1.75rem",
            width="1.75rem",
            border_radius=RADIO_MEDIO,
            background=AZUL_MARINO_NEON,
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.tablet_and_desktop(
            rx.text(
                NOMBRE_INSTITUTO,
                font_size="0.9375rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="0.05em",
            ),
        ),
        align="center",
        gap="0.625rem",
        flex_shrink="0",
    )


# ======================================================================
# CTA WhatsApp (opcional, para el lado derecho)
# ======================================================================


def _cta_whatsapp() -> rx.Component:
    """
    CTA compacto de WhatsApp en la navbar (tablet/desktop).
    """
    return rx.tablet_and_desktop(
        enlace_navegacion(
            WHATSAPP_URL,
            rx.icon("message-circle", size=14, color="white"),
            rx.text(
                "WhatsApp",
                font_size="0.8125rem",
                font_weight="600",
                color="white",
            ),
            externo=True,
            display="inline-flex",
            align_items="center",
            gap="0.375rem",
            padding="0.5rem 0.875rem",
            border_radius=RADIO_PASTILLA,
            background=AZUL_MARINO_NEON,
            text_decoration="none",
            transition="all 0.2s",
            _hover={"filter": "brightness(1.1)"},
        ),
    )


# ======================================================================
# Barra completa
# ======================================================================


def barra_navegacion_superior() -> rx.Component:
    """
    Barra de navegación superior sticky — estilo Neon.com.
    """
    return rx.box(
        rx.flex(
            # ─── Izquierda: logo + menú ─────────────────────────
            rx.flex(
                _logo_institucional(),
                rx.flex(
                    elemento_menu("Inicio", "home", "/"),
                    elemento_menu("Carreras", "graduation-cap", "/carreras"),
                    elemento_menu("Contacto", "map-pin", "/contacto"),
                    align="center",
                    gap="0.25rem",
                    flex_shrink="0",
                ),
                align="center",
                gap=["0.75rem", "1.5rem", "2rem"],
                flex_shrink="0",
                min_width="0",
            ),
            # ─── Derecha: WhatsApp + toggle ─────────────────────
            rx.flex(
                _cta_whatsapp(),
                rx.color_mode.button(),
                align="center",
                gap="0.75rem",
                flex_shrink="0",
            ),
            align="center",
            justify="between",
            width="100%",
            max_width=ANCHO_MAXIMO_BARRA,
            margin="0 auto",
            gap="1rem",
        ),
        width="100%",
        padding="0.75rem 1.5rem",
        position="sticky",
        top="0",
        z_index="30",
        background=FONDO_BARRA_HOME,
        backdrop_filter="blur(20px)",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        role="banner",
        aria_label="Navegación principal",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "barra_navegacion_superior",
    "elemento_menu",
]