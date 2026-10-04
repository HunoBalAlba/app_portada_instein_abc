"""
Badges reutilizables — componentes únicos para toda la app.

Reemplaza las 7 implementaciones duplicadas que existían en:
- `componentes/carreras/tarjetas_carrera.py`  → `_badges_demanda()`
- `componentes/carreras/secciones_detalle.py` → `_badge_contador()`
- `paginas/carreras.py`                        → badge inline
- `componentes/blog/helpers_categoria.py`     → `_badge_ui()`
- `componentes/calendario/tabs_instituto.py`  → `_badge_tipo_evento()`
- `componentes/calendario/tabs_fechas.py`     → `_badge_tipo_fecha()`
- Varios módulos                              → badges inline

Ventajas de unificar
--------------------
- 1 sola implementación → 1 sola corrección de bugs.
- Estilos consistentes en toda la app.
- Personalizable por props (color, tamaño, icono, mayúsculas, etc.).
- Auto-adaptativo al `color_mode` cuando se usan tokens Radix.

Variantes disponibles
---------------------
1. **`badge_icono_texto`** — Badge con icono opcional a la izquierda.
   Uso: categorías, tipos, estados.

2. **`badge_solido`** — Badge con fondo sólido (contraste alto).
   Uso: badges de marca ("TÉCNICO SUPERIOR", "DESTACADO").

3. **`badge_contador`** — Badge minimalista de contador numérico.
   Uso: contadores de items ("5 habilidades", "8 resultados").

4. **`badge_estado`** — Badge semántico (éxito/warning/error/info).
   Uso: disponibilidad, estado del sistema.

Nota técnica: ESCALA RADIX
--------------------------
Los badges siguen la convención Radix:
- `step 3`  → fondo suave (chips)
- `step 7`  → borde
- `step 11` → texto de alto contraste sobre fondo suave

Cuando usas `color_scheme="blue"`, el badge renderiza:
- fondo:   `rx.color("blue", 3)`
- borde:   `rx.color("blue", 7)`
- texto:   `rx.color("blue", 11)`
- icono:   `rx.color("blue", 11)`

Todos adaptativos automáticamente al `color_mode`.

Nota técnica: COLORES PERSONALIZADOS (HEX O VAR)
------------------------------------------------
Además de `color_scheme` (paleta Radix), puedes pasar colores
personalizados con hex o Vars adaptativos:

    badge_icono_texto(
        icono="star",
        texto="Destacado",
        color_fondo="#fef3c7",
        color_borde="#f59e0b",
        color_texto="#92400e",
    )

    # O con Vars adaptativos
    badge_icono_texto(
        icono="check",
        texto="Activo",
        color_fondo=FONDO_AZUL_SUAVE,
        color_borde=BORDE_HOME_AZUL,
        color_texto=AZUL_MARINO_NEON,
    )

Los parámetros `color_fondo`, `color_borde`, `color_texto` y
`color_icono` son MUTUAMENTE EXCLUYENTES con `color_scheme`. Si
pasas ambos, los colores explícitos tienen prioridad.
"""

from __future__ import annotations

from typing import Any

import reflex as rx

from ...infraestructura.constantes.colores import (
    COLOR_ALERTA_FONDO,
    COLOR_ALERTA_TEXTO,
    COLOR_ERROR_FONDO,
    COLOR_ERROR_TEXTO,
    COLOR_EXITO_FONDO,
    COLOR_EXITO_TEXTO,
    COLOR_TEXTO_SECUNDARIO,
)
from ...infraestructura.constantes.dimensiones import (
    RADIO_PASTILLA,
)


# ======================================================================
# Constantes locales
# ======================================================================

TAMANO_ICONO_PEQUENO: int = 12
"""Tamaño del icono para badges pequeños."""

TAMANO_ICONO_MEDIO: int = 14
"""Tamaño del icono para badges medianos."""

TAMANO_ICONO_GRANDE: int = 16
"""Tamaño del icono para badges grandes."""

TAMANOS_VALIDOS: frozenset[str] = frozenset({"sm", "md", "lg"})
"""Tamaños válidos de badge."""

ESTADOS_VALIDOS: frozenset[str] = frozenset({
    "exito", "success",
    "alerta", "warning",
    "error",
    "info",
})
"""Estados semánticos válidos."""


