"""
Hero principal del home — estilo Neon.com adaptado a INSTEIN.

Diseño
------
Inspirado en Neon.com:

1. **Fondo oscuro casi puro** con gradiente radial sutil.
2. **Barras verticales tipo "datacenter"** (patrón de columnas
   animadas con iconos de carreras).
3. **Título hero grande** con jerarquía clara (2-3 líneas).
4. **Dos CTAs** side-by-side (primario + secundario).
5. **Badge superior** tipo "parte de la plataforma".
6. **Carrusel infinito** (marquee) con iconos de carreras.
7. **Trust badges** inline con credenciales.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: CARRUSEL INFINITO (MARQUEE)
-----------------------------------------
El carrusel infinito usa una técnica CSS pura:

1. Duplicar la lista de iconos `[iconos, iconos]` (2x).
2. Animar `translateX(-50%)` en `@keyframes marquee`.
3. Al terminar la animación, el segundo bloque reemplaza al primero
   visualmente, creando la ilusión de scroll infinito.

Ventajas:
- No usa JavaScript (CSS puro).
- No interfiere con el evento de scroll.
- Suave y sin saltos visuales.

Nota técnica: BARRAS VERTICALES TIPO DATACENTER
-----------------------------------------------
Las barras verticales se renderizan como un grid de columnas con
alturas variables (con semilla fija para reproducibilidad).
Cada barra contiene iconos de carreras apilados verticalmente.

Es el patrón característico de Neon.com.
"""

from __future__ import annotations

import random
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
    FONDO_AZUL_SUAVE,
    FONDO_HOME_HERO,
    GRADIENTE_TEXTO_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_PASTILLA,
)


# ======================================================================
# Catálogo de iconos de carreras (para el marquee y las barras)
# ======================================================================

ICONOS_CARRERAS: list[str] = [
    # Sistemas
    "cpu", "code-2", "database", "terminal", "binary", "hard-drive",
    # Contaduría
    "calculator", "receipt", "coins", "chart-line", "wallet",
    # Secretariado
    "briefcase", "calendar-clock", "mail", "clipboard-list",
    # Comercio
    "globe", "ship", "package", "truck",
    # Electrónica
    "zap", "circuit-board", "radio", "plug-zap",
    # Académicos generales
    "graduation-cap", "book-open", "award", "lightbulb", "target",
]


# ======================================================================
# Configuración del marquee
# ======================================================================

CANTIDAD_ICONOS_MARQUEE: int = 30
DURACION_MARQUEE_SEGUNDOS: int = 40
ALTURA_MARQUEE: str = "4rem"


# ======================================================================
# Configuración de las barras verticales (datacenter)
# ======================================================================

CANTIDAD_BARRAS_VERTICALES: int = 12
SEMILLA_BARRAS: int = 42
ICONOS_POR_BARRA_MIN: int = 3
ICONOS_POR_BARRA_MAX: int = 8


class BarraVertical(TypedDict):
    """Configuración de una barra vertical del fondo."""

    iconos: list[str]
    altura: str
    opacidad: float
    delay: float
    duracion: float


def _generar_barras_verticales(
    cantidad: int = CANTIDAD_BARRAS_VERTICALES,
    semilla: int = SEMILLA_BARRAS,
) -> list[BarraVertical]:
    """
    Genera la configuración de las barras verticales.

    Cada barra contiene N iconos apilados verticalmente con opacidad
    y animación aleatoria.

    Args:
        cantidad: Número de barras.
        semilla: Semilla para reproducibilidad.

    Returns:
        Lista de `BarraVertical` con la configuración.
    """
    rng = random.Random(semilla)
    barras: list[BarraVertical] = []

    for _ in range(cantidad):
        n_iconos = rng.randint(
            ICONOS_POR_BARRA_MIN,
            ICONOS_POR_BARRA_MAX,
        )
        iconos = [rng.choice(ICONOS_CARRERAS) for _ in range(n_iconos)]
        altura = f"{rng.uniform(40, 90)}%"
        opacidad = rng.uniform(0.03, 0.10)
        delay = rng.uniform(0, 3)
        duracion = rng.uniform(4, 8)

        barras.append({
            "iconos": iconos,
            "altura": altura,
            "opacidad": opacidad,
            "delay": delay,
            "duracion": duracion,
        })

    return barras


