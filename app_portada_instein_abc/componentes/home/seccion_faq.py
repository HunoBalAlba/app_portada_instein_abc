

from __future__ import annotations

import reflex as rx

from ...componentes.base.acordeon_faq import (
    ItemFaq,
    acordeon_faq,
)
from ...componentes.base.primitivos import (
    enlace_navegacion,
)
from ...infraestructura.constantes.colores import (
    AZUL_MARINO_NEON,
    COLOR_DIVISOR,
    TEXTO_HOME_MAS_SUAVE,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_LISTA: str = "56rem"


# ======================================================================
# Datos estáticos
# ======================================================================

PREGUNTAS_FRECUENTES: list[ItemFaq] = [
    # ─── Generales ─────────────────────────────────────────────
    {
        "pregunta": "¿Qué es el INSTEIN?",
        "respuesta": (
            "El Instituto Técnico Integrado San Antonio de Padua "
            "(INSTEIN) es una institución educativa de nivel técnico "
            "superior autorizada por Resolución Ministerial "
            "R.M. 0871/2016. Ofrecemos formación técnica de excelencia "
            "en 5 carreras con títulos de Provisión Nacional."
        ),
    },
    {
        "pregunta": "¿Cómo puedo inscribirme a una carrera?",
        "respuesta": (
            "Puedes inscribirte presencialmente en nuestras oficinas "
            "ubicadas en la Galería FLOR DE ORO (1er piso), o "
            "contactarnos por WhatsApp al 71282993. El proceso incluye "
            "la presentación de documentos personales y el pago de la "
            "matrícula. Te acompañamos en cada paso."
        ),
    },
    {
        "pregunta": "¿Cuánto duran las carreras?",
        "respuesta": (
            "Todas nuestras carreras tienen una duración de 3 años "
            "(6 semestres). Al finalizar, los estudiantes obtienen el "
            "título de Técnico Superior en Provisión Nacional, "
            "reconocido por empleadores en todo el país."
        ),
    },
    {
        "pregunta": "¿Cuáles son los requisitos de admisión?",
        "respuesta": (
            "Los requisitos son: fotocopia del diploma de bachiller, "
            "fotocopia del carnet de identidad, 2 fotografías tamaño "
            "carnet, y el pago de la matrícula y primera mensualidad. "
            "Si te falta algún documento, contáctanos y te ayudamos."
        ),
    },
    # ─── Específicas ───────────────────────────────────────────
    {
        "pregunta": "¿Qué horarios ofrecen?",
        "respuesta": (
            "Ofrecemos turnos de mañana (08:30 - 12:30) y tarde "
            "(14:30 - 18:30). Algunas carreras también tienen turno "
            "nocturno (19:00 - 22:00) y turno de sábados "
            "(09:00 - 14:30) para estudiantes que trabajan."
        ),
    },
    {
        "pregunta": "¿Los títulos son válidos para trabajar?",
        "respuesta": (
            "Sí, nuestros títulos son emitidos por el Ministerio de "
            "Educación con validez nacional. Están registrados en el "
            "sistema educativo boliviano y son reconocidos por "
            "empleadores de los sectores público y privado."
        ),
    },
    {
        "pregunta": "¿Cuánto cuesta estudiar en INSTEIN?",
        "respuesta": (
            "Ofrecemos planes de pago accesibles con mensualidades "
            "cómodas. Escríbenos por WhatsApp al 71282993 para recibir "
            "el detalle de costos de tu carrera específica."
        ),
    },
    {
        "pregunta": "¿Puedo trabajar mientras estudio?",
        "respuesta": (
            "Sí. Todas las carreras tienen turno nocturno (19:00 - "
            "22:00) y turno de sábados (09:00 - 14:30) especialmente "
            "diseñados para estudiantes que trabajan durante el día."
        ),
    },
]


# ======================================================================
# Link "Ver todas las FAQ"
# ======================================================================


def _link_ver_todas_faq() -> rx.Component:
    """
    Link discreto hacia la página completa de FAQ.

    Estilo minimalista: texto + flecha, sin botón.
    """
    return enlace_navegacion(
        "/faq",
        rx.text(
            "Ver todas las preguntas frecuentes",
            font_size="0.875rem",
            font_weight="600",
            color=AZUL_MARINO_NEON,
        ),
        rx.icon(
            "arrow-right",
            size=14,
            color=AZUL_MARINO_NEON,
        ),
        display="inline-flex",
        align_items="center",
        gap="0.375rem",
        text_decoration="none",
        transition="gap 0.2s",
        width="fit-content",
        _hover={"gap": "0.625rem"},
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final_faq() -> rx.Component:
    """
    CTA al final del acordeón: "¿No encontraste tu respuesta?".

    Estructura:
    - Pregunta en texto plano.
    - Link a /contacto.
    """
    return rx.flex(
        rx.text(
            "¿No encontraste tu respuesta?",
            font_size="0.9375rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        enlace_navegacion(
            "/contacto",
            rx.text(
                "Contáctanos",
                font_size="0.9375rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
            ),
            rx.icon(
                "arrow-right",
                size=14,
                color=AZUL_MARINO_NEON,
            ),
            display="inline-flex",
            align_items="center",
            gap="0.375rem",
            text_decoration="none",
            transition="gap 0.2s",
            _hover={"gap": "0.625rem"},
        ),
        align="center",
        justify="start",
        gap="0.5rem",
        flex_wrap="wrap",
        width="100%",
        padding_top="2rem",
        margin_top="1rem",
        border_top=f"1px solid {COLOR_DIVISOR}",
    )


# ======================================================================
# Sección completa
# ======================================================================


def seccion_preguntas_frecuentes() -> rx.Component:
    """
    Sección completa con la lista de preguntas frecuentes del home.

    Estructura:
    1. Acordeón con 8 preguntas categorizadas (generales → específicas).
    2. Link "Ver todas las preguntas frecuentes" → /faq.
    3. CTA final: "¿No encontraste tu respuesta?" → /contacto.

    El encabezado (número + etiqueta + título + subtítulo) se
    renderiza desde `vista_inicio.py` con `_encabezado_seccion`.
    Este componente SOLO renderiza el contenido.

    Estilo:
    - Acordeón variante "light" (sin glassmorphism).
    - Ancho máximo `56rem` (para lectura cómoda).
    - Espaciado generoso al final (`3rem`).

    Returns:
        Componente `rx.box` con el bloque completo.
    """
    return rx.box(
        rx.vstack(
            # ─── Acordeón ──────────────────────────────────────
            acordeon_faq(
                items=PREGUNTAS_FRECUENTES,
                variante="light",
                icono="help-circle",
                color_acento=AZUL_MARINO_NEON,
                tamano_texto_pregunta="1rem",
                tamano_texto_respuesta="0.9375rem",
                padding_cabecera="1.25rem 1.5rem",
                padding_respuesta="0 1.5rem 1.25rem 3.5rem",
                max_width=ANCHO_MAXIMO_LISTA,
            ),
            # ─── Link "Ver todas las FAQ" ──────────────────────
            rx.box(
                _link_ver_todas_faq(),
                width="100%",
                max_width=ANCHO_MAXIMO_LISTA,
                margin="0 auto",
                margin_top="2rem",
            ),
            # ─── CTA final ────────────────────────────────────
            rx.box(
                _cta_final_faq(),
                width="100%",
                max_width=ANCHO_MAXIMO_LISTA,
                margin="0 auto",
            ),
            spacing="0",
            width="100%",
            align="center",
        ),
        width="100%",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "PREGUNTAS_FRECUENTES",
    "seccion_preguntas_frecuentes",
]