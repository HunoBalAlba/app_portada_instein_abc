

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ...dominio.estados.estado_acordeon_faq import (
    EstadoAcordeonFaq,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_HOME_CARD,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_MEDIO,
)


# ======================================================================
# Tipos
# ======================================================================


class ItemFaq(TypedDict):
    """
    Item individual de FAQ (pregunta + respuesta).

    Se usa `TypedDict` (no `rx.Base`) para mantener consistencia con
    el resto del proyecto (`Post`, `Carrera`) y compatibilidad total
    con `rx.foreach`.
    """

    pregunta: str
    respuesta: str


# ======================================================================
# Configuración por variante
# ======================================================================


def _config_variante(variante: str) -> dict:
    """
    Devuelve la configuración visual del acordeón según la variante.

    Args:
        variante: `"light"` o `"neon"`.

    Returns:
        Dict con claves de estilo (fondo, bordes, colores de texto).

    Raises:
        ValueError: Si la variante no es `"light"` ni `"neon"`.
    """
    if variante == "neon":
        return {
            "fondo_card": FONDO_HOME_CARD,
            "fondo_card_abierta": FONDO_AZUL_MUY_SUAVE,
            "fondo_icono_abierto": FONDO_AZUL_SUAVE,
            "borde_card": BORDE_HOME_SUAVE,
            "borde_hover": BORDE_HOME_MEDIO,
            "borde_abierto": BORDE_HOME_AZUL,
            "color_texto": TEXTO_HOME_PRINCIPAL,
            "color_texto_secundario": TEXTO_HOME_MAS_SUAVE,
            "color_texto_cuerpo": TEXTO_HOME_SUAVE,
            "con_blur": True,
        }

    if variante == "light":
        return {
            "fondo_card": COLOR_FONDO_CARTA,
            "fondo_card_abierta": COLOR_FONDO_CARTA,
            "fondo_icono_abierto": FONDO_AZUL_SUAVE,
            "borde_card": COLOR_BORDE_SUAVE,
            "borde_hover": COLOR_BORDE_SUAVE,
            "borde_abierto": AZUL_MARINO_NEON,
            "color_texto": COLOR_TEXTO_PRINCIPAL,
            "color_texto_secundario": COLOR_TEXTO_SECUNDARIO,
            "color_texto_cuerpo": COLOR_TEXTO_CUERPO,
            "con_blur": False,
        }

    raise ValueError(
        f"Variante no válida: {variante!r}. "
        f"Usa 'light' o 'neon'."
    )


# ======================================================================
# Item individual
# ======================================================================


def _item_acordeon(
    item: ItemFaq | rx.Var,
    indice: int,
    *,
    icono: str,
    color_acento: str | rx.Var,
    radio_item: str,
    fondo_card,
    fondo_card_abierta,
    fondo_icono_abierto,
    borde_card,
    borde_hover,
    borde_abierto,
    color_texto,
    color_texto_secundario,
    color_texto_cuerpo,
    con_blur: bool,
    tamano_texto_pregunta: str,
    tamano_texto_respuesta: str,
    padding_cabecera: str,
    padding_respuesta: str,
) -> rx.Component:
    """
    Item individual del acordeón.

    Args:
        item: `ItemFaq` (dict estático) O `rx.Var` que apunta a un
            dict con `pregunta` y `respuesta`. En ambos casos, el
            acceso `item["pregunta"]` / `item["respuesta"]` funciona.
        indice: Índice del item en el `rx.foreach`.
        icono: Nombre del icono Lucide (kebab-case). Pasa `""` para
            ocultarlo.
        color_acento: Color del acento (hex o Var) cuando el item
            está abierto.
        radio_item: Border-radius de cada item.
        fondo_card, fondo_card_abierta, fondo_icono_abierto: Fondos
            para los diferentes estados.
        borde_card, borde_hover, borde_abierto: Bordes para los
            diferentes estados.
        color_texto, color_texto_secundario, color_texto_cuerpo:
            Colores de texto.
        con_blur: Si `True`, aplica `backdrop_filter`.
        tamano_texto_pregunta: Tamaño de la pregunta.
        tamano_texto_respuesta: Tamaño de la respuesta.
        padding_cabecera: Padding de la cabecera.
        padding_respuesta: Padding de la respuesta (con sangría).

    Returns:
        Item de acordeón clicable y colapsable.
    """
    esta_abierta = EstadoAcordeonFaq.indice_abierto == indice

    # --- Icono lateral (opcional) ---
    # Se renderiza siempre, pero se oculta con `display="none"` si
    # `icono` es cadena vacía. Esto evita `rx.cond` con `rx.fragment`.
    tiene_icono = icono != ""

    icono_componente = rx.box(
        rx.icon(
            icono if tiene_icono else "circle",
            size=16,
            color=rx.cond(
                esta_abierta,
                color_acento,
                color_texto_secundario,
            ),
        ),
        padding="0.5rem",
        border_radius=RADIO_MEDIO,
        background=rx.cond(
            esta_abierta,
            fondo_icono_abierto,
            COLOR_FONDO_SUAVE,
        ),
        display="none" if not tiene_icono else "flex",
        align_items="center",
        justify_content="center",
        flex_shrink="0",
        transition="all 0.2s",
    )

    # --- Padding de la respuesta ---
    # Si hay icono, la respuesta respeta la sangría del texto.
    # Si no, usa un padding uniforme.
    padding_respuesta_final = (
        padding_respuesta if tiene_icono else "0 1.25rem 1.25rem 1.25rem"
    )

    return rx.box(
        # ==========================================================
        # Cabecera clicable
        # ==========================================================
        rx.box(
            rx.flex(
                icono_componente,
                rx.text(
                    item["pregunta"],
                    font_size=tamano_texto_pregunta,
                    font_weight="700",
                    color=color_texto,
                    flex="1",
                    line_height="1.4",
                ),
                rx.icon(
                    "chevron-down",
                    size=20,
                    color=rx.cond(
                        esta_abierta,
                        color_acento,
                        color_texto_secundario,
                    ),
                    transform=rx.cond(
                        esta_abierta,
                        "rotate(180deg)",
                        "rotate(0deg)",
                    ),
                    transition=(
                        "transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), "
                        "color 0.2s"
                    ),
                    flex_shrink="0",
                ),
                align="center",
                gap="0.75rem",
                width="100%",
            ),
            on_click=lambda: EstadoAcordeonFaq.alternar(indice),
            cursor="pointer",
            padding=padding_cabecera,
            role="button",
            tab_index=0,
            width="100%",
        ),
        # ==========================================================
        # Respuesta colapsable
        # ==========================================================
        rx.cond(
            esta_abierta,
            rx.box(
                rx.text(
                    item["respuesta"],
                    font_size=tamano_texto_respuesta,
                    line_height="1.7",
                    color=color_texto_cuerpo,
                ),
                padding=padding_respuesta_final,
            ),
            rx.fragment(),
        ),
        # ==========================================================
        # Estilos base
        # ==========================================================
        width="100%",
        border=rx.cond(
            esta_abierta,
            f"1px solid {borde_abierto}",
            f"1px solid {borde_card}",
        ),
        border_radius=radio_item,
        background=rx.cond(
            esta_abierta,
            fondo_card_abierta,
            fondo_card,
        ),
        backdrop_filter="blur(12px)" if con_blur else "none",
        transition="all 0.2s",
        overflow="hidden",
        _hover={
            "border_color": rx.cond(
                esta_abierta,
                borde_abierto,
                borde_hover,
            ),
        },
    )


