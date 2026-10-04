"""
Modelos de carreras técnicas.

Este módulo re-exporta los tipos definidos en
`infraestructura.repositorios.repositorio_carreras` para que la ruta
canónica de importación sea `dominio.modelos.carrera`.

Decisión arquitectónica
-----------------------
Los modelos `Carrera`, `PlanAnual`, `IconoAnimado`, etc. **NO se
duplican** aquí. Viven en `repositorio_carreras.py` junto con los
datos del catálogo. Este módulo solo expone la API pública.

Motivo: mantener una sola fuente de verdad para cada tipo. Si el
tipo cambia (ej: añadir un campo), se toca un solo lugar.

Convención de imports
---------------------
✅ **RECOMENDADO** — importar desde aquí:
    from app_portada_instein.dominio.modelos.carrera import (
        Carrera,
        PlanAnual,
        IconoAnimado,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el repositorio:
    from app_portada_instein.infraestructura.repositorios import (
        Carrera,
        PlanAnual,
    )

❌ **EVITAR** — importar desde módulos internos.
"""

from __future__ import annotations


# ======================================================================
# Re-export de tipos
# ======================================================================

from ...infraestructura.repositorios.repositorio_carreras import (
    # Alias de tipos
    ColorHex,
    DemandaLaboral,
    Modalidad,
    Turno,
    # Constantes
    HORARIOS_TURNO,
    TURNOS_VALIDOS,
    # Modelos anidados
    CaracteristicaCarrera,
    EstadisticasCarrera,
    IconoAnimado,
    PlanAnual,
    PreguntaFrecuente,
    # Modelos principales
    Carrera,
    CarreraConEtiqueta,
)


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Alias de tipos ---
    "ColorHex",
    "DemandaLaboral",
    "Modalidad",
    "Turno",
    # --- Constantes ---
    "HORARIOS_TURNO",
    "TURNOS_VALIDOS",
    # --- Modelos anidados ---
    "CaracteristicaCarrera",
    "EstadisticasCarrera",
    "IconoAnimado",
    "PlanAnual",
    "PreguntaFrecuente",
    # --- Modelos principales ---
    "Carrera",
    "CarreraConEtiqueta",
]