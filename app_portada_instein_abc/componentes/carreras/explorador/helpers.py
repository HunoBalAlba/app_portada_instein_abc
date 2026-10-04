"""
Helpers internos del explorador de carreras.

Este módulo provee las funciones de resolución de color que usan los
componentes del explorador. Como el proyecto unificó el acento visual
bajo un único azul marino (`AZUL_MARINO_NEON`), los helpers mantienen
la firma anterior (reciben `carrera`) pero devuelven siempre el mismo
valor.

Nota técnica: ¿POR QUÉ EXISTEN ESTOS HELPERS SI NO DIFERENCIAN?
---------------------------------------------------------------
Los helpers se conservan por dos razones:

1. **Compatibilidad**: los componentes del explorador los importan
   con la misma firma que antes. Migrarlos a llamadas directas de
   `AZUL_MARINO_NEON` implicaría tocar ~15 archivos.

2. **Punto único de extensión**: si en el futuro se decide volver a
   colorear por carrera, solo hay que modificar estas funciones.

Cuando NO usar estos helpers
----------------------------
Si un componente nuevo sabe que el acento es siempre azul marino,
NO necesita pasar por aquí. Importa `AZUL_MARINO_NEON` directamente.
"""

from __future__ import annotations

import reflex as rx

from app_portada_instein.infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    FONDO_AZUL_SUAVE,
)
from app_portada_instein.dominio.modelos.carrera import Carrera


# ======================================================================
# Colores del acento
# ======================================================================

COLOR_PRINCIPAL: str = AZUL_MARINO_NEON
"""Color sólido del acento (hex fijo, mismo en light/dark)."""

COLOR_SUAVE: rx.Var = FONDO_AZUL_SUAVE
"""Fondo suave del acento (Var adaptativo al color_mode)."""


# ======================================================================
# API pública de compatibilidad
# ======================================================================


def color_carrera(carrera: Carrera | None = None) -> str:
    """
    Color del acento global (azul marino neon).

    Args:
        carrera: Ignorado. Se mantiene por compatibilidad.

    Returns:
        Hex del azul marino neon (`#3b5bdb`).
    """
    return COLOR_PRINCIPAL


def color_suave_carrera(carrera: Carrera | None = None) -> rx.Var:
    """
    Fondo suave del acento global.

    Args:
        carrera: Ignorado. Se mantiene por compatibilidad.

    Returns:
        Var reactiva con el fondo azul marino translúcido adaptativo.
    """
    return COLOR_SUAVE


def color_carrera_destacada() -> str:
    """Color del acento global (sin argumentos, para conveniencia)."""
    return COLOR_PRINCIPAL


def color_suave_carrera_destacada() -> rx.Var:
    """Fondo suave del acento global (sin argumentos)."""
    return COLOR_SUAVE


__all__ = [
    "COLOR_PRINCIPAL",
    "COLOR_SUAVE",
    "color_carrera",
    "color_carrera_destacada",
    "color_suave_carrera",
    "color_suave_carrera_destacada",
]