"""
Barra de navegación superior — estilo Neon adaptativo (dark/light).

Sistema de color
----------------
- Fondo: glassmorphism adaptativo (`FONDO_BARRA_HOME`).
- Elemento activo: fondo azul marino translúcido + borde azul tenue.
- Elementos inactivos: texto adaptativo (`TEXTO_HOME_MAS_SUAVE`).
- Hover: fondo azul marino translúcido + texto adaptativo.
- Logo: badge con gradiente azul marino + texto "INSTEIN" adaptativo.
- Toggle de color_mode: a la derecha.

Comportamiento
--------------
La barra es **sticky** (`position: sticky; top: 0`) y siempre visible.
El fondo es translúcido con `backdrop-filter: blur(20px)` para que el
contenido se vea difuminado detrás.

Accesibilidad
-------------
- `<nav role="navigation" aria-label="Navegación principal">` en el
  contenedor raíz (vía `role` + `aria_label` de Reflex).
- Cada elemento del menú es un `<a>` real (SEO + teclado).
- El color_mode button es accesible por Radix Themes.

Nota técnica: `rx.icon(size=...)`
---------------------------------
`rx.icon(size=...)` SOLO acepta `int`, nunca `str`. Los tamaños están
declarados como constantes enteras (`TAMANO_ICONO_MENU = 20`).

Nota técnica: `padding` y `gap` con listas
------------------------------------------
Los props CSS abiertos (`padding`, `gap`, `width`, etc.) aceptan
LISTAS de breakpoints: `padding=["0.5rem", "0.5rem 1rem"]` significa
`initial="0.5rem"`, `lg="0.5rem 1rem"`.

NO uses `rx.breakpoints(...)` para estos props: es innecesariamente
verboso. Reserva `rx.breakpoints(...)` para props **cerrados** como
`direction`, `align`, `justify`, `wrap`.

Nota técnica: `RUTA_ACTIVA` comparación
---------------------------------------
Para evitar recalcular `ruta_activa == ruta` tres veces por elemento,
la comparación se hace UNA VEZ en una variable local y se reutiliza.
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
    AZUL_MARINO_PROFUNDO,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_BARRA_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_MEDIO,
)
from ...infraestructura.constantes.identidad import (
    NOMBRE_INSTITUTO,
)


# ======================================================================
# Constantes locales
# ======================================================================

TAMANO_ICONO_MENU: int = 20
"""Tamaño del icono del menú en tablet/desktop (px)."""

TAMANO_ICONO_MENU_MOVIL: int = 22
"""Tamaño del icono del menú en móvil (px)."""

TAMANO_ICONO_LOGO: int = 18
"""Tamaño del icono del logo (px)."""

ANCHO_MAXIMO_BARRA: str = "72rem"
"""Ancho máximo del contenido de la barra (alineado con el resto del sitio)."""

SOMBRA_LOGO: str = f"0 0 20px {AZUL_MARINO_NEON}80"
"""Glow azul marino del logo (80 = 50% opacidad en hex)."""

GRADIENTE_LOGO: str = (
    f"linear-gradient(135deg, {AZUL_MARINO_NEON} 0%, "
    f"{AZUL_MARINO_PROFUNDO} 100%)"
)
"""Gradiente diagonal del badge del logo."""


# ======================================================================
# Elemento individual del menú
# ======================================================================


def elemento_menu(
    etiqueta: str,
    icono: str,
    ruta: str,
) -> rx.Component:
    """
    Elemento individual del menú de navegación, con estado activo.

    UX:
    - Móvil:          solo icono (ahorra espacio).
    - Tablet/desktop: icono + etiqueta de texto.

    Estado activo:
    - Fondo azul marino translúcido.
    - Borde azul marino tenue.
    - Texto principal (mayor contraste).

    Estado inactivo:
    - Sin fondo, sin borde.
    - Texto secundario.

    Args:
        etiqueta: Texto visible (ej: "Inicio", "Carreras").
        icono: Nombre del icono Lucide (kebab-case).
        ruta: Ruta de destino (ej: "/", "/carreras").

    Returns:
        Enlace estilizado como elemento de menú.
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
            # --- Icono móvil (size=22) ---
            rx.mobile_only(
                rx.icon(
                    icono,
                    size=TAMANO_ICONO_MENU_MOVIL,
                    color=color_contenido,
                ),
            ),
            # --- Icono + texto tablet/desktop (size=20) ---
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.icon(
                        icono,
                        size=TAMANO_ICONO_MENU,
                        color=color_contenido,
                    ),
                    rx.text(
                        etiqueta,
                        font_size="0.875rem",
                        font_weight=rx.cond(esta_activo, "700", "500"),
                        color=color_contenido,
                        white_space="nowrap",
                    ),
                    spacing="2",
                    align="center",
                ),
            ),
            align="center",
            gap="0.4rem",
        ),
        # `padding` es prop CSS abierto → acepta lista.
        # initial="0.5rem" (cuadrado, solo icono), lg="0.5rem 1rem" (ancho).
        padding=["0.5rem", "0.5rem", "0.5rem 1rem"],
        border_radius=RADIO_MEDIO,
        background=rx.cond(esta_activo, FONDO_AZUL_SUAVE, "transparent"),
        border=rx.cond(
            esta_activo,
            f"1px solid {BORDE_HOME_MEDIO}",
            "1px solid transparent",
        ),
        transition="all 0.2s",
        display="inline-flex",
        align_items="center",
        justify_content="center",
        text_decoration="none",
        _hover={
            "background": FONDO_AZUL_MUY_SUAVE,
            "color": TEXTO_HOME_PRINCIPAL,
        },
    )