# ======================================================================
# Acordeón completo
# ======================================================================


def acordeon_faq(
    items: list[ItemFaq] | rx.Var,
    *,
    variante: str = "light",
    icono: str = "help-circle",
    color_acento: str | rx.Var = AZUL_MARINO_NEON,
    radio_item: str = RADIO_MEDIO,
    tamano_texto_pregunta: str = "0.9375rem",
    tamano_texto_respuesta: str = "0.875rem",
    padding_cabecera: str = "1.125rem 1.25rem",
    padding_respuesta: str = "0 1.25rem 1.25rem 3.5rem",
    max_width: str | None = None,
) -> rx.Component:
    """
    Acordeón de preguntas frecuentes reutilizable.

    Args:
        items: Lista estática (`list[ItemFaq]`) O `Var` reactiva que
            apunta a una lista de dicts con `pregunta` y `respuesta`.
        variante: `"light"` (por defecto) o `"neon"`.
        icono: Nombre del icono Lucide a la izquierda. Pasa `""`
            para ocultarlo.
        color_acento: Color del acento (hex o Var).
        radio_item: Border-radius de cada item.
        tamano_texto_pregunta: Tamaño de la pregunta.
        tamano_texto_respuesta: Tamaño de la respuesta.
        padding_cabecera: Padding de la cabecera.
        padding_respuesta: Padding de la respuesta (con sangría).
        max_width: Ancho máximo del contenedor. `None` = 100% del padre.

    Returns:
        Componente `rx.vstack` con la lista de preguntas en acordeón.

    Raises:
        ValueError: Si la `variante` no es `"light"` ni `"neon"`.

    Examples:
        Estático:
            acordeon_faq(
                items=[
                    {"pregunta": "¿...?", "respuesta": "..."},
                    {"pregunta": "¿...?", "respuesta": "..."},
                ],
                variante="neon",
                icono="circle-help",
            )

        Reactivo:
            acordeon_faq(
                items=EstadoInstitucional.carrera_seleccionada[
                    "preguntas_frecuentes"
                ],
                variante="light",
                icono="circle-help",
            )
    """
    config = _config_variante(variante)

    props_estilo: dict = {
        "icono": icono,
        "color_acento": color_acento,
        "radio_item": radio_item,
        "fondo_card": config["fondo_card"],
        "fondo_card_abierta": config["fondo_card_abierta"],
        "fondo_icono_abierto": config["fondo_icono_abierto"],
        "borde_card": config["borde_card"],
        "borde_hover": config["borde_hover"],
        "borde_abierto": config["borde_abierto"],
        "color_texto": config["color_texto"],
        "color_texto_secundario": config["color_texto_secundario"],
        "color_texto_cuerpo": config["color_texto_cuerpo"],
        "con_blur": config["con_blur"],
        "tamano_texto_pregunta": tamano_texto_pregunta,
        "tamano_texto_respuesta": tamano_texto_respuesta,
        "padding_cabecera": padding_cabecera,
        "padding_respuesta": padding_respuesta,
    }

    contenedor = rx.vstack(
        rx.foreach(
            items,
            lambda item, idx: _item_acordeon(item, idx, **props_estilo),
        ),
        spacing="3",
        width="100%",
    )

    if max_width is not None:
        return rx.box(
            contenedor,
            width="100%",
            max_width=max_width,
            margin="0 auto",
        )

    return contenedor


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "ItemFaq",
    "acordeon_faq",
]