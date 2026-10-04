"""
Paquete `dominio.modelos`: modelos tipados del dominio.

Este paquete es la **ruta canónica** de importación para todos los
tipos que describen las entidades del dominio:

1. **carrera**:    carrera técnica + plan de estudios + métricas.
2. **blog**:       posts y categorías del blog.
3. **calendario**: eventos del instituto + fechas importantes.

Filosofía
---------
Los modelos son `TypedDict` (no `dataclass` ni `BaseModel`) para:
- Compatibilidad total con `rx.foreach`.
- Sin dependencias externas.
- Serialización JSON trivial.

Dónde viven realmente los tipos
-------------------------------
Los modelos se **definen** en `infraestructura.repositorios.*` (junto
con sus datos) y se **re-exportan** aquí para dar una ruta canónica
desde la capa de dominio.

Esto evita duplicar definiciones y mantiene una sola fuente de verdad
por tipo.

Convención de imports
---------------------
✅ **RECOMENDADO** — importar desde aquí:
    from app_portada_instein.dominio.modelos import (
        # Carrera
        Carrera,
        PlanAnual,
        # Blog
        Post,
        Categoria,
        # Calendario
        ProximoEvento,
        FechaImportante,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el submódulo:
    from app_portada_instein.dominio.modelos.blog import Post

❌ **EVITAR** — importar desde el repositorio:
    from app_portada_instein.infraestructura.repositorios import Post

Motivo: la ruta canónica es `dominio.modelos`; el repositorio es un
detalle de implementación de la capa de infraestructura.
"""

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