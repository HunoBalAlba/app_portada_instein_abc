"""
Componentes primitivos reutilizables en toda la aplicación.

Agrupa los bloques de construcción base que se repiten en múltiples
vistas:

- `contenedor_clicable`: caja con semántica de botón (eventos internos).
- `enlace_navegacion`:  enlace estilizado para navegación SPA/externa.
- `tarjeta_estilizada`: tarjeta con estilo institucional estándar.
- `tarjeta_dato`:       tarjeta compacta con icono + etiqueta + valor.

Filosofía
---------
Todos los componentes de este módulo:

1. Aplican defaults sensatos con `setdefault` (permiten override sin
   duplicar kwargs).
2. Usan tokens de `infraestructura/constantes/` para consistencia
   visual.
3. Documentan exhaustivamente sus props y defaults.
4. Respetan accesibilidad (WCAG 2.1 AA) cuando aplica.

Nota técnica: `setdefault` vs `**kwargs`
----------------------------------------
Cada helper aplica `propiedades.setdefault("clave", valor)` para
valores por defecto. Esto permite al llamador SOBRESCRIBIR cualquier
default sin duplicar kwargs:

    tarjeta_estilizada(padding="2rem")   # ✅ override funciona
    tarjeta_estilizada()                 # ✅ usa default 1.25rem

Nota técnica: `contenedor_clicable` vs `enlace_navegacion`
----------------------------------------------------------
Usar el correcto según el caso:

- **Eventos internos** (abrir diálogo, cambiar estado) → `contenedor_clicable`
  Renderiza un `<div role="button">` con `tabindex` y `on_click`.

- **Navegación** (ir a otra ruta, abrir URL externa) → `enlace_navegacion`
  Renderiza un `<a href>` correcto para SEO y accesibilidad.

Nunca uses `contenedor_clicable` para navegar: rompe la semántica HTML
y el botón "atrás" del navegador.
"""

from __future__ import annotations

from typing import Any

import reflex as rx

from ...infraestructura.constantes.colores import (
    BORDE_PREDETERMINADO,
    COLOR_BORDE_SUAVE,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_SECUNDARIO,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_BORDE,
    RADIO_MEDIO,
    SOMBRA_CAJA,
)


# ======================================================================
# Constantes locales
# ======================================================================

PADDING_TARJETA: str = "1.25rem"
"""Padding por defecto de `tarjeta_estilizada`."""

PADDING_TARJETA_DATO: str = "1rem"
"""Padding por defecto de `tarjeta_dato`."""

GAP_ICONO_CONTENIDO: str = "0.75rem"
"""Espaciado entre icono y contenido en `tarjeta_dato`."""

TAMANO_ICONO_TARJETA: int = 18
"""Tamaño del icono de `tarjeta_dato` (px)."""


# ======================================================================
# Contenedor clicable (semántica de botón)
# ======================================================================


def contenedor_clicable(
    *hijos: rx.Component,
    al_hacer_clic: Any = None,
    **propiedades: Any,
) -> rx.Component:
    """
    Contenedor con semántica de botón para eventos internos.

    Aplica por defecto:
    - `cursor="pointer"`
    - `role="button"`
    - `tab_index=0` (navegable por teclado)

    ⚠️ Solo para eventos internos (abrir diálogo, cambiar estado).
    Para NAVEGAR usa `enlace_navegacion` (genera un `<a>` real).

    Args:
        *hijos: Elementos hijos del contenedor.
        al_hacer_clic: Evento a disparar en click. Puede ser un evento
            de Reflex (`EstadoX.handler`) o un `lambda`.
        **propiedades: Props adicionales de Reflex que sobrescriben
            los defaults (padding, background, etc.).

    Returns:
        `rx.box` con semántica de botón.

    Examples:
        Botón simple:
            contenedor_clicable(
                rx.icon("x", size=16),
                al_hacer_clic=Estado.cerrar,
                padding="0.5rem",
            )

        Botón como card:
            contenedor_clicable(
                rx.text("Contenido"),
                al_hacer_clic=Estado.abrir,
                padding="1rem",
                border_radius=RADIO_MEDIO,
                _hover={"background": COLOR_FONDO_SUAVE},
            )
    """
    propiedades.setdefault("cursor", "pointer")
    propiedades.setdefault("role", "button")
    propiedades.setdefault("tab_index", 0)

    return rx.box(
        *hijos,
        on_click=al_hacer_clic,
        **propiedades,
    )


