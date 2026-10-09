

from __future__ import annotations

import reflex as rx

from ..componentes.base import (
    encabezado_seccion,
    separador_secciones,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    DIRECCION,
    FONDO_HOME,
    HORARIO_ATENCION,
    NOMBRE_INSTITUTO,
    RADIO_EXTRA_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TELEFONO_PRINCIPAL,
    TELEFONO_SECUNDARIO,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    UBICACION_FISICA,
    WHATSAPP_URL,
)

# Componente externo: sección de plataforma académica (tutorial)
from .tutorial_crear_cuenta import cuadro_de_tutorial


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "72rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"

# Coordenadas del instituto
LATITUD: float = -16.5084167
LONGITUD: float = -68.1635278
COORDENADAS_TEXTO: str = '16°30\'30.3"S 68°09\'48.7"W'

# Colores semánticos mínimos
COLOR_VERDE_ACTIVO: str = "#22c55e"


# ======================================================================
# Sección: Hero
# ======================================================================


def _hero_contacto() -> rx.Component:
    """
    Hero de contacto alineado a la izquierda.

    Estilo Neon.com:
    - Badge con punto verde pulsante.
    - Título grande con énfasis bicolor.
    - Subtítulo descriptivo.
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ─────────────────────────────────────────
            rx.flex(
                rx.box(
                    width="0.5rem",
                    height="0.5rem",
                    border_radius=RADIO_PASTILLA,
                    background=COLOR_VERDE_ACTIVO,
                    animation="pulse 2s ease-in-out infinite",
                    flex_shrink="0",
                ),
                rx.text(
                    "MANTENTE EN CONTACTO",
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
                rx.text.span("Comunícate "),
                rx.text.span(
                    "con nosotros",
                    color=AZUL_MARINO_NEON,
                ),
                as_="h1",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                max_width="48rem",
            ),
            # ─── Subtítulo ─────────────────────────────────────
            rx.text(
                "Estamos disponibles para resolver tus dudas sobre "
                "admisiones, carreras, horarios y toda la "
                "información institucional.",
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
# Tarjeta base de contacto
# ======================================================================


def _tarjeta_contacto(
    icono: str,
    etiqueta: str,
    valor_principal: str,
    valor_secundario: str | None = None,
    acciones: rx.Component | None = None,
    con_indicador: bool = False,
    texto_indicador: str | None = None,
) -> rx.Component:
    """
    Tarjeta genérica de contacto.

    Estilo Neon.com:
    - Fondo plano (`COLOR_FONDO_CARTA`).
    - Borde sutil.
    - Icono directo (sin caja).
    - Hover: solo cambia el borde a azul marino.

    Args:
        icono: Nombre del icono Lucide.
        etiqueta: Texto pequeño en mayúsculas.
        valor_principal: Valor grande (ej: teléfono, dirección).
        valor_secundario: Valor pequeño opcional.
        acciones: Componente de acciones opcional (botones).
        con_indicador: Si `True`, muestra un punto verde pulsante.
        texto_indicador: Texto del indicador (si `con_indicador=True`).
    """
    hijos: list[rx.Component] = [
        # ─── Icono ─────────────────────────────────────────────
        rx.icon(
            icono,
            size=20,
            color=AZUL_MARINO_NEON,
        ),
        # ─── Etiqueta ──────────────────────────────────────────
        rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=TEXTO_HOME_MAS_SUAVE,
            text_transform="uppercase",
            letter_spacing="0.15em",
            margin_top="0.75rem",
        ),
        # ─── Valor principal ───────────────────────────────────
        rx.text(
            valor_principal,
            font_size="1.125rem",
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.3",
            margin_top="0.5rem",
        ),
    ]

    # ─── Valor secundario opcional ─────────────────────────────
    if valor_secundario is not None:
        hijos.append(
            rx.text(
                valor_secundario,
                font_size="0.8125rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.5",
                margin_top="0.375rem",
            )
        )

    # ─── Indicador opcional ────────────────────────────────────
    if con_indicador and texto_indicador:
        hijos.append(
            rx.flex(
                rx.box(
                    width="0.5rem",
                    height="0.5rem",
                    border_radius=RADIO_PASTILLA,
                    background=COLOR_VERDE_ACTIVO,
                    animation="pulse 2s ease-in-out infinite",
                    flex_shrink="0",
                ),
                rx.text(
                    texto_indicador,
                    font_size="0.75rem",
                    font_weight="600",
                    color=COLOR_VERDE_ACTIVO,
                ),
                align="center",
                gap="0.5rem",
                margin_top="1rem",
                width="fit-content",
            )
        )

    # ─── Acciones opcionales ───────────────────────────────────
    if acciones is not None:
        hijos.append(
            rx.box(
                acciones,
                margin_top="1.5rem",
                width="100%",
            )
        )

    return rx.box(
        rx.vstack(
            *hijos,
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="2rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


# ======================================================================
# Botones de acción
# ======================================================================


def _boton_accion(
    icono: str,
    etiqueta: str,
    href: str,
    externo: bool = False,
    primario: bool = True,
) -> rx.Component:
    """
    Botón de acción con icono + etiqueta.

    Args:
        icono: Nombre del icono Lucide.
        etiqueta: Texto visible.
        href: URL destino.
        externo: Si `True`, abre en nueva pestaña.
        primario: Si `True`, fondo azul marino; si `False`, outline.
    """
    if primario:
        estilos = {
            "background": AZUL_MARINO_NEON,
            "color": "white",
            "border": "none",
        }
    else:
        estilos = {
            "background": "transparent",
            "color": TEXTO_HOME_PRINCIPAL,
            "border": f"1px solid {BORDE_HOME_MEDIO}",
        }

    return rx.link(
        rx.icon(icono, size=16, color=estilos["color"]),
        rx.text(
            etiqueta,
            font_size="0.8125rem",
            font_weight="600",
            color=estilos["color"],
            white_space="nowrap",
        ),
        href=href,
        is_external=externo,
        display="inline-flex",
        align_items="center",
        justify_content="center",
        gap="0.5rem",
        padding="0.625rem 1rem",
        border_radius=RADIO_MEDIO,
        text_decoration="none",
        transition="all 0.2s",
        flex="1",
        **estilos,
        _hover={
            "filter": "brightness(1.1)",
            "border_color": BORDE_HOME_AZUL,
        },
    )


# ======================================================================
# Tarjetas específicas
# ======================================================================


def _tarjeta_contacto_telefono() -> rx.Component:
    """Tarjeta con teléfonos y botones de acción."""
    return _tarjeta_contacto(
        icono="phone",
        etiqueta="Atención al cliente",
        valor_principal=TELEFONO_PRINCIPAL,
        valor_secundario=f"Alterno: {TELEFONO_SECUNDARIO}",
        acciones=rx.flex(
            _boton_accion(
                icono="message-circle",
                etiqueta="WhatsApp",
                href=WHATSAPP_URL,
                externo=True,
                primario=True,
            ),
            _boton_accion(
                icono="phone",
                etiqueta="Llamar",
                href=f"tel:+591{TELEFONO_PRINCIPAL}",
                externo=True,
                primario=False,
            ),
            gap="0.5rem",
            width="100%",
            direction=rx.breakpoints(
                initial="column",
                sm="row",
            ),
        ),
    )


def _tarjeta_contacto_direccion() -> rx.Component:
    """Tarjeta con la dirección física."""
    return _tarjeta_contacto(
        icono="map-pin",
        etiqueta="Dirección",
        valor_principal=DIRECCION,
        valor_secundario=UBICACION_FISICA,
    )


def _tarjeta_contacto_horario() -> rx.Component:
    """Tarjeta con el horario de atención."""
    return _tarjeta_contacto(
        icono="clock",
        etiqueta="Horario de atención",
        valor_principal=HORARIO_ATENCION,
        con_indicador=True,
        texto_indicador="Atención presencial y telefónica",
    )


# ======================================================================
# Grid de tarjetas de contacto
# ======================================================================


def _grid_tarjetas_contacto() -> rx.Component:
    """Grid responsive con las 3 tarjetas de contacto."""
    return rx.grid(
        _tarjeta_contacto_telefono(),
        _tarjeta_contacto_direccion(),
        _tarjeta_contacto_horario(),
        columns=rx.breakpoints(
            initial="1",
            sm="1",
            md="2",
            lg="3",
        ),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección: Ubicación (mapa)
# ======================================================================


def _item_ubicacion(
    icono: str,
    etiqueta: str,
    valor: str,
) -> rx.Component:
    """Item de ubicación (dirección, referencia, coordenadas)."""
    return rx.flex(
        rx.icon(
            icono,
            size=16,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(
                etiqueta,
                font_size="0.6875rem",
                font_weight="700",
                color=TEXTO_HOME_MAS_SUAVE,
                text_transform="uppercase",
                letter_spacing="0.1em",
                line_height="1.2",
            ),
            rx.text(
                valor,
                font_size="0.875rem",
                font_weight="600",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.4",
            ),
            spacing="1",
            align="start",
            flex="1",
            min_width="0",
        ),
        align="start",
        gap="0.75rem",
        flex="1",
        min_width=["100%", "220px"],
        padding="1rem",
        border_radius=RADIO_MEDIO,
        background=COLOR_FONDO_SUAVE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
    )


def _bloque_mapa() -> rx.Component:
    """
    Bloque con Google Maps embebido + datos de ubicación + CTA.
    """
    url_mapa = (
        f"https://www.google.com/maps"
        f"?q={LATITUD},{LONGITUD}"
        f"&hl=es"
        f"&z=17"
        f"&output=embed"
    )

    url_como_llegar = (
        f"https://www.google.com/maps/dir/?api=1"
        f"&destination={LATITUD},{LONGITUD}"
    )

    return rx.vstack(
        # ─── Mapa ──────────────────────────────────────────────
        rx.box(
            rx.el.iframe(
                src=url_mapa,
                width="100%",
                height="100%",
                style={"border": "0"},
                loading="lazy",
                referrer_policy="no-referrer-when-downgrade",
                allow_fullscreen=True,
                title="Ubicación de INSTEIN en Google Maps",
            ),
            width="100%",
            height=["18rem", "22rem", "26rem"],
            border_radius=RADIO_EXTRA_GRANDE,
            overflow="hidden",
            border=f"1px solid {COLOR_BORDE_SUAVE}",
        ),
        # ─── Datos de ubicación ─────────────────────────────────
        rx.flex(
            _item_ubicacion(
                icono="map-pin",
                etiqueta="Dirección",
                valor=DIRECCION,
            ),
            _item_ubicacion(
                icono="building-2",
                etiqueta="Referencia",
                valor=UBICACION_FISICA,
            ),
            _item_ubicacion(
                icono="compass",
                etiqueta="Coordenadas",
                valor=COORDENADAS_TEXTO,
            ),
            gap="1rem",
            width="100%",
            margin_top="1.5rem",
            flex_wrap="wrap",
        ),
        # ─── CTA "Cómo llegar" ──────────────────────────────────
        rx.link(
            rx.text(
                "Cómo llegar",
                font_size="0.9375rem",
                font_weight="600",
                color="white",
            ),
            rx.icon("navigation", size=16, color="white"),
            href=url_como_llegar,
            is_external=True,
            text_decoration="none",
            display="inline-flex",
            align_items="center",
            gap="0.5rem",
            padding="0.875rem 1.5rem",
            border_radius=RADIO_PASTILLA,
            background=AZUL_MARINO_NEON,
            transition="all 0.2s",
            margin_top="1.5rem",
            width="fit-content",
            _hover={"filter": "brightness(1.1)"},
        ),
        spacing="0",
        width="100%",
        align="start",
    )


# ======================================================================
# Sección: Plataforma académica (tutorial)
# ======================================================================


def _bloque_tutorial() -> rx.Component:
    """
    Bloque que envuelve el tutorial de creación de cuenta.

    Añade un encabezado de sección + el componente `cuadro_de_tutorial`.
    """
    return rx.box(
        cuadro_de_tutorial(),
        width="100%",
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final() -> rx.Component:
    """
    CTA final: "¿Listo para inscribirte?".
    """
    return rx.flex(
        rx.text(
            "¿Listo para inscribirte?",
            font_size="1rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.link(
            rx.text(
                "Ver guía de admisión",
                font_size="1rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
            ),
            rx.icon(
                "arrow-right",
                size=16,
                color=AZUL_MARINO_NEON,
            ),
            href="/admision",
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
    route="/contacto",
    title=f"Contacto | {NOMBRE_INSTITUTO}",
    description=(
        "Contacta al Instituto Técnico Integrado San Antonio de "
        "Padua (INSTEIN): teléfonos, WhatsApp, dirección y ubicación."
    ),
)
def vista_contacto() -> rx.Component:
    """
    Página de contacto — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">`  → barra de navegación.
    - `<main>`                  → contenido principal.
    - `<section>`               → cada sección temática.
    - `<footer role="contentinfo">` → pie de página.
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
                _hero_contacto(),
                # ─── Sección 01 — Información de contacto ───────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Información de contacto",
                            titulo="Cómo comunicarte",
                            titulo_enfasis="con nosotros",
                            subtitulo=(
                                "Elige el canal que prefieras: "
                                "teléfono, WhatsApp o visita nuestro "
                                "campus."
                            ),
                        ),
                        _grid_tarjetas_contacto(),
                        max_width=ANCHO_MAXIMO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="info-contacto",
                    aria_label="Información de contacto",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── Sección 02 — Ubicación ─────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="02",
                            etiqueta="Ubicación",
                            titulo="Encuéntranos",
                            titulo_enfasis="en el mapa",
                            subtitulo=(
                                "Estamos en una ubicación céntrica y "
                                "de fácil acceso."
                            ),
                        ),
                        _bloque_mapa(),
                        max_width=ANCHO_MAXIMO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="ubicacion",
                    aria_label="Ubicación en el mapa",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO_CONTENIDO),
                # ─── Sección 03 — Plataforma académica ──────────────
                rx.el.section(
                    rx.box(
                        _bloque_tutorial(),
                        max_width=ANCHO_MAXIMO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="plataforma",
                    aria_label="Plataforma académica",
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
                aria_label="Contacto",
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

__all__ = ["vista_contacto"]