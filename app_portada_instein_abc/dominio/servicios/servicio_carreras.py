

from __future__ import annotations

from ...dominio.modelos.carrera import (
    Carrera,
    DemandaLaboral,
    Modalidad,
    Turno,
)
from ...infraestructura.repositorios.repositorio_carreras import (
    obtener_catalogo,
)


# ======================================================================
# 1. Filtros por criterios
# ======================================================================


def filtrar_carreras_por_demanda(
    demanda: DemandaLaboral,
) -> list[Carrera]:
    """
    Filtra carreras por nivel de demanda laboral.

    Args:
        demanda: Nivel de demanda (`"alta"`, `"media"` o `"baja"`).

    Returns:
        Lista de carreras que cumplen el criterio.
    """
    return [
        c for c in obtener_catalogo()
        if c["estadisticas"]["demanda_laboral"] == demanda
    ]


def filtrar_carreras_por_puntuacion_minima(
    puntuacion: float,
) -> list[Carrera]:
    """
    Filtra carreras con puntuación mayor o igual al umbral.

    Args:
        puntuacion: Puntuación mínima (0.0 - 5.0).

    Returns:
        Lista de carreras que cumplen el criterio.
    """
    return [
        c for c in obtener_catalogo()
        if c["estadisticas"]["puntuacion"] >= puntuacion
    ]


def filtrar_carreras_por_empleabilidad_minima(
    tasa: int,
) -> list[Carrera]:
    """
    Filtra carreras con tasa de empleabilidad >= umbral.

    Args:
        tasa: Tasa mínima en porcentaje (0-100).

    Returns:
        Lista de carreras que cumplen el criterio.
    """
    return [
        c for c in obtener_catalogo()
        if c["estadisticas"]["tasa_empleabilidad"] >= tasa
    ]


def filtrar_carreras_por_turno(turno: Turno) -> list[Carrera]:
    """
    Filtra carreras que ofrecen un turno específico.

    Args:
        turno: Turno a filtrar (`"Mañana"`, `"Tarde"`, `"Noche"`,
            `"Sábado"`).

    Returns:
        Lista de carreras que ofrecen ese turno.
    """
    return [
        c for c in obtener_catalogo()
        if turno in c["turnos"]
    ]


def filtrar_carreras_por_modalidad(
    modalidad: Modalidad,
) -> list[Carrera]:
    """
    Filtra carreras por modalidad de cursado.

    Args:
        modalidad: Modalidad (`"Presencial"`, `"Semipresencial"`,
            `"Virtual"`).

    Returns:
        Lista de carreras con esa modalidad.
    """
    return [
        c for c in obtener_catalogo()
        if c["modalidad"] == modalidad
    ]


def filtrar_carreras_con_cupos_disponibles() -> list[Carrera]:
    """
    Filtra carreras que tienen al menos un cupo disponible.

    Returns:
        Lista de carreras con `cupos_disponibles > 0`.
    """
    return [
        c for c in obtener_catalogo()
        if c["cupos_disponibles"] > 0
    ]


# ======================================================================
# 2. Búsqueda por texto
# ======================================================================


def buscar_carreras_por_texto(texto: str) -> list[Carrera]:
    """
    Busca carreras por texto en múltiples campos.

    Busca en: `nombre`, `nombre_corto`, `lema`, `descripcion`.
    La búsqueda es case-insensitive.

    Args:
        texto: Texto a buscar. Si está vacío, devuelve todo el catálogo.

    Returns:
        Lista de carreras que coinciden con el texto.
    """
    if not texto.strip():
        return list(obtener_catalogo())

    busqueda = texto.strip().lower()

    return [
        c for c in obtener_catalogo()
        if busqueda in c["nombre"].lower()
        or busqueda in c["nombre_corto"].lower()
        or busqueda in c["lema"].lower()
        or busqueda in c["descripcion"].lower()
    ]


# ======================================================================
# 3. Ordenamientos
# ======================================================================


def ordenar_carreras_por_puntuacion(
    carreras: list[Carrera] | None = None,
    descendente: bool = True,
) -> list[Carrera]:
    """
    Ordena carreras por puntuación.

    Args:
        carreras: Lista a ordenar. Si es `None`, usa todo el catálogo.
        descendente: Si `True`, mayor puntuación primero.

    Returns:
        Lista ordenada.
    """
    if carreras is None:
        carreras = list(obtener_catalogo())

    return sorted(
        carreras,
        key=lambda c: c["estadisticas"]["puntuacion"],
        reverse=descendente,
    )


def ordenar_carreras_por_inscritos(
    carreras: list[Carrera] | None = None,
    descendente: bool = True,
) -> list[Carrera]:
    """
    Ordena carreras por cantidad de estudiantes inscritos.

    Args:
        carreras: Lista a ordenar. Si es `None`, usa todo el catálogo.
        descendente: Si `True`, mayor cantidad primero.

    Returns:
        Lista ordenada.
    """
    if carreras is None:
        carreras = list(obtener_catalogo())

    return sorted(
        carreras,
        key=lambda c: c["estadisticas"]["estudiantes_inscritos"],
        reverse=descendente,
    )