# ======================================================================
# Helpers internos
# ======================================================================


def _resolver_tamano(tamano: str) -> dict:
    """
    Resuelve tamaños de fuente, padding e icono según el tamaño del badge.

    Args:
        tamano: `"sm"`, `"md"` o `"lg"`.

    Returns:
        Dict con `font_size`, `padding`, `tamano_icono`.

    Raises:
        ValueError: Si el tamaño no está en `TAMANOS_VALIDOS`.
    """
    if tamano == "sm":
        return {
            "font_size": "0.625rem",
            "padding": "0.25rem 0.625rem",
            "tamano_icono": TAMANO_ICONO_PEQUENO,
            "gap": "0.25rem",
        }
    if tamano == "md":
        return {
            "font_size": "0.6875rem",
            "padding": "0.25rem 0.625rem",
            "tamano_icono": TAMANO_ICONO_MEDIO,
            "gap": "0.375rem",
        }
    if tamano == "lg":
        return {
            "font_size": "0.75rem",
            "padding": "0.375rem 0.75rem",
            "tamano_icono": TAMANO_ICONO_GRANDE,
            "gap": "0.5rem",
        }

    raise ValueError(
        f"Tamaño no válido: {tamano!r}. "
        f"Usa uno de: {sorted(TAMANOS_VALIDOS)}"
    )


def _resolver_colores(
    color_scheme: str | None,
    color_fondo: Any,
    color_borde: Any,
    color_texto: Any,
    color_icono: Any,
) -> dict:
    """
    Resuelve los colores del badge (Radix vs personalizados).

    Prioridad:
    1. Colores explícitos (`color_fondo`, `color_borde`, etc.) si no son None.
    2. Colores de `color_scheme` (paleta Radix).
    3. Fallback a gris neutro.

    Args:
        color_scheme: Nombre del scheme Radix (`"blue"`, `"green"`, etc.).
        color_fondo, color_borde, color_texto, color_icono: Colores
            personalizados. Pueden ser `str` (hex) o `Var`.

    Returns:
        Dict con `fondo`, `borde`, `texto`, `icono` resueltos.
    """
    scheme = color_scheme or "gray"

    return {
        "fondo": (
            color_fondo
            if color_fondo is not None
            else rx.color(scheme, 3)
        ),
        "borde": (
            color_borde
            if color_borde is not None
            else rx.color(scheme, 7)
        ),
        "texto": (
            color_texto
            if color_texto is not None
            else rx.color(scheme, 11)
        ),
        "icono": (
            color_icono
            if color_icono is not None
            else rx.color(scheme, 11)
        ),
    }


def _resolver_colores_estado(estado: str) -> dict:
    """
    Resuelve los colores semánticos según el estado.

    Args:
        estado: `"exito"`, `"alerta"`, `"error"` o `"info"`.

    Returns:
        Dict con `fondo`, `texto` resueltos.

    Raises:
        ValueError: Si el estado no está en `ESTADOS_VALIDOS`.
    """
    if estado in ("exito", "success"):
        return {
            "fondo": COLOR_EXITO_FONDO,
            "texto": COLOR_EXITO_TEXTO,
        }
    if estado in ("alerta", "warning"):
        return {
            "fondo": COLOR_ALERTA_FONDO,
            "texto": COLOR_ALERTA_TEXTO,
        }
    if estado == "error":
        return {
            "fondo": COLOR_ERROR_FONDO,
            "texto": COLOR_ERROR_TEXTO,
        }
    if estado == "info":
        return {
            "fondo": rx.color("blue", 3),
            "texto": rx.color("blue", 11),
        }

    raise ValueError(
        f"Estado no válido: {estado!r}. "
        f"Usa uno de: {sorted(ESTADOS_VALIDOS)}"
    )


# ======================================================================
# 1. Badge con icono + texto (más versátil)
# ======================================================================


