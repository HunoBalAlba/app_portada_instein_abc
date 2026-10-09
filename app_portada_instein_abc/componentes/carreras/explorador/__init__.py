

from __future__ import annotations


# ======================================================================
# Ensamblador principal
# ======================================================================

from .explorador import explorador_carrera_destacada

# ======================================================================
# Constantes públicas de layout
# ======================================================================

from .constantes import (
    ALTO_MINIMO_CONTENIDO,
    ANCHO_MAXIMO_BUSCADOR,
    ANCHO_PANEL_FLOTANTE,
    OPCIONES_EXPLORADOR,
    PADDING_EXPLORADOR,
    POSICION_PANEL_FLOTANTE,
    TAMANO_BOTON_FLOTANTE,
    TAMANO_ICONO_ESTADO_VACIO,
    TAMANO_ICONO_OPCION,
)

# ======================================================================
# Widgets reutilizables
# ======================================================================

from .widgets import (
    bloque_texto_carrera_destacada,
    contenedor_animacion_orbital,
    cuadro_resumen_multimedia,
    pastilla_carrera_destacada,
    selector_carrera_destacada,
)


# ======================================================================
# API pública del subpaquete
# ======================================================================

__all__ = [
    # --- Constantes de layout ---
    "ALTO_MINIMO_CONTENIDO",
    "ANCHO_MAXIMO_BUSCADOR",
    "ANCHO_PANEL_FLOTANTE",
    "OPCIONES_EXPLORADOR",
    "PADDING_EXPLORADOR",
    "POSICION_PANEL_FLOTANTE",
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_ICONO_OPCION",
    # --- Ensamblador principal ---
    "explorador_carrera_destacada",
    # --- Widgets reutilizables ---
    "bloque_texto_carrera_destacada",
    "contenedor_animacion_orbital",
    "cuadro_resumen_multimedia",
    "pastilla_carrera_destacada",
    "selector_carrera_destacada",
]