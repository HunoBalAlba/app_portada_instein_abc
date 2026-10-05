"""
Vista de detalle de una carrera específica
(ruta dinámica "/carrera/[carrera_id]") — estilo Neon.com.

Estructura
----------
1. Encabezado sticky con breadcrumb.
2. Hero con imagen banner de fondo + gradiente oscuro + contenido.
3. Marquee de iconos (características de la carrera).
4. Pestañas descriptivas (Sobre la carrera, Malla curricular, Perfil y salidas).
5. Sección de FAQ (con separador).
6. Botón flotante "volver arriba" minimalista.
7. Pie de página institucional.

Diseño UX
---------
Inspirado en el **hero principal del home** y en **Neon.com**:

1. **Imagen banner de fondo** (`imagen_banner`) con `object_fit=cover`.
2. **Gradiente oscuro** (transparente → negro) para legibilidad.
3. **Contenido superpuesto**: badge + título + lema + CTAs.
4. **Trust badges** (duración, modalidad, cupos) sobre el hero.
5. **Marquee de iconos** de las características.
6. **Tabs descriptivas** (no genéricas como "Info" o "Plan").
7. **HTML5 semántico** (`main`, `section`, `article`).
8. **Breadcrumb sticky** con blur.
9. **Responsive mobile-first**.
10. **Énfasis bicolor** en el nombre de la carrera.

Sistema de color
----------------
✅ ACENTO ÚNICO: azul marino neon.
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.

Nota técnica: TABS DESCRIPTIVAS (NUEVO)
---------------------------------------
Las etiquetas de los tabs cambiaron de genéricas a descriptivas:

- **Antes**: `Info` / `Plan` / `Perfil`
- **Ahora**: `Sobre la carrera` / `Malla curricular` / `Perfil y salidas`

Motivo UX: los usuarios nuevos no saben qué esperar de "Info" o "Plan".
Las etiquetas descriptivas mejoran la descubribilidad del contenido y
el SEO (keywords: "carrera", "malla curricular", "salidas laborales").

Nota técnica: ELIMINACIÓN DEL SISTEMA ORBITAL
--------------------------------------------
Se eliminó TODO el sistema kepleriano:
- `_anillos_saturno()`
- `_icono_orbital()`
- `_contenedor_orbital_imagen()`
- El import de `IconoAnimado` desde `..dominio`

En su lugar, se usa:
- `imagen_banner` como fondo del hero.
- `caracteristicas` de la carrera en el marquee.

Nota técnica: MARQUEE DE ICONOS
-------------------------------
Debajo del hero se muestra un **marquee horizontal** con los
iconos de las características de la carrera. Técnica CSS:

1. Se duplica la lista de características `[items, items]`.
2. Se anima `translateX(-50%)` con la duración definida.
3. Al reiniciar, el segundo bloque ocupa el lugar del primero → scroll infinito.
4. Se pausa al hover (mejora UX).

⚠️ El marquee es DINÁMICO: usa `carrera["caracteristicas"]`, así
cada carrera muestra sus propios iconos.

Nota técnica: TRUST BADGES
--------------------------
Se muestran los datos clave (`duracion`, `modalidad`, `cupos`) en
badges con borde (patrón ya usado en `contacto.py`).

Nota técnica: ACORDEÓN FAQ UNIFICADO
------------------------------------
La sección de preguntas frecuentes delega en `acordeon_faq` con
variante `"light"`.

⚠️ IMPORTANTE: los items del acordeón vienen como `Var` reactiva
(`carrera_seleccionada["preguntas_frecuentes"]`), NO como lista
estática de Python.

Nota técnica: VALIDACIÓN DE RUTA
--------------------------------
El decorador `@rx.page` incluye
`on_load=EstadoInstitucional.redirigir_si_carrera_invalida`.

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa los componentes compartidos:

- `acordeon_faq` (de `..componentes.base`).
- `enlace_navegacion` (de `..componentes.base`).
- `separador_secciones` (de `..componentes.base`).
"""

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    acordeon_faq,
    enlace_navegacion,
    separador_secciones,
)
from ..componentes.carreras import (
    seccion_informacion,
    seccion_perfil_y_campo_laboral,
    seccion_plan_estudios,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..dominio import (
    EstadoInstitucional,
)
from ..infraestructura import (
    ANCHO_CONTENIDO,
    ANCHO_SECCION,
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    PADDING_LATERAL,
    RADIO_EXTRA_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_INFERIOR_PESTANAS = f"0 {PADDING_LATERAL} 4rem {PADDING_LATERAL}"

# Altura mínima del hero con imagen de fondo.
ALTURA_HERO: list[str] = ["28rem", "32rem", "36rem"]

# Duración de un ciclo completo del marquee (segundos).
DURACION_MARQUEE_SEGUNDOS: int = 30


# ======================================================================
# Configuración de tabs (NUEVO)
# ======================================================================

# Cada tab tiene: etiqueta descriptiva, icono Lucide, valor interno.
# Las etiquetas son DESCRIPTIVAS (UX) y los valores son INTERNOS (código).
TABS_DETALLE: list[dict] = [
    {
        "etiqueta": "Sobre la carrera",
        "icono": "info",
        "valor": "info",
    },
    {
        "etiqueta": "Malla curricular",
        "icono": "book-open-text",
        "valor": "plan",
    },
    {
        "etiqueta": "Perfil y salidas",
        "icono": "target",
        "valor": "perfil",
    },
]


# ======================================================================
# Tabs: triggers
# ======================================================================


def _tab_trigger(
    texto: str,
    icono: str,
    value: str,
) -> rx.Component:
    """
    Trigger de pestaña con icono + texto descriptivo.

    Diseño UX:
    - **Móvil**: solo texto (ahorra espacio).
    - **Tablet/desktop**: icono + texto.
    - **Activo**: color azul marino + border_bottom.
    - **Hover**: transición suave a azul marino.

    Args:
        texto: Etiqueta descriptiva (ej: "Sobre la carrera").
        icono: Icono Lucide (kebab-case).
        value: Valor interno del tab (ej: "info").

    Returns:
        Trigger de tab con icono + texto.
    """
    return rx.tabs.trigger(
        # ─── Móvil: solo texto ─────────────────────────────────
        rx.mobile_only(
            rx.text(
                texto,
                font_size="0.8125rem",
                font_weight="600",
                white_space="nowrap",
            ),
        ),
        # ─── Tablet/desktop: icono + texto ─────────────────────
        rx.tablet_and_desktop(
            rx.flex(
                rx.icon(icono, size=16),
                rx.text(
                    texto,
                    font_size="0.875rem",
                    font_weight="600",
                    white_space="nowrap",
                ),
                align="center",
                gap="0.5rem",
            ),
        ),
        value=value,
        padding="0.75rem 1rem",
        color=TEXTO_HOME_MAS_SUAVE,
        transition="all 0.2s",
        _hover={"color": AZUL_MARINO_NEON},
        _selected={
            "color": AZUL_MARINO_NEON,
        },
    )


# ======================================================================
# Encabezado sticky con breadcrumb
# ======================================================================


def _encabezado_fijo_detalle() -> rx.Component:
    """
    Encabezado sticky con breadcrumb integrado.

    Estilo Neon.com:
    - Botón "Volver" a la izquierda.
    - Breadcrumb integrado (Carreras > Nombre corto).
    - Border_bottom sutil.
    - Backdrop blur para legibilidad al hacer scroll.
    """
    nombre_corto = EstadoInstitucional.carrera_seleccionada["nombre_corto"]

    return rx.box(
        rx.flex(
            # ─── Botón de regreso ───────────────────────────────
            enlace_navegacion(
                "/carreras",
                rx.icon("arrow-left", size=16),
                rx.text(
                    "Volver",
                    font_size="0.8125rem",
                    font_weight="600",
                ),
                color=TEXTO_HOME_PRINCIPAL,
                padding="0.5rem 0.75rem",
                border_radius=RADIO_MEDIO,
                background="transparent",
                border=f"1px solid {BORDE_HOME_MEDIO}",
                display="flex",
                align_items="center",
                gap="0.375rem",
                transition="all 0.2s",
                flex_shrink="0",
                text_decoration="none",
                _hover={
                    "border_color": BORDE_HOME_AZUL,
                    "background": FONDO_AZUL_SUAVE,
                },
            ),
            # ─── Breadcrumb integrado ───────────────────────────
            rx.flex(
                rx.text(
                    "Carreras",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                rx.icon(
                    "chevron-right",
                    size=12,
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                rx.text(
                    nombre_corto,
                    font_size="0.8125rem",
                    font_weight="600",
                    color=TEXTO_HOME_PRINCIPAL,
                ),
                align="center",
                gap="0.375rem",
                display=rx.breakpoints(
                    initial="none",
                    md="flex",
                ),
            ),
            align="center",
            justify="between",
            width="100%",
            max_width=ANCHO_CONTENIDO,
            margin="0 auto",
            gap="1rem",
        ),
        width="100%",
        padding="0.75rem 1.5rem",
        background=rx.color("gray", 1, alpha=True),
        backdrop_filter="blur(12px)",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        position="sticky",
        top="0",
        z_index="50",
    )


# ======================================================================
# Trust badges (duración, modalidad, cupos)
# ======================================================================


def _badge_info(
    icono: str,
    texto: str,
) -> rx.Component:
    """
    Badge informativo sobre la imagen (duración, modalidad, cupos).

    Estilo Neon.com sobre imagen:
    - Fondo semitransparente con blur.
    - Texto blanco.
    - Borde blanco sutil.
    - Icono a la izquierda.
    """
    return rx.flex(
        rx.icon(icono, size=12, color="white"),
        rx.text(
            texto,
            font_size="0.75rem",
            font_weight="600",
            color="white",
            white_space="nowrap",
        ),
        align="center",
        gap="0.375rem",
        padding="0.375rem 0.75rem",
        border_radius=RADIO_PASTILLA,
        background="rgba(255, 255, 255, 0.1)",
        backdrop_filter="blur(8px)",
        border="1px solid rgba(255, 255, 255, 0.2)",
    )


# ======================================================================
# Hero con imagen banner de fondo
# ======================================================================


def _hero_carrera() -> rx.Component:
    """
    Hero del detalle de carrera con imagen banner de fondo.

    Estilo Neon.com (como la captura de referencia):
    - Imagen de fondo (`imagen_banner`) con `object_fit=cover`.
    - Gradiente lineal oscuro (transparente → negro) para legibilidad.
    - Contenido superpuesto: badge + título + lema + trust badges + CTAs.
    - Border radius grande.
    - Altura fija responsive.

    Returns:
        Hero completo con imagen de fondo.
    """
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.box(
        # ═════════════════════════════════════════════════════════
        # Capa 1: Imagen de fondo
        # ═════════════════════════════════════════════════════════
        rx.image(
            src=f"/{carrera['imagen_banner']}",
            alt=carrera["nombre"],
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
            z_index="0",
        ),
        # ═════════════════════════════════════════════════════════
        # Capa 2: Gradiente oscuro (para legibilidad)
        # ═════════════════════════════════════════════════════════
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=(
                "linear-gradient(180deg, "
                "rgba(0, 0, 0, 0.3) 0%, "
                "rgba(0, 0, 0, 0.5) 40%, "
                "rgba(0, 0, 0, 0.85) 100%)"
            ),
            z_index="1",
        ),
        # ═════════════════════════════════════════════════════════
        # Capa 3: Contenido superpuesto
        # ═════════════════════════════════════════════════════════
        rx.vstack(
            # ─── Badge de categoría ─────────────────────────────
            rx.flex(
                rx.icon("award", size=12, color="white"),
                rx.text(
                    "TÉCNICO SUPERIOR",
                    font_size="0.6875rem",
                    font_weight="700",
                    color="white",
                    letter_spacing="0.15em",
                    text_transform="uppercase",
                ),
                align="center",
                gap="0.5rem",
                padding="0.375rem 0.75rem",
                border_radius=RADIO_PASTILLA,
                background="rgba(255, 255, 255, 0.1)",
                backdrop_filter="blur(8px)",
                border="1px solid rgba(255, 255, 255, 0.2)",
                width="fit-content",
                margin_bottom="1.5rem",
            ),
            # ─── Nombre de la carrera ───────────────────────────
            rx.heading(
                carrera["nombre"],
                as_="h1",
                font_size=["2rem", "2.75rem", "3.5rem"],
                font_weight="700",
                color="white",
                line_height="1.1",
                letter_spacing="-0.03em",
                max_width="48rem",
                text_shadow="0 2px 12px rgba(0, 0, 0, 0.6)",
            ),
            # ─── Lema ───────────────────────────────────────────
            rx.text(
                carrera["lema"],
                font_size=["1rem", "1.125rem", "1.25rem"],
                color="rgba(255, 255, 255, 0.9)",
                line_height="1.6",
                max_width="42rem",
                margin_top="1rem",
                text_shadow="0 1px 6px rgba(0, 0, 0, 0.5)",
            ),
            # ─── Trust badges (duración, modalidad, cupos) ──────
            rx.flex(
                _badge_info("clock", carrera["duracion"]),
                _badge_info("building-2", carrera["modalidad"]),
                _badge_info(
                    "users",
                    f"{carrera['cupos_disponibles']} cupos",
                ),
                flex_wrap="wrap",
                gap="0.5rem",
                margin_top="1.5rem",
            ),
            # ─── CTAs ───────────────────────────────────────────
            rx.flex(
                enlace_navegacion(
                    "/admision",
                    rx.text(
                        "Inscribirme ahora",
                        as_="span",
                        font_weight="600",
                    ),
                    rx.icon("arrow-right", size=16, color=AZUL_MARINO_NEON),
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background="white",
                    color=AZUL_MARINO_NEON,
                    padding="0.875rem 1.5rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    text_decoration="none",
                    transition="all 0.2s",
                    width="fit-content",
                    _hover={"filter": "brightness(0.95)"},
                ),
                enlace_navegacion(
                    "/contacto",
                    rx.text(
                        "Contactar",
                        as_="span",
                        font_weight="600",
                    ),
                    display="inline-flex",
                    align_items="center",
                    gap="0.5rem",
                    background="rgba(255, 255, 255, 0.1)",
                    color="white",
                    padding="0.875rem 1.5rem",
                    border_radius=RADIO_PASTILLA,
                    font_size="0.9375rem",
                    border="1px solid rgba(255, 255, 255, 0.3)",
                    backdrop_filter="blur(8px)",
                    text_decoration="none",
                    transition="all 0.2s",
                    width="fit-content",
                    _hover={
                        "background": "rgba(255, 255, 255, 0.15)",
                        "border_color": "rgba(255, 255, 255, 0.5)",
                    },
                ),
                gap="0.75rem",
                margin_top="2rem",
                flex_direction=rx.breakpoints(
                    initial="column",
                    sm="row",
                ),
                align="start",
                flex_wrap="wrap",
            ),
            align="start",
            justify="end",
            spacing="0",
            width="100%",
            height="100%",
            padding=[
                "2rem 1.5rem",
                "3rem 2rem",
                "4rem 3rem",
            ],
            position="relative",
            z_index="2",
        ),
        # ═════════════════════════════════════════════════════════
        # Estilos base del hero
        # ═════════════════════════════════════════════════════════
        position="relative",
        width="100%",
        min_height=ALTURA_HERO,
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        max_width=ANCHO_CONTENIDO,
        margin="0 auto",
    )


# ======================================================================
# MARQUEE de iconos
# ======================================================================


def _item_marquee_caracteristica(caracteristica: dict) -> rx.Component:
    """
    Item individual del marquee: icono + etiqueta + separador vertical.

    Args:
        caracteristica: Dict con `icono`, `etiqueta`, `descripcion`.

    Returns:
        Fila con icono + texto + separador.
    """
    return rx.flex(
        # ─── Icono ─────────────────────────────────────────────
        rx.icon(
            caracteristica["icono"],
            size=18,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
        ),
        # ─── Etiqueta ──────────────────────────────────────────
        rx.text(
            caracteristica["etiqueta"],
            font_size="0.9375rem",
            font_weight="600",
            color=TEXTO_HOME_PRINCIPAL,
            white_space="nowrap",
            letter_spacing="-0.01em",
        ),
        # ─── Separador vertical ────────────────────────────────
        rx.box(
            width="1px",
            height="1rem",
            background=BORDE_HOME_SUAVE,
            flex_shrink="0",
        ),
        align="center",
        gap="0.75rem",
        padding_x="1.5rem",
        flex_shrink="0",
    )


def _marquee_caracteristicas() -> rx.Component:
    """
    Marquee horizontal infinito con los iconos de las características
    de la carrera.

    Propósito UX
    ------------
    Refuerza visualmente las características clave de cada carrera
    justo debajo del hero, mientras el visitante hace scroll.

    Técnica CSS
    -----------
    1. Duplicamos la lista `[items, items]`.
    2. Animamos `translateX(-50%)` en `DURACION_MARQUEE_SEGUNDOS`
       segundos, `linear`, `infinite`.
    3. Al terminar la animación, se reinicia sin que se note el
       salto porque el segundo bloque está en la posición del primero.
    4. Se pausa al hover para permitir lectura.

    Returns:
        Componente con el marquee horizontal.
    """
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.box(
        rx.box(
            rx.flex(
                # ─── Bloque 1: características ─────────────────────
                rx.foreach(
                    carrera["caracteristicas"],
                    _item_marquee_caracteristica,
                ),
                # ─── Bloque 2: características duplicadas ──────────
                rx.foreach(
                    carrera["caracteristicas"],
                    _item_marquee_caracteristica,
                ),
                align="center",
                width="max-content",
                class_name="marquee-track",
                animation=(
                    f"marquee_horizontal "
                    f"{DURACION_MARQUEE_SEGUNDOS}s "
                    f"linear infinite"
                ),
            ),
            width="100%",
            overflow="hidden",
            position="relative",
            mask=(
                "linear-gradient(90deg, "
                "transparent 0%, "
                "black 8%, "
                "black 92%, "
                "transparent 100%)"
            ),
            _hover={
                "& .marquee-track": {
                    "animation_play_state": "paused",
                },
            },
        ),
        width="100%",
        padding_y="1.5rem",
        border_top=f"1px solid {BORDE_HOME_SUAVE}",
        border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        background=rx.color_mode_cond(
            light="rgba(59, 91, 219, 0.02)",
            dark="rgba(59, 91, 219, 0.04)",
        ),
        max_width=ANCHO_CONTENIDO,
        margin="0 auto",
        border_radius=RADIO_EXTRA_GRANDE,
    )


# ======================================================================
# Sección: Preguntas frecuentes
# ======================================================================


def _seccion_preguntas_frecuentes() -> rx.Component:
    """
    Sección completa con las FAQ de la carrera.

    Estilo Neon.com:
    - Sin contador en caja.
    - Con encabezado limpio.
    - Separada de la sección anterior.
    """
    carrera = EstadoInstitucional.carrera_seleccionada

    return rx.vstack(
        # ─── Encabezado ────────────────────────────────────────
        rx.vstack(
            rx.text(
                "PREGUNTAS FRECUENTES",
                font_size="0.6875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.15em",
                text_transform="uppercase",
            ),
            rx.heading(
                "Dudas sobre esta carrera",
                as_="h2",
                font_size=["1.5rem", "1.75rem", "2rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.02em",
                line_height="1.2",
                margin_top="0.5rem",
            ),
            rx.text(
                "Respuestas a las dudas más comunes de esta carrera. "
                "Si no encuentras la tuya, contáctanos.",
                font_size="0.9375rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                max_width="48rem",
                margin_top="0.75rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            margin_bottom="3rem",
        ),
        # ─── Acordeón ───────────────────────────────────────────
        acordeon_faq(
            items=carrera["preguntas_frecuentes"],
            variante="light",
            icono="circle-help",
            color_acento=AZUL_MARINO_NEON,
            tamano_texto_pregunta="0.9375rem",
            tamano_texto_respuesta="0.875rem",
            padding_cabecera="1.125rem 1.25rem",
            padding_respuesta="0 1.25rem 1.25rem 3.5rem",
            max_width=ANCHO_SECCION,
        ),
        spacing="0",
        width="100%",
        align="start",
    )


# ======================================================================
# Tabs completas (con etiquetas descriptivas)
# ======================================================================


def _pestanas_secciones_detalle() -> rx.Component:
    """
    Sistema de pestañas con etiquetas DESCRIPTIVAS (UX).

    Estilo Neon.com:
    - Sin fondo de card.
    - Solo border_bottom en el list.
    - Indicador activo con color azul marino.

    UX:
    - Las etiquetas describen el contenido real (no genéricas).
    - En desktop: icono + texto. En móvil: solo texto.
    - Los tabs se generan desde `TABS_DETALLE` (fuente única).

    Returns:
        Sistema completo de tabs con sus contenidos.
    """
    return rx.tabs.root(
        rx.tabs.list(
            # Generamos los triggers desde la config
            *[
                _tab_trigger(
                    tab["etiqueta"],
                    tab["icono"],
                    tab["valor"],
                )
                for tab in TABS_DETALLE
            ],
            width="100%",
            gap="0.25rem",
            border_bottom=f"1px solid {BORDE_HOME_SUAVE}",
        ),
        # ─── Contenido de cada tab ──────────────────────────────
        rx.tabs.content(
            seccion_informacion(),
            margin_top="2rem",
            value="info",
        ),
        rx.tabs.content(
            seccion_plan_estudios(),
            margin_top="2rem",
            value="plan",
        ),
        rx.tabs.content(
            seccion_perfil_y_campo_laboral(),
            margin_top="2rem",
            value="perfil",
        ),
        default_value="info",
        width="100%",
    )


# ======================================================================
# Botón flotante "volver arriba"
# ======================================================================


def _boton_volver_arriba() -> rx.Component:
    """
    Botón flotante minimalista para volver al inicio de la página.

    Estilo Neon.com:
    - Sin glow.
    - Fondo azul marino sólido.
    - Solo visible en desktop (`md+`).
    """
    return rx.box(
        rx.icon(
            "arrow-up",
            size=18,
            color="white",
        ),
        position="fixed",
        bottom="2rem",
        right="2rem",
        height="2.75rem",
        width="2.75rem",
        border_radius=RADIO_PASTILLA,
        background=AZUL_MARINO_NEON,
        display=rx.breakpoints(
            initial="none",
            md="flex",
        ),
        align_items="center",
        justify_content="center",
        cursor="pointer",
        z_index="40",
        transition="all 0.2s",
        on_click=rx.call_script(
            "window.scrollTo({top: 0, behavior: 'smooth'})"
        ),
        _hover={
            "filter": "brightness(1.1)",
        },
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/carrera/[carrera_id]",
    title=f"Detalle de Carrera | {NOMBRE_INSTITUTO}",
    on_load=EstadoInstitucional.redirigir_si_carrera_invalida,
)
def vista_detalle_carrera() -> rx.Component:
    """
    Página de detalle de carrera — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">`  → barra de navegación.
    - `<main>`                  → contenido principal.
    - `<section>`               → cada sección temática.
    - `<footer role="contentinfo">` → pie de página.

    El `on_load` redirige a `/404?origen=carrera` si el `carrera_id`
    de la URL no existe o no es válido.
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
                # ─── Encabezado sticky con breadcrumb ───────────────
                _encabezado_fijo_detalle(),
                # ─── Hero con imagen banner ─────────────────────────
                rx.el.section(
                    rx.box(
                        _hero_carrera(),
                        padding=[
                            f"2rem {PADDING_LATERAL}",
                            f"3rem {PADDING_LATERAL}",
                            f"4rem {PADDING_LATERAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    aria_label="Información principal de la carrera",
                    id="hero-carrera",
                    scroll_margin_top="5rem",
                ),
                # ─── Marquee de iconos ──────────────────────────────
                rx.el.section(
                    _marquee_caracteristicas(),
                    width="100%",
                    padding_x=PADDING_LATERAL,
                    aria_label="Características de la carrera",
                    id="marquee-caracteristicas",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_CONTENIDO),
                # ─── Tabs (Sobre la carrera, Malla curricular, Perfil y salidas)
                rx.el.section(
                    rx.box(
                        _pestanas_secciones_detalle(),
                        padding=PADDING_INFERIOR_PESTANAS,
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        padding_top="4rem",
                        width="100%",
                    ),
                    width="100%",
                    aria_label="Información detallada de la carrera",
                    id="tabs-detalle",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_CONTENIDO),
                # ─── FAQ de la carrera ──────────────────────────────
                rx.el.section(
                    rx.box(
                        _seccion_preguntas_frecuentes(),
                        padding=f"6rem {PADDING_LATERAL}",
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        width="100%",
                    ),
                    width="100%",
                    aria_label="Preguntas frecuentes de la carrera",
                    id="faq-carrera",
                    scroll_margin_top="5rem",
                ),
                # ─── Botón flotante ────────────────────────────────
                _boton_volver_arriba(),
                width="100%",
                aria_label="Detalle de carrera",
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

__all__ = ["vista_detalle_carrera"]