def badge_icono_texto(
    texto: str,
    *,
    icono: str | None = None,
    color_scheme: str | None = None,
    color_fondo: Any = None,
    color_borde: Any = None,
    color_texto: Any = None,
    color_icono: Any = None,
    tamano: str = "md",
    mayusculas: bool = True,
    letter_spacing: str = "0.05em",
    radio: str = RADIO_PASTILLA,
    **propiedades: Any,
) -> rx.Component:
    """
    Badge con icono opcional + texto.

    Es el badge más versátil: se adapta a casi cualquier caso de uso
    (categorías, tipos, estados, etiquetas).

    Args:
        texto: Texto visible del badge.
        icono: Nombre del icono Lucide (kebab-case). `None` para omitir.
        color_scheme: Nombre del scheme Radix (ej: `"blue"`, `"green"`,
            `"amber"`, `"red"`, `"violet"`, `"crimson"`). Si se omite,
            usa `"gray"`.
        color_fondo: Color del fondo. Acepta `str` (hex) o `Var`.
            Sobrescribe `color_scheme`.
        color_borde: Color del borde. Acepta `str` o `Var`.
        color_texto: Color del texto. Acepta `str` o `Var`.
        color_icono: Color del icono. Acepta `str` o `Var`.
        tamano: `"sm"` (0.625rem), `"md"` (0.6875rem) o `"lg"` (0.75rem).
        mayusculas: Si `True`, el texto se renderiza en mayúsculas.
        letter_spacing: Espaciado entre letras.
        radio: Border-radius (por defecto: pastilla).
        **propiedades: Props adicionales de Reflex.

    Returns:
        Componente de badge con icono + texto.

    Raises:
        ValueError: Si `tamano` no es válido.

    Examples:
        Badge de demanda laboral:
            badge_icono_texto(
                "Demanda alta",
                icono="trending-up",
                color_scheme="green",
            )

        Badge de categoría del blog:
            badge_icono_texto(
                "Tecnología",
                icono="cpu",
                color_scheme="blue",
            )

        Badge de marca (hex fijo):
            badge_icono_texto(
                "TÉCNICO SUPERIOR",
                icono="award",
                color_fondo=AZUL_MARINO_NEON,
                color_borde=AZUL_MARINO_NEON,
                color_texto="white",
                color_icono="white",
                tamano="sm",
            )

        Badge sin icono:
            badge_icono_texto(
                "Nuevo",
                color_scheme="violet",
            )
    """
    dims = _resolver_tamano(tamano)
    colores = _resolver_colores(
        color_scheme,
        color_fondo,
        color_borde,
        color_texto,
        color_icono,
    )

    hijos: list[rx.Component] = []

    if icono is not None:
        hijos.append(
            rx.icon(
                icono,
                size=dims["tamano_icono"],
                color=colores["icono"],
            )
        )

    hijos.append(
        rx.text(
            texto,
            font_size=dims["font_size"],
            font_weight="700",
            color=colores["texto"],
            text_transform="uppercase" if mayusculas else "none",
            letter_spacing=letter_spacing if mayusculas else "normal",
            white_space="nowrap",
            line_height="1.2",
        )
    )

    propiedades.setdefault("align", "center")
    propiedades.setdefault("gap", dims["gap"])
    propiedades.setdefault("padding", dims["padding"])
    propiedades.setdefault("border_radius", radio)
    propiedades.setdefault("background", colores["fondo"])
    propiedades.setdefault("border", f"1px solid {colores['borde']}")
    propiedades.setdefault("width", "fit-content")
    propiedades.setdefault("display", "inline-flex")
    propiedades.setdefault("flex_shrink", "0")

    return rx.flex(*hijos, **propiedades)


# ======================================================================
# 2. Badge sólido (fondo de marca, contraste alto)
# ======================================================================


