

from __future__ import annotations


# ======================================================================
# Modelos (tipos y datos estáticos)
# ======================================================================

from .modelos import (
    # --- Modelos: carrera ---
    CaracteristicaCarrera,
    Carrera,
    CarreraConEtiqueta,
    ColorHex,
    DemandaLaboral,
    EstadisticasCarrera,
    HORARIOS_TURNO,
    IconoAnimado,
    Modalidad,
    PlanAnual,
    PreguntaFrecuente,
    TURNOS_VALIDOS,
    Turno,
    # --- Modelos: blog ---
    CATEGORIAS,
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
    # --- Modelos: calendario (alias de tipos) ---
    AlcanceFecha,
    SemestreAcademico,
    TipoEventoId,
    TipoFechaId,
    # --- Modelos: calendario (modelos) ---
    FechaImportante,
    InfoRapida,
    OpcionFiltro,
    OpcionOrden,
    ProximoEvento,
    # --- Modelos: calendario (metadata) ---
    TIPOS_EVENTO,
    TIPOS_FECHA,
    # --- Modelos: calendario (datos estáticos) ---
    FECHAS_IMPORTANTES,
    INFO_RAPIDA,
    OPCIONES_CARRERA,
    OPCIONES_ORDEN,
    OPCIONES_TIPO_EVENTO,
    PROXIMOS_EVENTOS,
)

# ======================================================================
# Estados (reactivos)
# ======================================================================

from .estados import (
    # --- Constantes ---
    CANTIDAD_ICONOS_FONDO,
    ETIQUETAS_CARRUSEL,
    FILTROS_VALIDOS,
    ORDENES_VALIDAS,
    ORDEN_MESES,
    POSTS_POR_PAGINA,
    SECCIONES_DETALLE_VALIDAS,
    SECCIONES_EXPLORADOR_VALIDAS,
    SEGUNDOS_ENTRE_BANNERS,
    SEMILLA_ICONOS_FONDO,
    TAMANOS_ICONOS_FONDO,
    # --- Estados ---
    EstadoAcordeonFaq,
    EstadoBannerCookies,
    EstadoBlog,
    EstadoCalendario,
    EstadoInstitucional,
    EstadoPlanEstudios,
    # --- Tipos ---
    OpcionAnio,
)

# ======================================================================
# Servicios (lógica de negocio pura)
# ======================================================================

from .servicios import (
    # ==================================================================
    # Servicio de carreras
    # ==================================================================
    # Búsqueda
    buscar_carreras_por_texto,
    # Estadísticas
    calcular_promedio_empleabilidad,
    calcular_promedio_puntuacion,
    calcular_promedio_salario,
    calcular_total_cupos_disponibles,
    calcular_total_graduados,
    calcular_total_inscritos,
    # Conteos
    contar_carreras,
    contar_carreras_con_turno,
    contar_carreras_por_demanda,
    # Validaciones
    es_demanda_valida,
    es_orden_valido,
    # Filtros
    filtrar_carreras_con_cupos_disponibles,
    filtrar_carreras_por_demanda,
    filtrar_carreras_por_empleabilidad_minima,
    filtrar_carreras_por_modalidad,
    filtrar_carreras_por_puntuacion_minima,
    filtrar_carreras_por_turno,
    # Combinaciones
    obtener_carreras_destacadas,
    obtener_carreras_por_demanda_y_orden,
    obtener_carreras_top_por_graduados,
    obtener_carreras_top_por_inscritos,
    obtener_carreras_top_por_puntuacion,
    # Ordenamientos
    ordenar_carreras_por_empleabilidad,
    ordenar_carreras_por_graduados,
    ordenar_carreras_por_inscritos,
    ordenar_carreras_por_puntuacion,
    ordenar_carreras_por_salario,
    # ==================================================================
    # Servicio del blog
    # ==================================================================
    # Búsqueda
    buscar_posts_por_texto,
    # Estadísticas
    calcular_tiempo_lectura_promedio,
    calcular_tiempo_lectura_total,
    # Conteos
    contar_posts,
    contar_posts_por_autor,
    contar_posts_por_categoria,
    # Validaciones
    es_categoria_valida,
    # Filtros
    filtrar_posts_por_autor,
    filtrar_posts_por_categoria,
    filtrar_posts_por_tiempo_lectura_maximo,
    filtrar_posts_sin_destacado,
    # Navegación
    hay_post_anterior,
    hay_post_siguiente,
    obtener_post_anterior,
    obtener_post_siguiente,
    # Combinaciones
    obtener_posts_de_categoria,
    obtener_posts_filtrados,
    obtener_posts_recientes,
    # Ordenamientos
    ordenar_posts_por_id,
    ordenar_posts_por_tiempo_lectura,
)


