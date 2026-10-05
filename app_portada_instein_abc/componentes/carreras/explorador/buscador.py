"""
Buscador de carreras + card + grid + estado vacío.

Estructura
----------
- `buscador_carreras`:        input de búsqueda con iconos decorativos.
- `card_imagen_carrera`:      card con imagen destacada (navega al detalle).
- `grid_imagenes_carreras`:   grid + contador + estado vacío.
- `estado_vacio_busqueda`:    estado vacío (delegado al componente unificado).

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.

- Fondo del buscador: `FONDO_HOME_CARD` (adaptativo).
- Acentos: `AZUL_MARINO_NEON` en ambos modos.
- Texto: `TEXTO_HOME_PRINCIPAL` / `TEXTO_HOME_SUAVE` / `TEXTO_HOME_MAS_SUAVE`.
- Bordes: `BORDE_HOME_AZUL` / `BORDE_HOME_SUAVE`.

Nota técnica: IMPORTS DESDE LA FACHADA
--------------------------------------
Todos los imports de infraestructura se hacen desde la fachada
`infraestructura` (no desde los módulos internos
`infraestructura.constantes.colores` ni `...dimensiones`).

Motivo: `ANCHO_CONTENIDO` vive en `dimensiones.py`, y mezclar rutas
es fuente de errores. La fachada unifica.
"""

from __future__ import annotations

import reflex as rx

from ....componentes.base.estado_vacio import (
    estado_vacio,
)
from ....componentes.base.primitivos import (
    enlace_navegacion,
)
from ....dominio.estados.estado_institucional import (
    EstadoInstitucional,
)
from ....dominio.modelos.carrera import Carrera
from ....infraestructura import (
    ANCHO_CONTENIDO,
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_HOME_CARD,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    SOMBRA_HOVER_CARD_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)

from .constantes import (
    ALTO_BANNER_CARD_GRANDE,
    ANCHO_MAXIMO_BUSCADOR,
    PADDING_INFERIOR_GRID,
    TAMANO_ICONO_ESTADO_VACIO,
)


# ======================================================================
# BUSCADOR
# ======================================================================


