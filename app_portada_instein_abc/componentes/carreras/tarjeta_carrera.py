

from __future__ import annotations

import reflex as rx

from ...componentes.base.primitivos import (
    contenedor_clicable,
    enlace_navegacion,
)
from ...dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ...dominio.modelos.carrera import Carrera, PlanAnual
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_SUAVE,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_MEDIO,
)


# ======================================================================
# Constantes locales
# ======================================================================

TAMANO_ICONO_CARRERA: str = "4rem"
"""Tamaño del icono/imagen de la carrera en la tarjeta."""

LONGITUD_MAXIMA_LEMA: int = 40
"""Longitud máxima del lema antes de truncarlo con "..."."""

SOMBRA_GLOW_AZUL_SUAVE: str = f"0 0 12px {AZUL_MARINO_NEON}60"
"""Glow azul marino suave (60 = 37.5% opacidad en hex)."""


# ======================================================================
# Helpers internos
# ======================================================================


def _icono_carrera_redondeado(carrera: Carrera) -> rx.Component:
    """
    Icono/imagen de la carrera con esquinas redondeadas.

    Args:
        carrera: `Carrera` con `imagen_archivo` y `nombre`.

    Returns:
        Imagen cuadrada con border-radius redondeado.
    """
    return rx.box(
        rx.image(
            src="/" + carrera["imagen_archivo"],
            alt=carrera["nombre"],
            width="100%",
            height="100%",
            object_fit="cover",
            border_radius=RADIO_MEDIO,
        ),
        width=TAMANO_ICONO_CARRERA,
        height=TAMANO_ICONO_CARRERA,
        flex_shrink="0",
        border_radius=RADIO_MEDIO,
        overflow="hidden",
        border=f"1px solid {BORDE_HOME_SUAVE}",
    )


def _rating_compacto(puntuacion: str | rx.Var) -> rx.Component:
    """
    Fila compacta con puntuación + estrella.

    Args:
        puntuacion: Valor de puntuación a mostrar. Acepta `str`
            estático (ej: "4.8") o `Var` reactivo.

    Returns:
        Fila con el número + icono de estrella.
    """
    return rx.flex(
        rx.text(
            puntuacion,
            font_size="0.75rem",
            font_weight="600",
            color=TEXTO_HOME_PRINCIPAL,
        ),
        rx.icon(
            "star",
            size=10,
            color=rx.color("amber", 9),
            fill=rx.color("amber", 9),
        ),
        align="center",
        gap="0.25rem",
        margin_top="0.125rem",
    )


def _info_carrera_compacta(
    carrera: Carrera,
    descripcion_corta: str | None = None,
) -> rx.Component:
    """
    Bloque de información textual de la carrera.

    Estructura:
    - Nombre corto (destacado).
    - Descripción secundaria (lema truncado o duración).
    - Rating con estrella.

    Args:
        carrera: `Carrera` con `nombre_corto`, `duracion`, `lema`.
        descripcion_corta: Si se pasa, se usa como segunda línea
            (ej: lema truncado). Si es `None`, se usa
            `"<duracion> · Técnico Superior"`.

    Returns:
        Bloque vertical con nombre + descripción + rating.
    """
    texto_secundario = (
        descripcion_corta
        if descripcion_corta is not None
        else f"{carrera['duracion']} · Técnico Superior"
    )

    puntuacion_carrera = carrera["estadisticas"]["puntuacion"]

    return rx.vstack(
        rx.text(
            carrera["nombre_corto"],
            font_size="0.9375rem",
            font_weight="700",
            color=TEXTO_HOME_PRINCIPAL,
            line_height="1.3",
        ),
        rx.text(
            texto_secundario,
            font_size="0.75rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.3",
        ),
        _rating_compacto(str(puntuacion_carrera)),
        align="start",
        spacing="1",
        flex="1",
        min_width="0",
    )


# ======================================================================
# Item de carrera (tarjeta base)
# ======================================================================


def tarjeta_carrera(carrera: Carrera) -> rx.Component:
    """
    Item de carrera estilo Google Play Store (adaptativo).

    Estructura horizontal:
    - Icono/imagen redondeada de la carrera.
    - Nombre corto + duración + rating.

    Estilo:
    - Fondo transparente por defecto.
    - Hover: fondo azul marino translúcido + elevación sutil.
    - Cada item es un enlace a `/carrera/{id}`.

    Args:
        carrera: `Carrera` con todos los datos necesarios.

    Returns:
        Enlace estilizado como tarjeta horizontal.
    """
    return enlace_navegacion(
        f"/carrera/{carrera['id']}",
        rx.flex(
            _icono_carrera_redondeado(carrera),
            _info_carrera_compacta(carrera),
            align="center",
            gap="1rem",
            width="100%",
        ),
        padding="0.75rem",
        border_radius=RADIO_MEDIO,
        background="transparent",
        width="100%",
        text_align="left",
        transition="all 0.15s ease-out",
        cursor="pointer",
        _hover={"background": FONDO_AZUL_SUAVE},
    )


# ======================================================================
# Item de carrera con ranking explícito
# ======================================================================


