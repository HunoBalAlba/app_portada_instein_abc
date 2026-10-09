

from __future__ import annotations

import reflex as rx

from ....infraestructura.constantes.dimensiones import (
    ANCHO_CONTENIDO,
)

# ======================================================================
# Imports relativos del propio paquete
# ======================================================================
# Se usan rutas relativas (`.`) para evitar ciclos de importación
# cuando múltiples submódulos se referencian entre sí.
# ----------------------------------------------------------------------

from .buscador import (
    buscador_carreras,
    grid_imagenes_carreras,
)
from .constantes import PADDING_EXPLORADOR
from .contenido import contenido_explorador
from .panel_flotante import panel_flotante_selector
from .widgets import selector_carrera_destacada


# ======================================================================
# Explorador completo
# ======================================================================


def explorador_carrera_destacada() -> rx.Component:
    """
    Explorador completo de carreras estilo Leonardo AI.

    Compone, en orden:
    1. Panel flotante de acceso rápido (oculto por defecto).
    2. Selector de carrera destacada (pastillas horizontales).
    3. Buscador de carreras (input con iconos).
    4. Grid de imágenes de carreras (navega al detalle).
    5. Contenido dinámico según la sección activa (Info/Plan/Perfil/Campo/FAQ).

    Nota: la barra de opciones del explorador (5 botones circulares)
    está **comentada** porque actualmente el contenido dinámico se
    controla desde el `panel_flotante` y las pastillas de selección.
    Si en el futuro se quiere reactivar, descomentar el bloque
    correspondiente e importar `barra_opciones_explorador`.

    Returns:
        Componente `rx.box` con el explorador completo.
    """
    return rx.box(
        # ==========================================================
        # Panel flotante (botón + overlay + panel desplegable)
        # ==========================================================
        panel_flotante_selector(),
        # ==========================================================
        # Contenido principal del explorador
        # ==========================================================
        rx.vstack(
            # --- Selector de carrera destacada (pastillas) ---
            selector_carrera_destacada(),
            # --- Buscador de carreras ---
            buscador_carreras(),
            # --- Grid de imágenes (navega al detalle) ---
            grid_imagenes_carreras(),
            # --- Contenido dinámico según la sección activa ---
            contenido_explorador(),
            width="100%",
            align="center",
            spacing="4",
            padding=PADDING_EXPLORADOR,
            max_width=ANCHO_CONTENIDO,
            margin="0 auto",
        ),
        width="100%",
        position="relative",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["explorador_carrera_destacada"]