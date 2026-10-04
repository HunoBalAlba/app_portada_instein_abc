"""
Paquete `componentes.carreras`: componentes de la oferta académica.

Agrupa todo lo relacionado con la presentación de carreras:

1. **Tarjetas base**:
   - `tarjeta_carrera`:      item horizontal con icono + info + rating.
   - `item_carrera_ranking`: variante con número de ranking a la izquierda.
   - `pastilla_anio`:        pastilla seleccionable de año del plan.
   - `fila_materia`:         fila de una materia del plan de estudios.
   - `hero_carreras`:        carrusel de banners destacados con auto-avance.

2. **Explorador** (`explorador/`):
   - Buscador de carreras + grid de imágenes + panel flotante.
   - Widgets orbitales reutilizables (contenedor, selector, etc.).
   - Expone `explorador_carrera_destacada` como ensamblador principal.

3. **Detalle** (`detalle/`):
   - Secciones que componen la vista `/carrera/{id}`:
     - `seccion_informacion`:  descripción + datos rápidos + CTA.
     - `seccion_plan_estudios`: selector de año + progreso + materias.
     - `seccion_perfil_y_campo_laboral`: perfil + campo laboral.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.componentes.carreras import (
        tarjeta_carrera,
        hero_carreras,
        explorador_carrera_destacada,
        seccion_informacion,
        seccion_plan_estudios,
        seccion_perfil_y_campo_laboral,
    )

❌ **EVITAR** — importar desde módulos internos:
    from app_portada_instein.componentes.carreras.tarjeta_carrera import (
        tarjeta_carrera,
    )

Motivo: la ruta interna puede cambiar sin romper consumidores,
siempre que la API pública se mantenga estable.

Qué NO exponer aquí
-------------------
- Estados de Reflex: viven en `dominio.estados`.
- Modelos de datos (`Carrera`, `PlanAnual`, `IconoAnimado`): viven
  en `dominio.modelos.carrera`.
- Constantes visuales: viven en `infraestructura.constantes`.

Este paquete SOLO expone componentes de UI puros.

Nota técnica: CONFLICTO MÓDULO vs FUNCIÓN
----------------------------------------
El módulo `hero_carreras.py` define la función `hero_carreras()`.
Al importar `from .hero_carreras import hero_carreras`, el nombre
`hero_carreras` se registra como la **función** (no el módulo).

⚠️ Si NO se importa aquí, `from ...carreras import hero_carreras`
resolvería al **módulo** `hero_carreras.py`, causando:

    TypeError: 'module' object is not callable

Por eso es CRÍTICO exponer `hero_carreras` en este `__init__.py`.
"""

from __future__ import annotations


# ======================================================================
# Tarjetas base y componentes del plan
# ======================================================================

from .tarjeta_carrera import (
    fila_materia,
    item_carrera_ranking,
    pastilla_anio,
    tarjeta_carrera,
)

# ======================================================================
# Hero del carrusel de carreras
# ======================================================================

from .hero_carreras import hero_carreras

# ======================================================================
# Explorador (subpaquete completo)
# ======================================================================

from .explorador import (
    ALTO_MINIMO_CONTENIDO,
    ANCHO_MAXIMO_BUSCADOR,
    ANCHO_PANEL_FLOTANTE,
    OPCIONES_EXPLORADOR,
    PADDING_EXPLORADOR,
    POSICION_PANEL_FLOTANTE,
    TAMANO_BOTON_FLOTANTE,
    TAMANO_ICONO_ESTADO_VACIO,
    TAMANO_ICONO_OPCION,
    bloque_texto_carrera_destacada,
    contenedor_animacion_orbital,
    cuadro_resumen_multimedia,
    explorador_carrera_destacada,
    pastilla_carrera_destacada,
    selector_carrera_destacada,
)

# ======================================================================
# Detalle (subpaquete completo)
# ======================================================================

from .detalle import (
    seccion_informacion,
    seccion_perfil_y_campo_laboral,
    seccion_plan_estudios,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Constantes del explorador ---
    "ALTO_MINIMO_CONTENIDO",
    "ANCHO_MAXIMO_BUSCADOR",
    "ANCHO_PANEL_FLOTANTE",
    "OPCIONES_EXPLORADOR",
    "PADDING_EXPLORADOR",
    "POSICION_PANEL_FLOTANTE",
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_ICONO_OPCION",
    # --- Detalle ---
    "seccion_informacion",
    "seccion_perfil_y_campo_laboral",
    "seccion_plan_estudios",
    # --- Explorador ---
    "bloque_texto_carrera_destacada",
    "contenedor_animacion_orbital",
    "cuadro_resumen_multimedia",
    "explorador_carrera_destacada",
    "pastilla_carrera_destacada",
    "selector_carrera_destacada",
    # --- Hero del carrusel ---
    "hero_carreras",
    # --- Tarjetas base ---
    "fila_materia",
    "item_carrera_ranking",
    "pastilla_anio",
    "tarjeta_carrera",
]