"""
Sección de preguntas frecuentes del home — estilo Neon adaptativo.

Contenido
---------
- Lista de preguntas frecuentes institucionales.
- Encabezado con número de sección ("03") + título + subtítulo.

Este archivo unifica lo que antes vivía en
`componentes/preguntas_frecuentes.py` (ahora eliminado).

Sistema de color
----------------
✅ ADAPTATIVO: el acordeón `neon` respeta el `color_mode`.

- Card cerrada: `FONDO_HOME_CARD` con glassmorphism.
- Card abierta: `FONDO_AZUL_MUY_SUAVE` + borde azul.
- Chevron abierto: azul marino neon + rotación 180°.
- Textos: `TEXTO_HOME_PRINCIPAL` / `TEXTO_HOME_MAS_SUAVE` / `TEXTO_HOME_SUAVE`.

Nota técnica: ELIMINADO `EstadoPreguntasFrecuentes` LOCAL
---------------------------------------------------------
El acordeón usa el `EstadoAcordeonFaq` global (vive en
`dominio.estados.estado_acordeon_faq`). No se necesita un State local.
"""

from __future__ import annotations

import reflex as rx

from ...componentes.base.acordeon_faq import (
    ItemFaq,
    acordeon_faq,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_LISTA: str = "56rem"
"""Ancho máximo de la lista de preguntas."""


# ======================================================================
# Datos estáticos
# ======================================================================

PREGUNTAS_FRECUENTES: list[ItemFaq] = [
    {
        "pregunta": "¿Qué es el INSTEIN?",
        "respuesta": (
            "El Instituto Técnico Integrado San Antonio de Padua (INSTEIN) "
            "es una institución educativa de nivel técnico superior "
            "autorizada por Resolución Ministerial R.M. 0871/2016. "
            "Ofrecemos formación técnica de excelencia en 5 carreras."
        ),
    },
    {
        "pregunta": "¿Cómo puedo inscribirme a una carrera?",
        "respuesta": (
            "Puedes inscribirte presencialmente en nuestras oficinas "
            "ubicadas en la Galería FLOR DE ORO (1er piso), o contactarnos "
            "por WhatsApp al 71282993. El proceso incluye la presentación "
            "de documentos personales y el pago de la matrícula."
        ),
    },
    {
        "pregunta": "¿Cuánto duran las carreras?",
        "respuesta": (
            "Todas nuestras carreras tienen una duración de 3 años "
            "(6 semestres). Al finalizar, los estudiantes obtienen el "
            "título de Técnico Superior en Provisión Nacional."
        ),
    },
    {
        "pregunta": "¿Cuáles son los requisitos de admisión?",
        "respuesta": (
            "Los requisitos son: fotocopia del diploma de bachiller, "
            "fotocopia del carnet de identidad, 2 fotografías tamaño "
            "carnet, y el pago de la matrícula y primera mensualidad."
        ),
    },
    {
        "pregunta": "¿Qué horarios ofrecen?",
        "respuesta": (
            "Ofrecemos turnos de mañana (08:30 - 12:30) y tarde "
            "(14:30 - 18:30). Algunas carreras también tienen turno "
            "nocturno (19:00 - 22:00) para estudiantes que trabajan."
        ),
    },
    {
        "pregunta": "¿Los títulos son válidos para trabajar?",
        "respuesta": (
            "Sí, nuestros títulos son emitidos por el Ministerio de "
            "Educación con validez nacional. Están registrados en el "
            "sistema educativo boliviano y son reconocidos por "
            "empleadores."
        ),
    },
]


# ======================================================================
# Sección completa
# ======================================================================


def seccion_preguntas_frecuentes() -> rx.Component:
    """
    Sección completa con la lista de preguntas frecuentes del home.

    El encabezado (número + título) se renderiza desde `vista_inicio.py`
    con `separador_numerado`. Este componente SOLO renderiza la lista.

    Delega en `acordeon_faq` con variante `"neon"`, sin icono lateral.
    """
    return rx.box(
        acordeon_faq(
            items=PREGUNTAS_FRECUENTES,
            variante="neon",
            icono="",
            tamano_texto_pregunta="1.0625rem",
            tamano_texto_respuesta="0.9375rem",
            padding_cabecera="1.25rem 1.5rem",
            padding_respuesta="0 1.5rem 1.5rem 1.5rem",
            max_width=ANCHO_MAXIMO_LISTA,
        ),
        width="100%",
        padding="0 1.5rem 4rem 1.5rem",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "PREGUNTAS_FRECUENTES",
    "seccion_preguntas_frecuentes",
]