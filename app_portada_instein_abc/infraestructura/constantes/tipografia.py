"""
Tipografía del proyecto INSTEIN.

Este módulo es la **fuente única de verdad** para:
- Nombres de fuentes (principal y monoespaciada).
- Hojas de estilo externas (Google Fonts).
- Fallbacks tipográficos.
- Estilo base de fuentes para distintos elementos HTML.

Elección de fuentes
-------------------
- **Inter** (principal): Sans-serif moderna, optimizada para
  interfaces digitales. Usada por reflex.dev, GitHub, Linear y otras
  plataformas técnicas. Excelente legibilidad en tamaños pequeños.
- **JetBrains Mono** (monoespaciada): Diseñada específicamente para
  programadores. Ligaduras tipográficas opcionales, alta legibilidad
  en código.

Ambas fuentes se cargan desde Google Fonts con `display=swap` para
evitar flash de texto invisible (FOIT).

Uso típico
----------
Desde `configuracion/app_config.py`:

    from app_portada_instein.infraestructura.constantes.tipografia import (
        ESTILO_BASE,
        FUENTE_PRINCIPAL,
        HOJAS_DE_ESTILO_BASE,
    )

    app = rx.App(
        theme=rx.theme(font_family=FUENTE_PRINCIPAL),
        style=ESTILO_BASE,
        stylesheets=[*HOJAS_DE_ESTILO_BASE, "/styles/global.css"],
    )

Nota técnica: ¿POR QUÉ GOOGLE FONTS Y NO ARCHIVOS LOCALES?
---------------------------------------------------------
Google Fonts ofrece:
- **Cache compartido** entre sitios (el usuario ya lo tiene descargado).
- **CDN global** con baja latencia.
- **Actualizaciones automáticas** de la fuente.
- **Sin gestión manual** de archivos `.woff2`.

Si en el futuro se necesita privacidad (GDPR estricto), migrar a
fuentes autohospedadas en `/public/fonts/`.

Nota técnica: `font_feature_settings` DE INTER
----------------------------------------------
Inter ofrece "características estilísticas" (OpenType features) que
mejoran la legibilidad:

- `cv02`: `a` con doble piso (más legible).
- `cv03`: `i` con serif más pronunciado.
- `cv04`: `l` con cola curva (evita confusión con `I`).
- `cv11`: `i` sin serif (alternativa).

Estas features se aplican vía `font-feature-settings` en `ESTILO_BASE`.
"""

from __future__ import annotations


# ======================================================================
# 1. Nombres de fuentes
# ======================================================================

FUENTE_PRINCIPAL: str = "Inter"
"""Fuente sans-serif principal del proyecto.

Usada en: textos, headings, botones, inputs.
"""

FUENTE_MONOESPACIADA: str = "JetBrains Mono"
"""Fuente monoespaciada para código y datos técnicos.

Usada en: `<code>`, `<pre>`, `<kbd>`, `<samp>`.
"""


# ======================================================================
# 2. Fallbacks tipográficos
# ======================================================================

FALLBACK_SANS: str = (
    '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, '
    '"Helvetica Neue", Arial, sans-serif'
)
"""Cadena de fallback para fuentes sans-serif.

Se usa como fallback en caso de que Inter no cargue:
- `-apple-system`: San Francisco (macOS/iOS).
- `BlinkMacSystemFont`: equivalente en Chrome/Blink.
- `Segoe UI`: Windows moderno.
- `Roboto`: Android y ChromeOS.
- `Helvetica Neue`, `Arial`: universales.
- `sans-serif`: último recurso del navegador.
"""

FALLBACK_MONO: str = (
    '"JetBrains Mono", "SF Mono", Monaco, "Cascadia Code", '
    '"Roboto Mono", Consolas, "Courier New", monospace'
)
"""Cadena de fallback para fuentes monoespaciadas.

- `JetBrains Mono`: fuente principal (si carga).
- `SF Mono`: San Francisco Mono (macOS).
- `Monaco`: alternativa macOS clásica.
- `Cascadia Code`: Windows moderno (VS Code).
- `Roboto Mono`: Android.
- `Consolas`: Windows clásico.
- `Courier New`: universal.
- `monospace`: último recurso.
"""


# ======================================================================
# 3. Hojas de estilo externas
# ======================================================================

HOJAS_DE_ESTILO_BASE: list[str] = [
    # Inter: pesos 400, 500, 600, 700, 800, 900
    (
        "https://fonts.googleapis.com/css2?"
        "family=Inter:wght@400;500;600;700;800;900"
        "&display=swap"
    ),
    # JetBrains Mono: pesos 400, 500, 600, 700
    (
        "https://fonts.googleapis.com/css2?"
        "family=JetBrains+Mono:wght@400;500;600;700"
        "&display=swap"
    ),
]
"""URLs de las hojas de estilo de Google Fonts.

Se cargan desde `configuracion/app_config.py` con:

    stylesheets=[*HOJAS_DE_ESTILO_BASE, "/styles/global.css"]

⚠️ `display=swap` permite que el texto se muestre con la fuente de
fallback mientras Inter/JetBrains Mono se descargan (evita FOIT).
"""


# ======================================================================
# 4. Estilo base tipográfico
# ======================================================================

FALLBACK_PRINCIPAL: str = f'"{FUENTE_PRINCIPAL}", {FALLBACK_SANS}'
"""Familia completa principal: fuente + fallbacks."""

