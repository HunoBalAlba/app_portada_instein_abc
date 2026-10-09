

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