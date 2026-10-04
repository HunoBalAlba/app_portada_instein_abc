"""
Helpers de color para la vista del Calendario Académico.

Resuelven los metadatos visuales (color, icono, etiqueta) de cada tipo
de evento y cada tipo de fecha importante.

Nota técnica: TIPOS DE RETORNO
------------------------------
Los helpers devuelven `dict` con `color`, `icono`, `etiqueta`. Estos
valores vienen de constantes estáticas (`TIPOS_EVENTO`, `TIPOS_FECHA`)
y NO son Vars reactivos — se usan en tiempo de compilación.
"""

from __future__ import annotations

from ...dominio.modelos.calendario import (
    TIPOS_EVENTO,
    TIPOS_FECHA,
)


# ======================================================================
# Helpers públicos
# ======================================================================


def color_por_tipo_evento(tipo: str) -> dict:
    """
    Devuelve los metadatos visuales del tipo de evento.

    Args:
        tipo: Clave del tipo de evento (ej: "taller", "seminario").

    Returns:
        Dict con `color`, `icono`, `etiqueta`. Si el tipo no existe,
        devuelve el de "institucional" como fallback.
    """
    return TIPOS_EVENTO.get(tipo, TIPOS_EVENTO["institucional"])


def color_por_tipo_fecha(tipo: str) -> dict:
    """
    Devuelve los metadatos visuales del tipo de fecha importante.

    Args:
        tipo: Clave del tipo de fecha (ej: "feriado_nacional").

    Returns:
        Dict con `color`, `icono`, `etiqueta`. Si el tipo no existe,
        devuelve el de "internacional" como fallback.
    """
    return TIPOS_FECHA.get(tipo, TIPOS_FECHA["internacional"])


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "color_por_tipo_evento",
    "color_por_tipo_fecha",
]