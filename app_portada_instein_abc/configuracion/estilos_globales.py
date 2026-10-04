"""
Estilos globales y keyframes del proyecto INSTEIN.

Contenido
---------
1. **Keyframes UI**:        pulso, flotar, deslizar, etc.
2. **Keyframes del carrusel**: progreso del auto-avance.
3. **Keyframes orbitales**: órbitas keplerianas (generadas).
4. **Estilos base**:        fuentes, colores globales de CodeMirror.

Filosofía
---------
Todos los keyframes y estilos globales del proyecto viven aquí.
NO se definen keyframes inline en los componentes.

Convención de nombres
---------------------
- `KEYFRAMES_UI`:             animaciones de UI generales.
- `KEYFRAMES_CARRUSEL`:       animaciones del carrusel de carreras.
- `KEYFRAMES_ORBITALES`:      animaciones de órbitas keplerianas.
- `ESTILOS_GLOBALES_CSS`:     estilos CSS globales del proyecto.
- `construir_estilos_globales()`: fusiona todo en un dict para `rx.App`.

Nota técnica: ÓRBITAS KEPLERIANAS
---------------------------------
Las órbitas keplerianas se generan dinámicamente en función de los
iconos animados del catálogo de carreras. Solo se generan los
keyframes ÚNICOS (por combinación de ángulo + semieje mayor).

El motor kepleriano vive en `dominio.servicios.kepler`.

Nota técnica: KEYFRAMES INLINE vs GLOBALES
------------------------------------------
Los keyframes se definen UNA VEZ aquí y se aplican a los componentes
con `animation="nombre_keyframe duracion timing delay iteracion"`.

NO definir keyframes inline en cada componente: duplica CSS y
aumenta el bundle size.

Dependencias de animación
-------------------------
Los siguientes keyframes son usados por componentes:
- `pulso_central`                → contenedor orbital del detalle.
- `flotar_estrella`              → estrellas de fondo.
- `pulso_verde`                  → badges de "inscripciones abiertas".
- `flotar_icono_particula`       → partículas del hero.
- `flotar_cristal`               → elementos decorativos.
- `deslizar_linea`               → líneas de fuga.
- `deslizar_desde_abajo`         → paneles flotantes.
- `progreso_carrusel`            → barra del carrusel.
- `orbita_*`                     → órbitas keplerianas de iconos.
- `pulse`                        → heredado de Reflex/Radix.
- `borderPulse`                  → indicadores con borde pulsante.
"""

from __future__ import annotations

import reflex as rx

from ..dominio.servicios.kepler import (
    DefinicionKeyframe,
    generar_keyframes_css,
    generar_pasos_orbita,
)
from ..infraestructura import (
    obtener_catalogo,
)


# ======================================================================
# 1. Keyframes de UI generales
# ======================================================================

KEYFRAMES_UI: dict = {
    # ==================================================================
    # Pulso central (imagen orbital del detalle)
    # ==================================================================
    "@keyframes pulso_central": {
        "0%, 100%": {"transform": "translate(-50%, -50%) scale(1)"},
        "50%": {"transform": "translate(-50%, -50%) scale(1.05)"},
    },
    # ==================================================================
    # Flotación de estrellas (fondo orbital)
    # ==================================================================
    "@keyframes flotar_estrella": {
        "0%, 100%": {"opacity": "0.4"},
        "50%": {"opacity": "1"},
    },
    # ==================================================================
    # Pulso verde (badges de "inscripciones abiertas")
    # ==================================================================
    "@keyframes pulso_verde": {
        "0%, 100%": {"opacity": "1", "transform": "scale(1)"},
        "50%": {"opacity": "0.6", "transform": "scale(1.15)"},
    },
    # ==================================================================
    # Partículas (iconos flotantes del hero)
    # ==================================================================
    "@keyframes flotar_icono_particula": {
        "0%, 100%": {
            "transform": "translateY(0) rotate(var(--rotacion, 0deg))",
            "opacity": "0.15",
        },
        "25%": {
            "transform": "translateY(-8px) rotate(var(--rotacion, 0deg))",
            "opacity": "0.25",
        },
        "50%": {
            "transform": "translateY(-15px) rotate(var(--rotacion, 0deg))",
            "opacity": "0.35",
        },
        "75%": {
            "transform": "translateY(-8px) rotate(var(--rotacion, 0deg))",
            "opacity": "0.25",
        },
    },
    # ==================================================================
    # Cristales decorativos (flotación + rotación)
    # ==================================================================
    "@keyframes flotar_cristal": {
        "0%, 100%": {"transform": "translateY(0) rotate(0deg)"},
        "50%": {"transform": "translateY(-30px) rotate(8deg)"},
    },
    # ==================================================================
    # Líneas de fuga (deslizamiento horizontal)
    # ==================================================================
    "@keyframes deslizar_linea": {
        "0%": {"transform": "translateX(-100%)", "opacity": "0"},
        "50%": {"opacity": "0.6"},
        "100%": {"transform": "translateX(100%)", "opacity": "0"},
    },
    # ==================================================================
    # Entrada de paneles desde abajo
    # ==================================================================
    "@keyframes deslizar_desde_abajo": {
        "from": {"transform": "translateY(20px)", "opacity": "0"},
        "to": {"transform": "translateY(0)", "opacity": "1"},
    },
    # ==================================================================
    # Pulso genérico (compatible con Radix)
    # ==================================================================
    "@keyframes pulse": {
        "0%": {"transform": "scale(0.95)", "opacity": "0.5"},
        "50%": {"transform": "scale(1.1)", "opacity": "1"},
        "100%": {"transform": "scale(0.95)", "opacity": "0.5"},
    },
    # ==================================================================
    # Border pulse (indicadores con borde pulsante)
    # ==================================================================
    "@keyframes borderPulse": {
        "0%": {
            "border-color": "rgba(0, 144, 255, 0.3)",
            "box-shadow": "0 0 0 0 rgba(0, 144, 255, 0.2)",
        },
        "50%": {
            "border-color": "rgba(0, 144, 255, 1)",
            "box-shadow": "0 0 0 4px rgba(0, 144, 255, 0.4)",
        },
        "100%": {
            "border-color": "rgba(0, 144, 255, 0.3)",
            "box-shadow": "0 0 0 0 rgba(0, 144, 255, 0)",
        },
    },
}


