"""
Paquete `componentes.calendario`: componentes del Calendario Académico.

Contenido
---------
- **hero**:            hero + grid de info rápida.
- **cta**:             CTA final hacia /contacto.
- **tabs**:            ensamblador de los 2 tabs (Actividades + Fechas).
- **tabs_instituto**:  tab de actividades con timeline y filtros.
- **tabs_fechas**:     tab de fechas importantes de Bolivia.
- **filtros**:         barra de filtros del tab de actividades.
- **helpers**:         metadatos visuales por tipo de evento/fecha.

Nota técnica: DATOS Y ESTADOS
----------------------------
- Datos estáticos: `dominio.modelos.calendario`.
- State: `dominio.estados.estado_calendario`.

Este paquete SOLO expone UI pura.

Convención de imports
---------------------
✅ **CORRECTO**:
    from app_portada_instein.componentes.calendario import (
        cta_calendario,
        grid_info_rapida,
        hero_calendario,
        tabs_calendario,
    )

❌ **EVITAR** — importar desde módulos internos.
"""

from __future__ import annotations


# ======================================================================
# CTA final
# ======================================================================

from .cta import cta_calendario

# ======================================================================
# Hero + grid de info rápida
# ======================================================================

from .hero import (
    INFO_RAPIDA,
    InfoRapida,
    grid_info_rapida,
    hero_calendario,
)

# ======================================================================
# Tabs
# ======================================================================

from .tabs import tabs_calendario


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Datos ---
    "INFO_RAPIDA",
    "InfoRapida",
    # --- Hero + grid ---
    "grid_info_rapida",
    "hero_calendario",
    # --- Tabs ---
    "tabs_calendario",
    # --- CTA ---
    "cta_calendario",
]