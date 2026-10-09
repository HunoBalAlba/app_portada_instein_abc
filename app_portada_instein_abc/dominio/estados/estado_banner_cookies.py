

from __future__ import annotations

import reflex as rx


# ======================================================================
# Constantes locales
# ======================================================================

CLAVE_LOCALSTORAGE: str = "instein_cookies_consent"
"""Clave usada en `localStorage` para persistir el consentimiento."""


class EstadoBannerCookies(rx.State):
    """
    Estado del banner de cookies.

    Atributos:
        consentimiento_otorgado: `False` hasta que el usuario elige
            una opción. Cuando pasa a `True`, el banner se oculta.
        motivo_consentimiento: Razón del consentimiento ("all",
            "necessary" o "rejected"). Útil para logging/analytics.
    """

    consentimiento_otorgado: bool = False
    motivo_consentimiento: str = ""

    # ==================================================================
    # Event handlers
    # ==================================================================

    @rx.event
    def aceptar_todas(self):
        """
        Acepta todas las cookies (necesarias + analíticas + marketing).
        """
        self.consentimiento_otorgado = True
        self.motivo_consentimiento = "all"
        yield rx.call_script(
            f"localStorage.setItem('{CLAVE_LOCALSTORAGE}', 'all');"
        )

    @rx.event
    def aceptar_solo_necesarias(self):
        """Acepta solo las cookies necesarias (mínimo legal)."""
        self.consentimiento_otorgado = True
        self.motivo_consentimiento = "necessary"
        yield rx.call_script(
            f"localStorage.setItem('{CLAVE_LOCALSTORAGE}', 'necessary');"
        )

    @rx.event
    def rechazar(self):
        """Rechaza todas las cookies no necesarias."""
        self.consentimiento_otorgado = True
        self.motivo_consentimiento = "rejected"
        yield rx.call_script(
            f"localStorage.setItem('{CLAVE_LOCALSTORAGE}', 'rejected');"
        )


__all__ = ["CLAVE_LOCALSTORAGE", "EstadoBannerCookies"]