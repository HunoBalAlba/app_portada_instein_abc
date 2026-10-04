"""
Sección "¿Por qué elegir INSTEIN?" — estilo Neon adaptativo.

Contenido
---------
- 6 tarjetas con razones clave.
- Cada tarjeta abre un diálogo con detalle ampliado.

Patrón de diálogo
-----------------
Se usa `rx.dialog.trigger` (patrón declarativo de Radix Themes) en
lugar de `on_click` manual. Cada card envuelve su propio
`rx.dialog.root` con su contenido específico.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.

- Fondo de card: `FONDO_HOME_CARD`.
- Acentos: `AZUL_MARINO_NEON` en ambos modos.
- Texto: `TEXTO_HOME_PRINCIPAL` / `TEXTO_HOME_SUAVE` / `TEXTO_HOME_MAS_SUAVE`.
- Bordes: `BORDE_HOME_AZUL` / `BORDE_HOME_MEDIO` / `BORDE_HOME_SUAVE`.

Nota técnica: FIX MÓVIL DEL DIÁLOGO
-----------------------------------
El diálogo aplica scroll interno en `flex: 1` + `min_height: 0`, marco
en `display: flex` + `flex-direction: column`, y altura máxima con
`dvh` para respetar la barra de URL móvil.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_HOME_CARD,
    SOMBRA_HOVER_CARD_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
)


# ======================================================================
# Tipos
# ======================================================================


class Razon(TypedDict):
    """Razón individual con detalle ampliado."""

    id: int
    icono: str
    titulo: str
    descripcion: str
    detalle: str
    puntos: list[str]


# ======================================================================
# Datos estáticos
# ======================================================================

RAZONES: list[Razon] = [
    {
        "id": 0,
        "icono": "award",
        "titulo": "Título de Provisión Nacional",
        "descripcion": (
            "Todos nuestros títulos están autorizados por el Ministerio de "
            "Educación con Resolución Ministerial R.M. 0871/2016."
        ),
        "detalle": (
            "Nuestros títulos tienen validez nacional y están respaldados "
            "por resoluciones ministeriales vigentes. Al egresar, recibirás "
            "un Técnico Superior en Provisión Nacional reconocido por "
            "empleadores de todo el país."
        ),
        "puntos": [
            "Resolución Ministerial R.M. 0871/2016",
            "Registro en el sistema educativo boliviano",
            "Reconocido por empresas públicas y privadas",
            "Válido para continuar estudios universitarios",
        ],
    },
    {
        "id": 1,
        "icono": "briefcase",
        "titulo": "Formación Práctica",
        "descripcion": (
            "Laboratorios equipados y docentes especializados con experiencia "
            "real en el campo profesional."
        ),
        "detalle": (
            "En INSTEIN no solo estudias teoría: practicas desde el primer "
            "año con equipamiento moderno y docentes que trabajan activamente "
            "en la industria. Nuestros laboratorios replican entornos reales "
            "de trabajo."
        ),
        "puntos": [
            "Laboratorios con equipamiento de última generación",
            "Docentes en activo en la industria",
            "Proyectos prácticos desde el primer semestre",
            "Prácticas profesionales garantizadas",
        ],
    },
    {
        "id": 2,
        "icono": "users",
        "titulo": "Alta Empleabilidad",
        "descripcion": (
            "El 100% de nuestros egresados encuentra trabajo en su área "
            "en menos de 6 meses tras graduarse."
        ),
        "detalle": (
            "Nuestra tasa de empleabilidad es del 100%. Esto se debe a la "
            "combinación de formación práctica, convenios con empresas y "
            "una red activa de egresados que comparten oportunidades "
            "laborales."
        ),
        "puntos": [
            "100% de empleabilidad en menos de 6 meses",
            "Salario promedio superior al mercado",
            "Red de 500+ egresados activos",
            "Bolsa de trabajo institucional",
        ],
    },
    {
        "id": 3,
        "icono": "building-2",
        "titulo": "Convenios Empresariales",
        "descripcion": (
            "Prácticas profesionales garantizadas en empresas líderes "
            "de la región y del país."
        ),
        "detalle": (
            "Tenemos convenios activos con más de 15 empresas líderes en "
            "sus sectores. Esto garantiza que cada estudiante realice "
            "prácticas profesionales en un entorno real antes de graduarse."
        ),
        "puntos": [
            "Más de 15 empresas aliadas",
            "Prácticas garantizadas para todos los estudiantes",
            "Convenios en Santa Cruz, La Paz y Cochabamba",
            "Posibilidad de contratación al finalizar prácticas",
        ],
    },
    {
        "id": 4,
        "icono": "book-open",
        "titulo": "Formación Integral",
        "descripcion": (
            "Además de la técnica, desarrollamos habilidades blandas, "
            "liderazgo y pensamiento crítico."
        ),
        "detalle": (
            "Un profesional técnico completo no solo domina su área: también "
            "sabe comunicar, liderar equipos y resolver problemas. En "
            "INSTEIN formamos profesionales completos para el mundo laboral "
            "actual."
        ),
        "puntos": [
            "Talleres de liderazgo y trabajo en equipo",
            "Comunicación efectiva y oratoria",
            "Pensamiento crítico y resolución de problemas",
            "Ética profesional y responsabilidad social",
        ],
    },
    {
        "id": 5,
        "icono": "heart",
        "titulo": "Comunidad",
        "descripcion": (
            "Una red de 500+ egresados que se apoyan mutuamente y "
            "comparten oportunidades profesionales."
        ),
        "detalle": (
            "Al egresar no estás solo: te unes a una comunidad activa de "
            "más de 500 profesionales que se apoyan mutuamente, comparten "
            "oportunidades y participan en eventos institucionales."
        ),
        "puntos": [
            "Grupo de WhatsApp y Telegram activos",
            "Eventos anuales de networking",
            "Mentorías de egresados a estudiantes actuales",
            "Bolsa de trabajo exclusiva para egresados",
        ],
    },
]


# ======================================================================
# Contenido del diálogo
# ======================================================================


def _contenido_dialogo(razon: Razon) -> rx.Component:
    """Contenido del diálogo: icono + descripción + puntos."""
    return rx.vstack(
        rx.box(
            rx.icon(razon["icono"], size=32, color=AZUL_MARINO_NEON),
            padding="1rem",
            border_radius=RADIO_EXTRA_GRANDE,
            background=FONDO_AZUL_SUAVE,
            border=f"1px solid {BORDE_HOME_AZUL}",
            box_shadow=rx.color_mode_cond(
                light=f"0 0 30px {AZUL_MARINO_NEON}30",
                dark=f"0 0 30px {AZUL_MARINO_NEON}40",
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            width="fit-content",
            margin="0 auto",
        ),
        rx.text(
            razon["detalle"],
            font_size=["0.875rem", "0.9375rem", "0.9375rem"],
            line_height="1.7",
            color=TEXTO_HOME_SUAVE,
            text_align="center",
        ),
        rx.box(
            rx.vstack(
                rx.foreach(
                    razon["puntos"],
                    lambda punto: rx.flex(
                        rx.icon(
                            "circle-check",
                            size=16,
                            color=AZUL_MARINO_NEON,
                            flex_shrink="0",
                            margin_top="0.125rem",
                        ),
                        rx.text(
                            punto,
                            font_size=["0.8125rem", "0.875rem", "0.875rem"],
                            color=TEXTO_HOME_SUAVE,
                            line_height="1.5",
                        ),
                        align="start",
                        gap="0.625rem",
                        width="100%",
                    ),
                ),
                spacing="2",
                align="start",
                width="100%",
            ),
            padding="1rem",
            background=FONDO_AZUL_MUY_SUAVE,
            border=f"1px solid {BORDE_HOME_SUAVE}",
            border_radius=RADIO_MEDIO,
            backdrop_filter="blur(12px)",
            width="100%",
        ),
        spacing="4",
        align="center",
        width="100%",
    )


# ======================================================================
# Pie del diálogo
# ======================================================================


def _boton_cerrar_dialogo() -> rx.Component:
    """Botón 'Cerrar' (soft gray)."""
    return rx.dialog.close(
        rx.button(
            rx.icon("x", size=16),
            rx.text("Cerrar", as_="span", font_weight="600"),
            variant="soft",
            color_scheme="gray",
            size="3",
            cursor="pointer",
            width=rx.breakpoints(initial="100%", sm="auto"),
        ),
    )


def _boton_mas_informacion() -> rx.Component:
    """Botón 'Más información' que navega a /contacto."""
    return rx.dialog.close(
        rx.button(
            rx.icon("message-circle", size=16),
            rx.text("Más información", as_="span", font_weight="700"),
            on_click=rx.redirect("/contacto"),
            size="3",
            cursor="pointer",
            width=rx.breakpoints(initial="100%", sm="auto"),
            background=AZUL_MARINO_NEON,
            color="white",
            box_shadow=f"0 0 20px {AZUL_MARINO_NEON}60",
            transition="all 0.2s",
            _hover={
                "transform": "translateY(-1px)",
                "box_shadow": f"0 0 30px {AZUL_MARINO_NEON}cc",
            },
        ),
    )


def _pie_dialogo() -> rx.Component:
    """Pie del diálogo responsive (móvil columna, desktop fila)."""
    return rx.box(
        rx.mobile_only(
            rx.vstack(
                _boton_mas_informacion(),
                _boton_cerrar_dialogo(),
                spacing="2",
                width="100%",
                align="stretch",
            ),
        ),
        rx.tablet_and_desktop(
            rx.flex(
                _boton_cerrar_dialogo(),
                _boton_mas_informacion(),
                spacing="3",
                justify="end",
                width="100%",
                flex_wrap="wrap",
            ),
        ),
        width="100%",
        padding=[
            "1rem 1rem 0 1rem",
            "1rem 1.5rem 0 1.5rem",
            "1rem 2rem 0 2rem",
        ],
        border_top=f"1px solid {BORDE_HOME_SUAVE}",
        margin_top="1rem",
    )


# ======================================================================
# Card + diálogo
# ======================================================================


def _tarjeta_razon_con_dialogo(razon: Razon) -> rx.Component:
    """Envuelve la card + el diálogo en un `rx.dialog.root`."""
    return rx.dialog.root(
        # ==========================================================
        # Trigger: la card
        # ==========================================================
        rx.dialog.trigger(
            rx.box(
                rx.vstack(
                    rx.box(
                        rx.icon(
                            razon["icono"],
                            size=24,
                            color=AZUL_MARINO_NEON,
                        ),
                        padding="0.75rem",
                        border_radius=RADIO_GRANDE,
                        background=FONDO_AZUL_SUAVE,
                        border=f"1px solid {BORDE_HOME_AZUL}",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        width="fit-content",
                        margin_bottom="1rem",
                    ),
                    rx.heading(
                        razon["titulo"],
                        size="3",
                        color=TEXTO_HOME_PRINCIPAL,
                        font_weight="800",
                        letter_spacing="-0.02em",
                    ),
                    rx.text(
                        razon["descripcion"],
                        font_size="0.875rem",
                        line_height="1.6",
                        color=TEXTO_HOME_MAS_SUAVE,
                    ),
                    rx.flex(
                        rx.text(
                            "Ver más",
                            font_size="0.875rem",
                            font_weight="700",
                            color=AZUL_MARINO_NEON,
                        ),
                        rx.icon(
                            "arrow-right",
                            size=14,
                            color=AZUL_MARINO_NEON,
                        ),
                        align="center",
                        gap="0.25rem",
                        margin_top="0.75rem",
                        transition="all 0.2s",
                    ),
                    align="start",
                    spacing="1",
                    width="100%",
                ),
                cursor="pointer",
                padding="1.75rem",
                border_radius=RADIO_EXTRA_GRANDE,
                border=f"1px solid {BORDE_HOME_SUAVE}",
                background=FONDO_HOME_CARD,
                backdrop_filter="blur(12px)",
                transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                width="100%",
                height="100%",
                _hover={
                    "transform": "translateY(-4px)",
                    "border_color": BORDE_HOME_AZUL,
                    "box_shadow": SOMBRA_HOVER_CARD_HOME,
                },
            ),
        ),
        # ==========================================================
        # Contenido del diálogo (con fix móvil)
        # ==========================================================
        rx.dialog.content(
            rx.vstack(
                rx.dialog.title(
                    razon["titulo"],
                    font_size=["1.125rem", "1.25rem", "1.25rem"],
                    font_weight="800",
                    color=TEXTO_HOME_PRINCIPAL,
                    line_height="1.2",
                    letter_spacing="-0.02em",
                ),
                rx.dialog.description(
                    "Conoce por qué esta característica hace la diferencia.",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                spacing="1",
                align="start",
                width="100%",
                padding=[
                    "1.25rem 1rem 0 1rem",
                    "1.5rem 1.5rem 0 1.5rem",
                    "1.5rem 2rem 0 2rem",
                ],
            ),
            rx.box(
                _contenido_dialogo(razon),
                flex="1",
                min_height="0",
                width="100%",
                overflow_y="auto",
                overflow_x="hidden",
                padding=["1rem", "1.25rem 1.5rem", "1.25rem 2rem"],
                css={
                    "&::-webkit-scrollbar": {"width": "8px"},
                    "&::-webkit-scrollbar-thumb": {
                        "background": BORDE_HOME_MEDIO,
                        "border_radius": "4px",
                    },
                    "&::-webkit-scrollbar-track": {
                        "background": "transparent",
                    },
                    "scrollbar-width": "thin",
                    "scrollbar-color": f"{BORDE_HOME_MEDIO} transparent",
                },
            ),
            _pie_dialogo(),
            max_width="34rem",
            width=[
                "calc(100vw - 1.5rem)",
                "calc(100vw - 2rem)",
                "100%",
            ],
            padding="0",
            border_radius=RADIO_EXTRA_GRANDE,
            background=FONDO_HOME_CARD,
            border=f"1px solid {BORDE_HOME_AZUL}",
            box_shadow=rx.color_mode_cond(
                light=(
                    f"0 30px 60px -15px rgba(0, 0, 0, 0.25), "
                    f"0 0 40px -10px {AZUL_MARINO_NEON}20"
                ),
                dark=(
                    f"0 30px 60px -15px rgba(0, 0, 0, 0.5), "
                    f"0 0 40px -10px {AZUL_MARINO_NEON}40"
                ),
            ),
            overflow="hidden",
            display="flex",
            flex_direction="column",
            max_height=rx.breakpoints(
                initial="90dvh",
                sm="90dvh",
                md="88dvh",
                lg="85dvh",
            ),
        ),
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_por_que_instein() -> rx.Component:
    """
    Sección completa "¿Por qué elegir INSTEIN?".

    Grid responsive de 6 tarjetas. Cada una abre su propio diálogo.
    """
    return rx.box(
        rx.vstack(
            rx.grid(
                *[_tarjeta_razon_con_dialogo(r) for r in RAZONES],
                columns=rx.breakpoints(initial="1", sm="2", lg="3"),
                spacing="4",
                width="100%",
            ),
            align="center",
            width="100%",
            max_width="72rem",
            margin="0 auto",
        ),
        width="100%",
        padding=[
            "0 1rem 4rem 1rem",
            "0 1.5rem 4rem 1.5rem",
            "0 1.5rem 4rem 1.5rem",
        ],
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "RAZONES",
    "Razon",
    "seccion_por_que_instein",
]