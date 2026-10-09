"""
Vista Blog Institucional (ruta "/blog") — estilo Neon.com.

Ensambla los componentes del blog. Toda la lógica vive en módulos
separados.

Diseño UX
---------
1. **Hero** alineado a la izquierda.
2. **Sección 01** con encabezado numerado.
3. **Post destacado** + filtros + grid.
4. **Newsletter** + CTA final.
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base import (
    encabezado_seccion,
    separador_secciones,
)
from ...componentes.blog import (
    barra_filtros,
    boton_cargar_mas,
    cta_blog,
    estado_vacio,
    grid_posts,
    hero_blog,
    newsletter_blog,
    post_destacado,
)
from ...componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ...dominio import EstadoBlog
from ...infraestructura import (
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    PADDING_LATERAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_CONTENIDO: str = "72rem"
ANCHO_MAXIMO_CONTENIDO: str = "80rem"


# ======================================================================
# Vista
# ======================================================================


@rx.page(route="/blog", title=f"Blog | {NOMBRE_INSTITUTO}")
def vista_blog() -> rx.Component:
    """
    Página del blog institucional del instituto.

    Estructura:
    1. Barra de navegación.
    2. Hero.
    3. Sección 01 — Artículos (con encabezado numerado).
    4. CTA final.
    5. Pie de página.
    """
    return rx.box(
        rx.vstack(
            # =============================================================
            # 1. HEADER
            # =============================================================
            rx.box(
                barra_navegacion_superior(),
                width="100%",
                role="banner",
                aria_label="Navegación principal",
            ),
            # =============================================================
            # 2. MAIN
            # =============================================================
            rx.el.main(
                # ─── Hero ───────────────────────────────────────────
                hero_blog(),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── Sección 01 — Artículos ─────────────────────────
                rx.box(
                    rx.vstack(
                        # Encabezado numerado
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Artículos",
                            titulo="Últimas",
                            titulo_enfasis="publicaciones",
                            subtitulo=(
                                "Explora artículos sobre tecnología, "
                                "empleabilidad, tutoriales y vida "
                                "institucional."
                            ),
                        ),
                        # Post destacado
                        post_destacado(),
                        # Filtros
                        barra_filtros(),
                        # Grid o estado vacío
                        rx.cond(
                            EstadoBlog.hay_resultados,
                            rx.vstack(
                                grid_posts(),
                                boton_cargar_mas(),
                                spacing="0",
                                width="100%",
                            ),
                            estado_vacio(),
                        ),
                        # Newsletter
                        newsletter_blog(),
                        spacing="6",
                        width="100%",
                    ),
                    max_width=ANCHO_CONTENIDO,
                    margin="0 auto",
                    padding=f"2rem {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
                    width="100%",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── CTA final ──────────────────────────────────────
                cta_blog(),
                width="100%",
                aria_label="Blog institucional",
            ),
            # =============================================================
            # 3. FOOTER
            # =============================================================
            rx.box(
                pie_pagina_institucional(),
                width="100%",
                role="contentinfo",
                aria_label="Información del sitio",
            ),
            align="center",
            min_height="100vh",
            width="100%",
            spacing="0",
            background=FONDO_HOME,
        ),
        width="100%",
        background=FONDO_HOME,
        lang="es",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_blog"]