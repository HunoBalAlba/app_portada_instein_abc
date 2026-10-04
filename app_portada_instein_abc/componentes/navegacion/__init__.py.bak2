"""
Paquete `componentes.navegacion`: barra de navegación y pie de página.

Contenido
---------
- **barra_navegacion**: barra superior sticky con logo, menú y toggle
  de color mode.
- **pie_pagina**:       footer institucional con brand, newsletter,
  grid de enlaces y barra inferior.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.componentes.navegacion import (
        barra_navegacion_superior,
        pie_pagina_institucional,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.componentes.navegacion.barra_navegacion import (
        barra_navegacion_superior,
    )

Motivo: permite refactorizar la estructura interna sin romper
consumidores, siempre que la API pública se mantenga.

Qué NO exponer aquí
-------------------
- Estados de Reflex: viven en `dominio.estados`.
- Modelos de datos: viven en `dominio.modelos`.
- Constantes visuales: viven en `infraestructura.constantes`.

Este paquete SOLO expone componentes de navegación/estructura.
"""

from __future__ import annotations


# ======================================================================
# Barra de navegación
# ======================================================================

from ...componentes.navegacion.barra_navegacion import (
    barra_navegacion_superior,
    elemento_menu,
)

# ======================================================================
# Pie de página
# ======================================================================

from ...componentes.navegacion.pie_pagina import (
    ColumnaFooter,
    ENLACES_FOOTER,
    ItemEnlaceFooter,
    pie_pagina_institucional,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Barra de navegación ---
    "barra_navegacion_superior",
    "elemento_menu",
    # --- Pie de página ---
    "ColumnaFooter",
    "ENLACES_FOOTER",
    "ItemEnlaceFooter",
    "pie_pagina_institucional",
]