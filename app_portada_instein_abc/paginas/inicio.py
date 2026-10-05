"""
Vista de la página de inicio (ruta "/") — estilo Neon.com.

Diseño
------
Inspirado en Neon.com:

1. **Fondo oscuro** con gradiente radial sutil.
2. **Layout horizontal** en cada sección: número a la izquierda,
   contenido a la derecha.
3. **Tipografía masiva** (`size="8"`, `font_weight="900"`).
4. **Espaciado generoso** (padding vertical de 8rem).
5. **Acento único** (azul marino neon).
6. **HTML semántico + SEO**.
7. **Separadores `<hr>`** entre secciones (marca visual).

Estructura
----------
1. Barra de navegación sticky (role="banner").
2. Hero principal con explorador.
2.5. **Sección 00 — Carreras destacadas** (NUEVO).
3. Sección 01 — Multimedia institucional.
4. Sección 02 — Estadísticas.
5. Sección 03 — ¿Por qué INSTEIN?.
6. Sección 04 — Preguntas frecuentes.
7. Banner CTA final.
8. Footer institucional (role="contentinfo").
9. Banner de cookies (RGPD).

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: PROPS DE FLEX EN REFLEX
-------------------------------------
Según la documentación de `rx.flex`:

- `direction`:  "row" | "column" | "row-reverse" | "column-reverse".
- `align`:      "start" | "center" | "end" | "baseline" | "stretch".
- `justify`:    "start" | "center" | "end" | "between".
- `wrap`:       "nowrap" | "wrap" | "wrap-reverse".
- `spacing`:    "0" - "9".

Todos son props **cerrados** → aceptan un solo valor string.
Para responsive, usar `rx.breakpoints(...)`.

Nota técnica: HTML5 SEMÁNTICO
-----------------------------
Uso `rx.el.main()` en lugar de `rx.box(role="main")` para
aprovechar la semántica nativa de HTML5:

- `<main>`: contenido principal de la página.
- `<section>`: secciones temáticas.
- `<footer>`: pie de página (implementado en `pie_pagina`).
- `<header>`: cabecera (role="banner").

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa los componentes compartidos:

- `encabezado_seccion` (de `..componentes.base`).
- `separador_secciones` (de `..componentes.base`).

Antes tenía copias locales `_encabezado_seccion` y
`_separador_secciones` (duplicadas en 6+ archivos). Ahora vive
una sola implementación en `componentes/base/`.

Nota técnica: SECCIÓN DE CARRERAS (NUEVO)
-----------------------------------------
Se añade la sección `seccion_carreras_inicio()` **inmediatamente
después del hero**, para que el visitante vea las carreras del
instituto en los primeros segundos.

Esta sección NO tiene número (`01`, `02`...) porque es una
"introducción" al catálogo, no una sección temática más. Las
secciones numeradas empiezan después, en Multimedia (01).
"""

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    encabezado_seccion,
    separador_secciones,
)
from ..componentes.home import (
    banner_cta_final,
    hero_principal,
    seccion_carreras_inicio,          # ← NUEVO
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
        numero: "01", "02", "03", "04".
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

    Composición:
    1. Header (barra de navegación).
    2. Hero principal.
    3. **Carreras destacadas** (NUEVO).
    4. Sección 01 — Multimedia institucional.
    5. Sección 02 — Estadísticas.
    6. Sección 03 — ¿Por qué INSTEIN?.
    7. Sección 04 — Preguntas frecuentes.
    8. Banner CTA final.
    9. Footer institucional.
    10. Banner de cookies.
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
                # ─── 2.2 Carreras destacadas (NUEVO) ────────────────
                seccion_carreras_inicio(),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── 2.3 Sección 01 — Multimedia ────────────────────
                _seccion(
                    numero="01",
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
                # ─── 2.4 Sección 02 — Estadísticas ──────────────────
                _seccion(
                    numero="02",
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
                # ─── 2.5 Sección 03 — ¿Por qué INSTEIN? ─────────────
                _seccion(
                    numero="03",
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
                # ─── 2.6 Sección 04 — FAQ ───────────────────────────
                _seccion(
                    numero="04",
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