def ordenar_carreras_por_graduados(
    carreras: list[Carrera] | None = None,
    descendente: bool = True,
) -> list[Carrera]:
    """
    Ordena carreras por cantidad de egresados históricos.

    Args:
        carreras: Lista a ordenar. Si es `None`, usa todo el catálogo.
        descendente: Si `True`, mayor cantidad primero.

    Returns:
        Lista ordenada.
    """
    if carreras is None:
        carreras = list(obtener_catalogo())

    return sorted(
        carreras,
        key=lambda c: c["estadisticas"]["estudiantes_graduados"],
        reverse=descendente,
    )


def ordenar_carreras_por_empleabilidad(
    carreras: list[Carrera] | None = None,
    descendente: bool = True,
) -> list[Carrera]:
    """
    Ordena carreras por tasa de empleabilidad.

    Args:
        carreras: Lista a ordenar. Si es `None`, usa todo el catálogo.
        descendente: Si `True`, mayor tasa primero.

    Returns:
        Lista ordenada.
    """
    if carreras is None:
        carreras = list(obtener_catalogo())

    return sorted(
        carreras,
        key=lambda c: c["estadisticas"]["tasa_empleabilidad"],
        reverse=descendente,
    )


def ordenar_carreras_por_salario(
    carreras: list[Carrera] | None = None,
    descendente: bool = True,
) -> list[Carrera]:
    """
    Ordena carreras por salario promedio.

    Args:
        carreras: Lista a ordenar. Si es `None`, usa todo el catálogo.
        descendente: Si `True`, mayor salario primero.

    Returns:
        Lista ordenada.
    """
    if carreras is None:
        carreras = list(obtener_catalogo())

    return sorted(
        carreras,
        key=lambda c: c["estadisticas"]["salario_promedio_bs"],
        reverse=descendente,
    )


# ======================================================================
# 4. Combinaciones (filtro + orden + límite)
# ======================================================================


def obtener_carreras_top_por_puntuacion(
    limite: int = 3,
) -> list[Carrera]:
    """
    Devuelve las N carreras con mejor puntuación.

    Args:
        limite: Número máximo de carreras a devolver.

    Returns:
        Lista de hasta `limite` carreras ordenadas por puntuación.
    """
    return ordenar_carreras_por_puntuacion()[:limite]


def obtener_carreras_top_por_inscritos(
    limite: int = 3,
) -> list[Carrera]:
    """
    Devuelve las N carreras con más estudiantes inscritos.

    Args:
        limite: Número máximo de carreras a devolver.

    Returns:
        Lista de hasta `limite` carreras.
    """
    return ordenar_carreras_por_inscritos()[:limite]


def obtener_carreras_top_por_graduados(
    limite: int = 3,
) -> list[Carrera]:
    """
    Devuelve las N carreras con más egresados históricos.

    Args:
        limite: Número máximo de carreras a devolver.

    Returns:
        Lista de hasta `limite` carreras.
    """
    return ordenar_carreras_por_graduados()[:limite]


def obtener_carreras_destacadas(
    limite: int = 3,
) -> list[Carrera]:
    """
    Devuelve las carreras más destacadas del instituto.

    Criterio: alta demanda + puntuación >= 4.7 + empleabilidad >= 90%.

    Args:
        limite: Número máximo de carreras a devolver.

    Returns:
        Lista de carreras destacadas, ordenadas por puntuación.
    """
    destacadas = [
        c for c in obtener_catalogo()
        if (
            c["estadisticas"]["demanda_laboral"] == "alta"
            and c["estadisticas"]["puntuacion"] >= 4.7
            and c["estadisticas"]["tasa_empleabilidad"] >= 90
        )
    ]
    return ordenar_carreras_por_puntuacion(destacadas)[:limite]


def obtener_carreras_por_demanda_y_orden(
    demanda: DemandaLaboral | None = None,
    orden: str = "puntuacion_desc",
    limite: int | None = None,
) -> list[Carrera]:
    """
    Combina filtro por demanda + ordenamiento + límite.

    Args:
        demanda: Nivel de demanda. `None` = sin filtro de demanda.
        orden: Clave de ordenamiento. Valores válidos:
            "puntuacion_desc", "inscritos_desc", "graduados_desc",
            "empleabilidad_desc", "salario_desc".
        limite: Número máximo de resultados. `None` = sin límite.

    Returns:
        Lista filtrada y ordenada.

    Raises:
        ValueError: Si `orden` no es una clave válida.
    """
    ordenamientos = {
        "puntuacion_desc": ordenar_carreras_por_puntuacion,
        "inscritos_desc": ordenar_carreras_por_inscritos,
        "graduados_desc": ordenar_carreras_por_graduados,
        "empleabilidad_desc": ordenar_carreras_por_empleabilidad,
        "salario_desc": ordenar_carreras_por_salario,
    }

    if orden not in ordenamientos:
        raise ValueError(
            f"Orden no válido: {orden!r}. "
            f"Usa uno de: {sorted(ordenamientos.keys())}"
        )

    # --- Filtrar ---
    carreras = (
        filtrar_carreras_por_demanda(demanda)
        if demanda is not None
        else list(obtener_catalogo())
    )

    # --- Ordenar ---
    carreras = ordenamientos[orden](carreras)

    # --- Limitar ---
    if limite is not None:
        carreras = carreras[:limite]

    return carreras


