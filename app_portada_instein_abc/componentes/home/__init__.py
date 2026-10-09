

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