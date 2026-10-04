"""
Subpaquete `paginas.blog`: vistas del blog institucional.

Contiene:
- **vista_blog**: página de la lista de posts (`/blog`).
- **vista_post**: página de detalle de un post (`/blog/[post_id]`).

Uso desde `paginas/__init__.py`:

    from app_portada_instein.paginas.blog import (
        vista_blog,
        vista_post,
    )

⚠️ IMPORTANTE: `vista_post` requiere `paginas/vista_post.py` (alias) o
que el registro de rutas se haga vía `paginas/__init__.py`.
"""

from __future__ import annotations


from .vista_blog import vista_blog
from .vista_post import vista_post


__all__ = [
    "vista_blog",
    "vista_post",
]