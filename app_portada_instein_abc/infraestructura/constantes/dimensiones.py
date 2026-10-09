

from __future__ import annotations


# ======================================================================
# 1. Radios (border-radius)
# ======================================================================

RADIO_PEQUENO: str = "0.5rem"
"""Radio para chips y elementos compactos."""

RADIO_MEDIO: str = "0.75rem"
"""Radio para botones, inputs y cards pequeñas."""

RADIO_GRANDE: str = "1rem"
"""Radio para cards medianas y contenedores."""

RADIO_EXTRA_GRANDE: str = "1.5rem"
"""Radio para cards grandes, diálogos y banners."""

RADIO_PASTILLA: str = "9999px"
"""Radio para pills, badges y avatares circulares."""

RADIO_BORDE: str = "var(--radius-2)"
"""Radio basado en el token del tema (`rx.theme(radius=...)`).

- Adapta al `radius` configurado en `rx.theme()`.
- Úsalo para tarjetas e inputs que deben seguir el tema global.
"""


# ======================================================================
# 2. Sombras (box-shadow)
# ======================================================================

SOMBRA_SUAVE: str = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
"""Sombra sutil para tarjetas en reposo."""

SOMBRA_MEDIA: str = "0 4px 12px -2px rgba(0, 0, 255, 0.25)"
"""Sombra media con tinte azul para hover de tarjetas."""

SOMBRA_FUERTE: str = "0 10px 25px -5px rgba(0, 0, 255, 0.20)"
"""Sombra elevada para modales y elementos flotantes."""

SOMBRA_CAJA: str = (
    "0 1px 3px 0 rgba(0, 0, 0, 0.1), "
    "0 1px 2px -1px rgba(0, 0, 0, 0.1)"
)
"""Sombra de dos capas, típica de tarjetas estilo Tailwind."""

SOMBRA_GLOW_AZUL: str = "0 0 20px rgba(59, 91, 219, 0.5)"
"""Glow azul marino para elementos con acento."""


# ======================================================================
# 3. Anchos (width / max-width)
# ======================================================================

ANCHO_CONTENIDO_VW: str = "90vw"
"""Ancho del contenido en viewport units (para casos especiales)."""

ANCHO_MENU_LATERAL: str = "32em"
"""Ancho del menú lateral desplegable (32em ≈ 512px)."""

ANCHO_CONTENIDO_MENU: str = "16em"
"""Ancho del contenido interno del menú lateral."""

ANCHO_MAXIMO: str = "1480px"
"""Ancho máximo global de la app (para pantallas ultra-wide)."""

ANCHO_CONTENIDO: str = "72rem"
"""Ancho máximo estándar del contenido principal (72rem ≈ 1152px)."""

ANCHO_SECCION: str = "64rem"
"""Ancho máximo de secciones internas (64rem ≈ 1024px)."""

ANCHO_LECTURA: str = "65ch"
"""Ancho óptimo de columna de lectura (65ch ≈ 650 caracteres)."""


# ======================================================================
# 4. Espaciados (padding, gap, margin)
# ======================================================================

PADDING_LATERAL: str = "1.5rem"
"""Padding lateral estándar del contenido (24px)."""

PADDING_LATERAL_MOVIL: str = "1rem"
"""Padding lateral reducido para móvil (16px)."""

PADDING_SECCION: str = "4rem 1.5rem"
"""Padding vertical + horizontal de secciones principales."""

PADDING_TARJETA: str = "1.25rem"
"""Padding interno de tarjetas estándar (20px)."""

GAP_PEQUENO: str = "0.5rem"
"""Gap pequeño entre elementos relacionados (8px)."""

GAP_MEDIO: str = "1rem"
"""Gap medio entre bloques (16px)."""

GAP_GRANDE: str = "1.5rem"
"""Gap grande entre secciones (24px)."""


# ======================================================================
# 5. Tamaños (cajas específicas)
# ======================================================================

TAMANOS_CAJA_COLOR: list[str] = ["2.25rem", "2.25rem", "2.5rem"]
"""Tamaños de la caja de color del theme switcher (responsive)."""

TAMANO_LOGO: str = "2rem"
"""Tamaño del badge del logo institucional."""

TAMANO_BOTON_FLOTANTE: str = "3.5rem"
"""Tamaño del botón flotante del panel de selección."""

TAMANO_ICONO_ESTADO_VACIO: int = 48
"""Tamaño del icono del estado vacío (px)."""


# ======================================================================
# 6. Radios de breakpoints (referencia)
# ======================================================================

BREAKPOINTS_RADIX: list[str] = ["initial", "sm", "md", "lg", "xl"]
"""Nombres canónicos de los breakpoints de Radix Themes.

Úsalos como referencia al construir `rx.breakpoints(...)`:

    columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4")
"""


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Radios ---
    "RADIO_BORDE",
    "RADIO_EXTRA_GRANDE",
    "RADIO_GRANDE",
    "RADIO_MEDIO",
    "RADIO_PASTILLA",
    "RADIO_PEQUENO",
    # --- Sombras ---
    "SOMBRA_CAJA",
    "SOMBRA_FUERTE",
    "SOMBRA_GLOW_AZUL",
    "SOMBRA_MEDIA",
    "SOMBRA_SUAVE",
    # --- Anchos ---
    "ANCHO_CONTENIDO",
    "ANCHO_CONTENIDO_MENU",
    "ANCHO_CONTENIDO_VW",
    "ANCHO_LECTURA",
    "ANCHO_MAXIMO",
    "ANCHO_MENU_LATERAL",
    "ANCHO_SECCION",
    # --- Espaciados ---
    "GAP_GRANDE",
    "GAP_MEDIO",
    "GAP_PEQUENO",
    "PADDING_LATERAL",
    "PADDING_LATERAL_MOVIL",
    "PADDING_SECCION",
    "PADDING_TARJETA",
    # --- Tamaños ---
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_LOGO",
    "TAMANOS_CAJA_COLOR",
    # --- Referencia de breakpoints ---
    "BREAKPOINTS_RADIX",
]