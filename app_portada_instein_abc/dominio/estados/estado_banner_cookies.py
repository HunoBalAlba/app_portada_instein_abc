"""
Estado del banner de consentimiento de cookies.

Gestiona el consentimiento del usuario y persiste la decisión en
`localStorage` para futuras visitas.

Referencia legal
----------------
- RGPD (UE) · Art. 7: consentimiento explícito e informado.
- LGPD (Brasil) · Art. 8: consentimiento del titular.
- CCPA (California) · §1798.100: derecho a saber y opt-out.

Nota técnica: `rx.call_script` con `yield`
------------------------------------------
Los eventos usan `yield rx.call_script(...)` (no `return`) para
permitir múltiples efectos:

1. Actualizar el State (oculta el banner).
2. Ejecutar JS en el cliente (persiste en `localStorage`).

⚠️ El ORDEN importa: primero se actualiza el State, luego el script.
"""

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