FALLBACK_MONOESPACIADO: str = (
    f'"{FUENTE_MONOESPACIADA}", {FALLBACK_MONO}'
)
"""Familia completa monoespaciada: fuente + fallbacks."""


ESTILO_BASE: dict = {
    # ==============================================================
    # Body: fuente principal
    # ==============================================================
    "font_family": FALLBACK_PRINCIPAL,
    "font_feature_settings": '"cv02", "cv03", "cv04", "cv11"',
    "WebkitFontSmoothing": "antialiased",
    "MozOsxFontSmoothing": "grayscale",
    # ==============================================================
    # Código y contenido monoespaciado
    # ==============================================================
    "code": {"font_family": FALLBACK_MONOESPACIADO},
    "pre": {"font_family": FALLBACK_MONOESPACIADO},
    "kbd": {"font_family": FALLBACK_MONOESPACIADO},
    "samp": {"font_family": FALLBACK_MONOESPACIADO},
    # ==============================================================
    # Controles de formulario (heredan la fuente principal)
    # ==============================================================
    "button": {"font_family": FALLBACK_PRINCIPAL},
    "input": {"font_family": FALLBACK_PRINCIPAL},
    "textarea": {"font_family": FALLBACK_PRINCIPAL},
    "select": {"font_family": FALLBACK_PRINCIPAL},
}
"""Estilo base tipográfico global.

Se pasa a `rx.App(style=ESTILO_BASE)` y se aplica a todo el árbol de
componentes. Refleja la estructura del archivo CSS global
(`styles/global.css`) pero a través de la API de Reflex.

Estructura:
- `font_family`:      fuente principal del body.
- `font_feature_settings`: features OpenType de Inter.
- `WebkitFontSmoothing` / `MozOsxFontSmoothing`: suavizado.
- `code`, `pre`, `kbd`, `samp`: fuentes monoespaciadas.
- `button`, `input`, `textarea`, `select`: heredan la fuente.

Nota técnica: NO duplicar `styles/global.css`
---------------------------------------------
`ESTILO_BASE` y `styles/global.css` cubren la misma área (tipografía
global). La duplicación es intencional porque:

- `ESTILO_BASE` aplica vía React (atributos inline y styled components).
- `styles/global.css` aplica vía CSS puro (mayor prioridad).

Si se quiere eliminar la duplicación, migrar todo a `global.css` y
vaciar `ESTILO_BASE`. Pero `ESTILO_BASE` es más fácil de mantener.
"""


# ======================================================================
# 5. Constantes tipográficas (pesos, tamaños)
# ======================================================================

# --- Pesos ---
PESO_REGULAR: str = "400"
PESO_MEDIO: str = "500"
PESO_SEMIBOLD: str = "600"
PESO_BOLD: str = "700"
PESO_EXTRABOLD: str = "800"
PESO_BLACK: str = "900"

# --- Tamaños base ---
TAMANO_TEXTO_XS: str = "0.75rem"      # 12px
TAMANO_TEXTO_SM: str = "0.875rem"     # 14px
TAMANO_TEXTO_BASE: str = "1rem"       # 16px
TAMANO_TEXTO_LG: str = "1.125rem"     # 18px
TAMANO_TEXTO_XL: str = "1.25rem"      # 20px

# --- Tamaños de heading (1-9, alineados con Radix Themes) ---
TAMANO_HEADING_1: str = "3rem"        # 48px
TAMANO_HEADING_2: str = "2.5rem"      # 40px
TAMANO_HEADING_3: str = "2rem"        # 32px
TAMANO_HEADING_4: str = "1.5rem"      # 24px
TAMANO_HEADING_5: str = "1.25rem"     # 20px
TAMANO_HEADING_6: str = "1.125rem"    # 18px

# --- Line-heights ---
LINE_HEIGHT_TIGHT: str = "1.1"
LINE_HEIGHT_SNUG: str = "1.3"
LINE_HEIGHT_NORMAL: str = "1.5"
LINE_HEIGHT_RELAXED: str = "1.6"
LINE_HEIGHT_LOOSE: str = "1.75"


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Fuentes ---
    "FALLBACK_MONO",
    "FALLBACK_MONOESPACIADO",
    "FALLBACK_PRINCIPAL",
    "FALLBACK_SANS",
    "FUENTE_MONOESPACIADA",
    "FUENTE_PRINCIPAL",
    # --- Hojas de estilo ---
    "HOJAS_DE_ESTILO_BASE",
    # --- Estilo base ---
    "ESTILO_BASE",
    # --- Pesos ---
    "PESO_BLACK",
    "PESO_BOLD",
    "PESO_EXTRABOLD",
    "PESO_MEDIO",
    "PESO_REGULAR",
    "PESO_SEMIBOLD",
    # --- Tamaños base ---
    "TAMANO_TEXTO_BASE",
    "TAMANO_TEXTO_LG",
    "TAMANO_TEXTO_SM",
    "TAMANO_TEXTO_XL",
    "TAMANO_TEXTO_XS",
    # --- Tamaños de heading ---
    "TAMANO_HEADING_1",
    "TAMANO_HEADING_2",
    "TAMANO_HEADING_3",
    "TAMANO_HEADING_4",
    "TAMANO_HEADING_5",
    "TAMANO_HEADING_6",
    # --- Line-heights ---
    "LINE_HEIGHT_LOOSE",
    "LINE_HEIGHT_NORMAL",
    "LINE_HEIGHT_RELAXED",
    "LINE_HEIGHT_SNUG",
    "LINE_HEIGHT_TIGHT",
]