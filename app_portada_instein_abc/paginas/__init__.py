"""
Paquete `paginas`: vistas registradas con `@rx.page`.

Rutas registradas
-----------------
- `/`                        → vista_inicio
- `/carreras`                → vista_carreras
- `/carrera/[carrera_id]`    → vista_detalle_carrera
- `/contacto`                → vista_contacto
- `/sobre-nosotros`          → vista_sobre_nosotros
- `/faq`                     → vista_faq
- `/calendario`              → vista_calendario
- `/admision`                → vista_admision
- `/becas`                   → vista_becas
- `/blog`                    → vista_blog
- `/blog/[post_id]`          → vista_post
- `/404`                     → vista_404

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.paginas import (
        vista_inicio,
        vista_carreras,
        vista_contacto,
    )

⚠️ El import de las vistas REGISTRA las rutas en `rx.App`. Si no se
importan, `reflex run` no las reconoce.

Uso típico
----------
En `configuracion/app_config.py`:

    from app_portada_instein import paginas  # noqa: F401
    # Este import registra todas las rutas automáticamente.
"""

from __future__ import annotations


# ======================================================================
# Vista de inicio
# ======================================================================

from .inicio import vista_inicio

# ======================================================================
# Vistas de carreras
# ======================================================================

from .carreras import vista_carreras
from .detalle_carrera import vista_detalle_carrera

# ======================================================================
# Vistas institucionales
# ======================================================================

from .contacto import vista_contacto
from .sobre_nosotros import vista_sobre_nosotros
from .faq import vista_faq
from .calendario import vista_calendario

# ======================================================================
# Vistas de admisión
# ======================================================================

from .admision import vista_admision
from .becas import vista_becas

# ======================================================================
# Vistas del blog
# ======================================================================

from .blog import vista_blog, vista_post

# ======================================================================
# Vista de error
# ======================================================================

from .error_404 import vista_404


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    "vista_404",
    "vista_admision",
    "vista_becas",
    "vista_blog",
    "vista_calendario",
    "vista_carreras",
    "vista_contacto",
    "vista_detalle_carrera",
    "vista_faq",
    "vista_inicio",
    "vista_post",
    "vista_sobre_nosotros",
]