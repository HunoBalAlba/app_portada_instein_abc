"""
Paquete `componentes.home`: secciones de la página de inicio.

Agrupa los 6 bloques que componen la vista `/` (inicio):

1. **hero_principal**:              hero con título + CTA + explorador.
2. **multimedia_institucional**:    video + plataforma académica + redes.
3. **estadisticas_instituto**:      grid de stats + gráfico de egresados.
4. **seccion_por_que_instein**:     6 razones con diálogos de detalle.
5. **seccion_preguntas_frecuentes**: acordeón de FAQ del home.
6. **banner_cta_final**:            banner CTA con trust indicators.

Estas secciones se ensamblan en `paginas/inicio.py` con
`separador_numerado` intercalados entre las secciones numeradas
(01, 02, 03).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.componentes.home import (
        hero_principal,
        seccion_multimedia_institucional,
        seccion_estadisticas,
        seccion_por_que_instein,
        seccion_preguntas_frecuentes,
        banner_cta_final,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.componentes.home.hero_principal import (
        hero_principal,
    )

Motivo: la ruta interna puede cambiar sin romper consumidores,
siempre que la API pública se mantenga estable.

Qué NO exponer aquí
-------------------
- Estados de Reflex: viven en `dominio.estados`.
- Modelos de datos: viven en `dominio.modelos`.
- Constantes visuales: viven en `infraestructura.constantes`.
- Subcomponentes privados (con guion bajo): no se exponen.

Este paquete SOLO expone componentes de UI puros.
"""

from __future__ import annotations


# ======================================================================
# Banner CTA final
# ======================================================================

from .banner_cta_final import banner_cta_final

# ======================================================================
# Estadísticas del instituto
# ======================================================================

from .estadisticas_instituto import (
    DATA_EGRESADOS,
    ESTADISTICAS,
    Estadistica,
    ItemGrafico,
    seccion_estadisticas,
)

# ======================================================================
# Hero principal
# ======================================================================

from .hero_principal import hero_principal

# ======================================================================
# Multimedia institucional
# ======================================================================

from .multimedia_institucional import seccion_multimedia_institucional

# ======================================================================
# Por qué elegir INSTEIN
# ======================================================================

from .seccion_por_que_instein import (
    RAZONES,
    Razon,
    seccion_por_que_instein,
)

# ======================================================================
# Preguntas frecuentes del home
# ======================================================================

from .seccion_faq import (
    PREGUNTAS_FRECUENTES,
    seccion_preguntas_frecuentes,
)

from .seccion_carreras import (                    # ← NUEVO
    CARRERAS_DESTACADAS,
    CarreraDestacada,
    seccion_carreras_inicio,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Datos exportados ---
    "DATA_EGRESADOS",
    "ESTADISTICAS",
    "Estadistica",
    "ItemGrafico",
    "PREGUNTAS_FRECUENTES",
    "RAZONES",
    "Razon",
    # --- Secciones del home ---
    "banner_cta_final",
    "hero_principal",
    "seccion_estadisticas",
    "seccion_multimedia_institucional",
    "seccion_por_que_instein",
    "seccion_preguntas_frecuentes",

    # ─── Carreras (NUEVO) ────────────────────────────────────
    "CARRERAS_DESTACADAS",
    "CarreraDestacada",
    "seccion_carreras_inicio",
]