# ======================================================================
# Logo institucional
# ======================================================================


def _logo_institucional() -> rx.Component:
    """
    Logo del instituto con badge de gradiente azul marino.

    Estructura:
    - Badge cuadrado con gradiente diagonal azul marino.
    - Icono "triangle" blanco dentro del badge.
    - Texto "INSTEIN" al lado (solo tablet/desktop).

    El texto usa `NOMBRE_INSTITUTO` (fuente única de verdad) en vez de
    hardcodear el string.

    ⚠️ `rx.icon(size=...)` SOLO acepta `int`. Nunca pasar un `str`.
    """
    return rx.flex(
        # --- Badge con gradiente ---
        rx.box(
            rx.icon(
                "triangle",
                size=TAMANO_ICONO_LOGO,   # ✅ int, no str
                color="white",
            ),
            height="2rem",
            width="2rem",
            border_radius=RADIO_MEDIO,
            background=GRADIENTE_LOGO,
            display="flex",
            align_items="center",
            justify_content="center",
            box_shadow=SOMBRA_LOGO,
            flex_shrink="0",
        ),
        # --- Texto del instituto (solo tablet/desktop) ---
        rx.tablet_and_desktop(
            rx.text(
                NOMBRE_INSTITUTO,
                font_size="0.9375rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="0.1em",
            ),
        ),
        align="center",
        gap="0.625rem",
        flex_shrink="0",
    )


# ======================================================================
# Barra de navegación completa
# ======================================================================


def barra_navegacion_superior() -> rx.Component:
    """
    Barra de navegación superior sticky — estilo Neon adaptativo.

    Estructura:
    - Logo institucional (izquierda).
    - Menú de navegación (centro-izquierda).
    - Botón de color_mode (derecha).

    Estilo:
    - Fondo glassmorphism adaptativo (`FONDO_BARRA_HOME`).
    - `backdrop-filter: blur(20px)` para difuminar el contenido detrás.
    - Borde inferior sutil.
    - `position: sticky; top: 0; z-index: 30`.

    ✅ ADAPTATIVO: el fondo y los bordes respetan el color_mode.

    Returns:
        Componente `rx.vstack` con `role="banner"`.
    """
    return rx.vstack(
        rx.flex(
            # ==========================================================
            # Bloque izquierdo: logo + menú
            # ==========================================================
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
                # `gap` es prop CSS abierto → acepta lista de breakpoints.
                gap=["0.75rem", "1.5rem", "2rem"],
                flex_shrink="0",
                min_width="0",
            ),
            # ==========================================================
            # Bloque derecho: toggle de color_mode
            # ==========================================================
            rx.flex(
                rx.color_mode.button(),
                align="center",
                gap="1rem",
                flex_shrink="0",
            ),
            # ==========================================================
            # Layout horizontal de la barra
            # ==========================================================
            align="center",
            justify="between",
            width="100%",
            max_width=ANCHO_MAXIMO_BARRA,
            margin="0 auto",
            gap="1rem",
        ),
        # ==============================================================
        # Estilos del contenedor raíz (sticky + glassmorphism)
        # ==============================================================
        align="center",
        justify="between",
        width="100%",
        padding="0.875rem 1.5rem",
        position="sticky",
        top="0",
        z_index="30",
        background=FONDO_BARRA_HOME,
        backdrop_filter="blur(20px)",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        # ==============================================================
        # Accesibilidad
        # ==============================================================
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