"""
Paquete `componentes.legal`: componentes legales transversales.

Contenido
---------
- **banner_cookies**: banner de consentimiento de cookies
  (RGPD/LGPD/CCPA).

Uso típico
----------
El banner se monta UNA SOLA VEZ en la vista que lo necesite
(generalmente `paginas/inicio.py`, o globalmente en el layout):

    from app_portada_instein.componentes.legal import banner_cookies

    def pagina():
        return rx.vstack(
            # ...
            banner_cookies(),
        )

El banner decide por sí solo si mostrarse u ocultarse en función del
`EstadoBannerCookies.consentimiento_otorgado`.

Nota técnica: ESTADO
--------------------
El `EstadoBannerCookies` vive en `dominio.estados.estado_banner_cookies`.
Este paquete SOLO expone UI pura.

Convención de imports
---------------------
✅ **CORRECTO**:
    from app_portada_instein.componentes.legal import banner_cookies

❌ **EVITAR** — importar desde módulos internos.
"""

from __future__ import annotations


# ======================================================================
# Banner de cookies
# ======================================================================

from .banner_cookies import banner_cookies


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = ["banner_cookies"]