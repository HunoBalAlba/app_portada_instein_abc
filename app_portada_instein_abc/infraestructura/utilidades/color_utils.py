

from __future__ import annotations

import re


# ======================================================================
# Constantes locales
# ======================================================================

PATRON_HEX: re.Pattern[str] = re.compile(r"^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")
"""Patrón para validar colores hex (3 o 6 dígitos)."""


# ======================================================================
# 1. Validación
# ======================================================================


def es_hex_valido(color: str) -> bool:
    """
    Verifica si un string es un color hex válido.

    Acepta formatos de 3 o 6 dígitos, con o sin `#`.

    Args:
        color: String a validar.

    Returns:
        `True` si es un hex válido, `False` en caso contrario.

    Examples:
        >>> es_hex_valido("#3b5bdb")
        True
        >>> es_hex_valido("#fff")
        True
        >>> es_hex_valido("3b5bdb")
        True
        >>> es_hex_valido("#xyz")
        False
    """
    return bool(PATRON_HEX.match(color.strip()))


def _normalizar_hex(color: str) -> str:
    """
    Normaliza un color hex a formato `#RRGGBB` (6 dígitos con `#`).

    Args:
        color: Hex en cualquier formato soportado.

    Returns:
        Hex normalizado `#RRGGBB` en minúsculas.

    Raises:
        ValueError: Si el color no es un hex válido.

    Examples:
        >>> _normalizar_hex("#fff")
        '#ffffff'
        >>> _normalizar_hex("3b5bdb")
        '#3b5bdb'
    """
    if not es_hex_valido(color):
        raise ValueError(f"Color hex inválido: {color!r}")

    codigo = color.strip().lstrip("#").lower()

    # Expansión de 3 a 6 dígitos: "#abc" → "#aabbcc"
    if len(codigo) == 3:
        codigo = "".join(c * 2 for c in codigo)

    return f"#{codigo}"


# ======================================================================
# 2. Inversión de color
# ======================================================================


def invertir_color_hexadecimal(color_hexadecimal: str) -> str:
    """
    Invierte un color hexadecimal (255 - cada canal).

    Args:
        color_hexadecimal: Color en formato `#RRGGBB` o `#RGB`.

    Returns:
        Color invertido en formato `#rrggbb` (minúsculas).

    Raises:
        ValueError: Si el color no tiene 6 (o 3) dígitos hexadecimales.

    Examples:
        >>> invertir_color_hexadecimal("#9ebae4")
        '#61451b'
        >>> invertir_color_hexadecimal("#ffffff")
        '#000000'
        >>> invertir_color_hexadecimal("#000")
        '#ffffff'
    """
    normalizado = _normalizar_hex(color_hexadecimal)
    codigo = normalizado.lstrip("#")

    rojo = 255 - int(codigo[0:2], 16)
    verde = 255 - int(codigo[2:4], 16)
    azul = 255 - int(codigo[4:6], 16)

    return f"#{rojo:02x}{verde:02x}{azul:02x}"


# ======================================================================
# 3. Conversión hex ↔ RGB
# ======================================================================


def hex_a_rgb(color_hexadecimal: str) -> tuple[int, int, int]:
    """
    Convierte un color hex a una tupla RGB.

    Args:
        color_hexadecimal: Color en formato `#RRGGBB` o `#RGB`.

    Returns:
        Tupla `(r, g, b)` con valores 0-255.

    Raises:
        ValueError: Si el color no es un hex válido.

    Examples:
        >>> hex_a_rgb("#3b5bdb")
        (59, 91, 219)
        >>> hex_a_rgb("#fff")
        (255, 255, 255)
    """
    normalizado = _normalizar_hex(color_hexadecimal)
    codigo = normalizado.lstrip("#")

    return (
        int(codigo[0:2], 16),
        int(codigo[2:4], 16),
        int(codigo[4:6], 16),
    )


