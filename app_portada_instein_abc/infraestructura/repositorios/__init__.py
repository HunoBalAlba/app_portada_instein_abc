

from __future__ import annotations


# ======================================================================
# Repositorio de carreras
# ======================================================================

from .repositorio_carreras import (
    # Constantes
    HORARIOS_TURNO,
    PALETA_COLORES,
    PERSPECTIVA_DEFECTO,
    TURNOS_VALIDOS,
    # API pública
    carrera_existe,
    obtener_carrera_destacada,
    obtener_carrera_por_id,
    obtener_catalogo,
    obtener_ids_carreras,
    # Tipos
    CaracteristicaCarrera,
    Carrera,
    CarreraConEtiqueta,
    ColorHex,
    DemandaLaboral,
    EstadisticasCarrera,
    IconoAnimado,
    Modalidad,
    PlanAnual,
    PreguntaFrecuente,
    Turno,
)

# ======================================================================
# Repositorio del blog
# ======================================================================

from .repositorio_blog import (
    # Datos
    CATEGORIAS,
    # API pública
    obtener_post,
    obtener_post_destacado,
    obtener_posts,
    obtener_posts_por_categoria,
    # Tipos
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Repositorio de carreras: constantes
    # ==================================================================
    "HORARIOS_TURNO",
    "PALETA_COLORES",
    "PERSPECTIVA_DEFECTO",
    "TURNOS_VALIDOS",
    # ==================================================================
    # Repositorio de carreras: API pública
    # ==================================================================
    "carrera_existe",
    "obtener_carrera_destacada",
    "obtener_carrera_por_id",
    "obtener_catalogo",
    "obtener_ids_carreras",
    # ==================================================================
    # Repositorio de carreras: tipos
    # ==================================================================
    "CaracteristicaCarrera",
    "Carrera",
    "CarreraConEtiqueta",
    "ColorHex",
    "DemandaLaboral",
    "EstadisticasCarrera",
    "IconoAnimado",
    "Modalidad",
    "PlanAnual",
    "PreguntaFrecuente",
    "Turno",
    # ==================================================================
    # Repositorio del blog: datos
    # ==================================================================
    "CATEGORIAS",
    # ==================================================================
    # Repositorio del blog: API pública
    # ==================================================================
    "obtener_post",
    "obtener_post_destacado",
    "obtener_posts",
    "obtener_posts_por_categoria",
    # ==================================================================
    # Repositorio del blog: tipos
    # ==================================================================
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
]