def badge_solido(
    texto: str,
    *,
    icono: str | None = None,
    color_fondo: Any,
    color_texto: Any = "white",
    tamano: str = "md",
    mayusculas: bool = True,
    letter_spacing: str = "0.1em",
    radio: str = RADIO_PASTILLA,
    box_shadow: Any = None,
    **propiedades: Any,
) -> rx.Component:
    """
    Badge con fondo sólido y texto claro.

    Ideal para badges de marca ("TÉCNICO SUPERIOR", "DESTACADO",
    "CARRERA DESTACADA") donde se necesita contraste máximo sobre
    cualquier fondo.

    Args:
        texto: Texto visible del badge.
        icono: Nombre del icono Lucide. `None` para omitir.
        color_fondo: Color del fondo (hex, Var o token de acento).
        color_texto: Color del texto. Por defecto `"white"`.
        tamano: `"sm"`, `"md"` o `"lg"`.
        mayusculas: Si `True`, mayúsculas (default).
        letter_spacing: Espaciado entre letras.
        radio: Border-radius.
        box_shadow: Sombra opcional (útil para glow del acento).
        **propiedades: Props adicionales.

    Returns:
        Badge con fondo sólido.

    Examples:
        Badge de marca con glow:
            badge_solido(
                "CARRERA DESTACADA",
                icono="star",
                color_fondo=AZUL_MARINO_NEON,
                box_shadow=f"0 4px 12px -2px {AZUL_MARINO_NEON}",
            )

        Badge sobre imagen:
            badge_solido(
                "DESTACADO",
                icono="star",
                color_fondo="rgba(0,0,0,0.5)",
                letter_spacing="0.15em",
            )
    """
    dims = _resolver_tamano(tamano)

    hijos: list[rx.Component] = []

    if icono is not None:
        hijos.append(
            rx.icon(
                icono,
                size=dims["tamano_icono"],
                color=color_texto,
                fill=color_texto if icono == "star" else None,
            )
        )

    hijos.append(
        rx.text(
            texto,
            font_size=dims["font_size"],
            font_weight="800",
            color=color_texto,
            text_transform="uppercase" if mayusculas else "none",
            letter_spacing=letter_spacing if mayusculas else "normal",
            white_space="nowrap",
            line_height="1.2",
        )
    )

    propiedades.setdefault("align", "center")
    propiedades.setdefault("gap", dims["gap"])
    propiedades.setdefault("padding", dims["padding"])
    propiedades.setdefault("border_radius", radio)
    propiedades.setdefault("background", color_fondo)
    propiedades.setdefault("width", "fit-content")
    propiedades.setdefault("display", "inline-flex")
    propiedades.setdefault("flex_shrink", "0")

    if box_shadow is not None:
        propiedades.setdefault("box_shadow", box_shadow)

    return rx.flex(*hijos, **propiedades)


# ======================================================================
# 3. Badge de contador (numérico minimalista)
# ======================================================================


def badge_contador(
    cantidad: str | rx.Var,
    *,
    sufijo: str = "",
    color_scheme: str | None = None,
    color_fondo: Any = None,
    color_borde: Any = None,
    color_texto: Any = None,
    tamano: str = "sm",
    **propiedades: Any,
) -> rx.Component:
    """
    Badge minimalista para contadores numéricos.

    Útil para mostrar cantidades junto a títulos de sección
    ("5 habilidades", "8 resultados", "3 materias").

    Args:
        cantidad: Cantidad a mostrar. Acepta `str` estático o `Var`
            reactiva (ej: `lista.length().to_string()`).
        sufijo: Texto opcional después del número (ej: " habilidades").
        color_scheme: Nombre del scheme Radix.
        color_fondo, color_borde, color_texto: Colores personalizados.
        tamano: `"sm"`, `"md"` o `"lg"`.
        **propiedades: Props adicionales.

    Returns:
        Badge con el contador.

    Examples:
        Contador estático:
            badge_contador("5", sufijo=" habilidades")

        Contador reactivo:
            badge_contador(
                EstadoInstitucional.habilidades.length().to_string(),
                sufijo=" habilidades",
            )

        Contador con acento de marca:
            badge_contador(
                "8",
                sufijo=" resultados",
                color_fondo=FONDO_AZUL_SUAVE,
                color_borde=BORDE_HOME_AZUL,
                color_texto=AZUL_MARINO_NEON,
            )
    """
    dims = _resolver_tamano(tamano)
    colores = _resolver_colores(
        color_scheme,
        color_fondo,
        color_borde,
        color_texto,
        color_icono=None,
    )

    texto_completo = rx.fragment(cantidad, sufijo) if sufijo else cantidad

    propiedades.setdefault("padding", dims["padding"])
    propiedades.setdefault("border_radius", RADIO_PASTILLA)
    propiedades.setdefault("background", colores["fondo"])
    propiedades.setdefault("border", f"1px solid {colores['borde']}")
    propiedades.setdefault("color", colores["texto"])
    propiedades.setdefault("font_size", dims["font_size"])
    propiedades.setdefault("font_weight", "700")
    propiedades.setdefault("letter_spacing", "0.05em")
    propiedades.setdefault("text_transform", "uppercase")
    propiedades.setdefault("white_space", "nowrap")
    propiedades.setdefault("width", "fit-content")
    propiedades.setdefault("display", "inline-flex")
    propiedades.setdefault("align_items", "center")
    propiedades.setdefault("flex_shrink", "0")

    return rx.text(texto_completo, **propiedades)