# ======================================================================
# Enlace de navegación
# ======================================================================


def enlace_navegacion(
    destino: str,
    *hijos: rx.Component,
    externo: bool = False,
    **propiedades: Any,
) -> rx.Component:
    """
    Enlace de navegación entre páginas (SPA) o a URLs externas.

    Aplica por defecto:
    - `text_decoration="none"`
    - `cursor="pointer"`
    - `is_external=externo` (abre en nueva pestaña si es externo)

    Args:
        destino: URL de destino (ej: `/carreras`, `/carrera/0`,
            `https://wa.me/59171282993`).
        *hijos: Contenido visible del enlace.
        externo: Si `True`, abre en una nueva pestaña. Detecta
            automáticamente URLs `http(s)://` como externas si no se
            especifica explícitamente.
        **propiedades: Props adicionales de Reflex que sobrescriben
            los defaults.

    Returns:
        `rx.link` con semántica HTML de ancla.

    Examples:
        Navegación interna:
            enlace_navegacion(
                "/carreras",
                rx.text("Ver carreras"),
                padding="0.5rem 1rem",
            )

        URL externa (se abre en nueva pestaña):
            enlace_navegacion(
                WHATSAPP_URL,
                rx.icon("message-circle", size=16),
                rx.text("WhatsApp"),
                externo=True,
            )

        URL externa (detección automática):
            enlace_navegacion(
                "https://google.com",
                rx.text("Google"),
                # externo=True se infiere automáticamente
            )
    """
    propiedades.setdefault("text_decoration", "none")
    propiedades.setdefault("cursor", "pointer")

    # Detección automática de URL externa si no se especificó.
    es_externo = externo or destino.startswith(("http://", "https://"))
    propiedades.setdefault("is_external", es_externo)

    return rx.link(
        *hijos,
        href=destino,
        **propiedades,
    )


# ======================================================================
# Tarjeta estilizada
# ======================================================================


def tarjeta_estilizada(
    *hijos: rx.Component,
    **propiedades: Any,
) -> rx.Component:
    """
    Tarjeta con estilo institucional estándar.

    Defaults aplicados (sobrescribibles vía `**propiedades`):
    - `padding="1.25rem"`
    - `border_radius=RADIO_BORDE`
    - `border=BORDE_PREDETERMINADO` (gris suave)
    - `background=COLOR_FONDO_CARTA` (adaptativo)
    - `box_shadow=SOMBRA_CAJA`

    Args:
        *hijos: Contenido de la tarjeta.
        **propiedades: Props adicionales de Reflex.

    Returns:
        `rx.box` con estilo de tarjeta institucional.

    Examples:
        Tarjeta por defecto:
            tarjeta_estilizada(
                rx.heading("Título", size="4"),
                rx.text("Contenido"),
            )

        Tarjeta con override:
            tarjeta_estilizada(
                rx.text("Contenido"),
                padding="2rem",
                background=COLOR_ACENTO_FONDO,
            )
    """
    propiedades.setdefault("padding", PADDING_TARJETA)
    propiedades.setdefault("border_radius", RADIO_BORDE)
    propiedades.setdefault("border", BORDE_PREDETERMINADO)
    propiedades.setdefault("background", COLOR_FONDO_CARTA)
    propiedades.setdefault("box_shadow", SOMBRA_CAJA)

    return rx.box(*hijos, **propiedades)


# ======================================================================
# Tarjeta de dato (KPI compacto)
# ======================================================================


