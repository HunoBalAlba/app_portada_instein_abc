

from __future__ import annotations


# ======================================================================
# Utilidades de color
# ======================================================================

from .color_utils import (
    PATRON_HEX,
    aclarar_color,
    calcular_contraste,
    cumple_contraste_wcag_aa,
    es_hex_valido,
    hex_a_rgb,
    hex_a_rgba,
    invertir_color_hexadecimal,
    mezclar_colores,
    oscurecer_color,
    rgb_a_hex,
)

# ======================================================================
# Utilidades de formato
# ======================================================================

from .formatos import (
    capitalizar_primera,
    formatear_numero,
    formatear_porcentaje,
    formatear_salario,
    iniciales,
    pluralizar,
    slugify,
    titulo_case,
    truncar_texto,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Utilidades de color
    # ==================================================================
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
    # ==================================================================
    # Utilidades de formato
    # ==================================================================
    "capitalizar_primera",
    "formatear_numero",
    "formatear_porcentaje",
    "formatear_salario",
    "iniciales",
    "pluralizar",
    "slugify",
    "titulo_case",
    "truncar_texto",
]