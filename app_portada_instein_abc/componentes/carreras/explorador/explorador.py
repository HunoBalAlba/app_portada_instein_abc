"""
Ensamblador del explorador de carrera destacada.

Este módulo es el **punto de entrada** del paquete `explorador/`.
Compone los subcomponentes en el orden correcto y expone una única
función pública: `explorador_carrera_destacada()`.

Estructura del explorador
-------------------------
1. **Panel flotante** (oculto por defecto):
   - Botón de acceso rápido (esquina inferior derecha).
   - Overlay + panel desplegable con todas las carreras.

2. **Buscador**:
   - Input con búsqueda por nombre, lema o descripción.

3. **Grid de imágenes**:
   - Cards con imagen + nombre + duración.
   - Cada card navega al detalle `/carrera/{id}`.
   - Estado vacío si no hay resultados.

4. **Barra de opciones**:
   - 5 botones circulares (Info, Plan, Perfil, Campo, FAQ).

5. **Contenido dinámico**:
   - Cambia según la opción seleccionada.

Nota técnica: ¿POR QUÉ ESTE MÓDULO ES TAN CORTO?
------------------------------------------------
Aquí solo **ensamblamos**. Cada pieza vive en su propio módulo
(`buscador.py`, `panel_flotante.py`, `widgets.py`, `contenido.py`).
Este archivo es el "conductor" — mantiene el orden y la composición,
nada más.

Ventajas:
- Cambiar el orden del explorador solo toca este archivo.
- Cada submódulo se testea/refactoriza de forma aislada.
- Los imports son explícitos y trazables.

Nota técnica: IMPORTS
---------------------
Todos los imports usan rutas **absolutas** desde
`app_portada_instein.componentes.carreras.explorador.*`. La única
excepción son los imports desde el propio paquete, que usan **rutas
relativas** (`.buscador`, `.constantes`, etc.) para evitar ciclos.

⚠️ NO mezclar: si importas `_buscador_carreras` (con guion bajo) es
porque estás usando una versión antigua. Los nombres públicos
actuales son `buscador_carreras`, `grid_imagenes_carreras`,
`panel_flotante_selector`.
"""

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