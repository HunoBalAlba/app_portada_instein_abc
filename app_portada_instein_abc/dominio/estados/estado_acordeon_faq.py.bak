"""
Estado global del acordeón de FAQ.

Compartido por todos los acordeones de la aplicación:
- FAQ del home.
- FAQ de cada carrera.
- FAQ del programa de becas.
- FAQ de admisión.
- FAQ del explorador.

Nota técnica: VARIOS ACORDEONES EN LA MISMA PÁGINA
--------------------------------------------------
Como todos comparten el mismo State, dos acordeones en la misma
página estarán sincronizados (al abrir uno se cierra el otro).

Si en el futuro se necesitan múltiples acordeones independientes en
la misma página, crear subclases de State por instancia.
"""

from __future__ import annotations

import reflex as rx


class EstadoAcordeonFaq(rx.State):
    """
    Estado del acordeón de FAQ compartido por toda la app.

    Atributos:
        indice_abierto: Índice del item abierto. `-1` = ninguno.
    """

    indice_abierto: int = -1

    @rx.event
    def alternar(self, indice: int):
        """
        Abre o cierra una pregunta del acordeón.

        Args:
            indice: Índice del item clicado.
        """
        if self.indice_abierto == indice:
            self.indice_abierto = -1
        else:
            self.indice_abierto = indice


__all__ = ["EstadoAcordeonFaq"]