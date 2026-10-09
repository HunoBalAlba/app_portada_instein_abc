

from __future__ import annotations

import reflex as rx

from ...componentes.base.primitivos import (
    enlace_navegacion,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    GRADIENTE_HOME_BANNER,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
)
from ...infraestructura.constantes.identidad import (
    WHATSAPP_URL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_BANNER: str = "80rem"
PADDING_CONTENIDO: str = "6rem 2rem"
COLOR_VERDE_ACTIVO: str = "#22c55e"


# ======================================================================
# Trust badges
# ======================================================================


def _trust_badge(icono: str, texto: str) -> rx.Component:
    """Badge inline con icono + texto."""
    return rx.flex(
        rx.icon(icono, size=14, color=AZUL_MARINO_NEON),
        rx.text(
            texto,
            font_size="0.75rem",
            font_weight="600",
            color=TEXTO_HOME_PRINCIPAL,
            white_space="nowrap",
        ),
        align="center",
        gap="0.5rem",
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.7)",
            dark="rgba(59, 91, 219, 0.1)",
        ),
        border=f"1px solid {BORDE_HOME_MEDIO}",
        backdrop_filter="blur(12px)",
    )


# ======================================================================
# Botones
# ======================================================================


def _boton_primario() -> rx.Component:
    """Botón "Ver Carreras" con glow."""
    return enlace_navegacion(
        "/carreras",
        rx.text("Ver Carreras", as_="span", font_weight="700"),
        rx.icon("arrow-right", size=18),
        display="flex",
        align_items="center",
        gap="0.5rem",
        background=AZUL_MARINO_NEON,
        color="white",
        padding="1rem 2rem",
        border_radius=RADIO_PASTILLA,
        font_size="1rem",
        font_weight="700",
        box_shadow=f"0 0 30px {AZUL_MARINO_NEON}40",
        transition="all 0.2s",
        _hover={
            "transform": "translateY(-2px)",
            "box_shadow": f"0 0 40px {AZUL_MARINO_NEON}70",
            "filter": "brightness(1.1)",
        },
    )


def _boton_secundario() -> rx.Component:
    """Botón "WhatsApp"."""
    return enlace_navegacion(
        WHATSAPP_URL,
        rx.icon("message-circle", size=18),
        rx.text("Contactar por WhatsApp", as_="span", font_weight="600"),
        display="flex",
        align_items="center",
        gap="0.5rem",
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        padding="1rem 2rem",
        border_radius=RADIO_PASTILLA,
        font_size="1rem",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        _hover={
            "transform": "translateY(-2px)",
            "border_color": BORDE_HOME_AZUL,
            "background": rx.color_mode_cond(
                light="rgba(255, 255, 255, 0.5)",
                dark="rgba(59, 91, 219, 0.08)",
            ),
        },
    )


# ======================================================================
# Banner completo
# ======================================================================


def banner_cta_final() -> rx.Component:
    """
    Banner de llamada a la acción final (estilo Neon.com).

    Estructura:
    - Badge "Inscripciones abiertas".
    - Título grande.
    - Subtítulo con propuesta de valor.
    - Trust badges inline.
    - Par de botones.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ────────────────────────────────────────
            rx.flex(
                rx.box(
                    height="0.5rem",
                    width="0.5rem",
                    border_radius=RADIO_PASTILLA,
                    background=COLOR_VERDE_ACTIVO,
                    box_shadow=f"0 0 12px {COLOR_VERDE_ACTIVO}",
                    animation="pulse 2s ease-in-out infinite",
                    flex_shrink="0",
                ),
                rx.text(
                    "INSCRIPCIONES ABIERTAS · GESTIÓN 2026",
                    font_size="0.75rem",
                    font_weight="700",
                    color=TEXTO_HOME_PRINCIPAL,
                    letter_spacing="0.1em",
                ),
                align="center",
                gap="0.5rem",
                padding="0.5rem 1rem",
                border_radius=RADIO_PASTILLA,
                background=rx.color_mode_cond(
                    light="rgba(255, 255, 255, 0.7)",
                    dark="rgba(59, 91, 219, 0.1)",
                ),
                border=f"1px solid {BORDE_HOME_AZUL}",
                width="fit-content",
                margin_bottom="1.5rem",
            ),
            # ─── Título ────────────────────────────────────────
            rx.heading(
                "Tu futuro profesional empieza hoy",
                size="8",
                color=TEXTO_HOME_PRINCIPAL,
                text_align="center",
                font_weight="900",
                letter_spacing="-0.03em",
                line_height="1.05",
                max_width="42rem",
            ),
            # ─── Subtítulo ─────────────────────────────────────
            rx.text(
                "Formación práctica, títulos oficiales y una red de "
                "egresados que te acompañan desde el primer día.",
                font_size="1.125rem",
                color=TEXTO_HOME_SUAVE,
                text_align="center",
                max_width="42rem",
                margin_top="0.75rem",
                line_height="1.6",
            ),
            # ─── Trust badges inline ────────────────────────────
            rx.flex(
                _trust_badge("award", "Título Nacional"),
                _trust_badge("trending-up", "100% Empleabilidad"),
                _trust_badge("building-2", "Convenios Empresariales"),
                gap="0.5rem",
                margin_top="2rem",
                flex_wrap="wrap",
                justify="center",
            ),
            # ─── Botones ────────────────────────────────────────
            rx.flex(
                _boton_primario(),
                _boton_secundario(),
                gap="0.75rem",
                margin_top="2.5rem",
                direction=rx.breakpoints(
                    initial="column",
                    sm="row",
                ),
                align="center",
                justify="center",
            ),
            align="center",
            position="relative",
            z_index="1",
            padding=PADDING_CONTENIDO,
        ),
        position="relative",
        width="100%",
        background=GRADIENTE_HOME_BANNER,
        border_radius=RADIO_EXTRA_GRANDE,
        border=f"1px solid {BORDE_HOME_AZUL}",
        overflow="hidden",
        max_width=ANCHO_MAXIMO_BANNER,
        margin="0 auto",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["banner_cta_final"]