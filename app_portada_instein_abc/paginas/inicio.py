

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    encabezado_seccion,
    separador_secciones,
)
from ..componentes.home import (
    banner_cta_final,
    hero_principal,
    seccion_carreras_inicio,
    seccion_estadisticas,
    seccion_multimedia_institucional,
    seccion_por_que_instein,
    seccion_preguntas_frecuentes,
)
from ..componentes.legal import banner_cookies
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    FONDO_HOME,
    NOMBRE_INSTITUTO,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"

# SEO
DESCRIPCION_SEO: str = (
    "INSTEIN · Instituto Técnico Integrado San Antonio de Padua. "
    "Formación técnica de excelencia con títulos de Provisión "
    "Nacional. 5 carreras, equipamiento moderno y docentes "
    "especializados."
)

URL_BASE: str = "https://instein.edu.bo"
IMAGEN_OG: str = f"{URL_BASE}/og_image.png"


# ======================================================================
# Sección (estilo Neon.com)
# ======================================================================


def _seccion(
    numero: str,
    etiqueta: str,
    titulo: str,
    subtitulo: str | None,
    contenido: rx.Component,
    id_seccion: str,
) -> rx.Component:
    """
    Sección con encabezado horizontal + contenido.

    Estilo Neon.com:
    - Padding vertical generoso (unificado).
    - Encabezado horizontal (número + título).
    - Contenido debajo, ocupando el ancho completo.
    - `scroll-margin-top` para compensar la barra sticky.

    Args:
        numero: "02", "03", "04", "05".
        etiqueta: Texto pequeño en mayúsculas.
        titulo: Título de la sección.
        subtitulo: Subtítulo opcional.
        contenido: Componente con el contenido.
        id_seccion: ID único (para anchor links).

    Returns:
        Componente `<section>` completo.
    """
    return rx.section(
        rx.box(
            # ─── Encabezado horizontal ───────────────────────────
            encabezado_seccion(numero, etiqueta, titulo, subtitulo),
            # ─── Contenido ──────────────────────────────────────
            contenido,
            padding=[
                f"5rem {PADDING_SECCION_HORIZONTAL}",
                f"7rem {PADDING_SECCION_HORIZONTAL}",
                f"8rem {PADDING_SECCION_HORIZONTAL}",
            ],
            max_width=ANCHO_MAXIMO_CONTENIDO,
            margin="0 auto",
            width="100%",
        ),
        width="100%",
        id=id_seccion,
        aria_label=titulo,
        # Compensa la barra sticky al hacer scroll a un anchor
        scroll_margin_top="5rem",
    )


# ======================================================================
# Vista de inicio
# ======================================================================


@rx.page(
    route="/",
    title=f"Inicio | {NOMBRE_INSTITUTO}",
    description=DESCRIPCION_SEO,
    image=IMAGEN_OG,
)
def vista_inicio() -> rx.Component:
    """
    Página principal de bienvenida — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">` → barra de navegación.
    - `<main>`                 → contenido principal.
    - `<section>`              → cada sección temática.
    - `<footer>`               → pie de página (en su componente).
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
                # ─── 2.1 Hero principal ─────────────────────────────
                rx.box(
                    hero_principal(),
                    width="100%",
                    role="article",
                    aria_label="Presentación principal",
                ),
                # ─── 2.2 Sección 01 — Carreras destacadas ───────────
                seccion_carreras_inicio(),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── 2.3 Sección 02 — Multimedia ────────────────────
                _seccion(
                    numero="02",
                    etiqueta="Multimedia",
                    titulo="Conoce nuestro instituto",
                    subtitulo=(
                        "Video institucional, plataforma académica y "
                        "redes sociales oficiales."
                    ),
                    contenido=seccion_multimedia_institucional(),
                    id_seccion="multimedia",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── 2.4 Sección 03 — Estadísticas ──────────────────
                _seccion(
                    numero="03",
                    etiqueta="Métricas institucionales",
                    titulo="15 años formando técnicos de excelencia",
                    subtitulo=(
                        "Cifras que respaldan nuestro compromiso con la "
                        "formación técnica superior."
                    ),
                    contenido=seccion_estadisticas(),
                    id_seccion="estadisticas",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── 2.5 Sección 04 — ¿Por qué INSTEIN? ─────────────
                _seccion(
                    numero="04",
                    etiqueta="Nuestra propuesta",
                    titulo="Formación que transforma",
                    subtitulo=(
                        "Todo lo que necesitas para convertirte en un "
                        "profesional técnico de excelencia."
                    ),
                    contenido=seccion_por_que_instein(),
                    id_seccion="por-que-instein",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── 2.6 Sección 05 — FAQ ───────────────────────────
                _seccion(
                    numero="05",
                    etiqueta="Resolvemos tus dudas",
                    titulo="¿Tienes preguntas?",
                    subtitulo=(
                        "Las respuestas a las dudas más comunes de "
                        "nuestros estudiantes."
                    ),
                    contenido=seccion_preguntas_frecuentes(),
                    id_seccion="faq",
                ),
                # ─── 2.7 Banner CTA final ───────────────────────────
                rx.box(
                    banner_cta_final(),
                    padding=[
                        f"4rem {PADDING_SECCION_HORIZONTAL}",
                        f"6rem {PADDING_SECCION_HORIZONTAL}",
                        f"6rem {PADDING_SECCION_HORIZONTAL}",
                    ],
                    max_width=ANCHO_MAXIMO_CONTENIDO,
                    margin="0 auto",
                    width="100%",
                ),
                width="100%",
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
            # =============================================================
            # 4. BANNER DE COOKIES
            # =============================================================
            banner_cookies(),
            # =============================================================
            # Layout del contenedor raíz
            # =============================================================
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

__all__ = ["vista_inicio"]