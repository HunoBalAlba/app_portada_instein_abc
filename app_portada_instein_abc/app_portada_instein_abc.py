

from __future__ import annotations

from .configuracion.app_config import crear_aplicacion


# ======================================================================
# Variable global que Reflex busca
# ======================================================================

app = crear_aplicacion()
"""Instancia global del `rx.App`.

Reflex busca esta variable al ejecutar `reflex run`.
"""


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["app"]