# ======================================================================
# 4. Badge de estado semántico
# ======================================================================


def badge_estado(
    texto: str,
    *,
    estado: str,
    icono: str | None = None,
    con_punto: bool = False,
    tamano: str = "md",
    **propiedades: Any,
) -> rx.Component:
    """
    Badge semántico con colores predefinidos por estado.

    Estados disponibles:
    - `"exito"` / `"success"` → verde
    - `"alerta"` / `"warning"` → ámbar
    - `"error"` → rojo
    - `"info"` → azul

    Args:
        texto: Texto visible del badge.
        estado: Estado semántico (ver `ESTADOS_VALIDOS`).
        icono: Nombre del icono Lucide. `None` para omitir.
        con_punto: Si `True`, muestra un punto pulsante en vez de icono.
            Útil para "activo", "en línea", "disponible".
        tamano: `"sm"`, `"md"` o `"lg"`.
        **propiedades: Props adicionales.

    Returns:
        Badge con colores semánticos según el estado.

    Raises:
        ValueError: Si `estado` no está en `ESTADOS_VALIDOS`.

    Examples:
        Estado de éxito con punto pulsante:
            badge_estado(
                "En línea",
                estado="exito",
                con_punto=True,
            )

        Estado de alerta con icono:
            badge_estado(
                "Pocos cupos",
                estado="alerta",
                icono="alert-triangle",
            )

        Estado de error:
            badge_estado(
                "No disponible",
                estado="error",
                icono="x-circle",
            )
    """
    dims = _resolver_tamano(tamano)
    colores = _resolver_colores_estado(estado)

    hijos: list[rx.Component] = []

    if con_punto:
        hijos.append(
            rx.box(
                height="0.375rem",
                width="0.375rem",
                border_radius=RADIO_PASTILLA,
                background=colores["texto"],
                animation="pulse 2s ease-in-out infinite",
                flex_shrink="0",
            )
        )
    elif icono is not None:
        hijos.append(
            rx.icon(
                icono,
                size=dims["tamano_icono"],
                color=colores["texto"],
            )
        )

    hijos.append(
        rx.text(
            texto,
            font_size=dims["font_size"],
            font_weight="600",
            color=colores["texto"],
            white_space="nowrap",
            line_height="1.2",
        )
    )

    propiedades.setdefault("align", "center")
    propiedades.setdefault("gap", dims["gap"])
    propiedades.setdefault("padding", dims["padding"])
    propiedades.setdefault("border_radius", RADIO_PASTILLA)
    propiedades.setdefault("background", colores["fondo"])
    propiedades.setdefault("width", "fit-content")
    propiedades.setdefault("display", "inline-flex")
    propiedades.setdefault("flex_shrink", "0")

    return rx.flex(*hijos, **propiedades)


# ======================================================================
# 5. Helper de compatibilidad: badge con color_scheme simple
# ======================================================================


def badge(
    texto: str,
    *,
    icono: str | None = None,
    color_scheme: str = "gray",
    tamano: str = "md",
    **propiedades: Any,
) -> rx.Component:
    """
    Badge simple con `color_scheme` (atajo de `badge_icono_texto`).

    Alias de conveniencia para el caso más común: badge con icono
    y un scheme de color Radix. Delega en `badge_icono_texto`.

    Args:
        texto: Texto visible.
        icono: Nombre del icono Lucide. `None` para omitir.
        color_scheme: Nombre del scheme Radix (default: `"gray"`).
        tamano: `"sm"`, `"md"` o `"lg"`.
        **propiedades: Props adicionales.

    Returns:
        Badge con icono + texto.

    Examples:
        badge("Tecnología", icono="cpu", color_scheme="blue")
        badge("Activo", color_scheme="green")
    """
    return badge_icono_texto(
        texto,
        icono=icono,
        color_scheme=color_scheme,
        tamano=tamano,
        **propiedades,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "badge",
    "badge_contador",
    "badge_estado",
    "badge_icono_texto",
    "badge_solido",
]