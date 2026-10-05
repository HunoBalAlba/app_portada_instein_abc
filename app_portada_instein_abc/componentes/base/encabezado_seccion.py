# componentes/base/encabezado_seccion.py

"""
Encabezado de sección con número (estilo Neon.com).

Compatible con Reflex 0.5+ y 0.6+.

Diseño
------
Estructura visual (fiel a Neon.com):

    ┌──────────────────────────────────────────────────┐
    │  ▶ ETIQUETA              Título grande           │
    │                          con mezcla de pesos     │
    │  01                      (blanco + gris)         │
    │                          Subtítulo descriptivo   │
    └──────────────────────────────────────────────────┘

Diferencias con la v1.0:
------------------------
1. **Icono en la etiqueta** (`▶ ETIQUETA`) — distintivo de Neon.
2. **Número más grande y sutil** (`font_size` hasta 10rem,
   `opacity="0.12"`).
3. **Peso tipográfico reducido** (`700` en lugar de `900`).
4. **Nuevo parámetro `titulo_enfasis`** que permite pintar la
   segunda mitad del título en gris (patrón Neon).
5. **Orden etiqueta/número invertido** para replicar el layout
   de Neon.com (etiqueta arriba, número abajo).

Uso
---
Básico:
    encabezado_seccion(
        numero="01",
        etiqueta="Nuestra historia",
        titulo="15 años formando profesionales",
    )

Con énfasis (título bicolor):
    encabezado_seccion(
        numero="01",
        etiqueta="Nuestra historia",
        titulo="15 años",
        titulo_enfasis="formando profesionales",
    )
    → Renderiza: "15 años" en blanco + "formando profesionales" en gris.
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

TAMANO_NUMERO_DEFECTO: list[str] = ["4rem", "6rem", "8rem"]
"""Tamaños responsive por defecto del número de sección."""

TAMANO_TITULO_DEFECTO: list[str] = ["1.75rem", "2.25rem", "2.75rem"]
"""Tamaños responsive por defecto del título."""

PESO_TITULO_DEFECTO: str = "700"
"""Peso tipográfico del título (Neon usa 500-700, no 900)."""

OPACIDAD_NUMERO: str = "0.12"
"""Opacidad del número de sección (muy sutil, como Neon)."""

ICONO_ETIQUETA_DEFECTO: str = "play"
"""Icono por defecto a la izquierda de la etiqueta."""


# ======================================================================
# Sub-componente: etiqueta con icono
# ======================================================================


def _etiqueta_con_icono(
    etiqueta: str,
    icono: str | None,
) -> rx.Component:
    """
    Etiqueta de sección con icono opcional a la izquierda.

    Estructura:
        ▶ ETIQUETA EN MAYÚSCULAS

    Si `icono=None`, se renderiza solo el texto (útil para
    secciones que no quieren el prefijo decorativo).
    """
    if icono is None:
        return rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            letter_spacing="0.15em",
            text_transform="uppercase",
            white_space="nowrap",
        )

    return rx.flex(
        rx.icon(
            icono,
            size=10,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
        ),
        rx.text(
            etiqueta,
            font_size="0.6875rem",
            font_weight="700",
            color=AZUL_MARINO_NEON,
            letter_spacing="0.15em",
            text_transform="uppercase",
            white_space="nowrap",
        ),
        align="center",
        gap="0.5rem",
        width="fit-content",
    )


# ======================================================================
# Sub-componente: título con mezcla de pesos
# ======================================================================


def _titulo_con_enfasis(
    titulo: str,
    titulo_enfasis: str | None,
    tamano: list[str],
    peso: str,
) -> rx.Component:
    """
    Título con mezcla de pesos (patrón Neon.com).

    Si `titulo_enfasis` es None → todo el título en blanco.
    Si `titulo_enfasis` tiene valor → la primera parte en blanco
    y la segunda en gris, en la misma línea.

    Ejemplo:
        titulo="15 años"
        titulo_enfasis="formando profesionales"
        → "15 años" (blanco) + "formando profesionales" (gris)
    """
    if titulo_enfasis is None:
        return rx.heading(
            titulo,
            as_="h2",
            font_size=tamano,
            font_weight=peso,
            color=TEXTO_HOME_PRINCIPAL,
            letter_spacing="-0.03em",
            line_height="1.15",
            max_width="52rem",
        )

    return rx.heading(
        rx.text.span(
            titulo,
            color=TEXTO_HOME_PRINCIPAL,
        ),
        " ",
        rx.text.span(
            titulo_enfasis,
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        as_="h2",
        font_size=tamano,
        font_weight=peso,
        letter_spacing="-0.03em",
        line_height="1.15",
        max_width="52rem",
    )


# ======================================================================
# Componente principal
# ======================================================================


def encabezado_seccion(
    numero: str,
    etiqueta: str,
    titulo: str,
    subtitulo: str | None = None,
    titulo_enfasis: str | None = None,
    icono_etiqueta: str | None = ICONO_ETIQUETA_DEFECTO,
    tamano_numero: list[str] | None = None,
    tamano_titulo: list[str] | None = None,
    peso_titulo: str = PESO_TITULO_DEFECTO,
) -> rx.Component:
    """
    Encabezado de sección con número (estilo Neon.com).

    Args:
        numero: "01", "02", "03"...
        etiqueta: Texto pequeño en mayúsculas.
        titulo: Título grande (h2). Puede ser la primera parte
            si se usa `titulo_enfasis`.
        subtitulo: Texto descriptivo opcional.
        titulo_enfasis: Segunda parte del título (se pinta en gris).
            Si se especifica, `titulo` es la parte blanca y
            `titulo_enfasis` la parte gris.
        icono_etiqueta: Icono Lucide a la izquierda de la etiqueta.
            `None` para ocultarlo. Por defecto `"play"` (▶).
        tamano_numero: Tamaños responsive del número.
        tamano_titulo: Tamaños responsive del título.
        peso_titulo: Peso tipográfico del título (default `"700"`).

    Returns:
        Fila con número + etiqueta (izq) y título + subtítulo (der).

    Examples:
        Sin énfasis:
            encabezado_seccion(
                numero="01",
                etiqueta="Nuestra historia",
                titulo="15 años formando profesionales",
            )

        Con énfasis (título bicolor estilo Neon):
            encabezado_seccion(
                numero="01",
                etiqueta="Nuestra historia",
                titulo="15 años",
                titulo_enfasis="formando profesionales",
            )

        Sin icono en la etiqueta:
            encabezado_seccion(
                numero="01",
                etiqueta="Nuestra historia",
                titulo="15 años formando profesionales",
                icono_etiqueta=None,
            )
    """
    return rx.flex(
        # ══════════════════════════════════════════════════════
        # Columna izquierda: etiqueta + número
        # (etiqueta ARRIBA, número ABAJO — orden Neon.com)
        # ══════════════════════════════════════════════════════
        rx.vstack(
            _etiqueta_con_icono(etiqueta, icono_etiqueta),
            rx.text(
                numero,
                font_size=tamano_numero or TAMANO_NUMERO_DEFECTO,
                font_weight="900",
                color=AZUL_MARINO_NEON,
                line_height="1",
                letter_spacing="-0.05em",
                font_family="JetBrains Mono",
                opacity=OPACIDAD_NUMERO,
                aria_hidden="true",
            ),
            spacing="3",
            align="start",
            flex_shrink="0",
            min_width=["3.5rem", "4.5rem", "5.5rem"],
        ),
        # ══════════════════════════════════════════════════════
        # Columna derecha: título + subtítulo
        # ══════════════════════════════════════════════════════
        rx.vstack(
            _titulo_con_enfasis(
                titulo=titulo,
                titulo_enfasis=titulo_enfasis,
                tamano=tamano_titulo or TAMANO_TITULO_DEFECTO,
                peso=peso_titulo,
            ),
            rx.cond(
                subtitulo is not None,
                rx.text(
                    subtitulo,
                    font_size=["1rem", "1.125rem"],
                    color=TEXTO_HOME_MAS_SUAVE,
                    line_height="1.6",
                    max_width="48rem",
                    margin_top="1rem",
                ),
                rx.fragment(),
            ),
            spacing="0",
            align="start",
            flex="1",
            min_width="0",
        ),
        # ══════════════════════════════════════════════════════
        # Layout responsive
        # ══════════════════════════════════════════════════════
        direction=rx.breakpoints(initial="column", md="row"),
        align="start",
        justify="start",
        gap=["2rem", "3rem"],
        width="100%",
        margin_bottom="4rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["encabezado_seccion"]