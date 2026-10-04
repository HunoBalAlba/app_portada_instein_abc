"""
Subpaquete `componentes.carreras.explorador`: explorador de carreras.

Agrupa todo lo relacionado con el explorador de carrera destacada:
buscador, panel flotante, widgets orbitales y contenido dinámico.

Contenido
---------
- **explorador**:      ensamblador principal (`explorador_carrera_destacada`).
- **buscador**:        buscador + cards + grid + estado vacío.
- **panel_flotante**:  botón flotante + panel desplegable.
- **widgets**:         contenedor orbital, selector de carrera, etc.
- **contenido**:       grids dinámicos (Info/Plan/Perfil/Campo/FAQ).
- **constantes**:      layout y opciones del explorador.
- **helpers**:         helpers de color (compatibilidad).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el subpaquete:
    from app_portada_instein.componentes.carreras.explorador import (
        explorador_carrera_destacada,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.componentes.carreras.explorador.explorador import (
        explorador_carrera_destacada,
    )

Qué exponer y qué no
--------------------
Se exponen:
- `explorador_carrera_destacada`:  función principal (ensamblador).
- Widgets reutilizables:            por si otra vista los necesita.
- Constantes de layout:             por si otra vista las reutiliza.

NO se exponen:
- Helpers privados (`_generar_estrellas`, `_card_explorador`, etc.).
- Constantes internas (colores hardcodeados, tamaños específicos).
"""

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