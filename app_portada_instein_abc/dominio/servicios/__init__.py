

from __future__ import annotations


# ======================================================================
# Servicio de carreras
# ======================================================================

from .servicio_carreras import (
    # Búsqueda
    buscar_carreras_por_texto,
    # Estadísticas agregadas
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
)

# ======================================================================
# Servicio del blog
# ======================================================================

from .servicio_blog import (
    # Búsqueda
    buscar_posts_por_texto,
    # Estadísticas agregadas
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
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Servicio de carreras
    # ==================================================================
    # Búsqueda
    "buscar_carreras_por_texto",
    # Estadísticas
    "calcular_promedio_empleabilidad",
    "calcular_promedio_puntuacion",
    "calcular_promedio_salario",
    "calcular_total_cupos_disponibles",
    "calcular_total_graduados",
    "calcular_total_inscritos",
    # Conteos
    "contar_carreras",
    "contar_carreras_con_turno",
    "contar_carreras_por_demanda",
    # Validaciones
    "es_demanda_valida",
    "es_orden_valido",
    # Filtros
    "filtrar_carreras_con_cupos_disponibles",
    "filtrar_carreras_por_demanda",
    "filtrar_carreras_por_empleabilidad_minima",
    "filtrar_carreras_por_modalidad",
    "filtrar_carreras_por_puntuacion_minima",
    "filtrar_carreras_por_turno",
    # Combinaciones
    "obtener_carreras_destacadas",
    "obtener_carreras_por_demanda_y_orden",
    "obtener_carreras_top_por_graduados",
    "obtener_carreras_top_por_inscritos",
    "obtener_carreras_top_por_puntuacion",
    # Ordenamientos
    "ordenar_carreras_por_empleabilidad",
    "ordenar_carreras_por_graduados",
    "ordenar_carreras_por_inscritos",
    "ordenar_carreras_por_puntuacion",
    "ordenar_carreras_por_salario",
    # ==================================================================
    # Servicio del blog
    # ==================================================================
    # Búsqueda
    "buscar_posts_por_texto",
    # Estadísticas
    "calcular_tiempo_lectura_promedio",
    "calcular_tiempo_lectura_total",
    # Conteos
    "contar_posts",
    "contar_posts_por_autor",
    "contar_posts_por_categoria",
    # Validaciones
    "es_categoria_valida",
    # Filtros
    "filtrar_posts_por_autor",
    "filtrar_posts_por_categoria",
    "filtrar_posts_por_tiempo_lectura_maximo",
    "filtrar_posts_sin_destacado",
    # Navegación
    "hay_post_anterior",
    "hay_post_siguiente",
    "obtener_post_anterior",
    "obtener_post_siguiente",
    # Combinaciones
    "obtener_posts_de_categoria",
    "obtener_posts_filtrados",
    "obtener_posts_recientes",
    # Ordenamientos
    "ordenar_posts_por_id",
    "ordenar_posts_por_tiempo_lectura",
]