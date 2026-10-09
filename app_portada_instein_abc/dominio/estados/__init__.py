

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