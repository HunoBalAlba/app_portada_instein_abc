

from __future__ import annotations

import reflex as rx

# ======================================================================
# Imports de componentes (rutas relativas dentro de `componentes/`)
# ======================================================================

from ...base.vinetas import (
    vineta_campo_laboral,
    vineta_perfil_profesional,
)

# ======================================================================
# Imports de dominio (fachada)
# ======================================================================

from ....dominio import EstadoInstitucional

# ======================================================================
# Imports de infraestructura (fachada)
# ======================================================================

from ....infraestructura import (
    ANCHO_SECCION,
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    FONDO_AZUL_SUAVE,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_TARJETA: str = "1.75rem"
"""Padding interno de las tarjetas de perfil/campo."""


# ======================================================================
# Helpers internos
# ======================================================================


def _badge_contador(texto: str) -> rx.Component:
    """
    Badge pill con el contador de items de una sección.

    Estilo Neon.com:
    - Fondo con tinte azul muy suave.
    - Borde sutil azul marino.
    - Texto azul marino.

    Args:
        texto: Texto del contador (ej: "5 habilidades").

    Returns:
        Badge pill con el contador.
    """
    return rx.box(
        rx.text(
            texto,
            font_size="0.6875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            text_transform="uppercase",
            letter_spacing="0.05em",
            white_space="nowrap",
        ),
        padding="0.25rem 0.625rem",
        border_radius=RADIO_PASTILLA,
        background=FONDO_AZUL_SUAVE,
        border=f"1px solid {BORDE_HOME_AZUL}",
        flex_shrink="0",
    )


def _encabezado_seccion(
    icono: str,
    titulo: str,
    subtitulo: str | None = None,
    badge: str | None = None,
) -> rx.Component:
    """
    Encabezado limpio para las secciones del detalle.

    Estilo Neon.com:
    - Icono directo (sin caja).
    - Título en mayúsculas con acento.
    - Subtítulo en gris.
    - Badge opcional a la derecha.

    Estructura:
    ┌─────────────────────────────────────────┐
    │  ✓  PERFIL PROFESIONAL       [5 skills] │
    │     Competencias que...                  │
    └─────────────────────────────────────────┘

    Args:
        icono: Nombre del icono Lucide (kebab-case).
        titulo: Título de la sección (mayúsculas).
        subtitulo: Texto opcional debajo del título.
        badge: Texto opcional para el badge a la derecha.

    Returns:
        Fila con icono + título/subtítulo + badge opcional.
    """
    hijos: list[rx.Component] = [
        # ─── Icono directo (sin caja) ──────────────────────────
        rx.icon(
            icono,
            size=18,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
        ),
        # ─── Título + subtítulo ────────────────────────────────
        rx.vstack(
            rx.text(
                titulo,
                font_size="0.6875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.15em",
                text_transform="uppercase",
                line_height="1.2",
            ),
            rx.cond(
                subtitulo is not None,
                rx.text(
                    subtitulo or "",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                    line_height="1.5",
                    margin_top="0.25rem",
                ),
                rx.fragment(),
            ),
            spacing="0",
            align="start",
            flex="1",
            min_width="0",
        ),
    ]

    if badge is not None:
        hijos.append(_badge_contador(badge))

    return rx.flex(
        *hijos,
        align="center",
        gap="0.75rem",
        width="100%",
        margin_bottom="1.5rem",
        flex_wrap="wrap",
    )


# ======================================================================
# Tarjeta genérica para listas
# ======================================================================


def _tarjeta_lista(
    icono: str,
    titulo: str,
    subtitulo: str,
    items: rx.Var,
    render_item,
    badge: str | None = None,
) -> rx.Component:
    """
    Tarjeta genérica para listas (perfil, campo laboral).

    Estilo Neon.com:
    - Fondo plano (COLOR_FONDO_CARTA).
    - Borde sutil + borde superior de acento (2px).
    - Hover: solo cambio de borde.
    - Sin glow ni translateY.

    Args:
        icono: Nombre del icono Lucide del encabezado.
        titulo: Título de la sección.
        subtitulo: Subtítulo descriptivo.
        items: `Var` reactivo con la lista de items.
        render_item: Función que renderiza cada item (debe aceptar un `Var`).
        badge: Texto opcional para el badge del encabezado.

    Returns:
        Tarjeta estilizada con el encabezado + la lista.
    """
    return rx.box(
        _encabezado_seccion(icono, titulo, subtitulo, badge),
        rx.vstack(
            rx.foreach(items, render_item),
            gap="0.75rem",
            width="100%",
        ),
        padding=PADDING_TARJETA,
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_perfil_y_campo_laboral() -> rx.Component:
    """
    Sección con dos columnas:
    - **Perfil Profesional**: habilidades y competencias del egresado.
    - **Campo Laboral**: dónde puede trabajar el egresado.

    Grid responsive que colapsa a 1 columna en móvil.

    Estilo Neon.com:
    - Grid de 2 columnas (`md+`).
    - Tarjetas con borde superior de acento.
    - Hover sutil.
    - Alineado con el ancho de sección del sitio.

    Returns:
        Grid con las 2 tarjetas.
    """
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.grid(
        # =============================================================
        # Columna 1: Perfil Profesional
        # =============================================================
        _tarjeta_lista(
            icono="user-check",
            titulo="Perfil profesional",
            subtitulo="Competencias que desarrollarás durante la carrera.",
            badge=f"{carrera['perfil_profesional'].length()} habilidades",
            items=carrera["perfil_profesional"],
            render_item=vineta_perfil_profesional,
        ),
        # =============================================================
        # Columna 2: Campo Laboral
        # =============================================================
        _tarjeta_lista(
            icono="building-2",
            titulo="Campo laboral",
            subtitulo="Dónde podrás trabajar al egresar.",
            badge=f"{carrera['campo_laboral'].length()} opciones",
            items=carrera["campo_laboral"],
            render_item=vineta_campo_laboral,
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="4",
        width="100%",
        max_width=ANCHO_SECCION,
        margin="0 auto",
        align_items="stretch",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_perfil_y_campo_laboral"]