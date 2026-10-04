"""
Estado del selector de año del plan de estudios.

Usado en la sección de plan de estudios de la vista de detalle de
carrera (`componentes/carreras/detalle/seccion_plan.py`).

Nota técnica: SEPARADO DE `EstadoInstitucional`
-----------------------------------------------
El estado del plan de estudios vive aquí separado porque:
1. Es un estado de UI (no de negocio).
2. Solo se usa en la sección de plan.
3. No necesita persistir entre navegaciones.
"""

from __future__ import annotations

import reflex as rx


class EstadoPlanEstudios(rx.State):
    """
    Estado del selector segmentado de año.

    Atributos:
        anio_seleccionado: Valor del año seleccionado como string
            (ej: "0", "1", "2"). Es `str` porque el
            `rx.segmented_control` maneja valores como strings.
    """

    anio_seleccionado: str = "0"

    @rx.event
    def cambiar_anio(self, valor: str | list[str]):
        """
        Cambia el año seleccionado desde el segmented control.

        Args:
            valor: Valor del item seleccionado. Puede ser `"1"` o
                `["1"]` dependiendo de la versión de Radix Themes.
        """
        if isinstance(valor, list):
            self.anio_seleccionado = valor[0] if valor else "0"
        else:
            self.anio_seleccionado = str(valor)

    @rx.var
    def indice_anio_actual(self) -> int:
        """
        Índice del año seleccionado como `int`.

        Returns:
            Índice (0-based). Si el valor no es convertible a int,
            devuelve 0 (fallback seguro).
        """
        try:
            return int(self.anio_seleccionado)
        except (ValueError, TypeError):
            return 0


__all__ = ["EstadoPlanEstudios"]