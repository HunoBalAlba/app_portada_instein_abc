

from __future__ import annotations

import reflex as rx


# ======================================================================
# 1. Acento de marca (azul marino neon)
# ======================================================================

AZUL_MARINO_HEX: str = "#000080"
"""Azul marino puro (referencia histórica)."""

AZUL_MARINO_NEON: str = "#3b5bdb"
"""Azul marino neon — ÚNICO acento del proyecto."""

AZUL_MARINO_PROFUNDO: str = "#0a0f2e"
"""Azul marino oscurecido (para gradientes en dark)."""

AZUL_MARINO_CLARO: str = "#1a237e"
"""Azul marino aclarado (para gradientes en light)."""

ACCENT_COLOR_TEMA: str = "blue"
"""Nombre del `accent_color` para `rx.theme(accent_color=...)`."""


# ======================================================================
# 2. Paleta semántica Radix (adaptativa automática)
# ======================================================================

# --- Texto ---
COLOR_TEXTO_PRINCIPAL = rx.color("gray", 12)
COLOR_TEXTO_SECUNDARIO = rx.color("gray", 11)
COLOR_TEXTO_CUERPO = rx.color("gray", 11)
COLOR_TEXTO_APAGADO = rx.color("gray", 10)

# --- Fondos ---
COLOR_FONDO_CARTA = rx.color("gray", 1)
COLOR_FONDO_SUAVE = rx.color("gray", 2)
COLOR_FONDO_GRIS = rx.color("gray", 3)

# --- Bordes ---
COLOR_BORDE_SUAVE = rx.color("gray", 6)
COLOR_BORDE_HOVER = rx.color("gray", 7)
COLOR_BORDE_ACTIVO = rx.color("gray", 8)
COLOR_DIVISOR = rx.color("gray", 4)
BORDE_PREDETERMINADO: str = f"1px solid {COLOR_BORDE_SUAVE}"

# --- Acento (tokens Radix para blue) ---
COLOR_ACENTO_SOLIDO = rx.color("blue", 9)
COLOR_ACENTO_TEXTO_SOLIDO = "var(--blue-9-contrast)"
COLOR_ACENTO_TEXTO = rx.color("blue", 11)
COLOR_ACENTO_FONDO = rx.color("blue", 3)
COLOR_ACENTO_BORDE = rx.color("blue", 7)

# --- Estados semánticos ---
COLOR_EXITO_TEXTO = rx.color("green", 11)
COLOR_EXITO_FONDO = rx.color("green", 3)
COLOR_EXITO_SOLIDO = rx.color("green", 9)

COLOR_ALERTA_TEXTO = rx.color("amber", 11)
COLOR_ALERTA_FONDO = rx.color("amber", 3)

COLOR_ERROR_TEXTO = rx.color("red", 11)
COLOR_ERROR_FONDO = rx.color("red", 3)


# ======================================================================
# 3. Tokens adaptativos del home
# ======================================================================

# --- Fondos ---
FONDO_HOME = rx.color_mode_cond(light="#f8fafc", dark="#0a0f1f")

FONDO_HOME_HERO = rx.color_mode_cond(
    light="linear-gradient(135deg, #f8fafc 0%, #e0e7ff 50%, #c7d2fe 100%)",
    dark="linear-gradient(135deg, #0a0f1f 0%, #0f172a 50%, #1a237e 100%)",
)

FONDO_HOME_CARD = rx.color_mode_cond(
    light="rgba(255, 255, 255, 0.8)",
    dark="rgba(15, 23, 42, 0.6)",
)

FONDO_BARRA_HOME = rx.color_mode_cond(
    light="rgba(255, 255, 255, 0.75)",
    dark="rgba(10, 15, 31, 0.75)",
)

FONDO_AZUL_SUAVE = rx.color_mode_cond(
    light="rgba(59, 91, 219, 0.10)",
    dark="rgba(59, 91, 219, 0.15)",
)

FONDO_AZUL_MUY_SUAVE = rx.color_mode_cond(
    light="rgba(59, 91, 219, 0.05)",
    dark="rgba(59, 91, 219, 0.10)",
)

# --- Texto ---
TEXTO_HOME_PRINCIPAL = rx.color_mode_cond(
    light="#0f172a",
    dark="#ffffff",
)

TEXTO_HOME_SUAVE = rx.color_mode_cond(
    light="rgba(15, 23, 42, 0.75)",
    dark="rgba(255, 255, 255, 0.8)",
)

TEXTO_HOME_MAS_SUAVE = rx.color_mode_cond(
    light="rgba(15, 23, 42, 0.6)",
    dark="rgba(255, 255, 255, 0.6)",
)

# --- Bordes ---
BORDE_HOME_SUAVE = rx.color_mode_cond(
    light="rgba(15, 23, 42, 0.10)",
    dark="rgba(255, 255, 255, 0.08)",
)