def tarjeta_dato(
    icono: str,
    etiqueta: str,
    valor: str,
    *,
    color_icono: Any = None,
    color_fondo_icono: Any = None,
    color_hover: Any = None,
) -> rx.Component:
    """
    Tarjeta compacta con icono + etiqueta + valor.

    Usada en vistas de detalle para mostrar datos rápidos
    (duración, modalidad, cupos, etc.).

    Estructura visual:
        ┌─────────────────────────────┐
        │ [icono]  ETIQUETA           │
        │          Valor destacado    │
        └─────────────────────────────┘

    Args:
        icono: Nombre del icono Lucide (kebab-case).
        etiqueta: Texto de la etiqueta (ej: "DURACIÓN").
        valor: Valor a mostrar (ej: "3 Años").
        color_icono: Color del icono. Acepta `str` (hex) o `Var`.
            Por defecto: `COLOR_TEXTO_SECUNDARIO`.
        color_fondo_icono: Fondo del icono. Acepta `str` o `Var`.
            Por defecto: `COLOR_FONDO_SUAVE`.
        color_hover: Color del hover (borde + sombra). Acepta `str`
            o `Var`. Por defecto: igual que `color_icono`.

    Returns:
        `rx.card` con la estructura completa.

    Examples:
        Tarjeta neutra (defaults):
            tarjeta_dato(
                icono="clock",
                etiqueta="DURACIÓN",
                valor="3 Años",
            )

        Tarjeta con acento de color:
            tarjeta_dato(
                icono="award",
                etiqueta="TÍTULO",
                valor="Técnico Superior",
                color_icono=AZUL_MARINO_NEON,
                color_fondo_icono=FONDO_AZUL_SUAVE,
            )
    """
    # --- Resolución de defaults ---
    color_icono_final = (
        color_icono if color_icono is not None else COLOR_TEXTO_SECUNDARIO
    )
    color_fondo_final = (
        color_fondo_icono
        if color_fondo_icono is not None
        else COLOR_FONDO_SUAVE
    )
    color_hover_final = (
        color_hover if color_hover is not None else color_icono_final
    )

    # --- Estilo del hover ---
    # El box_shadow usa interpolación de Var compatible con Reflex
    # vía rx.cond, NO f-string (evita que el Var se serialice mal).
    estilo_hover: dict = {
        "border_color": color_hover_final,
        "transform": "translateY(-2px)",
        "box_shadow": rx.cond(
            rx.Var.create(color_hover_final) != None,  # noqa: E711
            f"0 8px 20px -8px {color_hover_final}",
            "0 8px 20px -8px rgba(0, 0, 0, 0.15)",
        ),
    }

    return rx.card(
        rx.flex(
            # ==========================================================
            # Icono en caja tintada
            # ==========================================================
            rx.box(
                rx.icon(
                    icono,
                    size=TAMANO_ICONO_TARJETA,
                    color=color_icono_final,
                ),
                padding="0.5rem",
                border_radius=RADIO_MEDIO,
                background=color_fondo_final,
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            # ==========================================================
            # Etiqueta + Valor
            # ==========================================================
            rx.vstack(
                rx.text(
                    etiqueta,
                    font_size="0.6875rem",
                    font_weight="700",
                    color=COLOR_TEXTO_SECUNDARIO,
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                    line_height="1.1",
                ),
                rx.text(
                    valor,
                    font_size="0.9375rem",
                    font_weight="700",
                    color=COLOR_TEXTO_CUERPO,
                    line_height="1.3",
                ),
                spacing="1",
                align="start",
                flex="1",
                min_width="0",
            ),
            align="start",
            gap=GAP_ICONO_CONTENIDO,
            width="100%",
        ),
        width="100%",
        padding=PADDING_TARJETA_DATO,
        transition="all 0.2s",
        _hover=estilo_hover,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "contenedor_clicable",
    "enlace_navegacion",
    "tarjeta_dato",
    "tarjeta_estilizada",
]