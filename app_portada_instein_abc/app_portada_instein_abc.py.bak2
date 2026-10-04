"""
Punto de entrada de la aplicación INSTEIN.

Este módulo es lo primero que ejecuta Reflex (`reflex run`). Su única
responsabilidad es:
1. Crear el `rx.App` (delegando en `configuracion.app_config`).
2. Exponerlo como variable global `app`.

Estructura del proyecto
-----------------------
    app_portada_instein/
    ├── componentes/       → UI (presentación)
    ├── infraestructura/   → constantes, repositorios, utilidades
    ├── dominio/           → modelos, estados, servicios
    ├── paginas/           → vistas con @rx.page
    └── configuracion/     → setup del rx.App

    app.py                 → punto de entrada (este archivo)
    rxconfig.py            → configuración de Reflex

Uso
---
    reflex init    # solo la primera vez
    reflex run     # inicia el servidor en http://localhost:3000

Nota técnica: `app = crear_aplicacion()`
----------------------------------------
Reflex busca la variable `app` en el módulo configurado en
`rxconfig.py`. Por defecto, el módulo es `app` y la variable es
`app`.

No renombrar esta variable sin actualizar `rxconfig.py`.
"""

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