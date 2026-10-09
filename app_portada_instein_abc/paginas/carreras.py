

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    encabezado_seccion,
    estado_vacio,
    separador_secciones,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..dominio import (
    Carrera,
    EstadoInstitucional,
)
from ..infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ─── Colores del badge de demanda laboral ─────────────────────────
# Solo 3 colores, porque comunica un estado semántico real.
DEMANDA_ALTA_TEXTO = rx.color("green", 11)
DEMANDA_ALTA_FONDO = rx.color("green", 3)
DEMANDA_ALTA_BORDE = rx.color("green", 7)

DEMANDA_MEDIA_TEXTO = rx.color("amber", 11)
DEMANDA_MEDIA_FONDO = rx.color("amber", 3)
DEMANDA_MEDIA_BORDE = rx.color("amber", 7)

DEMANDA_BAJA_TEXTO = rx.color("gray", 11)
DEMANDA_BAJA_FONDO = rx.color("gray", 3)
DEMANDA_BAJA_BORDE = rx.color("gray", 7)


# ======================================================================
# Helpers
# ======================================================================


def _icono_por_filtro(filtro: str) -> str:
    """Icono Lucide correspondiente a cada filtro."""
    iconos = {
        "demanda_alta": "trending-up",
        "puntuacion_top": "star",
        "todos": "list",
    }
    return iconos.get(filtro, "filter")


# ======================================================================
# Hero
# ======================================================================


