"""
Vista Blog Institucional (ruta "/blog").

Ensambla los componentes del blog. Toda la lógica vive en módulos
separados:

- `dominio.modelos.blog`:      CATEGORIAS + POSTS.
- `dominio.estados.estado_blog`: filtros + paginación.
- `componentes.blog.*`:        componentes visuales.
"""

from __future__ import annotations

import reflex as rx

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

ANCHO_CONTENIDO: str = "64rem"


# ======================================================================
# Vista
# ======================================================================


@rx.page(route="/blog", title=f"Blog | {NOMBRE_INSTITUTO}")
def vista_blog() -> rx.Component:
    """Página del blog institucional del instituto."""
    return rx.vstack(
        barra_navegacion_superior(),
        hero_blog(),
        rx.box(
            rx.vstack(
                # --- Post destacado ---
                post_destacado(),
                # --- Filtros ---
                barra_filtros(),
                # --- Grid o estado vacío ---
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
                # --- Newsletter ---
                newsletter_blog(),
                spacing="6",
                width="100%",
            ),
            max_width=ANCHO_CONTENIDO,
            margin="0 auto",
            padding=f"2rem {PADDING_LATERAL} 4rem {PADDING_LATERAL}",
            width="100%",
        ),
        cta_blog(),
        pie_pagina_institucional(),
        align="center",
        min_height="100vh",
        width="100%",
        spacing="0",
        background=FONDO_HOME,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_blog"]