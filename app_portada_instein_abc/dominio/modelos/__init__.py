

from __future__ import annotations


# ======================================================================
# Modelos: carrera
# ======================================================================

from .carrera import (
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
# Modelos: blog
# ======================================================================

from .blog import (
    CATEGORIAS,
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
)

# ======================================================================
# Modelos: calendario
# ======================================================================

from .calendario import (
    # Alias de tipos
    AlcanceFecha,
    SemestreAcademico,
    TipoEventoId,
    TipoFechaId,
    # Modelos
    FechaImportante,
    InfoRapida,
    OpcionFiltro,
    OpcionOrden,
    ProximoEvento,
    # Tipos (metadata)
    TIPOS_EVENTO,
    TIPOS_FECHA,
    # Datos estáticos
    FECHAS_IMPORTANTES,
    INFO_RAPIDA,
    OPCIONES_CARRERA,
    OPCIONES_ORDEN,
    OPCIONES_TIPO_EVENTO,
    PROXIMOS_EVENTOS,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Modelos: carrera
    # ==================================================================
    "ColorHex",
    "DemandaLaboral",
    "Modalidad",
    "Turno",
    "HORARIOS_TURNO",
    "TURNOS_VALIDOS",
    "CaracteristicaCarrera",
    "EstadisticasCarrera",
    "IconoAnimado",
    "PlanAnual",
    "PreguntaFrecuente",
    "Carrera",
    "CarreraConEtiqueta",
    # ==================================================================
    # Modelos: blog
    # ==================================================================
    "CATEGORIAS",
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
    # ==================================================================
    # Modelos: calendario (alias de tipos)
    # ==================================================================
    "AlcanceFecha",
    "SemestreAcademico",
    "TipoEventoId",
    "TipoFechaId",
    # ==================================================================
    # Modelos: calendario (modelos)
    # ==================================================================
    "FechaImportante",
    "InfoRapida",
    "OpcionFiltro",
    "OpcionOrden",
    "ProximoEvento",
    # ==================================================================
    # Modelos: calendario (metadata)
    # ==================================================================
    "TIPOS_EVENTO",
    "TIPOS_FECHA",
    # ==================================================================
    # Modelos: calendario (datos estáticos)
    # ==================================================================
    "FECHAS_IMPORTANTES",
    "INFO_RAPIDA",
    "OPCIONES_CARRERA",
    "OPCIONES_ORDEN",
    "OPCIONES_TIPO_EVENTO",
    "PROXIMOS_EVENTOS",
]