BORDE_HOME_MEDIO = rx.color_mode_cond(
    light="rgba(15, 23, 42, 0.15)",
    dark="rgba(255, 255, 255, 0.15)",
)

BORDE_HOME_AZUL = rx.color_mode_cond(
    light="rgba(59, 91, 219, 0.5)",
    dark="rgba(59, 91, 219, 0.4)",
)

# --- Gradientes ---
GRADIENTE_TEXTO_HOME = rx.color_mode_cond(
    light="linear-gradient(135deg, #1a237e 0%, #3b5bdb 100%)",
    dark="linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%)",
)

GRADIENTE_HOME_BANNER = rx.color_mode_cond(
    light="linear-gradient(135deg, #eef2ff 0%, #c7d2fe 50%, #a5b4fc 100%)",
    dark="linear-gradient(135deg, #0a0f1f 0%, #0f172a 50%, #1a237e 100%)",
)

# --- Sombras ---
SOMBRA_HOVER_CARD_HOME = rx.color_mode_cond(
    light=f"0 20px 40px -10px {AZUL_MARINO_NEON}40",
    dark=f"0 20px 40px -10px {AZUL_MARINO_NEON}",
)


# ======================================================================
# 4. Alias retrocompatibles
# ======================================================================

FONDO_HOME_CARD_ADAPTATIVO = FONDO_HOME_CARD
"""Alias retrocompatible de `FONDO_HOME_CARD`.

⚠️ DEPRECADO: usar `FONDO_HOME_CARD`.
Se mantiene para no romper imports existentes en componentes.
"""


# ======================================================================
# 5. Helper de categorías semánticas
# ======================================================================


def color_categoria(scheme: str, nivel: int = 11) -> rx.Var:
    """
    Devuelve un color Radix para una categoría semántica.

    Args:
        scheme: Nombre del scheme ("blue", "green", "amber", ...).
        nivel: Step de Radix (1-12).

    Returns:
        Var de color adaptativa al color_mode.

    Examples:
        >>> color_categoria("blue", 11)      # texto
        >>> color_categoria("green", 3)      # fondo
        >>> color_categoria("amber", 7)      # borde
    """
    return rx.color(scheme, nivel)


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Acento de marca ---
    "ACCENT_COLOR_TEMA",
    "AZUL_MARINO_CLARO",
    "AZUL_MARINO_HEX",
    "AZUL_MARINO_NEON",
    "AZUL_MARINO_PROFUNDO",
    # --- Paleta semántica: texto ---
    "COLOR_TEXTO_APAGADO",
    "COLOR_TEXTO_CUERPO",
    "COLOR_TEXTO_PRINCIPAL",
    "COLOR_TEXTO_SECUNDARIO",
    # --- Paleta semántica: fondos ---
    "COLOR_FONDO_CARTA",
    "COLOR_FONDO_GRIS",
    "COLOR_FONDO_SUAVE",
    # --- Paleta semántica: bordes ---
    "BORDE_PREDETERMINADO",
    "COLOR_BORDE_ACTIVO",
    "COLOR_BORDE_HOVER",
    "COLOR_BORDE_SUAVE",
    "COLOR_DIVISOR",
    # --- Paleta semántica: acento ---
    "COLOR_ACENTO_BORDE",
    "COLOR_ACENTO_FONDO",
    "COLOR_ACENTO_SOLIDO",
    "COLOR_ACENTO_TEXTO",
    "COLOR_ACENTO_TEXTO_SOLIDO",
    # --- Paleta semántica: estados ---
    "COLOR_ALERTA_FONDO",
    "COLOR_ALERTA_TEXTO",
    "COLOR_ERROR_FONDO",
    "COLOR_ERROR_TEXTO",
    "COLOR_EXITO_FONDO",
    "COLOR_EXITO_SOLIDO",
    "COLOR_EXITO_TEXTO",
    # --- Tokens adaptativos: fondos ---
    "FONDO_AZUL_MUY_SUAVE",
    "FONDO_AZUL_SUAVE",
    "FONDO_BARRA_HOME",
    "FONDO_HOME",
    "FONDO_HOME_CARD",
    "FONDO_HOME_CARD_ADAPTATIVO",   # ← alias retrocompatible
    "FONDO_HOME_HERO",
    # --- Tokens adaptativos: textos ---
    "TEXTO_HOME_MAS_SUAVE",
    "TEXTO_HOME_PRINCIPAL",
    "TEXTO_HOME_SUAVE",
    # --- Tokens adaptativos: bordes ---
    "BORDE_HOME_AZUL",
    "BORDE_HOME_MEDIO",
    "BORDE_HOME_SUAVE",
    # --- Tokens adaptativos: gradientes ---
    "GRADIENTE_HOME_BANNER",
    "GRADIENTE_TEXTO_HOME",
    # --- Tokens adaptativos: sombras ---
    "SOMBRA_HOVER_CARD_HOME",
    # --- Helper ---
    "color_categoria",
]