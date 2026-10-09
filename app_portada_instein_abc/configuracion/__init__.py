

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
    # construir_estilos_globales,
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