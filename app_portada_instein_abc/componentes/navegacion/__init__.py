

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