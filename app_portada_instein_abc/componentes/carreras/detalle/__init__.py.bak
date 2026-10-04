"""
Subpaquete `componentes.carreras.detalle`: secciones del detalle.

Agrupa las 3 secciones que componen la vista de detalle de carrera
(`/carrera/{id}`):

- **seccion_informacion**:  descripción + datos rápidos + CTA.
- **seccion_plan**:         selector de año + progreso + materias.
- **seccion_perfil**:       perfil profesional + campo laboral.

Estas secciones se muestran como pestañas en la vista de detalle
(`Tabs`: Info · Plan · Perfil).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el subpaquete:
    from app_portada_instein.componentes.carreras.detalle import (
        seccion_informacion,
        seccion_plan_estudios,
        seccion_perfil_y_campo_laboral,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.componentes.carreras.detalle.seccion_plan import (
        seccion_plan_estudios,
    )

Nota técnica: `EstadoPlanEstudios`
----------------------------------
El State del selector segmentado de años vive en
`dominio.estados.estado_plan_estudios`. NO se exporta desde aquí.

Qué NO exponer aquí
-------------------
- Estados de Reflex: viven en `dominio.estados`.
- Modelos de datos: viven en `dominio.modelos`.
- Constantes visuales: viven en `infraestructura.constantes`.

Este subpaquete SOLO expone componentes de UI puros.
"""

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