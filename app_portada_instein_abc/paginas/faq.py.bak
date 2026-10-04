"""
Vista de Preguntas Frecuentes (ruta "/faq").

Reutiliza el componente `seccion_preguntas_frecuentes` del home.
"""

from __future__ import annotations

import reflex as rx

from ..componentes.home import (
    seccion_preguntas_frecuentes,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    AZUL_MARINO_NEON,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
)


@rx.page(route="/faq", title=f"Preguntas frecuentes | {NOMBRE_INSTITUTO}")
def vista_faq() -> rx.Component:
    """Página dedicada a las preguntas frecuentes del instituto."""
    return rx.vstack(
        barra_navegacion_superior(),
        # ==========================================================
        # Hero
        # ==========================================================
        rx.vstack(
            rx.text(
                "PREGUNTAS FRECUENTES",
                font_size="0.75rem",
                font_weight="700",
                letter_spacing="0.15em",
                color=AZUL_MARINO_NEON,
            ),
            rx.heading(
                "¿En qué podemos ayudarte?",
                size="8",
                font_weight="900",
                color=COLOR_TEXTO_PRINCIPAL,
                text_align="center",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "Encuentra respuestas a las dudas más comunes sobre "
                "inscripciones, carreras, horarios y títulos.",
                font_size="1rem",
                color=COLOR_TEXTO_CUERPO,
                text_align="center",
                max_width="48rem",
                line_height="1.7",
                margin_top="0.5rem",
            ),
            align="center",
            spacing="3",
            padding="5rem 1.5rem 2rem 1.5rem",
            max_width="72rem",
            margin="0 auto",
            width="100%",
        ),
        # ==========================================================
        # Acordeón (reutilizado del home)
        # ==========================================================
        seccion_preguntas_frecuentes(),
        pie_pagina_institucional(),
        align="center",
        min_height="100vh",
        width="100%",
        spacing="0",
        background=FONDO_HOME,
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["vista_faq"]