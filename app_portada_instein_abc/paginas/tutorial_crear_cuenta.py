"""
Sección: Plataforma de seguimiento académico (con tutoriales).

Contenido
---------
- Título + descripción de la plataforma.
- Segmented control para cambiar entre:
  - "Crear cuenta" (video tutorial).
  - "Inicio de sesión" (video tutorial).
- Video tutorial vertical 9:16 según la opción activa.
- CTA para crear cuenta institucional.

Diseño
------
Refactorizado al estilo Neon.com:

1. **Layout 2 columnas**: título + CTA (izq), video (der).
2. **Segmented control con iconos** (más intuitivo).
3. **Título dinámico** según la opción seleccionada.
4. **Card limpia**: sin banner redundante, sin badge genérico.
5. **Responsive mobile-first**.
6. **Dark mode adaptativo**.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: TIPO DEL EVENTO `on_change`
------------------------------------------
`rx.segmented_control.root` envía el valor como `str | list[str]`
(según la versión de Radix Themes).

⚠️ Si el handler recibe solo `str`, Reflex lanza:

    EventHandlerArgTypeMismatchError: Event handler on_change
    expects str | list[str] for argument valor but got <class 'str'>
    as annotated in EstadoTutorial.seleccionar_video instead.

**Solución**: anotar el parámetro como `str | list[str]` y
normalizar el valor dentro del handler.

Nota técnica: UBICACIÓN DEL ARCHIVO
-----------------------------------
Este archivo vive en `paginas/`, no en `componentes/`. Por eso
los imports relativos usan `..` (2 puntos) en lugar de `...`.

⚠️ Usar `...` desde `paginas/` causa:
    ImportError: attempted relative import beyond top-level package
"""

from __future__ import annotations

import reflex as rx

# ✅ CORREGIDO: 2 puntos (no 3) porque estamos en `paginas/`
from ..infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_SUAVE,
    COLOR_DIVISOR,
    FONDO_HOME_CARD,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)
from ..infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

# Ancho del video en cada breakpoint
ANCHO_VIDEO_RESPONSIVE: list[str] = [
    "100%",   # initial
    "280px",  # sm
    "320px",  # md
    "360px",  # lg
]

# Opciones del segmented control
OPCIONES_VIDEO: list[dict] = [
    {
        "valor": "crear_cuenta",
        "etiqueta": "Crear cuenta",
        "icono": "user-plus",
    },
    {
        "valor": "iniciar_sesion",
        "etiqueta": "Inicio de sesión",
        "icono": "log-in",
    },
]

# Rutas de los videos
VIDEO_CREAR_CUENTA: str = "/tutorial.mp4"
VIDEO_INICIAR_SESION: str = "/video1.mp4"


# ======================================================================
# State
# ======================================================================


class EstadoTutorial(rx.State):
    """
    Estado del tutorial de la plataforma académica.

    Atributos:
        opcion_activa: Clave del video activo (`"crear_cuenta"` o
            `"iniciar_sesion"`).
    """

    opcion_activa: str = "crear_cuenta"

    @rx.event
    def seleccionar_video(self, valor: str | list[str]):
        """
        Cambia la opción de video activa.

        ⚠️ `rx.segmented_control.root` envía el valor como
        `str | list[str]`. Por eso el parámetro acepta ambos tipos
        y se normaliza a `str`.

        Args:
            valor: Clave de la opción (`"crear_cuenta"` o
                `"iniciar_sesion"`). Si llega como lista, se toma
                el primer elemento.
        """
        if isinstance(valor, list):
            self.opcion_activa = valor[0] if valor else "crear_cuenta"
        else:
            self.opcion_activa = valor


# ======================================================================
# Segmented control
# ======================================================================


def _segmented_control() -> rx.Component:
    """
    Segmented control para cambiar entre los 2 videos tutoriales.

    Estilo Neon.com:
    - Iconos descriptivos en cada opción.
    - Fondo plano.
    - Activo: fondo azul marino.

    Returns:
        Componente `rx.segmented_control.root`.
    """
    return rx.segmented_control.root(
        *[
            rx.segmented_control.item(
                rx.flex(
                    rx.icon(opcion["icono"], size=14),
                    rx.text(
                        opcion["etiqueta"],
                        font_size="0.8125rem",
                        font_weight="600",
                    ),
                    align="center",
                    gap="0.375rem",
                ),
                value=opcion["valor"],
            )
            for opcion in OPCIONES_VIDEO
        ],
        on_change=EstadoTutorial.seleccionar_video,
        value=EstadoTutorial.opcion_activa,
        size="2",
        variant="surface",
        radius="large",
        width="100%",
    )