def buscador_carreras() -> rx.Component:
    """
    Buscador central adaptativo.

    UX:
    - Icono de búsqueda (izquierda) en azul marino.
    - Input con placeholder adaptativo.
    - Icono decorativo "sparkles" (derecha) en azul marino.
    - Glassmorphism adaptativo en el fondo.
    - Hover: borde azul marino.
    """
    return rx.box(
        rx.flex(
            rx.box(
                rx.icon("search", size=20, color=AZUL_MARINO_NEON),
                padding="0.5rem",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.input(
                placeholder=(
                    "Busca una carrera: Sistemas, Contaduría, "
                    "Electrónica..."
                ),
                value=EstadoInstitucional.texto_busqueda_carrera,
                on_change=EstadoInstitucional.actualizar_busqueda_carrera,
                variant="soft",
                size="3",
                width="100%",
                border="none",
                background="transparent",
                color=TEXTO_HOME_PRINCIPAL,
                _placeholder={"color": TEXTO_HOME_MAS_SUAVE},
                _focus={"box_shadow": "none", "outline": "none"},
            ),
            rx.box(
                rx.icon("sparkles", size=18, color=AZUL_MARINO_NEON),
                padding="0.5rem",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            align="center",
            width="100%",
            gap="0.5rem",
        ),
        width="100%",
        max_width=ANCHO_MAXIMO_BUSCADOR,
        margin="0 auto 1.5rem auto",
        padding="0.75rem 1rem",
        border_radius=RADIO_GRANDE,
        background=FONDO_HOME_CARD,
        border=f"1px solid {BORDE_HOME_SUAVE}",
        backdrop_filter="blur(12px)",
        box_shadow=rx.color_mode_cond(
            light=f"0 10px 30px -10px {AZUL_MARINO_NEON}20",
            dark=f"0 10px 30px -10px {AZUL_MARINO_NEON}40",
        ),
        transition="all 0.2s",
        _hover={"border_color": BORDE_HOME_AZUL},
    )


# ======================================================================
# ESTADO VACÍO
# ======================================================================


def estado_vacio_busqueda() -> rx.Component:
    """
    Estado vacío cuando la búsqueda no devuelve resultados.

    Delega en `componentes.base.estado_vacio`. El mensaje se pasa como
    `rx.Component` para mostrar el término buscado con estilo.
    """
    mensaje_enriquecido = rx.text(
        "No hay resultados para ",
        rx.text.span(
            f'"{EstadoInstitucional.texto_busqueda_carrera}"',
            font_weight="700",
            color=AZUL_MARINO_NEON,
        ),
        ". Intenta con otro término o explora todas las carreras "
        "disponibles.",
        font_size="0.875rem",
        color=TEXTO_HOME_MAS_SUAVE,
        text_align="center",
        max_width="32rem",
        line_height="1.6",
    )

    return estado_vacio(
        titulo="No se encontraron carreras",
        mensaje=mensaje_enriquecido,
        icono="search-x",
        variante="neon",
        tamano_icono=TAMANO_ICONO_ESTADO_VACIO,
        icono_acento=True,
        boton_accion_etiqueta="Restablecer búsqueda",
        boton_accion_icono="rotate-ccw",
        boton_accion_on_click=(
            EstadoInstitucional.actualizar_busqueda_carrera("")
        ),
        boton_accion_color_scheme="blue",
    )


# ======================================================================
# CARD DE IMAGEN DE CARRERA
# ======================================================================


def card_imagen_carrera(carrera: Carrera) -> rx.Component:
    """
    Card con la imagen de la carrera destacada arriba.

    Al hacer clic, navega al detalle (`/carrera/{id}`).

    Patrón `rx.card` + `rx.inset(side="top")`:
    - Imagen edge-to-edge arriba.
    - Icono + nombre + duración abajo.
    - Indicador de navegación "arrow-up-right".

    ✅ ADAPTATIVO: fondo, textos y borde cambian con el modo.
    """
    return enlace_navegacion(
        f"/carrera/{carrera['id']}",
        rx.card(
            rx.inset(
                rx.box(
                    rx.image(
                        src="/" + carrera["imagen_archivo"],
                        alt=carrera["nombre"],
                        width="100%",
                        height="100%",
                        object_fit="cover",
                    ),
                    rx.box(
                        position="absolute",
                        top="0",
                        left="0",
                        right="0",
                        bottom="0",
                        background=(
                            f"linear-gradient(180deg, "
                            f"transparent 40%, "
                            f"rgba(59, 91, 219, 0.4) 100%)"
                        ),
                        pointer_events="none",
                    ),
                    position="relative",
                    width="100%",
                    height=ALTO_BANNER_CARD_GRANDE,
                    overflow="hidden",
                    border_radius=RADIO_MEDIO,
                ),
                side="top",
                pb="current",
            ),
            rx.flex(
                rx.flex(
                    rx.icon(
                        carrera["icono"],
                        size=14,
                        color=AZUL_MARINO_NEON,
                    ),
                    height="1.75rem",
                    width="1.75rem",
                    border_radius=RADIO_MEDIO,
                    background=FONDO_AZUL_SUAVE,
                    border=f"1px solid {BORDE_HOME_AZUL}",
                    align="center",
                    justify="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(
                        carrera["nombre_corto"],
                        font_size="0.875rem",
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        line_height="1.2",
                    ),
                    rx.text(
                        carrera["duracion"],
                        font_size="0.6875rem",
                        color=TEXTO_HOME_MAS_SUAVE,
                        line_height="1.2",
                    ),
                    spacing="0",
                    align="start",
                    flex="1",
                    min_width="0",
                ),
                rx.icon(
                    "arrow-up-right",
                    size=14,
                    color=TEXTO_HOME_MAS_SUAVE,
                    flex_shrink="0",
                ),
                align="center",
                gap="0.5rem",
                width="100%",
            ),
            padding="0.5rem",
            width="100%",
            cursor="pointer",
            background=FONDO_HOME_CARD,
            backdrop_filter="blur(12px)",
            border=f"1px solid {BORDE_HOME_SUAVE}",
            transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
            _hover={
                "transform": "translateY(-4px)",
                "border_color": BORDE_HOME_AZUL,
                "box_shadow": SOMBRA_HOVER_CARD_HOME,
            },
        ),
        text_decoration="none",
        width="100%",
    )


# ======================================================================
# GRID DE CARRERAS
# ======================================================================


def grid_imagenes_carreras() -> rx.Component:
    """
    Grid con las imágenes de todas las carreras filtradas.

    Muestra:
    - Contador de resultados.
    - Grid de cards (si hay resultados).
    - Estado vacío (si no hay resultados).
    """
    return rx.box(
        rx.flex(
            rx.text(
                "Carreras disponibles",
                font_size="0.75rem",
                font_weight="700",
                letter_spacing="0.1em",
                text_transform="uppercase",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.text(
                EstadoInstitucional.carreras_filtradas.length().to_string(),
                font_size="0.75rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                padding="0.125rem 0.5rem",
                background=FONDO_AZUL_SUAVE,
                border=f"1px solid {BORDE_HOME_AZUL}",
                border_radius=RADIO_PASTILLA,
            ),
            align="center",
            gap="0.5rem",
            margin_bottom="1rem",
        ),
        rx.cond(
            EstadoInstitucional.carreras_filtradas.length() > 0,
            rx.grid(
                rx.foreach(
                    EstadoInstitucional.carreras_filtradas,
                    card_imagen_carrera,
                ),
                columns=rx.breakpoints(initial="2", md="3", lg="5"),
                spacing="3",
                width="100%",
            ),
            estado_vacio_busqueda(),
        ),
        width="100%",
        max_width=ANCHO_CONTENIDO,
        margin=PADDING_INFERIOR_GRID,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "buscador_carreras",
    "card_imagen_carrera",
    "estado_vacio_busqueda",
    "grid_imagenes_carreras",
]