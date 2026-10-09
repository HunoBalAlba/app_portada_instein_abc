

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