"""
Paquete `dominio.servicios`: lógica de negocio.

Los servicios implementan **reglas de negocio** sobre los datos
obtenidos del repositorio. Aíslan los componentes y estados de la
lógica compleja, permitiendo testearla en aislamiento.

Contenido
---------
1. **servicio_carreras**: filtros, ordenamientos, búsquedas y
   estadísticas del catálogo de carreras.
2. **servicio_blog**:     filtros, ordenamientos, búsquedas y   navegación del blog.
3. **kepler**:            motor kepleriano para órbitas de iconos
   (dominio matemático puro).

Filosofía
---------
- **Puros**:         sin efectos secundarios.
- **Testeables**:    fáciles de cubrir con pytest.
- **Sin UI**:        no dependen de Reflex excepto donde es inevitable.
- **Con nombres claros**: verbo + sustantivo (ej: `filtrar_*`,
  `ordenar_*`, `buscar_*`, `calcular_*`, `contar_*`).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.dominio.servicios import (
        filtrar_carreras_por_demanda,
        ordenar_carreras_por_puntuacion,
        buscar_posts_por_texto,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el módulo específico:
    from app_portada_instein.dominio.servicios.servicio_carreras import (
        filtrar_carreras_por_demanda,
    )

Diferencia con `dominio.estados`
--------------------------------
- **estados**:  reactivos, contienen estado mutable, disparan renders.
- **servicios**: puros, sin estado, ejecutables en cualquier contexto.

Los estados pueden llamar a servicios, pero no al revés.
"""

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