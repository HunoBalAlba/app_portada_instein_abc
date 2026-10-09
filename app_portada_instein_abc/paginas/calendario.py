

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    encabezado_seccion,
    separador_secciones,
)
from ..componentes.calendario import (
    cronograma_bimestres,
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


ANCHO_MAXIMO_CONTENIDO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


@rx.page(
    route="/calendario",
    title=f"Calendario académico | {NOMBRE_INSTITUTO}",
    description=(
        "Calendario académico del Instituto Técnico Integrado San "
        "Antonio de Padua (INSTEIN): cronograma de bimestres, "
        "actividades y fechas importantes de Bolivia."
    ),
)
def vista_calendario() -> rx.Component:
    """
    Página del calendario académico del instituto — estilo Neon.com.

    Estructura:
    1. Hero.
    2. Grid de info rápida (4 tarjetas).
    3. Sección 01 — Cronograma de bimestres.
    4. Sección 02 — Actividades y fechas importantes.
    5. CTA final.
    """
    return rx.box(
        rx.vstack(
            # ─── HEADER ────────────────────────────────────────────
            rx.box(
                barra_navegacion_superior(),
                width="100%",
                role="banner",
                aria_label="Navegación principal",
            ),
            # ─── MAIN ──────────────────────────────────────────────
            rx.el.main(
                # Hero
                rx.el.section(
                    hero_calendario(),
                    width="100%",
                    id="hero-calendario",
                    aria_label="Presentación del calendario académico",
                    scroll_margin_top="5rem",
                ),
                # Grid de info rápida
                rx.el.section(
                    grid_info_rapida(),
                    width="100%",
                    id="info-rapida",
                    aria_label="Información rápida del instituto",
                    scroll_margin_top="5rem",
                ),
                # Separador
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── Sección 01 — Cronograma de bimestres ──────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Cronograma académico",
                            titulo="4 bimestres,",
                            titulo_enfasis="12 meses",
                            subtitulo=(
                                "Cada bimestre tiene un inicio, "
                                "parciales, examen final y cierre de "
                                "actas. Consulta las fechas clave."
                            ),
                        ),
                        cronograma_bimestres(),
                        max_width=ANCHO_SECCION,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="cronograma",
                    aria_label="Cronograma de bimestres",
                    scroll_margin_top="5rem",
                ),
                # Separador
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── Sección 02 — Actividades + Fechas ─────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="02",
                            etiqueta="Calendario detallado",
                            titulo="Actividades y",
                            titulo_enfasis="fechas importantes",
                            subtitulo=(
                                "Consulta todas las actividades del "
                                "instituto y las fechas relevantes del "
                                "calendario boliviano."
                            ),
                        ),
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
                    aria_label="Calendario detallado",
                    scroll_margin_top="5rem",
                ),
                # Separador
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # CTA final
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
            # ─── FOOTER ────────────────────────────────────────────
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


__all__ = ["vista_calendario"]