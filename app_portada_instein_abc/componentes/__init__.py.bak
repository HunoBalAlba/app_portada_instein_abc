"""
Paquete `componentes`: capa de presentación (UI pura).

Este es el paquete raíz de todos los componentes visuales del proyecto.
Agrupa 7 subpaquetes organizados por dominio funcional:

1. **base**:        primitivos y bloques reutilizables.
2. **navegacion**:  barra superior + pie de página.
3. **carreras**:    tarjetas, explorador y secciones de detalle.
4. **home**:        secciones de la página de inicio.
5. **blog**:        componentes del blog institucional.
6. **calendario**:  componentes del calendario académico.
7. **legal**:       banner de cookies (RGPD/LGPD/CCPA).

Filosofía
---------
Esta capa NO contiene lógica de negocio. Solo:
- Componentes visuales puros.
- Composición de componentes.
- Estilos y presentación.

Toda la lógica vive en `dominio/`. Los datos viven en
`dominio.modelos`. Las constantes visuales viven en
`infraestructura.constantes`.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete raíz:
    from app_portada_instein.componentes import (
        # Base
        acordeon_faq, badge, estado_vacio, enlace_navegacion,
        # Navegación
        barra_navegacion_superior, pie_pagina_institucional,
        # Carreras
        tarjeta_carrera, explorador_carrera_destacada,
        # Home
        hero_principal, banner_cta_final,
        # Blog
        hero_blog, post_destacado,
        # Calendario
        hero_calendario, tabs_calendario,
        # Legal
        banner_cookies,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el subpaquete:
    from app_portada_instein.componentes.home import hero_principal

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.componentes.home.hero_principal import (
        hero_principal,
    )

Motivo: la ruta interna puede cambiar sin romper consumidores,
siempre que la API pública se mantenga estable.

Reglas del paquete
------------------
1. **Solo UI pura**: NO exponer States (`rx.State`) desde aquí.
2. **Solo tipos públicos**: los `TypedDict` de UI (ej: `ItemFaq`)
   SÍ; los de dominio (`Post`, `Carrera`) NO (viven en
   `dominio.modelos`).
3. **Re-exports agrupados**: cada bloque de `import` viene de un
   subpaquete distinto.
4. **`__all__` exhaustivo**: cualquier símbolo público debe estar
   listado.
"""

from __future__ import annotations


# ======================================================================
# 1. Base: primitivos y bloques reutilizables
# ======================================================================

from .base import (
    ItemFaq,
    acordeon_faq,
    badge,
    badge_contador,
    badge_estado,
    badge_icono_texto,
    badge_solido,
    contenedor_clicable,
    enlace_navegacion,
    estado_vacio,
    tarjeta_dato,
    tarjeta_estilizada,
)

# ======================================================================
# 2. Navegación: barra + pie
# ======================================================================

from .navegacion import (
    ENLACES_FOOTER,
    ColumnaFooter,
    ItemEnlaceFooter,
    barra_navegacion_superior,
    elemento_menu,
    pie_pagina_institucional,
)

# ======================================================================
# 3. Carreras: tarjetas, explorador y detalle
# ======================================================================

from .carreras import (
    fila_materia,
    item_carrera_ranking,
    pastilla_anio,
    seccion_informacion,
    seccion_perfil_y_campo_laboral,
    seccion_plan_estudios,
    tarjeta_carrera,
)

# ======================================================================
# 3.1. Carreras · Explorador (subpaquete específico)
# ======================================================================

from .carreras.explorador import (
    bloque_texto_carrera_destacada,
    contenedor_animacion_orbital,
    cuadro_resumen_multimedia,
    explorador_carrera_destacada,
    pastilla_carrera_destacada,
    selector_carrera_destacada,
)

# ======================================================================
# 4. Home: secciones de la página de inicio
# ======================================================================

from .home import (
    banner_cta_final,
    hero_principal,
    seccion_estadisticas,
    seccion_multimedia_institucional,
    seccion_por_que_instein,
    seccion_preguntas_frecuentes,
)

# ======================================================================
# 5. Blog: componentes del blog institucional
# ======================================================================

from .blog import (
    barra_filtros as barra_filtros_blog,
    boton_cargar_mas,
    card_post,
    cta_blog,
    estado_vacio as estado_vacio_blog,
    grid_posts,
    hero_blog,
    meta_info_post,
    newsletter_blog,
    post_destacado,
)

# ======================================================================
# 6. Calendario: componentes del calendario académico
# ======================================================================

from .calendario import (
    INFO_RAPIDA,
    InfoRapida,
    cta_calendario,
    grid_info_rapida,
    hero_calendario,
    tabs_calendario,
)

# ======================================================================
# 7. Legal: banner de cookies
# ======================================================================

from .legal import (
    banner_cookies,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # 1. Base
    # ==================================================================
    "ItemFaq",
    "acordeon_faq",
    "badge",
    "badge_contador",
    "badge_estado",
    "badge_icono_texto",
    "badge_solido",
    "contenedor_clicable",
    "enlace_navegacion",
    "estado_vacio",
    "tarjeta_dato",
    "tarjeta_estilizada",
    # ==================================================================
    # 2. Navegación
    # ==================================================================
    "ENLACES_FOOTER",
    "ColumnaFooter",
    "ItemEnlaceFooter",
    "barra_navegacion_superior",
    "elemento_menu",
    "pie_pagina_institucional",
    # ==================================================================
    # 3. Carreras
    # ==================================================================
    "fila_materia",
    "item_carrera_ranking",
    "pastilla_anio",
    "seccion_informacion",
    "seccion_perfil_y_campo_laboral",
    "seccion_plan_estudios",
    "tarjeta_carrera",
    # 3.1. Carreras · Explorador
    "bloque_texto_carrera_destacada",
    "contenedor_animacion_orbital",
    "cuadro_resumen_multimedia",
    "explorador_carrera_destacada",
    "pastilla_carrera_destacada",
    "selector_carrera_destacada",
    # ==================================================================
    # 4. Home
    # ==================================================================
    "banner_cta_final",
    "hero_principal",
    "seccion_estadisticas",
    "seccion_multimedia_institucional",
    "seccion_por_que_instein",
    "seccion_preguntas_frecuentes",
    # ==================================================================
    # 5. Blog (alias con sufijo _blog para evitar colisiones)
    # ==================================================================
    "barra_filtros_blog",
    "boton_cargar_mas",
    "card_post",
    "cta_blog",
    "estado_vacio_blog",
    "grid_posts",
    "hero_blog",
    "meta_info_post",
    "newsletter_blog",
    "post_destacado",
    # ==================================================================
    # 6. Calendario
    # ==================================================================
    "INFO_RAPIDA",
    "InfoRapida",
    "cta_calendario",
    "grid_info_rapida",
    "hero_calendario",
    "tabs_calendario",
    # ==================================================================
    # 7. Legal
    # ==================================================================
    "banner_cookies",
]