def item_carrera_ranking(carrera: Carrera, indice: int) -> rx.Component:
    """
    Item de carrera con número de ranking a la izquierda.

    Estilo "Listas de éxitos" de Google Play. La diferencia con
    `tarjeta_carrera` es el número de ranking a la izquierda y el
    lema truncado como segunda línea (en vez de la duración).

    Args:
        carrera: `Carrera` con todos los datos necesarios.
        indice: Posición en el ranking (0-based, se muestra 1-based).

    Returns:
        Enlace estilizado con número de ranking.
    """
    lema_truncado = carrera["lema"][:LONGITUD_MAXIMA_LEMA] + "..."

    return enlace_navegacion(
        f"/carrera/{carrera['id']}",
        rx.flex(
            # --- Número de ranking ---
            rx.box(
                rx.text(
                    (indice + 1).to_string(),
                    font_size="1rem",
                    font_weight="600",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                width="1.5rem",
                text_align="center",
                flex_shrink="0",
            ),
            _icono_carrera_redondeado(carrera),
            _info_carrera_compacta(
                carrera,
                descripcion_corta=lema_truncado,
            ),
            align="center",
            gap="1rem",
            width="100%",
        ),
        padding="0.75rem",
        border_radius=RADIO_MEDIO,
        background="transparent",
        width="100%",
        text_align="left",
        transition="all 0.15s ease-out",
        cursor="pointer",
        _hover={"background": FONDO_AZUL_SUAVE},
    )


# ======================================================================
# Pastilla de año del plan de estudios
# ======================================================================


def pastilla_anio(plan_anual: PlanAnual, indice: int) -> rx.Component:
    """
    Pastilla seleccionable que representa un año del plan de estudios.

    Estilo:
    - **Activa**: fondo azul marino neon + texto blanco + glow azul.
    - **Inactiva**: fondo azul marino muy translúcido + texto adaptativo.
    - Hover: elevación sutil.

    ✅ ADAPTATIVO: los colores inactivos cambian según el modo.

    Args:
        plan_anual: `PlanAnual` con `anio` (ej: "Primer Año").
        indice: Índice del año en el plan (0-based).

    Returns:
        Contenedor clicable con la pastilla del año.
    """
    esta_activo: rx.Var = (
        EstadoInstitucional.indice_anio_seleccionado == indice
    )

    return contenedor_clicable(
        rx.text(plan_anual["anio"], size="2"),
        al_hacer_clic=lambda: EstadoInstitucional.seleccionar_anio(indice),
        padding="0.625rem 1.125rem",
        border_radius=RADIO_MEDIO,
        background=rx.cond(
            esta_activo,
            AZUL_MARINO_NEON,
            FONDO_AZUL_SUAVE,
        ),
        color=rx.cond(
            esta_activo,
            "white",
            TEXTO_HOME_SUAVE,
        ),
        border=rx.cond(
            esta_activo,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {BORDE_HOME_SUAVE}",
        ),
        box_shadow=rx.cond(
            esta_activo,
            f"0 0 20px {AZUL_MARINO_NEON}60",
            "none",
        ),
        font_weight="600",
        white_space="nowrap",
        display="inline-flex",
        align_items="center",
        transition="all 0.2s",
        _hover={"transform": "translateY(-2px)"},
    )


# ======================================================================
# Fila de materia del plan de estudios
# ======================================================================


def fila_materia(materia: str, indice: int) -> rx.Component:
    """
    Fila individual de una materia dentro del plan de estudios.

    Estilo:
    - Número de materia: fondo azul marino neon con glow.
    - Nombre de la materia: texto adaptativo.
    - Icono decorativo `book-open`.
    - Hover: fondo azul + borde azul + desplazamiento lateral.

    ✅ ADAPTATIVO: fondo, textos y bordes cambian según el modo.

    Args:
        materia: Nombre de la materia.
        indice: Índice de la materia en el año (0-based, se muestra
            1-based como número visible).

    Returns:
        Fila estilizada con la materia.
    """
    return rx.box(
        rx.flex(
            # --- Número de materia (acento) ---
            rx.flex(
                rx.text(
                    (indice + 1).to_string(),
                    font_size="0.875rem",
                    font_weight="700",
                    color="white",
                ),
                height="2rem",
                width="2rem",
                border_radius=RADIO_MEDIO,
                background=AZUL_MARINO_NEON,
                box_shadow=SOMBRA_GLOW_AZUL_SUAVE,
                align="center",
                justify="center",
                flex_shrink="0",
            ),
            # --- Nombre de la materia ---
            rx.text(
                materia,
                font_size="0.9375rem",
                color=TEXTO_HOME_SUAVE,
                flex="1",
            ),
            # --- Icono decorativo ---
            rx.icon(
                "book-open",
                size=16,
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            align="center",
            gap="0.875rem",
            width="100%",
        ),
        padding="0.875rem 1rem",
        border_radius=RADIO_MEDIO,
        background=FONDO_AZUL_SUAVE,
        border=f"1px solid {BORDE_HOME_SUAVE}",
        transition="all 0.2s",
        _hover={
            "background": FONDO_AZUL_SUAVE,
            "border_color": BORDE_HOME_AZUL,
            "transform": "translateX(4px)",
        },
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "fila_materia",
    "item_carrera_ranking",
    "pastilla_anio",
    "tarjeta_carrera",
]