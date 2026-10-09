

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