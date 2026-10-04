"""
Paquete `dominio.estados`: estados reactivos de la aplicación.

Este paquete agrupa todos los `rx.State` del proyecto. Cada estado
tiene una responsabilidad concreta y vive en su propio módulo.

Contenido
---------
1. **estado_institucional**:   catálogo, explorador, carrusel, filtros.
2. **estado_blog**:            filtros, paginación y navegación del blog.
3. **estado_calendario**:      filtros del calendario académico.
4. **estado_acordeon_faq**:    estado del acordeón de FAQ.
5. **estado_plan_estudios**:   selector de año del plan.
6. **estado_banner_cookies**:  consentimiento de cookies.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.dominio.estados import (
        EstadoInstitucional,
        EstadoBlog,
        EstadoCalendario,
        EstadoAcordeonFaq,
        EstadoPlanEstudios,
        EstadoBannerCookies,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el módulo específico:
    from app_portada_instein.dominio.estados.estado_blog import EstadoBlog

Qué exponer y qué no
--------------------
Se exponen:
- Clases `Estado*`: son la API pública.
- Constantes de módulo relevantes (ej: `POSTS_POR_PAGINA`).
- Tipos auxiliares (`OpcionAnio`).

NO se exponen:
- Helpers privados internos de cada estado.
"""

from __future__ import annotations


# ======================================================================
# Estado del acordeón de FAQ
# ======================================================================

from .estado_acordeon_faq import EstadoAcordeonFaq

# ======================================================================
# Estado del banner de cookies
# ======================================================================

from .estado_banner_cookies import EstadoBannerCookies

# ======================================================================
# Estado del blog
# ======================================================================

from .estado_blog import (
    EstadoBlog,
    POSTS_POR_PAGINA,
)

# ======================================================================
# Estado del calendario
# ======================================================================

from .estado_calendario import (
    EstadoCalendario,
    ORDEN_MESES,
)

# ======================================================================
# Estado institucional
# ======================================================================

from .estado_institucional import (
    # Constantes
    CANTIDAD_ICONOS_FONDO,
    ETIQUETAS_CARRUSEL,
    FILTROS_VALIDOS,
    ORDENES_VALIDAS,
    SECCIONES_DETALLE_VALIDAS,
    SECCIONES_EXPLORADOR_VALIDAS,
    SEGUNDOS_ENTRE_BANNERS,
    SEMILLA_ICONOS_FONDO,
    TAMANOS_ICONOS_FONDO,
    # Estado
    EstadoInstitucional,
    # Tipos
    OpcionAnio,
)

# ======================================================================
# Estado del plan de estudios
# ======================================================================

from .estado_plan_estudios import EstadoPlanEstudios


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Constantes de estado_institucional ---
    "CANTIDAD_ICONOS_FONDO",
    "ETIQUETAS_CARRUSEL",
    "FILTROS_VALIDOS",
    "ORDENES_VALIDAS",
    "SECCIONES_DETALLE_VALIDAS",
    "SECCIONES_EXPLORADOR_VALIDAS",
    "SEGUNDOS_ENTRE_BANNERS",
    "SEMILLA_ICONOS_FONDO",
    "TAMANOS_ICONOS_FONDO",
    # --- Constantes de estado_blog ---
    "POSTS_POR_PAGINA",
    # --- Constantes de estado_calendario ---
    "ORDEN_MESES",
    # --- Estados ---
    "EstadoAcordeonFaq",
    "EstadoBannerCookies",
    "EstadoBlog",
    "EstadoCalendario",
    "EstadoInstitucional",
    "EstadoPlanEstudios",
    # --- Tipos ---
    "OpcionAnio",
]