# ======================================================================
# 2. Keyframes del carrusel
# ======================================================================

KEYFRAMES_CARRUSEL: dict = {
    # ==================================================================
    # Barra de progreso del auto-avance del carrusel
    # ==================================================================
    "@keyframes progreso_carrusel": {
        "0%": {"width": "0%"},
        "100%": {"width": "100%"},
    },
}


# ======================================================================
# 3. Keyframes orbitales (keplerianos)
# ======================================================================


def _iconos_unicos_por_keyframe() -> dict[str, dict]:
    """
    Recopila los iconos animados únicos del catálogo.

    Como varios iconos pueden compartir el mismo `keyframe_orbita`
    (si tienen el mismo ángulo + semieje mayor), se deduplican por
    clave.

    Returns:
        Dict `{nombre_keyframe: icono_animado}`.
    """
    vistos: dict[str, dict] = {}
    for carrera in obtener_catalogo():
        for icono in carrera["iconos_animados"]:
            clave = icono["keyframe_orbita"]
            if clave not in vistos:
                vistos[clave] = icono
    return vistos


def _generar_keyframes_orbitales() -> dict:
    """
    Genera los `@keyframes` de todas las órbitas keplerianas.

    Cada órbita se define por:
    - `semieje_mayor`: radio horizontal (% del contenedor).
    - `excentricidad`: qué tan elíptica es.
    - `factor_perspectiva`: aplanamiento vertical (3D).
    - `angulo_inicial`: orientación en grados.

    Returns:
        Dict con todos los `@keyframes orbita_*` listos para `rx.App`.
    """
    definiciones: list[DefinicionKeyframe] = []

    for sufijo, icono in _iconos_unicos_por_keyframe().items():
        pasos = generar_pasos_orbita(
            semieje_mayor=icono["semieje_mayor"],
            excentricidad=icono["excentricidad"],
            factor_perspectiva=icono["factor_perspectiva"],
            angulo_inicial_grados=icono["angulo_inicial"],
        )
        definiciones.append({"nombre": sufijo, "pasos": pasos})

    return generar_keyframes_css(definiciones)


KEYFRAMES_ORBITALES: dict = _generar_keyframes_orbitales()
"""Keyframes orbitales precalculados (constante de módulo)."""


# ======================================================================
# 4. Estilos CSS globales
# ======================================================================

ESTILOS_GLOBALES_CSS: dict = {
    # ==================================================================
    # Ajustes globales de scroll
    # ==================================================================
    "html": {
        "scroll_behavior": "smooth",
    },
    # ==================================================================
    # Estilos de selección de texto
    # ==================================================================
    "::selection": {
        "background_color": "rgba(59, 91, 219, 0.2)",
        "color": "inherit",
    },
    # ==================================================================
    # Scrollbar personalizada
    # ==================================================================
    "::-webkit-scrollbar": {
        "width": "10px",
        "height": "10px",
    },
    "::-webkit-scrollbar-track": {
        "background_color": "transparent",
    },
    "::-webkit-scrollbar-thumb": {
        "background_color": "rgba(100, 100, 100, 0.3)",
        "border_radius": "5px",
        "border": "2px solid transparent",
        "background_clip": "content-box",
    },
    "::-webkit-scrollbar-thumb:hover": {
        "background_color": "rgba(100, 100, 100, 0.5)",
    },
}


# ======================================================================
# 5. Ensamblador de estilos globales
# ======================================================================


def construir_estilos_globales() -> dict:
    """
    Ensambla TODOS los estilos globales en un único dict.

    Orden de fusión (importa para colisiones de claves):
    1. `ESTILOS_GLOBALES_CSS` → estilos CSS base.
    2. `KEYFRAMES_UI`          → animaciones de UI.
    3. `KEYFRAMES_CARRUSEL`    → animaciones del carrusel.
    4. `KEYFRAMES_ORBITALES`   → animaciones orbitales.

    Los keyframes se añaden al final para que NO puedan ser
    sobrescritos por estilos CSS genéricos.

    Returns:
        Dict listo para `rx.App(style=...)`.

    Examples:
        >>> estilos = construir_estilos_globales()
        >>> "@keyframes pulse" in estilos
        True
        >>> "html" in estilos
        True
    """
    return {
        **ESTILOS_GLOBALES_CSS,
        **KEYFRAMES_UI,
        **KEYFRAMES_CARRUSEL,
        **KEYFRAMES_ORBITALES,
    }


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ESTILOS_GLOBALES_CSS",
    "KEYFRAMES_CARRUSEL",
    "KEYFRAMES_ORBITALES",
    "KEYFRAMES_UI",
    "construir_estilos_globales",
]