# ======================================================================
# Video vertical 9:16
# ======================================================================


def _video_tutorial() -> rx.Component:
    """
    Video tutorial vertical (9:16) según la opción activa.

    Estilo:
    - Border radius grande.
    - Sombra sutil.
    - Fondo oscuro (para que se vea bien mientras carga).

    Returns:
        Componente `rx.box` con el video.
    """
    return rx.box(
        rx.cond(
            EstadoTutorial.opcion_activa == "crear_cuenta",
            rx.aspect_ratio(
                rx.video(
                    src=VIDEO_CREAR_CUENTA,
                    width="100%",
                    height="100%",
                    controls=True,
                    auto_play=False,
                    loop=False,
                    muted=False,
                    border_radius=RADIO_EXTRA_GRANDE,
                ),
                ratio=9 / 16,
            ),
            rx.aspect_ratio(
                rx.video(
                    src=VIDEO_INICIAR_SESION,
                    width="100%",
                    height="100%",
                    controls=True,
                    auto_play=False,
                    loop=False,
                    muted=False,
                    border_radius=RADIO_EXTRA_GRANDE,
                ),
                ratio=9 / 16,
            ),
        ),
        width=ANCHO_VIDEO_RESPONSIVE,
        max_width="100%",
        border_radius=RADIO_EXTRA_GRANDE,
        overflow="hidden",
        background="#0a0a0a",
        box_shadow=rx.color_mode_cond(
            light="0 8px 24px -8px rgba(0, 0, 0, 0.15)",
            dark="0 8px 24px -8px rgba(0, 0, 0, 0.5)",
        ),
        margin="0 auto",
    )


# ======================================================================
# Bloque de texto dinámico
# ======================================================================