BARRAS_VERTICALES: list[BarraVertical] = _generar_barras_verticales()


# ======================================================================
# CAPA 1: Barras verticales tipo datacenter
# ======================================================================


def _barra_vertical(barra: BarraVertical) -> rx.Component:
    """
    Renderiza una barra vertical con iconos apilados.

    La barra tiene:
    - Una columna delgada (2-3px de ancho) con gradiente vertical.
    - Iconos superpuestos verticalmente.
    - Animación de pulso sutil.
    """
    return rx.box(
        # Columna vertical con gradiente
        rx.box(
            position="absolute",
            top="0",
            left="50%",
            transform="translateX(-50%)",
            width="2px",
            height=barra["altura"],
            background=(
                f"linear-gradient(180deg, "
                f"{AZUL_MARINO_NEON} 0%, "
                f"transparent 100%)"
            ),
            opacity=barra["opacidad"],
            border_radius=RADIO_PASTILLA,
        ),
        # Iconos apilados verticalmente
        rx.vstack(
            *[
                rx.icon(
                    icono,
                    size=16,
                    color=AZUL_MARINO_NEON,
                    opacity="0.5",
                )
                for icono in barra["iconos"]
            ],
            spacing="2",
            align="center",
            justify="start",
            position="absolute",
            top="0",
            left="50%",
            transform="translateX(-50%)",
            height=barra["altura"],
            overflow="hidden",
        ),
        position="relative",
        width="100%",
        height="100%",
        animation=(
            f"pulso_columna {barra['duracion']}s ease-in-out "
            f"{barra['delay']}s infinite"
        ),
        pointer_events="none",
    )


def _capa_barras_verticales() -> rx.Component:
    """
    Capa con el grid de barras verticales.

    Layout: grid de 12 columnas que ocupa todo el ancho del hero.
    En móvil, solo 6 columnas visibles.
    """
    return rx.box(
        rx.grid(
            *[_barra_vertical(b) for b in BARRAS_VERTICALES],
            columns="12",
            spacing="0",
            width="100%",
            height="100%",
        ),
        position="absolute",
        top="0",
        left="0",
        right="0",
        bottom="0",
        overflow="hidden",
        pointer_events="none",
        z_index="1",
    )


# ======================================================================
# CAPA 0: Fondo gradiente + orbes sutiles
# ======================================================================


def _capa_fondo() -> rx.Component:
    """Fondo con gradiente radial sutil y orbes de glow."""
    return rx.box(
        # Gradiente radial sutil
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=FONDO_HOME_HERO,
            z_index="-2",
            pointer_events="none",
        ),
        # Orbe superior derecha
        rx.box(
            position="absolute",
            top="-20%",
            right="-10%",
            width="50%",
            height="80%",
            background=(
                f"radial-gradient(circle, "
                f"{AZUL_MARINO_NEON} 0%, transparent 60%)"
            ),
            opacity=rx.color_mode_cond(light="0.08", dark="0.15"),
            filter="blur(120px)",
            z_index="-1",
            pointer_events="none",
        ),
        # Orbe inferior izquierda
        rx.box(
            position="absolute",
            bottom="-20%",
            left="-10%",
            width="50%",
            height="80%",
            background=(
                "radial-gradient(circle, "
                "#1a237e 0%, transparent 60%)"
            ),
            opacity=rx.color_mode_cond(light="0.10", dark="0.18"),
            filter="blur(120px)",
            z_index="-1",
            pointer_events="none",
        ),
        position="absolute",
        top="0",
        left="0",
        right="0",
        bottom="0",
        pointer_events="none",
        z_index="0",
    )


# ======================================================================
# Badge superior "parte de la plataforma"
# ======================================================================


def _badge_plataforma() -> rx.Component:
    """
    Badge superior tipo "INSTEIN IS PART OF ...".

    Coherente con el diseño de Neon.com: ícono + texto pequeño
    en mayúsculas, espaciado amplio.
    """
    return rx.flex(
        rx.icon(
            "circle-dot",
            size=12,
            color=AZUL_MARINO_NEON,
        ),
        rx.text(
            "INSTEIN · INSTITUTO TÉCNICO INTEGRADO",
            font_size="0.6875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            letter_spacing="0.15em",
            text_transform="uppercase",
        ),
        align="center",
        gap="0.5rem",
        margin_bottom="2rem",
    )


