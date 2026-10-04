"""
Paquete `configuracion`: setup del `rx.App`.

Contenido
---------
- **app_config**:      creación del `rx.App` con tema + estilos.
- **estilos_globales**: keyframes + estilos CSS globales.

Uso típico
----------
Desde `app.py` (raíz del proyecto):

    from app_portada_instein.configuracion import crear_aplicacion

    app = crear_aplicacion()

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.configuracion import crear_aplicacion

✅ **TAMBIÉN VÁLIDO** — importar desde el módulo:
    from app_portada_instein.configuracion.app_config import (
        crear_aplicacion,
    )

Qué exponer y qué no
--------------------
Se exponen:
- `crear_aplicacion()`: único punto de entrada.
- `construir_estilos_globales()`: helper útil para tests.

NO se exponen:
- Configuración interna (constantes de tema).
- Keyframes individuales (usa `construir_estilos_globales()`).
"""

from __future__ import annotations


# ======================================================================
# Configuración del App
# ======================================================================

from .app_config import (
    APARIENCIA_INICIAL,
    HOJAS_DE_ESTILO_LOCALES,
    RADIO_TEMA,
    crear_aplicacion,
)

# ======================================================================
# Estilos globales
# ======================================================================

from .estilos_globales import (
    ESTILOS_GLOBALES_CSS,
    KEYFRAMES_CARRUSEL,
    KEYFRAMES_ORBITALES,
    KEYFRAMES_UI,
    construir_estilos_globales,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Configuración del App ---
    "APARIENCIA_INICIAL",
    "HOJAS_DE_ESTILO_LOCALES",
    "RADIO_TEMA",
    "crear_aplicacion",
    # --- Estilos globales ---
    "ESTILOS_GLOBALES_CSS",
    "KEYFRAMES_CARRUSEL",
    "KEYFRAMES_ORBITALES",
    "KEYFRAMES_UI",
    "construir_estilos_globales",
]