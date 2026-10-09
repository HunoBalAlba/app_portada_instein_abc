

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ..componentes.base import (
    ItemFaq,
    acordeon_faq,
    encabezado_seccion,
    separador_secciones,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..infraestructura import (
    ANCHO_CONTENIDO,
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    RADIO_EXTRA_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"

# Colores de los badges de demanda/nivel (semánticos reales)
COLOR_VERDE_TEXTO = rx.color("green", 11)
COLOR_VERDE_FONDO = rx.color("green", 3)
COLOR_VERDE_BORDE = rx.color("green", 7)

COLOR_AMBAR_TEXTO = rx.color("amber", 11)
COLOR_AMBAR_FONDO = rx.color("amber", 3)
COLOR_AMBAR_BORDE = rx.color("amber", 7)

COLOR_GRIS_TEXTO = rx.color("gray", 11)
COLOR_GRIS_FONDO = rx.color("gray", 3)
COLOR_GRIS_BORDE = rx.color("gray", 7)

# Color del nivel "Oro" (máximo premio)
COLOR_ORO_TEXTO = rx.color("crimson", 11)
COLOR_ORO_FONDO = rx.color("crimson", 3)
COLOR_ORO_BORDE = rx.color("crimson", 7)


# ======================================================================
# Tipos
# ======================================================================


class Base(TypedDict):
    """Base del programa."""
    icono: str
    titulo: str
    descripcion: str


class PasoProceso(TypedDict):
    """Paso del proceso."""
    numero: str
    icono: str
    titulo: str
    descripcion: str


class AreaInnovacion(TypedDict):
    """Área de innovación."""
    icono: str
    titulo: str
    descripcion: str
    carrera: str


class NivelBeca(TypedDict):
    """Nivel de beca."""
    rango: str
    puntos: str
    titulo: str
    porcentaje: str
    descripcion: str
    icono: str
    destacado: bool


class Requisito(TypedDict):
    """Requisito."""
    icono: str
    texto: str


class ProyectoGanador(TypedDict):
    """Proyecto ganador."""
    anio: str
    titulo: str
    equipo: str
    puntaje: str
    beca: str
    descripcion: str


# ======================================================================
# Datos estáticos
# ======================================================================

BASES_PROGRAMA: list[Base] = [
    {
        "icono": "trophy",
        "titulo": "Se gana en las ferias",
        "descripcion": (
            "Las becas se otorgan en las ferias de innovación internas "
            "del instituto. No son automáticas ni por promedio."
        ),
    },
    {
        "icono": "target",
        "titulo": "Mínimo 90 puntos",
        "descripcion": (
            "El proyecto debe obtener un puntaje de innovación igual o "
            "superior a 90 sobre 100 para ser elegible."
        ),
    },
    {
        "icono": "users",
        "titulo": "Solo estudiantes activos",
        "descripcion": (
            "Debes estar inscrito y cursando una carrera del instituto "
            "al momento de la feria."
        ),
    },
]

PASOS_PROCESO: list[PasoProceso] = [
    {
        "numero": "01",
        "icono": "clipboard-list",
        "titulo": "Forma tu equipo y elige un área",
        "descripcion": (
            "Puedes participar individualmente o en equipos de hasta 3 "
            "estudiantes. Elige el área de innovación en la que "
            "competirás."
        ),
    },
    {
        "numero": "02",
        "icono": "lightbulb",
        "titulo": "Desarrolla tu proyecto",
        "descripcion": (
            "Trabaja durante el semestre en tu proyecto con apoyo de "
            "docentes mentores. Documenta todo el proceso."
        ),
    },
    {
        "numero": "03",
        "icono": "presentation",
        "titulo": "Preséntalo en la feria",
        "descripcion": (
            "Expón tu proyecto en la feria de innovación del instituto "
            "con un stand y una presentación de 10 minutos."
        ),
    },
    {
        "numero": "04",
        "icono": "scale",
        "titulo": "Evaluación del jurado",
        "descripcion": (
            "Un jurado de docentes y profesionales externos evalúa "
            "originalidad, impacto, viabilidad e innovación técnica."
        ),
    },
    {
        "numero": "05",
        "icono": "trophy",
        "titulo": "Beca otorgada",
        "descripcion": (
            "Si obtienes 90 puntos o más, accedes a la beca según el "
            "nivel alcanzado. Se aplica al siguiente semestre."
        ),
    },
]

AREAS_INNOVACION: list[AreaInnovacion] = [
    {
        "icono": "cpu",
        "titulo": "Tecnología e Informática",
        "descripcion": (
            "Software, hardware, automatización, IA aplicada, "
            "ciberseguridad."
        ),
        "carrera": "Sistemas Informáticos",
    },
    {
        "icono": "circuit-board",
        "titulo": "Electrónica y Control",
        "descripcion": (
            "Circuitos, robótica, telecomunicaciones, domótica, "
            "energías renovables."
        ),
        "carrera": "Electrónica",
    },
    {
        "icono": "globe",
        "titulo": "Comercio y Logística",
        "descripcion": (
            "Importación/exportación, logística, comercio digital, "
            "trámites aduaneros."
        ),
        "carrera": "Comercio Internacional",
    },
    {
        "icono": "calculator",
        "titulo": "Gestión Financiera",
        "descripcion": (
            "Contabilidad digital, finanzas, emprendimiento, "
            "automatización contable."
        ),
        "carrera": "Contaduría General",
    },
    {
        "icono": "briefcase",
        "titulo": "Innovación Administrativa",
        "descripcion": (
            "Procesos, gestión documental, atención al cliente, "
            "organización empresarial."
        ),
        "carrera": "Secretariado Ejecutivo",
    },
]

NIVELES_BECA: list[NivelBeca] = [
    {
        "rango": "90 - 93",
        "puntos": "90-93 pts",
        "titulo": "Beca Bronce",
        "porcentaje": "30%",
        "descripcion": "Cubre el 30% de la mensualidad del siguiente semestre.",
        "icono": "medal",
        "destacado": False,
    },
    {
        "rango": "94 - 97",
        "puntos": "94-97 pts",
        "titulo": "Beca Plata",
        "porcentaje": "50%",
        "descripcion": "Cubre el 50% de la mensualidad del siguiente semestre.",
        "icono": "award",
        "destacado": False,
    },
    {
        "rango": "98 - 100",
        "puntos": "98-100 pts",
        "titulo": "Beca Oro",
        "porcentaje": "100%",
        "descripcion": "Cubre el 100% de la mensualidad del siguiente semestre.",
        "icono": "trophy",
        "destacado": True,
    },
]

REQUISITOS_BECA: list[Requisito] = [
    {"icono": "user-check", "texto": "Ser estudiante activo del instituto al momento de la feria"},
    {"icono": "users", "texto": "Participar individualmente o en equipos de hasta 3 personas"},
    {"icono": "lightbulb", "texto": "Presentar un proyecto original de innovación en cualquier área"},
    {"icono": "file-text", "texto": "Documentar el proceso y entregar la memoria del proyecto"},
    {"icono": "presentation", "texto": "Exponer el proyecto en la feria con stand y presentación"},
    {"icono": "shield-check", "texto": "No tener sanciones disciplinarias vigentes"},
    {"icono": "handshake", "texto": "Aceptar los términos y condiciones del programa de becas"},
]

PROYECTOS_GANADORES: list[ProyectoGanador] = [
    {
        "anio": "2025",
        "titulo": "Sistema de riego inteligente con IoT",
        "equipo": "Equipo Electrónica",
        "puntaje": "96",
        "beca": "Beca Plata · 50%",
        "descripcion": (
            "Sistema de riego automatizado con sensores de humedad y "
            "control desde app móvil. Redujo el consumo de agua en 40%."
        ),
    },
    {
        "anio": "2025",
        "titulo": "Plataforma de gestión para microempresas",
        "equipo": "Equipo Sistemas",
        "puntaje": "94",
        "beca": "Beca Plata · 50%",
        "descripcion": (
            "Aplicación web para digitalizar inventarios, ventas y "
            "facturación de microempresas locales."
        ),
    },
    {
        "anio": "2024",
        "titulo": "Optimización de rutas para exportadoras",
        "equipo": "Equipo Comercio Int.",
        "puntaje": "91",
        "beca": "Beca Bronce · 30%",
        "descripcion": (
            "Modelo de optimización logística para reducir costos de "
            "transporte en exportaciones bolivianas."
        ),
    },
]

PREGUNTAS_BECA: list[ItemFaq] = [
    {
        "pregunta": "¿Hay becas por promedio académico?",
        "respuesta": (
            "No. En INSTEIN no otorgamos becas por promedio ni por "
            "situación socioeconómica. Nuestro único programa de becas "
            "es el de innovación, y se gana presentando un proyecto "
            "destacado en las ferias internas."
        ),
    },
    {
        "pregunta": "¿Hay descuentos por pago adelantado o familiar?",
        "respuesta": (
            "No manejamos descuentos comerciales de ningún tipo. La "
            "mensualidad es única y el único beneficio económico "
            "disponible es la beca por innovación."
        ),
    },
    {
        "pregunta": "¿Cuántas veces al año se puede participar?",
        "respuesta": (
            "Hay dos ferias al año, una por semestre. Puedes participar "
            "en todas las que quieras. Si ya tienes una beca activa, "
            "puedes intentar mejorarla en la siguiente feria."
        ),
    },
    {
        "pregunta": "¿La beca aplica retroactiva al semestre actual?",
        "respuesta": (
            "No. La beca se aplica al semestre siguiente al de la feria "
            "en la que ganaste. Así todos los estudiantes compiten en "
            "igualdad de condiciones al inicio de cada semestre."
        ),
    },
    {
        "pregunta": "¿Cuánto dura la beca?",
        "respuesta": (
            "La beca cubre una mensualidad completa. Si quieres "
            "mantenerla para el siguiente semestre, debes volver a "
            "participar en la feria y volver a obtener 90 puntos o más."
        ),
    },
    {
        "pregunta": "¿Puedo participar si estoy en primer semestre?",
        "respuesta": (
            "Sí. No hay restricción por semestre. Cualquier estudiante "
            "activo puede participar, incluso si acaba de ingresar. "
            "Mentores y docentes te apoyarán en el desarrollo."
        ),
    },
    {
        "pregunta": "¿Qué pasa si mi proyecto no llega a 90 puntos?",
        "respuesta": (
            "Puedes seguir mejorándolo y presentarlo en la siguiente "
            "feria. Recibirás retroalimentación del jurado para "
            "fortalecer tu propuesta."
        ),
    },
    {
        "pregunta": "¿Los equipos comparten la beca?",
        "respuesta": (
            "Sí. Si ganas en equipo, la beca se otorga a cada integrante "
            "de manera individual, aplicada a su propia mensualidad."
        ),
    },
]


# ======================================================================
# Hero
# ======================================================================


def _hero_becas() -> rx.Component:
    """
    Hero alineado a la izquierda.

    Estilo Neon.com:
    - Badge con icono de trofeo.
    - Título con énfasis bicolor.
    - Subtítulo descriptivo.
    """
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.icon("trophy", size=12, color=AZUL_MARINO_NEON),
                rx.text(
                    "PROGRAMA DE BECAS POR INNOVACIÓN",
                    font_size="0.6875rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    letter_spacing="0.15em",
                    text_transform="uppercase",
                ),
                align="center",
                gap="0.5rem",
                margin_bottom="1.5rem",
            ),
            # ─── Título con énfasis bicolor ────────────────────
            rx.heading(
                rx.text.span("Becas y "),
                rx.text.span(
                    "Reconocimientos",
                    color=AZUL_MARINO_NEON,
                ),
                as_="h1",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                max_width="56rem",
            ),
            rx.text(
                "En INSTEIN no damos becas por promedio ni descuentos "
                "comerciales. Premiamos la innovación real: si tu "
                "proyecto destaca en nuestras ferias internas, te "
                "becamos.",
                font_size=["1rem", "1.125rem"],
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                max_width="48rem",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=[
            f"4rem {PADDING_SECCION_HORIZONTAL} 3rem {PADDING_SECCION_HORIZONTAL}",
            f"6rem {PADDING_SECCION_HORIZONTAL} 4rem {PADDING_SECCION_HORIZONTAL}",
        ],
        width="100%",
    )


# ======================================================================
# Sección 01 — Bases del programa
# ======================================================================


def _tarjeta_base(item: Base) -> rx.Component:
    """Tarjeta de base del programa."""
    return rx.box(
        rx.vstack(
            rx.icon(item["icono"], size=24, color=AZUL_MARINO_NEON),
            rx.text(
                item["titulo"],
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
                margin_top="0.75rem",
            ),
            rx.text(
                item["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.5rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="2rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _seccion_bases() -> rx.Component:
    """Grid con las 3 bases del programa."""
    return rx.grid(
        *[_tarjeta_base(item) for item in BASES_PROGRAMA],
        columns=rx.breakpoints(initial="1", md="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 02 — Cómo funciona (timeline)
# ======================================================================


def _paso_timeline(paso: PasoProceso) -> rx.Component:
    """Paso individual del timeline."""
    return rx.flex(
        # ─── Número ─────────────────────────────────────────────
        rx.box(
            rx.text(
                paso["numero"],
                font_size="0.875rem",
                font_weight="900",
                color="white",
                line_height="1",
            ),
            height="2.5rem",
            width="2.5rem",
            border_radius=RADIO_PASTILLA,
            background=AZUL_MARINO_NEON,
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        # ─── Contenido ──────────────────────────────────────────
        rx.vstack(
            rx.flex(
                rx.icon(paso["icono"], size=16, color=AZUL_MARINO_NEON),
                rx.text(
                    paso["titulo"],
                    font_size="1rem",
                    font_weight="700",
                    color=TEXTO_HOME_PRINCIPAL,
                ),
                align="center",
                gap="0.5rem",
            ),
            rx.text(
                paso["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.5rem",
            ),
            align="start",
            spacing="0",
            flex="1",
            min_width="0",
        ),
        align="start",
        gap="1rem",
        width="100%",
    )


def _seccion_proceso() -> rx.Component:
    """Timeline con los 5 pasos."""
    return rx.vstack(
        *[_paso_timeline(paso) for paso in PASOS_PROCESO],
        spacing="6",
        width="100%",
    )


# ======================================================================
# Sección 03 — Áreas de innovación
# ======================================================================


def _tarjeta_area(item: AreaInnovacion) -> rx.Component:
    """Tarjeta de área de innovación."""
    return rx.box(
        rx.vstack(
            rx.icon(item["icono"], size=20, color=AZUL_MARINO_NEON),
            rx.text(
                item["titulo"],
                font_size="1rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
                margin_top="0.75rem",
            ),
            rx.text(
                item["descripcion"],
                font_size="0.8125rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.5rem",
            ),
            rx.flex(
                rx.icon("graduation-cap", size=12, color=AZUL_MARINO_NEON),
                rx.text(
                    item["carrera"],
                    font_size="0.6875rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    text_transform="uppercase",
                    letter_spacing="0.1em",
                ),
                align="center",
                gap="0.375rem",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _seccion_areas() -> rx.Component:
    """Grid con las 5 áreas de innovación."""
    return rx.grid(
        *[_tarjeta_area(item) for item in AREAS_INNOVACION],
        columns=rx.breakpoints(initial="1", sm="2", lg="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 04 — Niveles de beca
# ======================================================================


def _tarjeta_nivel(nivel: NivelBeca) -> rx.Component:
    """
    Tarjeta de nivel de beca.

    El nivel "Oro" (destacado) usa crimson. El resto usa azul marino.
    """
    destacado = nivel["destacado"]

    color_texto = COLOR_ORO_TEXTO if destacado else AZUL_MARINO_NEON
    color_fondo = COLOR_ORO_FONDO if destacado else FONDO_AZUL_SUAVE
    color_borde = COLOR_ORO_BORDE if destacado else BORDE_HOME_AZUL

    return rx.box(
        rx.vstack(
            # ─── Badge de puntos ────────────────────────────────
            rx.flex(
                rx.text(
                    nivel["puntos"],
                    font_size="0.6875rem",
                    font_weight="700",
                    color=color_texto,
                    letter_spacing="0.05em",
                    text_transform="uppercase",
                ),
                padding="0.25rem 0.625rem",
                border_radius=RADIO_PASTILLA,
                background=color_fondo,
                border=f"1px solid {color_borde}",
                width="fit-content",
            ),
            # ─── Icono ──────────────────────────────────────────
            rx.icon(
                nivel["icono"],
                size=28,
                color=color_texto,
                margin_top="1rem",
            ),
            # ─── Título ─────────────────────────────────────────
            rx.text(
                nivel["titulo"],
                font_size="1.125rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.2",
                margin_top="0.75rem",
            ),
            # ─── Porcentaje grande ──────────────────────────────
            rx.text(
                nivel["porcentaje"],
                font_size="3rem",
                font_weight="900",
                color=color_texto,
                line_height="1",
                letter_spacing="-0.03em",
                margin_top="0.75rem",
            ),
            rx.text(
                "de la mensualidad",
                font_size="0.75rem",
                font_weight="600",
                color=TEXTO_HOME_MAS_SUAVE,
                text_transform="uppercase",
                letter_spacing="0.1em",
                margin_top="0.25rem",
            ),
            # ─── Descripción ────────────────────────────────────
            rx.text(
                nivel["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="2rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {color_texto}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": color_texto},
    )


def _seccion_niveles() -> rx.Component:
    """Grid con los 3 niveles de beca."""
    return rx.grid(
        *[_tarjeta_nivel(nivel) for nivel in NIVELES_BECA],
        columns=rx.breakpoints(initial="1", md="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 05 — Requisitos
# ======================================================================


def _item_requisito(item: Requisito) -> rx.Component:
    """Item individual de requisito."""
    return rx.flex(
        rx.icon(
            item["icono"],
            size=16,
            color=AZUL_MARINO_NEON,
            flex_shrink="0",
            margin_top="0.1875rem",
        ),
        rx.text(
            item["texto"],
            font_size="0.9375rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            flex="1",
        ),
        align="start",
        gap="0.75rem",
        width="100%",
        padding="1rem",
        border_radius=RADIO_MEDIO,
        background=COLOR_FONDO_SUAVE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _seccion_requisitos() -> rx.Component:
    """Lista de requisitos."""
    return rx.vstack(
        *[_item_requisito(item) for item in REQUISITOS_BECA],
        spacing="3",
        width="100%",
        max_width="48rem",
    )


# ======================================================================
# Sección 06 — Proyectos ganadores
# ======================================================================


def _tarjeta_ganador(proyecto: ProyectoGanador) -> rx.Component:
    """Tarjeta de proyecto ganador."""
    return rx.box(
        rx.vstack(
            # ─── Año + puntaje ──────────────────────────────────
            rx.flex(
                rx.text(
                    proyecto["anio"],
                    font_size="0.6875rem",
                    font_weight="700",
                    color=AZUL_MARINO_NEON,
                    letter_spacing="0.05em",
                ),
                rx.text(
                    "·",
                    font_size="0.6875rem",
                    color=TEXTO_HOME_MAS_SUAVE,
                ),
                rx.flex(
                    rx.icon(
                        "star",
                        size=12,
                        color=COLOR_AMBAR_TEXTO,
                        fill=COLOR_AMBAR_TEXTO,
                    ),
                    rx.text(
                        f"{proyecto['puntaje']} pts",
                        font_size="0.6875rem",
                        font_weight="700",
                        color=COLOR_AMBAR_TEXTO,
                    ),
                    align="center",
                    gap="0.25rem",
                ),
                align="center",
                gap="0.5rem",
                margin_bottom="0.75rem",
            ),
            # ─── Título ─────────────────────────────────────────
            rx.text(
                proyecto["titulo"],
                font_size="1rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
            ),
            # ─── Equipo ─────────────────────────────────────────
            rx.text(
                proyecto["equipo"],
                font_size="0.75rem",
                font_weight="600",
                color=TEXTO_HOME_MAS_SUAVE,
                text_transform="uppercase",
                letter_spacing="0.1em",
                margin_top="0.5rem",
            ),
            # ─── Descripción ────────────────────────────────────
            rx.text(
                proyecto["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.75rem",
            ),
            # ─── Badge de beca ──────────────────────────────────
            rx.flex(
                rx.icon("trophy", size=12, color=COLOR_ORO_TEXTO),
                rx.text(
                    proyecto["beca"],
                    font_size="0.6875rem",
                    font_weight="700",
                    color=COLOR_ORO_TEXTO,
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                ),
                align="center",
                gap="0.375rem",
                padding="0.375rem 0.75rem",
                border_radius=RADIO_PASTILLA,
                background=COLOR_ORO_FONDO,
                border=f"1px solid {COLOR_ORO_BORDE}",
                width="fit-content",
                margin_top="1rem",
            ),
            align="start",
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        border_top=f"2px solid {AZUL_MARINO_NEON}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={"border_color": AZUL_MARINO_NEON},
    )


def _seccion_ganadores() -> rx.Component:
    """Grid con los proyectos ganadores."""
    return rx.grid(
        *[_tarjeta_ganador(p) for p in PROYECTOS_GANADORES],
        columns=rx.breakpoints(initial="1", sm="2", lg="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 07 — FAQ
# ======================================================================


def _seccion_faq() -> rx.Component:
    """Acordeón de FAQ del programa."""
    return acordeon_faq(
        items=PREGUNTAS_BECA,
        variante="light",
        icono="help-circle",
        color_acento=AZUL_MARINO_NEON,
        max_width="56rem",
    )


# ======================================================================
# CTA final
# ======================================================================


def _cta_final() -> rx.Component:
    """CTA final hacia /contacto."""
    return rx.flex(
        rx.text(
            "¿Tienes una idea innovadora?",
            font_size="1rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.link(
            rx.text(
                "Consultar por WhatsApp",
                font_size="1rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
            ),
            rx.icon("arrow-right", size=16, color=AZUL_MARINO_NEON),
            href="/contacto",
            text_decoration="none",
            display="inline-flex",
            align_items="center",
            gap="0.375rem",
            transition="gap 0.2s",
            _hover={"gap": "0.625rem"},
        ),
        align="center",
        justify="start",
        gap="0.5rem",
        flex_wrap="wrap",
        width="100%",
        padding_top="3rem",
        margin_top="2rem",
        border_top=f"1px solid {COLOR_DIVISOR}",
    )


# ======================================================================
# Vista completa
# ======================================================================


@rx.page(
    route="/becas",
    title=f"Becas y Reconocimientos | {NOMBRE_INSTITUTO}",
    description=(
        "Programa de becas por innovación del Instituto Técnico "
        "Integrado San Antonio de Padua (INSTEIN). Becas de hasta "
        "100% de la mensualidad por proyectos destacados."
    ),
)
def vista_becas() -> rx.Component:
    """
    Página del programa de becas — estilo Neon.com.

    Aclaración importante: NO hay becas generales ni descuentos
    comerciales. El único programa de becas es el de innovación,
    que se gana en las ferias internas.
    """
    return rx.box(
        rx.vstack(
            # =============================================================
            # 1. HEADER
            # =============================================================
            rx.box(
                barra_navegacion_superior(),
                width="100%",
                role="banner",
                aria_label="Navegación principal",
            ),
            # =============================================================
            # 2. MAIN
            # =============================================================
            rx.el.main(
                # ─── Hero ───────────────────────────────────────────
                _hero_becas(),
                # ─── Sección 01 — Bases del programa ────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Bases del programa",
                            titulo="Cómo funciona",
                            titulo_enfasis="el programa de becas",
                            subtitulo=(
                                "El programa de becas por innovación "
                                "tiene 3 reglas simples."
                            ),
                        ),
                        _seccion_bases(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="bases",
                    aria_label="Bases del programa",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 02 — Cómo funciona ─────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="02",
                            etiqueta="El camino a la beca",
                            titulo="De la idea al reconocimiento",
                            titulo_enfasis="en 5 etapas",
                            subtitulo=(
                                "Un proceso claro para que sepas qué "
                                "esperar en cada momento."
                            ),
                        ),
                        _seccion_proceso(),
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="proceso",
                    aria_label="Proceso de evaluación",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 03 — Áreas de innovación ───────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="03",
                            etiqueta="Áreas de innovación",
                            titulo="Compite",
                            titulo_enfasis="en tu área",
                            subtitulo=(
                                "5 áreas de innovación alineadas con "
                                "las carreras del instituto."
                            ),
                        ),
                        _seccion_areas(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="areas",
                    aria_label="Áreas de innovación",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 04 — Niveles de beca ───────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="04",
                            etiqueta="Niveles de beca",
                            titulo="Según",
                            titulo_enfasis="tu puntaje de innovación",
                            subtitulo=(
                                "A mayor puntaje, mayor porcentaje de "
                                "beca. Se aplica al siguiente semestre."
                            ),
                        ),
                        _seccion_niveles(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="niveles",
                    aria_label="Niveles de beca",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 05 — Requisitos ────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="05",
                            etiqueta="Requisitos",
                            titulo="Para participar",
                            titulo_enfasis="en la feria",
                            subtitulo=(
                                "Cumpliendo estos requisitos, cualquier "
                                "estudiante activo puede competir."
                            ),
                        ),
                        _seccion_requisitos(),
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="requisitos",
                    aria_label="Requisitos para participar",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 06 — Proyectos ganadores ───────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="06",
                            etiqueta="Proyectos ganadores",
                            titulo="Ejemplos que",
                            titulo_enfasis="ya ganaron beca",
                            subtitulo=(
                                "Algunos de los proyectos destacados en "
                                "ferias anteriores."
                            ),
                        ),
                        _seccion_ganadores(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="ganadores",
                    aria_label="Proyectos ganadores",
                    scroll_margin_top="5rem",
                ),
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 07 — FAQ ───────────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="07",
                            etiqueta="Preguntas frecuentes",
                            titulo="Dudas",
                            titulo_enfasis="sobre las becas",
                            subtitulo=(
                                "Todo lo que necesitas saber antes de "
                                "participar."
                            ),
                        ),
                        _seccion_faq(),
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="faq",
                    aria_label="Preguntas frecuentes sobre becas",
                    scroll_margin_top="5rem",
                ),
                # ─── CTA final ──────────────────────────────────────
                rx.box(
                    _cta_final(),
                    max_width=ANCHO_CONTENIDO,
                    margin="0 auto",
                    padding_x=PADDING_SECCION_HORIZONTAL,
                    padding_bottom="6rem",
                    width="100%",
                ),
                width="100%",
                aria_label="Programa de becas",
            ),
            # =============================================================
            # 3. FOOTER
            # =============================================================
            rx.box(
                pie_pagina_institucional(),
                width="100%",
                role="contentinfo",
                aria_label="Información del sitio",
            ),
            align="center",
            min_height="100vh",
            width="100%",
            spacing="0",
            background=FONDO_HOME,
        ),
        width="100%",
        background=FONDO_HOME,
        lang="es",
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "AreaInnovacion",
    "Base",
    "NivelBeca",
    "PasoProceso",
    "ProyectoGanador",
    "Requisito",
    "vista_becas",
]