# ======================================================================
# Título hero (multi-línea, estilo Neon)
# ======================================================================


def _titulo_hero() -> rx.Component:
    """
    Título hero multi-línea al estilo Neon.com.

    Estructura:
        Forja tu futuro como
        Técnico Superior,
        construye tu camino profesional.

    El span "Técnico Superior" lleva gradiente de texto azul marino.
    """
    return rx.heading(
        "Forja tu futuro como",
        rx.box(height="0.25rem"),
        rx.text.span(
            "Técnico Superior",
            background=GRADIENTE_TEXTO_HOME,
            background_clip="text",
            color="transparent",
            webkit_background_clip="text",
        ),
        ",",
        rx.box(height="0.25rem"),
        "construye tu camino profesional.",
        as_="h1",
        font_size=["1.875rem", "2.5rem", "3rem", "3.75rem"],
        text_align="left",
        font_weight="900",
        letter_spacing="-0.04em",
        line_height="1.05",
        color=TEXTO_HOME_PRINCIPAL,
        max_width="56rem",
    )


# ======================================================================
# CTAs
# ======================================================================


def _cta_primario() -> rx.Component:
    """
    CTA primario estilo Neon.com: fondo blanco, texto negro.

    Es el botón principal del hero, contrasta con el fondo oscuro.
    """
    return enlace_navegacion(
        "/carreras",
        rx.text("Explorar carreras", as_="span", font_weight="600"),
        rx.icon("arrow-right", size=16),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background=rx.color_mode_cond(
            light=AZUL_MARINO_NEON,
            dark="white",
        ),
        color=rx.color_mode_cond(
            light="white",
            dark="#0a0a0a",
        ),
        padding="0.875rem 1.75rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        font_weight="600",
        transition="all 0.2s",
        _hover={
            "transform": "translateY(-2px)",
            "filter": "brightness(1.05)",
        },
    )


def _cta_secundario() -> rx.Component:
    """
    CTA secundario estilo Neon.com: outline transparente.

    Es el botón secundario del hero, menos prominente.
    """
    return enlace_navegacion(
        "/admision",
        rx.text("Leer la guía", as_="span", font_weight="500"),
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        background="transparent",
        color=TEXTO_HOME_PRINCIPAL,
        padding="0.875rem 1.75rem",
        border_radius=RADIO_PASTILLA,
        font_size="0.9375rem",
        border=f"1px solid {BORDE_HOME_MEDIO}",
        transition="all 0.2s",
        _hover={
            "border_color": BORDE_HOME_AZUL,
            "background": FONDO_AZUL_SUAVE,
        },
    )


# ======================================================================
# Marquee de iconos (carrusel infinito)
# ======================================================================


def _item_marquee(icono: str, indice: int) -> rx.Component:
    """
    Item individual del marquee.

    Cada item es un icono con espaciado a los lados.

    Args:
        icono: Nombre del icono Lucide.
        indice: Índice del item (no usado, requerido por rx.foreach).
    """
    return rx.box(
        # ✅ DESPUÉS
rx.icon(
    icono,
    size=24,
    color=AZUL_MARINO_NEON,
    opacity=rx.color_mode_cond(light="0.55", dark="0.4"),
),
        padding="0 1.5rem",
        flex_shrink="0",
    )


def _marquee_iconos() -> rx.Component:
    """
    Marquee infinito con iconos de carreras.

    Técnica CSS:
    1. Duplicamos la lista de iconos `[iconos, iconos]`.
    2. Animamos `translateX(-50%)` para que el primer bloque se
       desplace completamente fuera de la vista.
    3. Al reiniciar la animación, el segundo bloque ocupa el lugar
       del primero, creando la ilusión de scroll infinito.

    ⚠️ La lista duplicada se genera a nivel de Python (fuera del
    componente), no en `rx.foreach`, porque necesitamos duplicar
    literalmente los items.
    """
    iconos_duplicados = ICONOS_CARRERAS * 2

    return rx.box(
        rx.flex(
            *[_item_marquee(ic, i) for i, ic in enumerate(iconos_duplicados)],
            align="center",
            width="max-content",
            animation=(
                f"marquee_horizontal {DURACION_MARQUEE_SEGUNDOS}s "
                f"linear infinite"
            ),
        ),
        width="100%",
        overflow="hidden",
        position="relative",
        padding_y="1.5rem",
        border_top=f"1px solid {BORDE_HOME_SUAVE}",
        mask=(
            "linear-gradient(90deg, "
            "transparent 0%, "
            "black 10%, "
            "black 90%, "
            "transparent 100%)"
        ),
        _hover={"& .marquee-track": {"animation_play_state": "paused"}},
    )