def _titulo_dinamico() -> rx.Component:
    """
    Título + descripción según la opción activa.

    - "Crear cuenta"     → "Cómo crear tu cuenta institucional".
    - "Inicio de sesión" → "Cómo iniciar sesión en la plataforma".
    """
    return rx.cond(
        EstadoTutorial.opcion_activa == "crear_cuenta",
        rx.vstack(
            rx.text(
                "PASO 1 · CREAR CUENTA",
                font_size="0.6875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.15em",
                text_transform="uppercase",
            ),
            rx.heading(
                "Cómo crear tu cuenta institucional",
                as_="h3",
                font_size=["1.25rem", "1.5rem", "1.75rem"],
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.02em",
                line_height="1.2",
                margin_top="0.5rem",
            ),
            rx.text(
                "Regístrate con tu carnet de identidad y tu correo "
                "personal. Recibirás un correo de confirmación con "
                "tus credenciales de acceso.",
                font_size="0.9375rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.75rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        rx.vstack(
            rx.text(
                "PASO 2 · INICIAR SESIÓN",
                font_size="0.6875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                letter_spacing="0.15em",
                text_transform="uppercase",
            ),
            rx.heading(
                "Cómo iniciar sesión en la plataforma",
                as_="h3",
                font_size=["1.25rem", "1.5rem", "1.75rem"],
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.02em",
                line_height="1.2",
                margin_top="0.5rem",
            ),
            rx.text(
                "Ingresa con tu correo institucional y la contraseña "
                "que recibiste. Si olvidaste tu contraseña, usa la "
                "opción 'Recuperar acceso'.",
                font_size="0.9375rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.75rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
    )


# ======================================================================
# CTA
# ======================================================================


def _cta_crear_cuenta() -> rx.Component:
    """
    CTA para acceder a la plataforma institucional.

    Botón primario que enlaza a la sección de contacto (donde se
    solicitan las credenciales).
    """
    return rx.link(
        rx.text(
            "Solicitar credenciales",
            as_="span",
            font_size="0.9375rem",
            font_weight="600",
            color="white",
        ),
        rx.icon("arrow-right", size=16, color="white"),
        href="/contacto",
        text_decoration="none",
        display="inline-flex",
        align_items="center",
        gap="0.5rem",
        padding="0.875rem 1.5rem",
        border_radius=RADIO_PASTILLA,
        background=AZUL_MARINO_NEON,
        transition="all 0.2s",
        width="fit-content",
        margin_top="1.5rem",
        _hover={
            "transform": "translateY(-2px)",
            "filter": "brightness(1.1)",
        },
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_plataforma_academica() -> rx.Component:
    """
    Sección completa con:
    - Título de sección + descripción.
    - Segmented control para cambiar el video.
    - Título dinámico según el paso.
    - Video tutorial 9:16.
    - CTA para crear cuenta.

    Layout:
    - Móvil: 1 columna (título arriba, video abajo).
    - Desktop: 2 columnas (texto izq 55%, video der 45%).

    Estilo Neon.com:
    - Card con fondo adaptativo.
    - Borde sutil.
    - Padding generoso.
    """
    return rx.box(
        rx.vstack(
            # ==========================================================
            # Header de sección
            # ==========================================================
            rx.vstack(
                rx.text(
                    "PLATAFORMA OFICIAL",
                    font_size="0.75rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    letter_spacing="0.15em",
                    text_transform="uppercase",
                ),
                rx.heading(
                    "Seguimiento académico en línea",
                    as_="h2",
                    font_size=["1.75rem", "2rem", "2.25rem"],
                    font_weight="900",
                    color=TEXTO_HOME_PRINCIPAL,
                    letter_spacing="-0.03em",
                    line_height="1.15",
                    margin_top="0.5rem",
                ),
                rx.text(
                    "Accede a tu historial académico, calificaciones, "
                    "asistencia y materiales de estudio desde cualquier "
                    "dispositivo. Inicia sesión con tu cuenta institucional.",
                    font_size="1rem",
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
            # ==========================================================
            # Card del tutorial
            # ==========================================================
            rx.box(
                rx.vstack(
                    # ─── Segmented control ────────────────────────
                    _segmented_control(),
                    # ─── Separador ────────────────────────────────
                    rx.box(
                        height="1px",
                        width="100%",
                        background=COLOR_DIVISOR,
                        margin_y="2rem",
                    ),
                    # ─── Layout 2 columnas: texto + video ─────────
                    rx.flex(
                        # Columna izquierda: título dinámico + CTA
                        rx.box(
                            rx.vstack(
                                _titulo_dinamico(),
                                _cta_crear_cuenta(),
                                align="start",
                                spacing="0",
                                width="100%",
                            ),
                            width=rx.breakpoints(
                                initial="100%",
                                lg="55%",
                            ),
                            flex_shrink="0",
                        ),
                        # Columna derecha: video
                        rx.box(
                            _video_tutorial(),
                            width=rx.breakpoints(
                                initial="100%",
                                lg="45%",
                            ),
                            flex_shrink="0",
                            display="flex",
                            justify_content="center",
                        ),
                        # Layout responsive
                        direction=rx.breakpoints(
                            initial="column",
                            lg="row",
                        ),
                        align="start",
                        justify="between",
                        gap="3rem",
                        width="100%",
                    ),
                    spacing="0",
                    width="100%",
                ),
                padding=["1.5rem", "2rem", "2.5rem"],
                border_radius=RADIO_EXTRA_GRANDE,
                background=FONDO_HOME_CARD,
                border=f"1px solid {BORDE_HOME_SUAVE}",
                width="100%",
            ),
            spacing="0",
            width="100%",
            align="start",
        ),
        width="100%",
        max_width="72rem",
        margin="0 auto",
    )


# ======================================================================
# Aliases retrocompatibles
# ======================================================================

# El componente original era `cuadro_de_tutorial()`.
# Se mantiene como alias para no romper imports existentes en
# `paginas/contacto.py`.
cuadro_de_tutorial = seccion_plataforma_academica


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ANCHO_VIDEO_RESPONSIVE",
    "EstadoTutorial",
    "OPCIONES_VIDEO",
    "VIDEO_CREAR_CUENTA",
    "VIDEO_INICIAR_SESION",
    "cuadro_de_tutorial",
    "seccion_plataforma_academica",
]