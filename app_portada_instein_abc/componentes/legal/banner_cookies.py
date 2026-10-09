

from __future__ import annotations

import reflex as rx

from ...dominio.estados.estado_banner_cookies import (
    EstadoBannerCookies,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_FONDO_CARTA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

COLOR_FONDO_BANNER: str = "rgba(59, 91, 219, 0.15)"
"""Tinte azul marino translúcido para el icono del banner."""


# ======================================================================
# Enlaces legales
# ======================================================================


def _enlace_legal_banner(etiqueta: str, ruta: str) -> rx.Component:
    """
    Enlace legal dentro del banner de cookies.

    Args:
        etiqueta: Texto visible del enlace.
        ruta: Ruta de destino (ej: "/privacidad").
    """
    return rx.link(
        etiqueta,
        href=ruta,
        color=AZUL_MARINO_NEON,
        text_decoration="underline",
        font_weight="600",
        transition="color 0.2s",
        _hover={"color": TEXTO_HOME_PRINCIPAL},
    )


# ======================================================================
# Botones del banner
# ======================================================================


def _boton_aceptar_todas() -> rx.Component:
    """Botón primario 'Aceptar todas' con azul marino neon."""
    return rx.button(
        rx.icon("check", size=14),
        "Aceptar todas",
        on_click=EstadoBannerCookies.aceptar_todas,
        background=AZUL_MARINO_NEON,
        color="white",
        font_weight="700",
        size="2",
        cursor="pointer",
        border_radius=RADIO_PASTILLA,
        transition="all 0.2s",
        aria_label="Aceptar todas las cookies",
        _hover={
            "transform": "translateY(-1px)",
            "filter": "brightness(1.1)",
        },
    )


def _boton_solo_necesarias() -> rx.Component:
    """Botón secundario 'Solo necesarias'."""
    return rx.button(
        rx.icon("shield", size=14),
        "Solo necesarias",
        on_click=EstadoBannerCookies.aceptar_solo_necesarias,
        variant="outline",
        color_scheme="gray",
        size="2",
        cursor="pointer",
        border_radius=RADIO_PASTILLA,
        aria_label="Aceptar solo cookies necesarias",
    )


def _boton_rechazar() -> rx.Component:
    """Botón ghost 'Rechazar'."""
    return rx.button(
        rx.icon("x", size=14),
        "Rechazar",
        on_click=EstadoBannerCookies.rechazar,
        variant="ghost",
        color_scheme="gray",
        size="2",
        cursor="pointer",
        border_radius=RADIO_PASTILLA,
        aria_label="Rechazar todas las cookies no necesarias",
    )


def _botones_banner() -> rx.Component:
    """
    Fila responsive de 3 botones.

    En móvil: apilados verticales alineados al inicio.
    En desktop: en fila alineados a la derecha.

    Nota: `justify` con `rx.breakpoints(...)` porque NO acepta lista
    de strings (es prop cerrado de Radix Themes).
    """
    return rx.flex(
        _boton_aceptar_todas(),
        _boton_solo_necesarias(),
        _boton_rechazar(),
        gap="0.5rem",
        flex_wrap="wrap",
        width="100%",
        justify=rx.breakpoints(
            initial="start",
            sm="start",
            md="end",
            lg="end",
        ),
    )


# ======================================================================
# Icono decorativo
# ======================================================================


def _icono_banner() -> rx.Component:
    """Icono de cookie con fondo tintado azul marino."""
    return rx.flex(
        rx.icon(
            "cookie",
            size=24,
            color=AZUL_MARINO_NEON,
        ),
        height="2.75rem",
        width="2.75rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_BANNER,
        border=f"1px solid {BORDE_HOME_AZUL}",
        align="center",
        justify="center",
        flex_shrink="0",
        aria_hidden="true",
    )


# ======================================================================
# Contenido del banner
# ======================================================================


def _contenido_banner() -> rx.Component:
    """Contenido del banner: título + descripción + botones."""
    return rx.vstack(
        rx.heading(
            "Usamos cookies",
            as_="h3",
            size="4",
            font_weight="800",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.2",
            letter_spacing="-0.02em",
        ),
        rx.text(
            "Utilizamos cookies para mejorar tu experiencia, "
            "analizar el tráfico y personalizar el contenido. "
            "Puedes aceptar todas, solo las necesarias, o "
            "rechazarlas. ",
            _enlace_legal_banner(
                "Política de Privacidad", "/privacidad"
            ),
            " · ",
            _enlace_legal_banner("Términos", "/terminos"),
            font_size="0.875rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
        ),
        _botones_banner(),
        spacing="3",
        align="start",
        width="100%",
    )


# ======================================================================
# Banner de cookies
# ======================================================================


def banner_cookies() -> rx.Component:
    """
    Banner de cookies con consentimiento explícito.

    Se oculta automáticamente cuando el usuario elige una opción
    (a través de `EstadoBannerCookies.consentimiento_otorgado`).

    Comportamiento:
    - `condicional`: si ya dio consentimiento → no renderiza nada.
    - Si no → renderiza el banner flotante en la parte inferior.

    Estilo:
    - `position: fixed` abajo al centro.
    - Fondo con glassmorphism.
    - Borde con acento azul marino.
    - Sombra elevada.

    Accesibilidad:
    - `role="dialog"`:    semántica de diálogo.
    - `aria_label`:       nombre accesible.
    - `aria_hidden`:      icono decorativo.

    Returns:
        Banner de cookies (o `rx.fragment()` si ya se aceptó).
    """
    return rx.cond(
        EstadoBannerCookies.consentimiento_otorgado,
        # ─── Ya dio consentimiento → no renderizar nada ────────
        rx.fragment(),
        # ─── Mostrar banner ────────────────────────────────────
        rx.box(
            rx.flex(
                _icono_banner(),
                _contenido_banner(),
                direction=rx.breakpoints(
                    initial="column",
                    sm="column",
                    md="row",
                    lg="row",
                ),
                align=rx.breakpoints(
                    initial="start",
                    sm="start",
                    md="start",
                    lg="start",
                ),
                gap="1rem",
                width="100%",
            ),
            # =====================================================
            # Estilos del contenedor
            # =====================================================
            position="fixed",
            bottom="1.5rem",
            left="50%",
            transform="translateX(-50%)",
            width=[
                "calc(100vw - 2rem)",
                "calc(100vw - 2rem)",
                "42rem",
                "42rem",
            ],
            max_width="42rem",
            padding="1.5rem",
            border_radius=RADIO_EXTRA_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {BORDE_HOME_AZUL}",
            box_shadow=(
                f"0 20px 40px -10px rgba(0, 0, 0, 0.3), "
                f"0 0 30px -10px {AZUL_MARINO_NEON}40"
            ),
            backdrop_filter="blur(20px)",
            z_index="1000",
            # =====================================================
            # Accesibilidad
            # =====================================================
            role="dialog",
            aria_label="Consentimiento de cookies",
        ),
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["banner_cookies"]