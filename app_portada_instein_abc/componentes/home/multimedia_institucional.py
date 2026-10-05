"""
Sección multimedia institucional del home — estilo Neon.com.

Diseño
------
Refactorizado al estilo de Neon.com:

1. **Video desnudo**: sin borde, sin glow, solo el radius.
2. **Layout 60/40**: video dominante (izq), texto (der).
3. **Sin badges redundantes**: un solo badge "PLATAFORMA OFICIAL".
4. **CTA alineado**: botón `fit-content`, no full-width.
5. **Redes sociales outline**: botones limpios al pie.
6. **Espaciado generoso**: coherente con el resto del home.
7. **Fondo del video consistente**: negro puro en ambos modos.

Contenido
---------
1. Video institucional (columna izquierda, 60%).
2. Bloque de plataforma académica (columna derecha, 40%):
   - Badge "PLATAFORMA OFICIAL".
   - Título.
   - Descripción.
   - CTA "Crear Cuenta Institucional".
3. Fila de redes sociales (pie, full width).

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: ¿POR QUÉ EL VIDEO SIN BORDE?
-----------------------------------------
El video en sí ya es un elemento visual fuerte (contiene imagen
en movimiento). Añadirle:

- Borde (`border`).
- Sombra (`box_shadow`).
- Padding interno (`padding`).
- Fondo de card.

...es **ruido visual**. El video debe respirar por sí solo.

En Neon.com, los videos y diagramas no tienen card wrapper: son el
elemento mismo.

Nota técnica: REDES SOCIALES EN OUTLINE
---------------------------------------
En el diseño original, las redes eran **botones con fondo del color
corporativo** (rojo YouTube, azul Facebook, etc.). Esto:

- Introduce 6 colores diferentes al diseño.
- Compite visualmente con el video.
- No es coherente con el minimalismo de Neon.

En la nueva versión, los botones son **outline** con:
- Fondo transparente.
- Icono en el color corporativo (mantiene identidad).
- Texto en color principal.
- Hover: borde del color de la red.

Resultado: identidad preservada, pero sin ruido.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_MEDIO,
    COLOR_DIVISOR,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
)
from ...infraestructura.constantes.identidad import (
    REDES_SOCIALES,
    RedSocial,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_SECCION: str = "80rem"
PADDING_LATERAL_SECCION: str = "2rem"
PADDING_VERTICAL_SECCION: str = "6rem"


# ======================================================================
# Video institucional
# ======================================================================


def _video_institucional() -> rx.Component:
    """
    Video institucional en formato 16:9 — estilo desnudo.

    Sin borde, sin glow, sin padding. Solo el video con su radius.

    El fondo del contenedor es negro puro en ambos modos, porque
    el video en sí suele ser oscuro. Si el video no carga, se ve
    un fondo oscuro elegante.
    """
    return rx.box(
        rx.aspect_ratio(
            rx.video(
                src="/video_in.mp4",
                width="100%",
                height="100%",
                controls=True,
                auto_play=False,
                loop=False,
                muted=False,
                border_radius=RADIO_EXTRA_GRANDE,
            ),
            ratio=16 / 9,
        ),
        width="100%",
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        background="#0a0a0a",
        # Sombra muy sutil para separar del fondo
        box_shadow=rx.color_mode_cond(
            light="0 4px 20px -4px rgba(0, 0, 0, 0.15)",
            dark="0 4px 20px -4px rgba(0, 0, 0, 0.5)",
        ),
    )


# ======================================================================
# Badge de plataforma
# ======================================================================


def _badge_plataforma() -> rx.Component:
    """
    Badge "PLATAFORMA OFICIAL" en outline sutil.

    Sin glow, sin fondo sólido. Solo texto + icono con borde.
    """
    return rx.flex(
        rx.icon("award", size=12, color=AZUL_MARINO_NEON),
        rx.text(
            "PLATAFORMA OFICIAL",
            font_size="0.6875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            letter_spacing="0.15em",
            text_transform="uppercase",
        ),
        align="center",
        gap="0.5rem",
        padding="0.375rem 0.75rem",
        border_radius=RADIO_PASTILLA,
        background="transparent",
        border=f"1px solid {AZUL_MARINO_NEON}",
        width="fit-content",
    )


# ======================================================================
# CTA crear cuenta
# ======================================================================


def _cta_crear_cuenta() -> rx.Component:
    """
    CTA "Crear Cuenta Institucional" — estilo Neon.com.

    Fondo azul marino sólido, sin glow. Ancho `fit-content`.
    """
    return rx.button(
        rx.text("Crear cuenta institucional", as_="span", font_weight="600"),
        rx.icon("arrow-right", size=16),
        size="3",
        cursor="pointer",
        background=AZUL_MARINO_NEON,
        color="white",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        padding="0.875rem 1.5rem",
        width="fit-content",
        transition="all 0.2s",
        _hover={
            "transform": "translateY(-2px)",
            "filter": "brightness(1.08)",
        },
    )


# ======================================================================
# Info de la plataforma
# ======================================================================


def _info_plataforma() -> rx.Component:
    """
    Bloque de texto que describe la plataforma académica.

    Estructura:
    - Badge "PLATAFORMA OFICIAL".
    - Título.
    - Descripción.
    - CTA.
    """
    return rx.vstack(
        # ─── Badge ─────────────────────────────────────────────
        _badge_plataforma(),
        # ─── Título ────────────────────────────────────────────
        rx.heading(
            "Plataforma web de ",
            rx.text.span(
                "seguimiento académico",
                color=AZUL_MARINO_NEON,
            ),
            "",
            as_="h3",
            font_size=["1.5rem", "1.75rem", "2rem"],
            font_weight="800",
            letter_spacing="-0.02em",
            line_height="1.15",
            color=TEXTO_HOME_PRINCIPAL,
            margin_top="1rem",
        ),
        # ─── Descripción ───────────────────────────────────────
        rx.text(
            "Accede a tu historial académico, calificaciones, "
            "asistencia y materiales de estudio desde cualquier "
            "dispositivo. Inicia sesión con tu cuenta institucional "
            "y mantén el control total de tu formación técnica.",
            font_size="0.9375rem",
            line_height="1.7",
            color=TEXTO_HOME_MAS_SUAVE,
            max_width="32rem",
            margin_top="0.5rem",
        ),
        # ─── CTA ───────────────────────────────────────────────
        rx.box(
            _cta_crear_cuenta(),
            margin_top="1.5rem",
        ),
        align="start",
        spacing="0",
        width="100%",
    )


# ======================================================================
# Redes sociales (outline)
# ======================================================================


def _boton_red_social(red: RedSocial) -> rx.Component:
    """
    Botón de red social en estilo outline.

    Estructura:
    - Icono en el color corporativo de la red.
    - Texto en color principal.
    - Fondo transparente.
    - Hover: borde + fondo sutil del color corporativo.

    Args:
        red: `RedSocial` con `nombre`, `icono`, `url`, `color`.
    """
    return rx.link(
        rx.flex(
            rx.icon(
                red["icono"],
                size=16,
                color=red["color"],
            ),
            rx.text(
                red["nombre"],
                font_size="0.8125rem",
                font_weight="600",
                color=TEXTO_HOME_PRINCIPAL,
            ),
            align="center",
            gap="0.5rem",
        ),
        href=red["url"],
        is_external=True,
        text_decoration="none",
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background="transparent",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        aria_label=f"Visitar {red['nombre']}",
        _hover={
            "border_color": red["color"],
            "background": f"{red['color']}10",
        },
    )


def _fila_redes_sociales() -> rx.Component:
    """
    Fila de redes sociales al pie de la sección.

    Estructura:
    - Etiqueta "SÍGUENOS".
    - Fila de botones outline.
    """
    return rx.flex(
        # ─── Etiqueta ──────────────────────────────────────────
        rx.text(
            "SÍGUENOS",
            font_size="0.6875rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            letter_spacing="0.15em",
            text_transform="uppercase",
            flex_shrink="0",
        ),
        # ─── Botones ───────────────────────────────────────────
        rx.flex(
            *[_boton_red_social(red) for red in REDES_SOCIALES],
            gap="0.5rem",
            flex_wrap="wrap",
            align="center",
        ),
        align="center",
        gap=["1.5rem", "2rem"],
        width="100%",
        flex_wrap="wrap",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_multimedia_institucional() -> rx.Component:
    """
    Sección completa del bloque multimedia institucional.

    Estructura:
    1. Video institucional (60%) + Info plataforma (40%).
    2. Separador horizontal.
    3. Fila de redes sociales.

    Layout responsive:
    - Desktop: video 60% / info 40%.
    - Tablet/Móvil: stack vertical.
    """
    return rx.box(
        rx.vstack(
            # ==========================================================
            # Fila principal: video + info plataforma
            # ==========================================================
            rx.flex(
                # ─── Video (60%) ────────────────────────────────
                rx.box(
                    _video_institucional(),
                    width=rx.breakpoints(
                        initial="100%",
                        lg="60%",
                    ),
                    flex_shrink="0",
                ),
                # ─── Info plataforma (40%) ──────────────────────
                rx.box(
                    _info_plataforma(),
                    width=rx.breakpoints(
                        initial="100%",
                        lg="40%",
                    ),
                    flex_shrink="0",
                ),
                # ─── Layout responsive ──────────────────────────
                direction=rx.breakpoints(
                    initial="column",
                    lg="row",
                ),
                align="start",
                justify="between",
                gap=["3rem", "3rem", "4rem"],
                width="100%",
            ),
            # ==========================================================
            # Separador
            # ==========================================================
            rx.box(
                height="1px",
                width="100%",
                background=COLOR_DIVISOR,
                margin_y=["3rem", "4rem"],
            ),
            # ==========================================================
            # Fila de redes sociales
            # ==========================================================
            _fila_redes_sociales(),
            spacing="0",
            width="100%",
        ),
        width="100%",
        max_width=ANCHO_MAXIMO_SECCION,
        margin="0 auto",
        padding=f"{PADDING_VERTICAL_SECCION} {PADDING_LATERAL_SECCION}",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["seccion_multimedia_institucional"]