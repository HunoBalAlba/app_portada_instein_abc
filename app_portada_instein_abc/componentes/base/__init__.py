"""
Paquete `componentes.base`: primitivos y bloques de construcción UI.

Este paquete agrupa los componentes de presentación **más reutilizables**
de la aplicación. Todos son "genéricos" (no dependen de un dominio
concreto) y se usan transversalmente en múltiples vistas.

Contenido
---------
- **acordeon_faq**:  acordeón de preguntas frecuentes reutilizable.
- **badge**:         badges unificados (icono+texto, sólido, contador, estado).
- **estado_vacio**:  estado vacío (sin resultados, error, etc.).
- **primitivos**:    bloques base (contenedor clicable, enlace, tarjetas).
- **vinetas**:       viñetas con icono para listas (perfil, campo laboral, etc.).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein_abc.componentes.base import (
        acordeon_faq, estado_vacio, enlace_navegacion, badge,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein_abc.componentes.base.acordeon_faq import acordeon_faq

Motivo: la ruta de implementación puede cambiar (refactor interno) sin
romper consumidores, siempre que la API pública se mantenga estable.

Qué NO exponer aquí
-------------------
- Estados de Reflex (`EstadoAcordeonFaq`): viven en `dominio.estados`.
- Modelos de datos (`ItemFaq`, `Carrera`): viven en `dominio.modelos`.
- Constantes visuales: viven en `infraestructura.constantes`.

Este paquete SOLO expone componentes de UI puros.

Nota técnica: RUTAS DE IMPORT
-----------------------------
Este archivo vive en `componentes/base/__init__.py`. Para importar
desde los módulos hermanos se usa `.` (un punto):

    from .acordeon_faq import acordeon_faq   # ✅ correcto
    from ...componentes.base.acordeon_faq    # ❌ incorrecto (y roto)

⚠️ El uso de `...componentes.base.X` en la versión anterior era
incorrecto: los 3 puntos suben 2 niveles desde `base/` (llega a la
raíz del paquete), y luego busca `componentes.base.X`, que resuelve
correctamente por casualidad, pero es innecesario y confuso.
"""

from __future__ import annotations


# ======================================================================
# Acordeón de FAQ
# ======================================================================

from .acordeon_faq import (
    ItemFaq,
    acordeon_faq,
)

# ======================================================================
# Badges
# ======================================================================

from .badge import (
    badge,
    badge_contador,
    badge_estado,
    badge_icono_texto,
    badge_solido,
)

# ======================================================================
# Estado vacío
# ======================================================================

from .estado_vacio import estado_vacio

# ======================================================================
# Primitivos
# ======================================================================

from .primitivos import (
    contenedor_clicable,
    enlace_navegacion,
    tarjeta_dato,
    tarjeta_estilizada,
)

# ======================================================================
# Viñetas
# ======================================================================

from .vinetas import (
    COLOR_ICONO,
    MARGEN_TOP_ICONO,
    TAMANO_ICONO,
    vineta_beneficio,
    vineta_campo_laboral,
    vineta_perfil_profesional,
    vineta_requisito,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Acordeón de FAQ
    # ==================================================================
    "ItemFaq",
    "acordeon_faq",
    # ==================================================================
    # Badges
    # ==================================================================
    "badge",
    "badge_contador",
    "badge_estado",
    "badge_icono_texto",
    "badge_solido",
    # ==================================================================
    # Estado vacío
    # ==================================================================
    "estado_vacio",
    # ==================================================================
    # Primitivos
    # ==================================================================
    "contenedor_clicable",
    "enlace_navegacion",
    "tarjeta_dato",
    "tarjeta_estilizada",
    # ==================================================================
    # Viñetas
    # ==================================================================
    "COLOR_ICONO",
    "MARGEN_TOP_ICONO",
    "TAMANO_ICONO",
    "vineta_beneficio",
    "vineta_campo_laboral",
    "vineta_perfil_profesional",
    "vineta_requisito",
]