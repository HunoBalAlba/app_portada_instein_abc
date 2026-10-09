

from __future__ import annotations


# ======================================================================
# Sección de información
# ======================================================================

from .seccion_informacion import (
    seccion_informacion,
)

# ======================================================================
# Sección de perfil y campo laboral
# ======================================================================

from .seccion_perfil import (
    seccion_perfil_y_campo_laboral,
)

# ======================================================================
# Sección de plan de estudios
# ======================================================================

from .seccion_plan import (
    seccion_plan_estudios,
)


# ======================================================================
# API pública del subpaquete
# ======================================================================

__all__ = [
    "seccion_informacion",
    "seccion_perfil_y_campo_laboral",
    "seccion_plan_estudios",
]