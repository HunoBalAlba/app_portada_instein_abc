"""
Modelos del blog institucional.

Este módulo re-exporta los tipos definidos en
`infraestructura.repositorios.repositorio_blog` para que la ruta
canónica de importación sea `dominio.modelos.blog`.

Decisión arquitectónica
-----------------------
Los modelos `Post` y `Categoria` **NO se duplican** aquí. Viven en
`repositorio_blog.py` junto con los datos estáticos. Este módulo
solo expone la API pública.

Motivo: mantener una sola fuente de verdad para cada tipo. Si el
tipo cambia (ej: añadir un campo), se toca un solo lugar.

Convención de imports
---------------------
✅ **RECOMENDADO** — importar desde aquí:
    from app_portada_instein.dominio.modelos.blog import (
        Post,
        Categoria,
        CategoriaId,
        CATEGORIAS,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el repositorio:
    from app_portada_instein.infraestructura.repositorios import (
        Post,
        Categoria,
    )

❌ **EVITAR** — importar desde módulos internos.
"""

from __future__ import annotations


# ======================================================================
# Re-export de tipos
# ======================================================================

from ...infraestructura.repositorios.repositorio_blog import (
    CATEGORIAS,
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
)


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "CATEGORIAS",
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
]