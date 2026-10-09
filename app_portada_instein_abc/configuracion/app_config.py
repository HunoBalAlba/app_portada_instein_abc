

# from __future__ import annotations

# import reflex as rx

# # from ..configuracion.estilos_globales import (
# #     construir_estilos_globales,
# # )
# from ..infraestructura import (
#     ACCENT_COLOR_TEMA,
#     ESTILO_BASE,
#     FUENTE_PRINCIPAL,
#     HOJAS_DE_ESTILO_BASE,
# )


# # ======================================================================
# # Constantes locales
# # ======================================================================

# HOJAS_DE_ESTILO_LOCALES: list[str] = [
#     "/styles/global.css",
# ]
# """Hojas de estilo locales del proyecto (en `assets/styles/`)."""

# RADIO_TEMA: str = "medium"
# """Radio del tema Radix (small | medium | large | full)."""

# APARIENCIA_INICIAL: str = "light"
# """Apariencia inicial (light | dark | inherit)."""


# # ======================================================================
# # API pública
# # ======================================================================


# def crear_aplicacion() -> rx.App:
#     """
#     Crea y configura la aplicación Reflex.

#     Estructura del App:
#     - **theme**:          accent_color, radius, font_family.
#     - **style**:          keyframes + estilos CSS globales + estilos base.
#     - **stylesheets**:    Google Fonts + CSS local.

#     Returns:
#         Instancia de `rx.App` configurada.

#     Examples:
#         Desde `app.py`:

#             from app_portada_instein_abc.configuracion.app_config import (
#                 crear_aplicacion,
#             )

#             app = crear_aplicacion()
#     """
#     # ==================================================================
#     # Importar el paquete `paginas` para REGISTRAR las rutas
#     # ==================================================================
#     # ⚠️ OBLIGATORIO: sin este import, `@rx.page` no registra nada.
#     #
#     # CORRECTO:    from .. import paginas       # importa el paquete
#     # INCORRECTO:  from ..paginas import paginas  # ❌ ImportError
#     #
#     # El import se hace DENTRO de `crear_aplicacion()` (no a nivel de
#     # módulo) para evitar ciclos de importación:
#     #   - paginas/*.py importa componentes/*.
#     #   - componentes/* no importa configuracion/*, pero sí app_config
#     #     cuando se cargan las vistas.
#     # ------------------------------------------------------------------
#     from .. import paginas  # noqa: F401

#     # ==================================================================
#     # Fusionar estilos globales
#     # ==================================================================
#     estilos_globales: dict = {
#         **ESTILO_BASE,
#         **construir_estilos_globales(),
#     }

#     # ==================================================================
#     # Crear el App
#     # ==================================================================
#     return rx.App(
#         theme=rx.theme(
#             appearance=APARIENCIA_INICIAL,
#             accent_color=ACCENT_COLOR_TEMA,
#             radius=RADIO_TEMA,
#             font_family=FUENTE_PRINCIPAL,
#         ),
#         style=estilos_globales,
#         stylesheets=[
#             *HOJAS_DE_ESTILO_BASE,
#             *HOJAS_DE_ESTILO_LOCALES,
#         ],
#     )


# # ======================================================================
# # EXPORTS
# # ======================================================================

# __all__ = [
#     "APARIENCIA_INICIAL",
#     "HOJAS_DE_ESTILO_LOCALES",
#     "RADIO_TEMA",
#     "crear_aplicacion",
# ]