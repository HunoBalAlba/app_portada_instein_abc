"""
Configuración del `rx.App` del proyecto INSTEIN.

Este módulo es el ÚNICO responsable de crear el `rx.App` con:
- Tema (`accent_color`, `radius`, `font_family`).
- Estilos globales (keyframes + CSS).
- Hojas de estilo externas (Google Fonts + CSS local).

Filosofía
---------
Toda la configuración del `App` vive aquí. `app.py` (raíz) solo
importa y expone `crear_aplicacion()`.

Nota técnica: REGISTRO DE RUTAS
-------------------------------
El `import` del paquete `paginas` es OBLIGATORIO para que `@rx.page`
registre las rutas. Sin este import, Reflex no conoce ninguna ruta y
el sitio arranca con 404 en todas.

El import se hace dentro de `crear_aplicacion()` (no a nivel de
módulo) para evitar problemas de orden de inicialización.

⚠️ FORMA CORRECTA:

    from .. import paginas  # noqa: F401

NO usar:

    from ..paginas import paginas    # ❌ ImportError
    from ...paginas import paginas   # ❌ ImportError

Motivo: `paginas` ES el paquete, no un submódulo dentro de él.

Nota técnica: ORDEN DE CREACIÓN
-------------------------------
`crear_aplicacion()` se debe llamar EXACTAMENTE UNA VEZ, al
importar el módulo `app.py`. Reflex crea el `App` como singleton.

No llamar a `crear_aplicacion()` desde otros módulos: causaría
errores de doble inicialización.

Nota técnica: ESTILOS
---------------------
`ESTILO_BASE` (de `tipografia.py`) contiene los estilos base
tipográficos.

`construir_estilos_globales()` (de `estilos_globales.py`) contiene
keyframes + estilos CSS globales.

La fusión se hace aquí para garantizar un orden consistente.
"""

from __future__ import annotations

import reflex as rx

from ..configuracion.estilos_globales import (
    construir_estilos_globales,
)
from ..infraestructura import (
    ACCENT_COLOR_TEMA,
    ESTILO_BASE,
    FUENTE_PRINCIPAL,
    HOJAS_DE_ESTILO_BASE,
)


# ======================================================================
# Constantes locales
# ======================================================================

HOJAS_DE_ESTILO_LOCALES: list[str] = [
    "/styles/global.css",
]
"""Hojas de estilo locales del proyecto (en `assets/styles/`)."""

RADIO_TEMA: str = "medium"
"""Radio del tema Radix (small | medium | large | full)."""

APARIENCIA_INICIAL: str = "light"
"""Apariencia inicial (light | dark | inherit)."""


# ======================================================================
# API pública
# ======================================================================


def crear_aplicacion() -> rx.App:
    """
    Crea y configura la aplicación Reflex.

    Estructura del App:
    - **theme**:          accent_color, radius, font_family.
    - **style**:          keyframes + estilos CSS globales + estilos base.
    - **stylesheets**:    Google Fonts + CSS local.

    Returns:
        Instancia de `rx.App` configurada.

    Examples:
        Desde `app.py`:

            from app_portada_instein_abc.configuracion.app_config import (
                crear_aplicacion,
            )

            app = crear_aplicacion()
    """
    # ==================================================================
    # Importar el paquete `paginas` para REGISTRAR las rutas
    # ==================================================================
    # ⚠️ OBLIGATORIO: sin este import, `@rx.page` no registra nada.
    #
    # CORRECTO:    from .. import paginas       # importa el paquete
    # INCORRECTO:  from ..paginas import paginas  # ❌ ImportError
    #
    # El import se hace DENTRO de `crear_aplicacion()` (no a nivel de
    # módulo) para evitar ciclos de importación:
    #   - paginas/*.py importa componentes/*.
    #   - componentes/* no importa configuracion/*, pero sí app_config
    #     cuando se cargan las vistas.
    # ------------------------------------------------------------------
    from .. import paginas  # noqa: F401

    # ==================================================================
    # Fusionar estilos globales
    # ==================================================================
    estilos_globales: dict = {
        **ESTILO_BASE,
        **construir_estilos_globales(),
    }

    # ==================================================================
    # Crear el App
    # ==================================================================
    return rx.App(
        theme=rx.theme(
            appearance=APARIENCIA_INICIAL,
            accent_color=ACCENT_COLOR_TEMA,
            radius=RADIO_TEMA,
            font_family=FUENTE_PRINCIPAL,
        ),
        style=estilos_globales,
        stylesheets=[
            *HOJAS_DE_ESTILO_BASE,
            *HOJAS_DE_ESTILO_LOCALES,
        ],
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "APARIENCIA_INICIAL",
    "HOJAS_DE_ESTILO_LOCALES",
    "RADIO_TEMA",
    "crear_aplicacion",
]