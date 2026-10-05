"""
Sección: Video de presentación institucional — estilo Neon.com.

Contenido
---------
- Título + subtítulo de presentación.
- Video de YouTube embebido en formato 16:9.
- CTAs duales (más información + crear cuenta).

Diseño
------
Refactorizado al estilo Neon.com:

1. **Layout 2 columnas**: texto (izq) + video (der).
2. **YouTube con iframe** (no `rx.video`, que no soporta YouTube).
3. **CTAs con acciones reales** (a /carreras y /admision).
4. **Iconos kebab-case** (Lucide oficial).
5. **Fondo adaptativo** al `color_mode`.
6. **Responsive mobile-first**.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: VIDEO DE YOUTUBE
-----------------------------
`rx.video` NO soporta URLs de YouTube (`youtu.be/...` o
`youtube.com/watch?v=...`). Solo acepta URLs directas a archivos
`.mp4`, `.webm`, etc.

Para YouTube se usa `rx.el.iframe` con la URL de embed:

    https://www.youtube.com/embed/VIDEO_ID

El ID del video se extrae de la URL original.

Ejemplo:
    Original:  https://youtu.be/uP00VWRCsrw
    Embed:     https://www.youtube.com/embed/uP00VWRCsrw

Nota técnica: NOMBRE DEL MÓDULO
-------------------------------
Este módulo se llamaba `portada_inicio_con_video.py`, lo cual era
engañoso porque NO es la portada del inicio, es UNA sección.

Se renombró a `seccion_video_portada.py` para reflejar su
propósito real.

Nota técnica: FUNCIONES ELIMINADAS
----------------------------------
- `icono_principal_de_curso()`: mostraba un icono de bitcoin
  (`bitcoin-svgrepo-com.svg`) que no tiene relación con el
  instituto. Se eliminó.

Nota técnica: `rx.video` vs `rx.el.iframe`
------------------------------------------
- `rx.video`: para archivos de video directos (`.mp4`, `.webm`).
- `rx.el.iframe`: para embeds externos (YouTube, Vimeo, Google Maps).

Esta distinción es importante porque YouTube sirve el video como
una página web embebida, no como un archivo de video.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
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

ANCHO_MAXIMO_SECCION: str = "72rem"
PADDING_LATERAL_SECCION: str = "2rem"
PADDING_VERTICAL_SECCION: str = "6rem"

# URL del video de YouTube (ID extraído de la URL original)
VIDEO_YOUTUBE_ID: str = "uP00VWRCsrw"
VIDEO_YOUTUBE_EMBED_URL: str = (
    f"https://www.youtube.com/embed/{VIDEO_YOUTUBE_ID}"
    f"?rel=0&modestbranding=1"
)


# ======================================================================
# Título + subtítulo + CTAs
# ======================================================================


def _titulo_hero() -> rx.Component:
    """
    Bloque de título, subtítulo y CTAs duales.

    Estructura:
    - Badge "VIDEO INSTITUCIONAL".
    - Título grande con acento azul marino.
    - Subtítulo descriptivo.
    - Par de CTAs (más información + crear cuenta).

    Returns:
        Bloque vertical con título + subtítulo + CTAs.
    """
    return rx.vstack(
        # ─── Badge ─────────────────────────────────────────────
        rx.flex(
            rx.icon("play-circle", size=12, color=AZUL_MARINO_NEON),
            rx.text(
                "VIDEO INSTITUCIONAL",
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
        # ─── Título ────────────────────────────────────────────
        rx.heading(
            "Forja tu futuro como ",
            rx.text.span(
                "Profesional Técnico Superior",
                color=AZUL_MARINO_NEON,
            ),
            "",
            as_="h3",
            font_size=["1.75rem", "2rem", "2.25rem"],
            font_weight="900",
            color=TEXTO_HOME_PRINCIPAL,
            letter_spacing="-0.03em",
            line_height="1.15",
        ),
        # ─── Subtítulo ─────────────────────────────────────────
        rx.text(
            "Sólida formación práctica con títulos de Provisión "
            "Nacional oficial. Estudia Sistemas Informáticos, "
            "Comercio Internacional, Electrónica, Contaduría y "
            "Secretariado Ejecutivo con equipamiento avanzado.",
            font_size="1rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            max_width="36rem",
            margin_top="1rem",
        ),
        # ─── CTAs ──────────────────────────────────────────────
        rx.flex(
            # CTA primario
            rx.link(
                rx.text(
                    "Más información",
                    as_="span",
                    font_size="0.9375rem",
                    font_weight="600",
                    color="white",
                ),
                rx.icon("arrow-right", size=16, color="white"),
                href="/carreras",
                text_decoration="none",
                display="inline-flex",
                align_items="center",
                gap="0.5rem",
                padding="0.875rem 1.5rem",
                border_radius=RADIO_PASTILLA,
                background=AZUL_MARINO_NEON,
                transition="all 0.2s",
                width="fit-content",
                _hover={
                    "transform": "translateY(-2px)",
                    "filter": "brightness(1.1)",
                },
            ),
            # CTA secundario
            rx.link(
                rx.text(
                    "Crear cuenta institucional",
                    as_="span",
                    font_size="0.9375rem",
                    font_weight="600",
                    color=TEXTO_HOME_PRINCIPAL,
                ),
                href="/admision",
                text_decoration="none",
                display="inline-flex",
                align_items="center",
                gap="0.5rem",
                padding="0.875rem 1.5rem",
                border_radius=RADIO_PASTILLA,
                background="transparent",
                border=f"1px solid {BORDE_HOME_MEDIO}",
                transition="all 0.2s",
                width="fit-content",
                _hover={
                    "border_color": BORDE_HOME_AZUL,
                    "background": rx.color_mode_cond(
                        light="rgba(59, 91, 219, 0.05)",
                        dark="rgba(59, 91, 219, 0.1)",
                    ),
                },
            ),
            gap="0.75rem",
            margin_top="2rem",
            direction=rx.breakpoints(initial="column", sm="row"),
            align="start",
            justify="start",
            flex_wrap="wrap",
        ),
        align="start",
        spacing="0",
        width="100%",
    )


# ======================================================================
# Video de YouTube (iframe)
# ======================================================================


def _video_youtube() -> rx.Component:
    """
    Video de YouTube embebido en formato 16:9.

    Usa `rx.el.iframe` en lugar de `rx.video` porque YouTube sirve
    el video como una página web, no como un archivo directo.

    Estilo:
    - Border radius grande.
    - Sombra sutil.
    - Aspect ratio 16:9.

    Returns:
        Componente con el iframe del video.
    """
    return rx.box(
        rx.aspect_ratio(
            rx.el.iframe(
                src=VIDEO_YOUTUBE_EMBED_URL,
                title="Video institucional INSTEIN",
                allow="accelerometer; autoplay; clipboard-write; "
                      "encrypted-media; gyroscope; picture-in-picture",
                allow_fullscreen=True,
                style={
                    "border": "0",
                    "width": "100%",
                    "height": "100%",
                },
            ),
            ratio=16 / 9,
        ),
        width="100%",
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        background="#0a0a0a",
        box_shadow=rx.color_mode_cond(
            light="0 8px 24px -8px rgba(0, 0, 0, 0.15)",
            dark="0 8px 24px -8px rgba(0, 0, 0, 0.5)",
        ),
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_video_portada() -> rx.Component:
    """
    Sección completa con video de presentación institucional.

    Estructura:
    1. Layout 2 columnas:
       - Izquierda (55%): título + subtítulo + CTAs.
       - Derecha (45%): video de YouTube.
    2. Responsive: stack vertical en móvil.

    Estilo Neon.com:
    - Layout con alineación izquierda.
    - Padding vertical generoso.
    - Coherente con el resto del home.

    Returns:
        Componente `rx.el.section` con la sección completa.
    """
    return rx.el.section(
        rx.flex(
            # ─── Columna izquierda: texto + CTAs ─────────────────
            rx.box(
                _titulo_hero(),
                width=rx.breakpoints(
                    initial="100%",
                    lg="55%",
                ),
                flex_shrink="0",
                display="flex",
                align_items="center",
            ),
            # ─── Columna derecha: video ──────────────────────────
            rx.box(
                _video_youtube(),
                width=rx.breakpoints(
                    initial="100%",
                    lg="45%",
                ),
                flex_shrink="0",
            ),
            # ─── Layout responsive ───────────────────────────────
            direction=rx.breakpoints(
                initial="column",
                lg="row",
            ),
            align="center",
            justify="between",
            gap=["3rem", "3rem", "4rem"],
            width="100%",
        ),
        width="100%",
        max_width=ANCHO_MAXIMO_SECCION,
        margin="0 auto",
        padding=f"{PADDING_VERTICAL_SECCION} {PADDING_LATERAL_SECCION}",
        aria_label="Video institucional",
    )


# ======================================================================
# Aliases retrocompatibles
# ======================================================================

# Alias por si algún módulo importaba la función original
portada_inicio_con_video = seccion_video_portada


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "VIDEO_YOUTUBE_EMBED_URL",
    "VIDEO_YOUTUBE_ID",
    "portada_inicio_con_video",
    "seccion_video_portada",
]