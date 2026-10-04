"""
Paquete `componentes.blog`: componentes del blog institucional.

Contenido
---------
- **hero**:              hero del blog con badge + título + subtítulo.
- **post_destacado**:    card destacada (featured).
- **filtros_blog**:      buscador + pills de categoría + contador.
- **card_post**:         card + grid + estado vacío + cargar más.
- **newsletter_blog**:   newsletter inline al pie.
- **cta_blog**:          CTA final hacia /carreras o /contacto.
- **meta_info**:         meta info (autor · fecha · minutos).
- **helpers_categoria**: helpers de `rx.match` para categorías.

Nota técnica: DATOS Y ESTADOS
----------------------------
Los datos estáticos (`CATEGORIAS`, `POSTS`) viven en
`dominio.modelos.blog`. El State (`EstadoBlog`) vive en
`dominio.estados.estado_blog`. Este paquete SOLO expone UI.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.componentes.blog import (
        barra_filtros,
        cta_blog,
        hero_blog,
        newsletter_blog,
        post_destacado,
        grid_posts,
        boton_cargar_mas,
        estado_vacio,
    )

❌ **EVITAR** — importar desde el módulo interno.
"""

from __future__ import annotations


# ======================================================================
# Card + grid + cargar más + estado vacío
# ======================================================================

from .card_post import (
    boton_cargar_mas,
    card_post,
    estado_vacio,
    grid_posts,
)

# ======================================================================
# CTA final
# ======================================================================

from .cta_blog import cta_blog

# ======================================================================
# Filtros
# ======================================================================

from .filtros_blog import barra_filtros

# ======================================================================
# Hero
# ======================================================================

from .hero import hero_blog

# ======================================================================
# Meta info
# ======================================================================

from .meta_info import meta_info_post

# ======================================================================
# Newsletter
# ======================================================================

from .newsletter_blog import newsletter_blog

# ======================================================================
# Post destacado
# ======================================================================

from .post_destacado import post_destacado


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # --- Card + grid ---
    "boton_cargar_mas",
    "card_post",
    "estado_vacio",
    "grid_posts",
    # --- CTA final ---
    "cta_blog",
    # --- Filtros ---
    "barra_filtros",
    # --- Hero ---
    "hero_blog",
    # --- Meta info ---
    "meta_info_post",
    # --- Newsletter ---
    "newsletter_blog",
    # --- Post destacado ---
    "post_destacado",
]