def rgb_a_hex(rojo: int, verde: int, azul: int) -> str:
    """
    Convierte una tupla RGB a hex.

    Args:
        rojo: Canal rojo (0-255).
        verde: Canal verde (0-255).
        azul: Canal azul (0-255).

    Returns:
        Color hex `#rrggbb` en minúsculas.

    Raises:
        ValueError: Si algún canal está fuera de rango.

    Examples:
        >>> rgb_a_hex(59, 91, 219)
        '#3b5bdb'
        >>> rgb_a_hex(255, 255, 255)
        '#ffffff'
    """
    if not all(0 <= canal <= 255 for canal in (rojo, verde, azul)):
        raise ValueError(
            f"Canales RGB deben estar en rango 0-255: "
            f"({rojo}, {verde}, {azul})"
        )

    return f"#{rojo:02x}{verde:02x}{azul:02x}"


# ======================================================================
# 4. Ajustar luminosidad
# ======================================================================


def aclarar_color(color_hexadecimal: str, factor: float = 0.2) -> str:
    """
    Aclara un color mezclándolo con blanco.

    Args:
        color_hexadecimal: Color en formato hex.
        factor: Cantidad de blanco a mezclar (0.0 = sin cambio,
            1.0 = blanco puro). Por defecto 0.2.

    Returns:
        Color aclarado en formato `#rrggbb`.

    Raises:
        ValueError: Si `factor` está fuera de rango.

    Examples:
        >>> aclarar_color("#3b5bdb", 0.5)
        '#9cadeb'
    """
    if not 0.0 <= factor <= 1.0:
        raise ValueError(f"factor debe estar en [0.0, 1.0]: {factor}")

    r, g, b = hex_a_rgb(color_hexadecimal)

    r_nuevo = int(r + (255 - r) * factor)
    g_nuevo = int(g + (255 - g) * factor)
    b_nuevo = int(b + (255 - b) * factor)

    return rgb_a_hex(r_nuevo, g_nuevo, b_nuevo)


def oscurecer_color(color_hexadecimal: str, factor: float = 0.2) -> str:
    """
    Oscurece un color mezclándolo con negro.

    Args:
        color_hexadecimal: Color en formato hex.
        factor: Cantidad de negro a mezclar (0.0 = sin cambio,
            1.0 = negro puro). Por defecto 0.2.

    Returns:
        Color oscurecido en formato `#rrggbb`.

    Raises:
        ValueError: Si `factor` está fuera de rango.

    Examples:
        >>> oscurecer_color("#3b5bdb", 0.5)
        '#1d2d6d'
    """
    if not 0.0 <= factor <= 1.0:
        raise ValueError(f"factor debe estar en [0.0, 1.0]: {factor}")

    r, g, b = hex_a_rgb(color_hexadecimal)

    r_nuevo = int(r * (1 - factor))
    g_nuevo = int(g * (1 - factor))
    b_nuevo = int(b * (1 - factor))

    return rgb_a_hex(r_nuevo, g_nuevo, b_nuevo)


# ======================================================================
# 5. Mezcla de colores
# ======================================================================


def mezclar_colores(
    color_a: str,
    color_b: str,
    factor: float = 0.5,
) -> str:
    """
    Mezcla dos colores lineálmente.

    Args:
        color_a: Primer color (hex).
        color_b: Segundo color (hex).
        factor: Peso del segundo color (0.0 = solo `color_a`,
            1.0 = solo `color_b`). Por defecto 0.5 (mezcla 50/50).

    Returns:
        Color mezclado en formato `#rrggbb`.

    Raises:
        ValueError: Si `factor` está fuera de rango.

    Examples:
        >>> mezclar_colores("#000000", "#ffffff", 0.5)
        '#808080'
    """
    if not 0.0 <= factor <= 1.0:
        raise ValueError(f"factor debe estar en [0.0, 1.0]: {factor}")

    r_a, g_a, b_a = hex_a_rgb(color_a)
    r_b, g_b, b_b = hex_a_rgb(color_b)

    r = int(r_a * (1 - factor) + r_b * factor)
    g = int(g_a * (1 - factor) + g_b * factor)
    b = int(b_a * (1 - factor) + b_b * factor)

    return rgb_a_hex(r, g, b)