def _hero_carreras() -> rx.Component:
    """
    Hero de la página de carreras — estilo Neon.com.

    Estructura:
    - Badge "OFERTA ACADÉMICA".
    - Título grande con énfasis bicolor.
    - Subtítulo.
    - Alineado a la izquierda.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ─────────────────────────────────────────
            rx.flex(
                rx.icon("graduation-cap", size=12, color=AZUL_MARINO_NEON),
                rx.text(
                    "OFERTA ACADÉMICA",
                    font_size="0.6875rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    letter_spacing="0.15em",
                    text_transform="uppercase",
                ),
                align="center",
                gap="0.5rem",
                margin_bottom="1.5rem",
            ),
            # ─── Título con énfasis bicolor ────────────────────
            rx.heading(
                rx.text.span("Nuestras "),
                rx.text.span(
                    "5 carreras",
                    color=AZUL_MARINO_NEON,
                ),
                rx.text.span(" técnicas"),
                as_="h1",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                max_width="56rem",
            ),
            # ─── Subtítulo ─────────────────────────────────────
            rx.text(
                "Todas nuestras carreras duran 3 años (6 semestres) y "
                "otorgan el título de Técnico Superior en Provisión "
                "Nacional. Filtra y ordena según tus prioridades.",
                font_size=["1rem", "1.125rem"],
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                max_width="48rem",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO_CONTENIDO,
        margin="0 auto",
        padding=[
            f"4rem {PADDING_SECCION_HORIZONTAL} 2rem {PADDING_SECCION_HORIZONTAL}",
            f"6rem {PADDING_SECCION_HORIZONTAL} 3rem {PADDING_SECCION_HORIZONTAL}",
        ],
        width="100%",
    )


# ======================================================================
# Filtros tipo pill (depurados)
# ======================================================================


def _filtro_pill(
    etiqueta: str,
    valor: str,
) -> rx.Component:
    """
    Pill de filtro con estado activo.

    Estilo Neon.com:
    - Activo: fondo azul marino + texto blanco.
    - Inactivo: fondo plano + borde sutil.
    - Sin glow.
    """
    activo = EstadoInstitucional.filtro_activo == valor

    return rx.box(
        rx.flex(
            rx.icon(
                _icono_por_filtro(valor),
                size=14,
                color=rx.cond(
                    activo,
                    "white",
                    AZUL_MARINO_NEON,
                ),
            ),
            rx.text(
                etiqueta,
                font_size="0.8125rem",
                font_weight="600",
                color=rx.cond(
                    activo,
                    "white",
                    TEXTO_HOME_PRINCIPAL,
                ),
                white_space="nowrap",
            ),
            align="center",
            gap="0.375rem",
        ),
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            activo,
            AZUL_MARINO_NEON,
            "transparent",
        ),
        border=rx.cond(
            activo,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {BORDE_HOME_MEDIO}",
        ),
        cursor="pointer",
        transition="all 0.2s",
        on_click=EstadoInstitucional.cambiar_filtro(valor),
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _orden_pill(
    etiqueta: str,
    valor: str,
) -> rx.Component:
    """Pill de ordenamiento con estado activo."""
    activo = EstadoInstitucional.orden_activo == valor

    return rx.box(
        rx.text(
            etiqueta,
            font_size="0.75rem",
            font_weight="600",
            color=rx.cond(
                activo,
                "white",
                TEXTO_HOME_PRINCIPAL,
            ),
            white_space="nowrap",
        ),
        padding="0.375rem 0.75rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            activo,
            AZUL_MARINO_NEON,
            "transparent",
        ),
        border=rx.cond(
            activo,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {BORDE_HOME_MEDIO}",
        ),
        cursor="pointer",
        transition="all 0.2s",
        on_click=EstadoInstitucional.cambiar_orden(valor),
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _etiqueta_grupo(texto: str) -> rx.Component:
    """Etiqueta en mayúsculas para encabezar un grupo de filtros."""
    return rx.text(
        texto,
        font_size="0.6875rem",
        font_weight="700",
        color=TEXTO_HOME_MAS_SUAVE,
        text_transform="uppercase",
        letter_spacing="0.15em",
        margin_bottom="0.75rem",
    )


def _barra_filtros() -> rx.Component:
    """
    Barra con filtros + ordenamientos (depurada).

    Solo filtros y órdenes que aportan al proceso de decisión:
    - Filtros: Todos, Alta demanda, Mejor puntuación.
    - Órdenes: Puntuación, Empleabilidad.
    """
    return rx.flex(
        # ─── Filtros ────────────────────────────────────────────
        rx.vstack(
            _etiqueta_grupo("Filtrar por"),
            rx.flex(
                _filtro_pill("Todos", "todos"),
                _filtro_pill("Alta demanda", "demanda_alta"),
                _filtro_pill("Mejor puntuación", "puntuacion_top"),
                gap="0.5rem",
                flex_wrap="wrap",
                width="100%",
            ),
            align="start",
            spacing="0",
            flex="1",
            min_width="0",
        ),
        # ─── Ordenamiento ───────────────────────────────────────
        rx.vstack(
            _etiqueta_grupo("Ordenar por"),
            rx.flex(
                _orden_pill("Puntuación", "puntuacion_desc"),
                _orden_pill("Empleabilidad", "empleabilidad_desc"),
                gap="0.5rem",
                flex_wrap="wrap",
                width="100%",
            ),
            align="start",
            spacing="0",
            flex="1",
            min_width="0",
        ),
        # ─── Layout responsive ─────────────────────────────────
        direction=rx.breakpoints(initial="column", md="row"),
        gap="2rem",
        width="100%",
        align="start",
        margin_bottom="3rem",
    )


# ======================================================================
# Stats de carrera
# ======================================================================


def _stat_item(
    icono: str,
    valor: str,
    etiqueta: str,
) -> rx.Component:
    """Item individual de estadística."""
    return rx.flex(
        rx.icon(icono, size=14, color=AZUL_MARINO_NEON),
        rx.text(
            valor,
            font_size="0.875rem",
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
        ),
        rx.text(
            etiqueta,
            font_size="0.75rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        align="center",
        gap="0.375rem",
    )


def _stats_carrera(carrera: Carrera) -> rx.Component:
    """Stats visibles de una carrera."""
    stats = carrera["estadisticas"]

    return rx.flex(
        _stat_item(
            icono="star",
            valor=f"{stats['puntuacion']}",
            etiqueta="puntuación",
        ),
        _stat_item(
            icono="briefcase",
            valor=f"{stats['tasa_empleabilidad']}%",
            etiqueta="empleabilidad",
        ),
        align="center",
        gap="1.5rem",
        width="100%",
        flex_wrap="wrap",
    )


# ======================================================================
# Badge de demanda laboral
# ======================================================================


def _badge_demanda(carrera: Carrera) -> rx.Component:
    """
    Badge de demanda laboral.

    Único badge que mantiene colores semánticos porque comunica un
    estado real (alta/media/baja).
    """
    demanda = carrera["estadisticas"]["demanda_laboral"]

    color_texto = rx.match(
        demanda,
        ("alta", DEMANDA_ALTA_TEXTO),
        ("media", DEMANDA_MEDIA_TEXTO),
        DEMANDA_BAJA_TEXTO,
    )
    color_fondo = rx.match(
        demanda,
        ("alta", DEMANDA_ALTA_FONDO),
        ("media", DEMANDA_MEDIA_FONDO),
        DEMANDA_BAJA_FONDO,
    )
    color_borde = rx.match(
        demanda,
        ("alta", DEMANDA_ALTA_BORDE),
        ("media", DEMANDA_MEDIA_BORDE),
        DEMANDA_BAJA_BORDE,
    )

    return rx.flex(
        rx.icon("trending-up", size=12, color=color_texto),
        rx.text(
            f"Demanda {demanda}",
            font_size="0.6875rem",
            font_weight="700",
            color=color_texto,
            text_transform="capitalize",
            white_space="nowrap",
        ),
        align="center",
        gap="0.375rem",
        padding="0.25rem 0.625rem",
        border_radius=RADIO_PASTILLA,
        background=color_fondo,
        border=f"1px solid {color_borde}",
        width="fit-content",
    )


# ======================================================================
# Card de carrera con imagen banner
# ======================================================================


def _card_carrera(
    carrera: Carrera,
    indice: int,
) -> rx.Component:
    """
    Card de carrera con imagen banner como fondo.

    Estructura:
    ┌────────────────────────────────────┐
    │  [badge demanda]                    │  ← arriba derecha
    │                                     │
    │        [imagen_banner]              │  ← fondo (con zoom en hover)
    │        [gradiente oscuro]           │
    │                                     │
    │  🖥️  Sistemas Informáticos          │  ← abajo, sobre el gradiente
    │      Lema corto...                  │
    │  ⭐ 4.8  💼 95%                     │
    │  Ver detalle →                      │
    └────────────────────────────────────┘

    Estilo Neon.com:
    - Imagen de fondo con `object_fit="cover"`.
    - Gradiente lineal oscuro para legibilidad.
    - Hover: zoom de la imagen + borde de acento.
    - Sin glow.

    Args:
        carrera: `Carrera` con los datos completos.
        indice: Índice en el `rx.foreach` (no usado, requerido por Reflex).

    Returns:
        Card clicable (enlace a `/carrera/{id}`).
    """
    return rx.link(
        rx.box(
            # ═════════════════════════════════════════════════════
            # Capa 1: Imagen banner
            # ═════════════════════════════════════════════════════
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
                transition="transform 0.5s ease",
                class_name="card-carrera-imagen",
            ),
            # ═════════════════════════════════════════════════════
            # Capa 2: Gradiente oscuro
            # ═════════════════════════════════════════════════════
            rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background=(
                    "linear-gradient(180deg, "
                    "rgba(0, 0, 0, 0.0) 0%, "
                    "rgba(0, 0, 0, 0.15) 35%, "
                    "rgba(0, 0, 0, 0.65) 70%, "
                    "rgba(0, 0, 0, 0.9) 100%)"
                ),
                z_index="1",
            ),
            # ═════════════════════════════════════════════════════
            # Capa 3: Contenido
            # ═════════════════════════════════════════════════════
            rx.vstack(
                # ─── Badge de demanda (arriba) ──────────────────
                rx.flex(
                    _badge_demanda(carrera),
                    width="100%",
                    justify="end",
                ),
                # ─── Espacio flexible ───────────────────────────
                rx.spacer(),
                # ─── Icono + Nombre + Lema ──────────────────────
                rx.vstack(
                    # Icono + Nombre
                    rx.flex(
                        rx.icon(
                            carrera["icono"],
                            size=20,
                            color="white",
                            flex_shrink="0",
                        ),
                        rx.text(
                            carrera["nombre_corto"],
                            font_size="1.25rem",
                            font_weight="800",
                            color="white",
                            line_height="1.2",
                            letter_spacing="-0.02em",
                            text_shadow="0 2px 8px rgba(0, 0, 0, 0.6)",
                        ),
                        align="center",
                        gap="0.625rem",
                    ),
                    # Lema
                    rx.text(
                        carrera["lema"],
                        font_size="0.875rem",
                        color="rgba(255, 255, 255, 0.85)",
                        line_height="1.5",
                        text_shadow="0 1px 4px rgba(0, 0, 0, 0.5)",
                        max_width="28rem",
                    ),
                    align="start",
                    spacing="1",
                    width="100%",
                ),
                # ─── Stats + CTA (abajo) ────────────────────────
                rx.vstack(
                    # Stats (sobre el gradiente oscuro)
                    rx.flex(
                        rx.flex(
                            rx.icon(
                                "star",
                                size=14,
                                color="white",
                            ),
                            rx.text(
                                f"{carrera['estadisticas']['puntuacion']}",
                                font_size="0.875rem",
                                font_weight="700",
                                color="white",
                            ),
                            rx.text(
                                "puntuación",
                                font_size="0.75rem",
                                color="rgba(255, 255, 255, 0.7)",
                            ),
                            align="center",
                            gap="0.375rem",
                        ),
                        rx.flex(
                            rx.icon(
                                "briefcase",
                                size=14,
                                color="white",
                            ),
                            rx.text(
                                f"{carrera['estadisticas']['tasa_empleabilidad']}%",
                                font_size="0.875rem",
                                font_weight="700",
                                color="white",
                            ),
                            rx.text(
                                "empleabilidad",
                                font_size="0.75rem",
                                color="rgba(255, 255, 255, 0.7)",
                            ),
                            align="center",
                            gap="0.375rem",
                        ),
                        align="center",
                        gap="1.25rem",
                        flex_wrap="wrap",
                        width="100%",
                        margin_top="0.75rem",
                    ),
                    # CTA "Ver detalle →"
                    rx.flex(
                        rx.text(
                            "Ver detalle",
                            font_size="0.875rem",
                            font_weight="600",
                            color="white",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=14,
                            color="white",
                        ),
                        align="center",
                        gap="0.375rem",
                        margin_top="1rem",
                        transition="gap 0.2s",
                    ),
                    align="start",
                    spacing="0",
                    width="100%",
                ),
                align="start",
                justify="between",
                width="100%",
                height="100%",
                padding="1.75rem",
                position="relative",
                z_index="2",
            ),
            # ═════════════════════════════════════════════════════
            # Estilos base de la card
            # ═════════════════════════════════════════════════════
            position="relative",
            width="100%",
            min_height="26rem",
            border_radius=RADIO_EXTRA_GRANDE,
            overflow="hidden",
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            transition="all 0.3s ease",
            cursor="pointer",
            height="100%",
            display="flex",
            flex_direction="column",
            _hover={
                "border_color": AZUL_MARINO_NEON,
                "& .card-carrera-imagen": {
                    "transform": "scale(1.06)",
                },
                "& .card-carrera-cta": {
                    "gap": "0.625rem",
                },
            },
        ),
        href=f"/carrera/{carrera['id']}",
        text_decoration="none",
        width="100%",
        height="100%",
        display="block",
    )


# ======================================================================
# Grid de carreras
# ======================================================================


def _grid_carreras() -> rx.Component:
    """
    Grid de carreras con altura uniforme.

    Layout:
    - Mobile: 1 columna.
    - Tablet: 1 columna (cards grandes y visuales).
    - Desktop: 2 columnas.
    """
    return rx.grid(
        rx.foreach(
            EstadoInstitucional.carreras_filtradas_y_ordenadas,
            _card_carrera,
        ),
        columns=rx.breakpoints(initial="1", lg="2"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Contador de resultados
# ======================================================================


def _contador_resultados() -> rx.Component:
    """Contador de resultados del filtro actual."""
    return rx.flex(
        rx.text(
            "Resultados:",
            font_size="0.875rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.text(
            EstadoInstitucional.carreras_filtradas_y_ordenadas
            .length()
            .to_string(),
            font_size="0.875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            padding="0.125rem 0.5rem",
            border_radius=RADIO_PASTILLA,
            background=FONDO_AZUL_SUAVE,
            border=f"1px solid {BORDE_HOME_AZUL}",
        ),
        rx.text(
            "carreras",
            font_size="0.875rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        align="center",
        gap="0.375rem",
        margin_bottom="1.5rem",
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final() -> rx.Component:
    """CTA final hacia /contacto."""
    return rx.flex(
        rx.text(
            "¿No encuentras la carrera ideal?",
            font_size="1rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.link(
            rx.text(
                "Contáctanos",
                font_size="1rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
            ),
            rx.icon("arrow-right", size=16, color=AZUL_MARINO_NEON),
            href="/contacto",
            text_decoration="none",
            display="inline-flex",
            align_items="center",
            gap="0.375rem",
            transition="gap 0.2s",
            _hover={"gap": "0.625rem"},
        ),
        align="center",
        justify="start",
        gap="0.5rem",
        flex_wrap="wrap",
        width="100%",
        padding_top="3rem",
        margin_top="2rem",
        border_top=f"1px solid {COLOR_DIVISOR}",
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/carreras",
    title=f"Carreras | {NOMBRE_INSTITUTO}",
    description=(
        "Explora las 5 carreras técnicas del Instituto Técnico "
        "Integrado San Antonio de Padua (INSTEIN): Sistemas, "
        "Contaduría, Secretariado, Comercio y Electrónica."
    ),
)
def vista_carreras() -> rx.Component:
    """
    Página con la oferta académica completa — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header>`  → barra de navegación.
    - `<main>`    → contenido principal.
    - `<section>` → catálogo con filtros.
    - `<footer>`  → pie de página.
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
                _hero_carreras(),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(),
                # ─── Sección 01 — Catálogo + Filtros ────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Catálogo académico",
                            titulo="Explora",
                            titulo_enfasis="nuestras carreras",
                            subtitulo=(
                                "Filtra y ordena según tus prioridades: "
                                "demanda laboral, puntuación y "
                                "empleabilidad."
                            ),
                        ),
                        _barra_filtros(),
                        _contador_resultados(),
                        rx.cond(
                            EstadoInstitucional.carreras_filtradas_y_ordenadas
                            .length()
                            > 0,
                            _grid_carreras(),
                            estado_vacio(
                                titulo="No se encontraron carreras",
                                mensaje=(
                                    "Prueba ajustando los filtros o "
                                    "limpiando la selección actual."
                                ),
                                icono="search-x",
                                tamano_icono=48,
                                boton_accion_etiqueta="Limpiar filtros",
                                boton_accion_icono="rotate-ccw",
                                boton_accion_on_click=(
                                    EstadoInstitucional.cambiar_filtro(
                                        "todos"
                                    )
                                ),
                                boton_accion_color_scheme="crimson",
                            ),
                        ),
                        max_width=ANCHO_MAXIMO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="catalogo",
                    aria_label="Catálogo de carreras",
                ),
                # ─── CTA final ──────────────────────────────────────
                rx.box(
                    _cta_final(),
                    max_width=ANCHO_MAXIMO_CONTENIDO,
                    margin="0 auto",
                    padding_x=PADDING_SECCION_HORIZONTAL,
                    padding_bottom="6rem",
                    width="100%",
                ),
                width="100%",
                aria_label="Carreras técnicas",
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

__all__ = ["vista_carreras"]