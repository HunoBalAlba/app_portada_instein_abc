"""
Vista del Calendario Académico (ruta "/calendario") — estilo Neon.com.

Contenido
---------
1. Hero del calendario (con badge + título + subtítulo).
2. Grid de info rápida (4 tarjetas: inscripciones, inicio, duración,
   modalidad).
3. Sección — Tabs con Actividades y Fechas importantes.
4. CTA final hacia /contacto.
5. Pie de página institucional.

Diseño
------
Refactorizado al estilo Neon.com:

1. **Estructura semántica HTML5** (`main`, `section`, `footer`).
2. **`role="banner"` y `role="contentinfo"`** en los contenedores.
3. **`lang="es"`** en el contenedor raíz.
4. **Descripción SEO** en `@rx.page`.
5. **Separadores** entre secciones (compartido).
6. **Constantes explícitas** (sin magic strings).
7. **`scroll_margin_top`** para compensar la barra sticky.
8. **Responsive mobile-first**.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon.

Nota técnica: COMPOSICIÓN
-------------------------
Este archivo es una **vista de composición**: importa los
componentes del calendario y los ensambla en el orden correcto.

Los componentes viven en `componentes/calendario/`:
- `hero_calendario` → hero con badge + título.
- `grid_info_rapida` → 4 tarjetas de info.
- `tabs_calendario` → tabs con actividades y fechas.
- `cta_calendario` → CTA final.

Este archivo NO define componentes propios. Solo los ensambla.

Nota técnica: `PADDING_LATERAL` IMPORTADO
-----------------------------------------
`PADDING_LATERAL` se importa desde `infraestructura` en lugar de
definirlo localmente. Esto mantiene una sola fuente de verdad para
las dimensiones del proyecto.

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa el componente compartido:

- `separador_secciones` (de `..componentes.base`).

Antes tenía una copia local `_separador_secciones` (duplicada en
6+ archivos). Ahora vive una sola implementación en
`componentes/base/`.
"""

from __future__ import annotations

import reflex as rx

from ..componentes.base import separador_secciones
from ..componentes.calendario import (
    cta_calendario,
    grid_info_rapida,
    hero_calendario,
    tabs_calendario,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    ANCHO_SECCION,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ======================================================================
# Vista
# ======================================================================


@rx.page(
    route="/calendario",
    title=f"Calendario académico | {NOMBRE_INSTITUTO}",
    description=(
        "Calendario académico del Instituto Técnico Integrado San "
        "Antonio de Padua (INSTEIN): actividades del instituto, "
        "fechas importantes de Bolivia y eventos académicos."
    ),
)
def vista_calendario() -> rx.Component:
    """
    Página del calendario académico del instituto — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">`  → barra de navegación.
    - `<main>`                  → contenido principal.
    - `<section>`               → cada sección temática.
    - `<footer role="contentinfo">` → pie de página.

    Composición:
    1. Hero del calendario.
    2. Grid de info rápida (4 tarjetas).
    3. Tabs (Actividades + Fechas importantes).
    4. CTA final hacia /contacto.
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
                # ─── Hero del calendario ────────────────────────────
                rx.el.section(
                    hero_calendario(),
                    width="100%",
                    id="hero-calendario",
                    aria_label="Presentación del calendario académico",
                    scroll_margin_top="5rem",
                ),
                # ─── Grid de info rápida ────────────────────────────
                rx.el.section(
                    grid_info_rapida(),
                    width="100%",
                    id="info-rapida",
                    aria_label="Información rápida del instituto",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(
                    ancho_maximo=ANCHO_MAXIMO_CONTENIDO,
                ),
                # ─── Tabs (Actividades + Fechas importantes) ────────
                rx.el.section(
                    rx.box(
                        tabs_calendario(),
                        max_width=ANCHO_SECCION,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="calendario",
                    aria_label="Calendario académico detallado",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(
                    ancho_maximo=ANCHO_MAXIMO_CONTENIDO,
                ),
                # ─── CTA final ──────────────────────────────────────
                rx.el.section(
                    cta_calendario(),
                    width="100%",
                    id="cta-calendario",
                    aria_label="Contacto para dudas del calendario",
                    scroll_margin_top="5rem",
                ),
                width="100%",
                aria_label="Calendario académico",
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

__all__ = ["vista_calendario"]