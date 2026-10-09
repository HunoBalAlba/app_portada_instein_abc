

from __future__ import annotations

import reflex as rx

from ...infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    RADIO_EXTRA_GRANDE,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


def newsletter_blog() -> rx.Component:
    """
    Bloque de newsletter inline al pie del blog.

    Estilo Neon.com:
    - Icono de mail.
    - Título + subtítulo.
    - Input de email + botón "Suscribirme" con indigo.
    - Borde sutil (sin fondo tintado).

    Returns:
        Bloque de newsletter completo.
    """
    return rx.box(
        rx.vstack(
            rx.icon("mail", size=32, color=AZUL_MARINO_NEON),
            rx.heading(
                "Recibe los nuevos artículos",
                as_="h3",
                font_size="1.25rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                text_align="center",
            ),
            rx.text(
                "Suscríbete a nuestro newsletter y recibe las novedades "
                "del blog directamente en tu correo.",
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                text_align="center",
                max_width="32rem",
                line_height="1.6",
            ),
            rx.flex(
                rx.input(
                    placeholder="tu@email.com",
                    type="email",
                    size="3",
                    width="100%",
                    flex="1",
                    min_width="0",
                ),
                rx.button(
                    rx.icon("send", size=16),
                    rx.text("Suscribirme", as_="span", font_weight="700"),
                    size="3",
                    variant="solid",
                    color_scheme="indigo",
                    cursor="pointer",
                    flex_shrink="0",
                ),
                gap="0.5rem",
                width="100%",
                max_width="32rem",
                align="center",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                margin_top="0.5rem",
            ),
            align="center",
            spacing="2",
            width="100%",
        ),
        padding="2.5rem 1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background="transparent",
        border=f"1px solid {BORDE_HOME_AZUL}",
        width="100%",
        margin_top="3rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = ["newsletter_blog"]