# ======================================================================
# 5. Estadísticas agregadas
# ======================================================================


def calcular_total_inscritos() -> int:
    """Suma de estudiantes inscritos en todas las carreras."""
    return sum(
        c["estadisticas"]["estudiantes_inscritos"]
        for c in obtener_catalogo()
    )


def calcular_total_graduados() -> int:
    """Suma de egresados históricos de todas las carreras."""
    return sum(
        c["estadisticas"]["estudiantes_graduados"]
        for c in obtener_catalogo()
    )


def calcular_promedio_puntuacion() -> float:
    """Promedio de puntuación entre todas las carreras."""
    catalogo = obtener_catalogo()
    if not catalogo:
        return 0.0
    return sum(
        c["estadisticas"]["puntuacion"] for c in catalogo
    ) / len(catalogo)


def calcular_promedio_empleabilidad() -> float:
    """Promedio de tasa de empleabilidad entre todas las carreras."""
    catalogo = obtener_catalogo()
    if not catalogo:
        return 0.0
    return sum(
        c["estadisticas"]["tasa_empleabilidad"] for c in catalogo
    ) / len(catalogo)


def calcular_promedio_salario() -> float:
    """Promedio de salario entre todas las carreras."""
    catalogo = obtener_catalogo()
    if not catalogo:
        return 0.0
    return sum(
        c["estadisticas"]["salario_promedio_bs"] for c in catalogo
    ) / len(catalogo)


def calcular_total_cupos_disponibles() -> int:
    """Suma de cupos disponibles en todas las carreras."""
    return sum(
        c["cupos_disponibles"] for c in obtener_catalogo()
    )


# ======================================================================
# 6. Conteos
# ======================================================================


def contar_carreras() -> int:
    """Cantidad total de carreras en el catálogo."""
    return len(obtener_catalogo())


def contar_carreras_por_demanda(demanda: DemandaLaboral) -> int:
    """Cantidad de carreras con un nivel de demanda específico."""
    return len(filtrar_carreras_por_demanda(demanda))


def contar_carreras_con_turno(turno: Turno) -> int:
    """Cantidad de carreras que ofrecen un turno específico."""
    return len(filtrar_carreras_por_turno(turno))


# ======================================================================
# 7. Validaciones
# ======================================================================


def es_demanda_valida(demanda: str) -> bool:
    """Verifica si un string es un nivel de demanda válido."""
    return demanda in ("alta", "media", "baja")


def es_orden_valido(orden: str) -> bool:
    """Verifica si un string es una clave de ordenamiento válida."""
    ordenes_validos = {
        "puntuacion_desc",
        "inscritos_desc",
        "graduados_desc",
        "empleabilidad_desc",
        "salario_desc",
    }
    return orden in ordenes_validos


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Búsqueda ---
    "buscar_carreras_por_texto",
    # --- Estadísticas agregadas ---
    "calcular_promedio_empleabilidad",
    "calcular_promedio_puntuacion",
    "calcular_promedio_salario",
    "calcular_total_cupos_disponibles",
    "calcular_total_graduados",
    "calcular_total_inscritos",
    # --- Conteos ---
    "contar_carreras",
    "contar_carreras_con_turno",
    "contar_carreras_por_demanda",
    # --- Validaciones ---
    "es_demanda_valida",
    "es_orden_valido",
    # --- Filtros ---
    "filtrar_carreras_con_cupos_disponibles",
    "filtrar_carreras_por_demanda",
    "filtrar_carreras_por_empleabilidad_minima",
    "filtrar_carreras_por_modalidad",
    "filtrar_carreras_por_puntuacion_minima",
    "filtrar_carreras_por_turno",
    # --- Combinaciones ---
    "obtener_carreras_destacadas",
    "obtener_carreras_por_demanda_y_orden",
    "obtener_carreras_top_por_graduados",
    "obtener_carreras_top_por_inscritos",
    "obtener_carreras_top_por_puntuacion",
    # --- Ordenamientos ---
    "ordenar_carreras_por_empleabilidad",
    "ordenar_carreras_por_graduados",
    "ordenar_carreras_por_inscritos",
    "ordenar_carreras_por_puntuacion",
    "ordenar_carreras_por_salario",
]