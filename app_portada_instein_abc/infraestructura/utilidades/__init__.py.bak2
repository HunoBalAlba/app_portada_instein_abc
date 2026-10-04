"""
Paquete `infraestructura.utilidades`: helpers transversales.

Contiene funciones utilitarias puras (sin dependencias de Reflex ni
de la UI) que se usan en múltiples capas del proyecto:

1. **color_utils**: manipulación de colores hex/rgb/hsl.
2. **formatos**:    formateo de texto, números y slugs.

Filosofía
---------
- **Puras**:          sin efectos secundarios.
- **Deterministas**:  mismo input → mismo output.
- **Sin dependencias externas**: solo stdlib.
- **Testeables**:     fáciles de cubrir con pytest.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.infraestructura.utilidades import (
        invertir_color_hexadecimal,
        formatear_numero,
        pluralizar,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el módulo específico:
    from app_portada_instein.infraestructura.utilidades.color_utils import (
        invertir_color_hexadecimal,
    )
"""

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