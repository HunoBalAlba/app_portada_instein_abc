

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