# ======================================================================
# API pública de la capa
# ======================================================================

__all__ = [
    # ==================================================================
    # Modelos: carrera
    # ==================================================================
    "CaracteristicaCarrera",
    "Carrera",
    "CarreraConEtiqueta",
    "ColorHex",
    "DemandaLaboral",
    "EstadisticasCarrera",
    "HORARIOS_TURNO",
    "IconoAnimado",
    "Modalidad",
    "PlanAnual",
    "PreguntaFrecuente",
    "TURNOS_VALIDOS",
    "Turno",
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
    # ==================================================================
    # Estados: constantes
    # ==================================================================
    "CANTIDAD_ICONOS_FONDO",
    "ETIQUETAS_CARRUSEL",
    "FILTROS_VALIDOS",
    "ORDENES_VALIDAS",
    "ORDEN_MESES",
    "POSTS_POR_PAGINA",
    "SECCIONES_DETALLE_VALIDAS",
    "SECCIONES_EXPLORADOR_VALIDAS",
    "SEGUNDOS_ENTRE_BANNERS",
    "SEMILLA_ICONOS_FONDO",
    "TAMANOS_ICONOS_FONDO",
    # ==================================================================
    # Estados
    # ==================================================================
    "EstadoAcordeonFaq",
    "EstadoBannerCookies",
    "EstadoBlog",
    "EstadoCalendario",
    "EstadoInstitucional",
    "EstadoPlanEstudios",
    # ==================================================================
    # Estados: tipos auxiliares
    # ==================================================================
    "OpcionAnio",
    # ==================================================================
    # Servicios: carreras (búsqueda, filtros, ordenamientos)
    # ==================================================================
    "buscar_carreras_por_texto",
    "filtrar_carreras_con_cupos_disponibles",
    "filtrar_carreras_por_demanda",
    "filtrar_carreras_por_empleabilidad_minima",
    "filtrar_carreras_por_modalidad",
    "filtrar_carreras_por_puntuacion_minima",
    "filtrar_carreras_por_turno",
    "obtener_carreras_destacadas",
    "obtener_carreras_por_demanda_y_orden",
    "obtener_carreras_top_por_graduados",
    "obtener_carreras_top_por_inscritos",
    "obtener_carreras_top_por_puntuacion",
    "ordenar_carreras_por_empleabilidad",
    "ordenar_carreras_por_graduados",
    "ordenar_carreras_por_inscritos",
    "ordenar_carreras_por_puntuacion",
    "ordenar_carreras_por_salario",
    # ==================================================================
    # Servicios: carreras (estadísticas, conteos, validaciones)
    # ==================================================================
    "calcular_promedio_empleabilidad",
    "calcular_promedio_puntuacion",
    "calcular_promedio_salario",
    "calcular_total_cupos_disponibles",
    "calcular_total_graduados",
    "calcular_total_inscritos",
    "contar_carreras",
    "contar_carreras_con_turno",
    "contar_carreras_por_demanda",
    "es_demanda_valida",
    "es_orden_valido",
    # ==================================================================
    # Servicios: blog (búsqueda, filtros, ordenamientos)
    # ==================================================================
    "buscar_posts_por_texto",
    "filtrar_posts_por_autor",
    "filtrar_posts_por_categoria",
    "filtrar_posts_por_tiempo_lectura_maximo",
    "filtrar_posts_sin_destacado",
    "obtener_posts_de_categoria",
    "obtener_posts_filtrados",
    "obtener_posts_recientes",
    "ordenar_posts_por_id",
    "ordenar_posts_por_tiempo_lectura",
    # ==================================================================
    # Servicios: blog (navegación entre posts)
    # ==================================================================
    "hay_post_anterior",
    "hay_post_siguiente",
    "obtener_post_anterior",
    "obtener_post_siguiente",
    # ==================================================================
    # Servicios: blog (estadísticas, conteos, validaciones)
    # ==================================================================
    "calcular_tiempo_lectura_promedio",
    "calcular_tiempo_lectura_total",
    "contar_posts",
    "contar_posts_por_autor",
    "contar_posts_por_categoria",
    "es_categoria_valida",
]