# ======================================================================
# 6. Contraste WCAG
# ======================================================================


def _luminancia_relativa(color_hexadecimal: str) -> float:
    """
    Calcula la luminancia relativa de un color (WCAG 2.1).

    Args:
        color_hexadecimal: Color en formato hex.

    Returns:
        Luminancia relativa (0.0 = negro, 1.0 = blanco).
    """

    def _canal_linealizado(canal: int) -> float:
        """Linealiza un canal RGB según WCAG."""
        c = canal / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = hex_a_rgb(color_hexadecimal)

    return (
        0.2126 * _canal_linealizado(r)
        + 0.7152 * _canal_linealizado(g)
        + 0.0722 * _canal_linealizado(b)
    )


def calcular_contraste(color_a: str, color_b: str) -> float:
    """
    Calcula el ratio de contraste WCAG entre dos colores.

    Args:
        color_a: Primer color (hex).
        color_b: Segundo color (hex).

    Returns:
        Ratio de contraste (1.0 a 21.0).

    Examples:
        >>> round(calcular_contraste("#000000", "#ffffff"), 2)
        21.0
        >>> round(calcular_contraste("#3b5bdb", "#ffffff"), 2)
        5.74
    """
    lum_a = _luminancia_relativa(color_a)
    lum_b = _luminancia_relativa(color_b)

    mas_claro = max(lum_a, lum_b)
    mas_oscuro = min(lum_a, lum_b)

    return (mas_claro + 0.05) / (mas_oscuro + 0.05)


def cumple_contraste_wcag_aa(
    color_texto: str,
    color_fondo: str,
    tamano_grande: bool = False,
) -> bool:
    """
    Verifica si un par texto/fondo cumple WCAG 2.1 AA.

    Args:
        color_texto: Color del texto (hex).
        color_fondo: Color del fondo (hex).
        tamano_grande: Si `True`, aplica el umbral de texto grande
            (≥ 18pt normal o ≥ 14pt bold). Si `False`, aplica el
            umbral de texto normal.

    Returns:
        `True` si cumple el umbral, `False` en caso contrario.

    Examples:
        >>> cumple_contraste_wcag_aa("#000000", "#ffffff")
        True
        >>> cumple_contraste_wcag_aa("#cccccc", "#ffffff")
        False
    """
    umbral = 3.0 if tamano_grande else 4.5
    return calcular_contraste(color_texto, color_fondo) >= umbral


# ======================================================================
# 7. Conversión a RGBA (con opacidad)
# ======================================================================


def hex_a_rgba(
    color_hexadecimal: str,
    opacidad: float = 1.0,
) -> str:
    """
    Convierte un hex a formato `rgba()` con opacidad.

    Args:
        color_hexadecimal: Color en formato hex.
        opacidad: Valor de opacidad (0.0 a 1.0). Por defecto 1.0.

    Returns:
        String `rgba(r, g, b, a)`.

    Raises:
        ValueError: Si `opacidad` está fuera de rango.

    Examples:
        >>> hex_a_rgba("#3b5bdb", 0.5)
        'rgba(59, 91, 219, 0.5)'
    """
    if not 0.0 <= opacidad <= 1.0:
        raise ValueError(f"opacidad debe estar en [0.0, 1.0]: {opacidad}")

    r, g, b = hex_a_rgb(color_hexadecimal)

    return f"rgba({r}, {g}, {b}, {opacidad})"


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "PATRON_HEX",
    "aclarar_color",
    "calcular_contraste",
    "cumple_contraste_wcag_aa",
    "es_hex_valido",
    "hex_a_rgb",
    "hex_a_rgba",
    "invertir_color_hexadecimal",
    "mezclar_colores",
    "oscurecer_color",
    "rgb_a_hex",
]