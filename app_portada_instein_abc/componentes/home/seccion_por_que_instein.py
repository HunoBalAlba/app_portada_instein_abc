"""
Sección "¿Por qué elegir INSTEIN?" — estilo Neon.com.

Diseño
------
Refactorizado al estilo de Neon.com:

1. **Cards limpias**: sin glow, sin backdrop_filter, sin translateY.
2. **Sin cajas para iconos**: el icono va directo, sin fondo.
3. **Número visible**: cada card lleva `01`, `02`, ..., `06`.
4. **CTA unificado**: el título mismo lleva la flecha `→`.
5. **Hover sutil**: solo cambia el borde, sin elevación.
6. **Diálogo simplificado**: sin icono grande centrado, sin
   fondo tintado en los puntos.
7. **Padding del contenedor eliminado**: coherente con
   `_seccion()` de inicio.
8. **Tipografía mejorada**: título `size="4"`, descripción más
   legible.

Contenido
---------
- 6 tarjetas con razones clave.
- Cada tarjeta abre un diálogo con detalle ampliado.

Patrón de diálogo
-----------------
Se usa `rx.dialog.trigger` (patrón declarativo de Radix Themes)
en lugar de `on_click` manual. Cada card envuelve su propio
`rx.dialog.root` con su contenido específico.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: ¿POR QUÉ SIN ICONO EN CAJA?
-----------------------------------------
El diseño original usaba un icono en caja cuadrada con fondo
tintado. Visualmente resultaba "ruidoso":

- 6 iconos idénticos en 6 cajas idénticas.
- Redundancia visual: el icono no aporta información nueva.
- Compite con el número y el título.

En la nueva versión, el icono va **directo** en color azul
marino, sin caja. Esto:

- Reduce el ruido visual.
- Enfoca la atención en el número + título.
- Es más minimalista y elegante.

Nota técnica: CTA "VER MÁS" UNIFICADO
-------------------------------------
El diseño original tenía un CTA "Ver más →" repetido en cada
card. Como hay 6 cards, era 6 veces el mismo CTA. Redundante.

En la nueva versión, el **título mismo lleva la flecha** `→`.
Al hacer click en cualquier parte de la card, se abre el diálogo.
Más limpio, menos texto.

Nota técnica: FIX MÓVIL DEL DIÁLOGO
-----------------------------------
El diálogo mantiene el fix móvil del original:

- Scroll interno en `flex: 1` + `min_height: 0`.
- Marco en `display: flex` + `flex-direction: column`.
- Altura máxima con `dvh` para respetar la barra de URL móvil.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    COLOR_DIVISOR,
    FONDO_HOME_CARD,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_EXTRA_GRANDE,
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
            "Todos nuestros títulos están autorizados por el Ministerio "
            "de Educación con Resolución Ministerial R.M. 0871/2016."
        ),
        "detalle": (
            "Nuestros títulos tienen validez nacional y están "
            "respaldados por resoluciones ministeriales vigentes. Al "
            "egresar, recibirás un Técnico Superior en Provisión "
            "Nacional reconocido por empleadores de todo el país."
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
            "Laboratorios equipados y docentes especializados con "
            "experiencia real en el campo profesional."
        ),
        "detalle": (
            "En INSTEIN no solo estudias teoría: practicas desde el "
            "primer año con equipamiento moderno y docentes que "
            "trabajan activamente en la industria. Nuestros "
            "laboratorios replican entornos reales de trabajo."
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
            "El 100% de nuestros egresados encuentra trabajo en su "
            "área en menos de 6 meses tras graduarse."
        ),
        "detalle": (
            "Nuestra tasa de empleabilidad es del 100%. Esto se debe a "
            "la combinación de formación práctica, convenios con "
            "empresas y una red activa de egresados que comparten "
            "oportunidades laborales."
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
            "Tenemos convenios activos con más de 15 empresas líderes "
            "en sus sectores. Esto garantiza que cada estudiante "
            "realice prácticas profesionales en un entorno real antes "
            "de graduarse."
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
            "Un profesional técnico completo no solo domina su área: "
            "también sabe comunicar, liderar equipos y resolver "
            "problemas. En INSTEIN formamos profesionales completos "
            "para el mundo laboral actual."
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
            "Al egresar no estás solo: te unes a una comunidad activa "
            "de más de 500 profesionales que se apoyan mutuamente, "
            "comparten oportunidades y participan en eventos "
            "institucionales."
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
    """
    Contenido del diálogo: descripción + lista de puntos.

    Estilo Neon.com:
    - Sin icono grande centrado.
    - Sin fondo tintado en los puntos.
    - Solo texto + lista con iconos discretos.
    """
    return rx.vstack(
        # ─── Descripción ───────────────────────────────────────
        rx.text(
            razon["detalle"],
            font_size=["0.9375rem", "1rem", "1rem"],
            line_height="1.7",
            color=TEXTO_HOME_SUAVE,
        ),
        # ─── Separador ────────────────────────────────────────
        rx.box(
            height="1px",
            width="100%",
            background=COLOR_DIVISOR,
            margin_y="1.5rem",
        ),
        # ─── Lista de puntos ──────────────────────────────────
        rx.vstack(
            rx.foreach(
                razon["puntos"],
                lambda punto: rx.flex(
                    rx.icon(
                        "check",
                        size=16,
                        color=AZUL_MARINO_NEON,
                        flex_shrink="0",
                        margin_top="0.1875rem",
                    ),
                    rx.text(
                        punto,
                        font_size=["0.875rem", "0.9375rem", "0.9375rem"],
                        color=TEXTO_HOME_SUAVE,
                        line_height="1.6",
                    ),
                    align="start",
                    gap="0.75rem",
                    width="100%",
                ),
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        spacing="0",
        align="start",
        width="100%",
    )


# ======================================================================
# Pie del diálogo
# ======================================================================


def _boton_cerrar_dialogo() -> rx.Component:
    """Botón 'Cerrar' (soft gray)."""
    return rx.dialog.close(
        rx.button(
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
            rx.text("Más información", as_="span", font_weight="700"),
            rx.icon("arrow-right", size=16),
            on_click=rx.redirect("/contacto"),
            size="3",
            cursor="pointer",
            width=rx.breakpoints(initial="100%", sm="auto"),
            background=AZUL_MARINO_NEON,
            color="white",
            transition="all 0.2s",
            _hover={
                "filter": "brightness(1.1)",
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
                gap="0.75rem",
                justify="end",
                width="100%",
                flex_wrap="wrap",
            ),
        ),
        width="100%",
        padding=[
            "1rem 1rem 0 1rem",
            "1.25rem 1.5rem 0 1.5rem",
            "1.5rem 2rem 0 2rem",
        ],
        border_top=f"1px solid {COLOR_DIVISOR}",
        margin_top="1.5rem",
    )


# ======================================================================
# Card + diálogo
# ======================================================================


def _tarjeta_razon_con_dialogo(razon: Razon) -> rx.Component:
    """
    Envuelve la card + el diálogo en un `rx.dialog.root`.

    Estilo de la card:
    - Fondo plano (`FONDO_HOME_CARD`).
    - Borde superior de acento (`2px solid AZUL_MARINO_NEON`).
    - Hover: solo cambia el borde, sin elevación.
    - Sin icono en caja.
    - Título con flecha `→` al final.
    - Sin CTA "Ver más" separado.

    Args:
        razon: `Razon` con `id`, `icono`, `titulo`, etc.

    Returns:
        Componente `rx.dialog.root` con card + diálogo.
    """
    numero = f"{razon['id'] + 1:02d}"  # "01", "02", ...

    return rx.dialog.root(
        # ==========================================================
        # Trigger: la card
        # ==========================================================
        rx.dialog.trigger(
            rx.box(
                rx.vstack(
                    # ─── Fila: número + icono ────────────────────
                    rx.flex(
                        rx.text(
                            numero,
                            font_size="0.75rem",
                            font_weight="700",
                            color=AZUL_MARINO_NEON,
                            letter_spacing="0.05em",
                            font_family="JetBrains Mono",
                        ),
                        rx.text(
                            "·",
                            font_size="0.75rem",
                            color=TEXTO_HOME_MAS_SUAVE,
                            margin_x="0.25rem",
                        ),
                        rx.icon(
                            razon["icono"],
                            size=14,
                            color=AZUL_MARINO_NEON,
                        ),
                        align="center",
                        gap="0.25rem",
                        margin_bottom="1rem",
                    ),
                    # ─── Título con flecha ───────────────────────
                    rx.flex(
                        rx.heading(
                            razon["titulo"],
                            size="4",
                            font_weight="700",
                            color=TEXTO_HOME_PRINCIPAL,
                            letter_spacing="-0.02em",
                            line_height="1.3",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=18,
                            color=AZUL_MARINO_NEON,
                            flex_shrink="0",
                            transition="transform 0.2s",
                        ),
                        align="center",
                        justify="between",
                        gap="0.75rem",
                        width="100%",
                    ),
                    # ─── Descripción ─────────────────────────────
                    rx.text(
                        razon["descripcion"],
                        font_size="0.875rem",
                        line_height="1.6",
                        color=TEXTO_HOME_MAS_SUAVE,
                        margin_top="0.75rem",
                    ),
                    align="start",
                    spacing="0",
                    width="100%",
                ),
                cursor="pointer",
                padding="1.75rem",
                border_radius=RADIO_EXTRA_GRANDE,
                border=f"1px solid {BORDE_HOME_SUAVE}",
                border_top=f"2px solid {AZUL_MARINO_NEON}",
                background=FONDO_HOME_CARD,
                transition="all 0.2s",
                width="100%",
                height="100%",
                _hover={
                    "border_color": AZUL_MARINO_NEON,
                    "border_top": f"2px solid {AZUL_MARINO_NEON}",
                    "& svg": {"transform": "translateX(4px)"},
                },
            ),
        ),
        # ==========================================================
        # Contenido del diálogo
        # ==========================================================
        rx.dialog.content(
            # ─── Header del diálogo ─────────────────────────────
            rx.vstack(
                rx.flex(
                    rx.icon(
                        razon["icono"],
                        size=20,
                        color=AZUL_MARINO_NEON,
                    ),
                    rx.dialog.title(
                        razon["titulo"],
                        font_size=["1.125rem", "1.25rem", "1.25rem"],
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        line_height="1.2",
                        letter_spacing="-0.02em",
                    ),
                    align="center",
                    gap="0.625rem",
                ),
                rx.dialog.description(
                    "Conoce por qué esta característica hace la "
                    "diferencia.",
                    font_size="0.8125rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                spacing="2",
                align="start",
                width="100%",
                padding=[
                    "1.25rem 1rem 0 1rem",
                    "1.5rem 1.5rem 0 1.5rem",
                    "1.5rem 2rem 0 2rem",
                ],
            ),
            # ─── Contenido con scroll interno ───────────────────
            rx.box(
                _contenido_dialogo(razon),
                flex="1",
                min_height="0",
                width="100%",
                overflow_y="auto",
                overflow_x="hidden",
                padding=["1rem", "1.25rem 1.5rem", "1.5rem 2rem"],
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
            # ─── Pie con botones ────────────────────────────────
            _pie_dialogo(),
            # ─── Estilos del marco del diálogo ──────────────────
            max_width="32rem",
            width=[
                "calc(100vw - 1.5rem)",
                "calc(100vw - 2rem)",
                "100%",
            ],
            padding="0",
            border_radius=RADIO_EXTRA_GRANDE,
            background=FONDO_HOME_CARD,
            border=f"1px solid {BORDE_HOME_SUAVE}",
            box_shadow=rx.color_mode_cond(
                light="0 20px 40px -10px rgba(0, 0, 0, 0.15)",
                dark="0 20px 40px -10px rgba(0, 0, 0, 0.5)",
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

    Layout:
    - Móvil:   1 columna.
    - Tablet:  2 columnas.
    - Desktop: 3 columnas.

    Returns:
        Componente `rx.box` con el grid de razones.
    """
    return rx.box(
        rx.grid(
            *[_tarjeta_razon_con_dialogo(r) for r in RAZONES],
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="4",
            width="100%",
            align_items="stretch",
        ),
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "RAZONES",
    "Razon",
    "seccion_por_que_instein",
]