# ======================================================================
# Trust badges (logos/credenciales)
# ======================================================================


def _trust_logo(icono: str, etiqueta: str) -> rx.Component:
    """
    Logo/credencial individual en la fila de trust.

    Estilo Neon.com: ícono + texto pequeño, opacidad reducida,
    alineación horizontal.
    """
    return rx.flex(
        rx.icon(
            icono,
            size=18,
            color=TEXTO_HOME_MAS_SUAVE,
            opacity="0.7",
        ),
        rx.text(
            etiqueta,
            font_size="0.75rem",
            font_weight="600",
            color=TEXTO_HOME_MAS_SUAVE,
            letter_spacing="0.05em",
            text_transform="uppercase",
            white_space="nowrap",
        ),
        align="center",
        gap="0.5rem",
        opacity="0.7",
        transition="opacity 0.2s",
        _hover={"opacity": "1"},
    )


def _fila_trust_logos() -> rx.Component:
    """
    Fila de logos/credenciales estilo Neon.com.

    Se muestra debajo de los CTAs y encima del marquee.
    """
    return rx.flex(
        _trust_logo("award", "R.M. 0871/2016"),
        _trust_logo("shield-check", "Título Nacional"),
        _trust_logo("users", "500+ Egresados"),
        _trust_logo("trending-up", "100% Empleabilidad"),
        _trust_logo("building-2", "15+ Convenios"),
        gap=["1.5rem", "2rem", "3rem"],
        align="center",
        justify="start",
        flex_wrap="wrap",
        width="100%",
        margin_top="4rem",
        margin_bottom="3rem",
    )


# ======================================================================
# Contenido principal del hero
# ======================================================================


def _contenido_hero() -> rx.Component:
    """
    Bloque de contenido del hero (badge + título + subtítulo + CTAs).

    Alineado a la izquierda (estilo Neon.com), no centrado.
    """
    return rx.vstack(
        # Badge superior
        _badge_plataforma(),
        # Título grande multi-línea
        _titulo_hero(),
        # Subtítulo
        rx.text(
            "Formación técnica de excelencia con títulos de Provisión "
            "Nacional. 5 carreras, laboratorios modernos y docentes "
            "especializados para que consigas tu primer empleo.",
            font_size=["0.9375rem", "1rem", "1.125rem"],
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            max_width="42rem",
            margin_top="2rem",
        ),
        # CTAs side-by-side
        rx.flex(
            _cta_primario(),
            _cta_secundario(),
            gap="0.75rem",
            margin_top="2.5rem",
            direction=rx.breakpoints(initial="column", sm="row"),
            align="start",
            justify="start",
        ),
        # Fila de trust logos
        _fila_trust_logos(),
        align="start",
        width="100%",
        max_width="72rem",
        margin="0 auto",
        padding=["3rem 1.5rem 0 1.5rem", "4rem 2rem 0 2rem", "5rem 2rem 0 2rem"],
        position="relative",
        z_index="2",
    )


# ======================================================================
# Hero principal
# ======================================================================


def hero_principal() -> rx.Component:
    """
    Hero principal del home — estilo Neon.com.

    Capas (de fondo a frente):
    1. Gradiente radial sutil.
    2. Barras verticales tipo datacenter.
    3. Contenido (badge + título + subtítulo + CTAs + trust).
    4. Marquee de iconos de carreras.

    Returns:
        Componente `rx.box` con el hero completo.
    """
    return rx.box(
        # CAPA 0-2: Fondo + orbes + barras verticales
        _capa_fondo(),
        _capa_barras_verticales(),
        # CAPA 3: Contenido principal
        _contenido_hero(),
        # CAPA 4: Marquee de iconos
        _marquee_iconos(),
        position="relative",
        width="100%",
        overflow="hidden",
        min_height=["auto", "auto", "auto"],
        background=FONDO_HOME_HERO,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "BARRAS_VERTICALES",
    "ICONOS_CARRERAS",
    "hero_principal",
]