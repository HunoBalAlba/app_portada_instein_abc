"""
Vista "Guía de Admisión" (ruta "/admision") — estilo Neon.com.

Contenido:
- Hero con badge "Inscripciones abiertas todo el año".
- Grid de 3 tarjetas destacadas (sin fechas, sin sorteo, proceso rápido).
- Proceso de admisión paso a paso (timeline de 5 pasos).
- Requisitos: documentos + académicos.
- Grid de beneficios del instituto.
- Formas de inscripción (presencial, WhatsApp, online).
- Preguntas frecuentes de admisión (acordeón).
- CTA final hacia /contacto.

Diseño
------
Refactorizado al estilo Neon.com:

1. **Layout izquierdo** del hero.
2. **Encabezados numerados** (01–06) con `encabezado_seccion`.
3. **Separadores** entre secciones (compartidos).
4. **Sin glow** excesivo ni `translateY` agresivo.
5. **Acento único** (azul marino) para toda la UI.
6. **Colores semánticos** solo en badges de estado y ventajas.
7. **HTML5 semántico** (`main`, `section`, `footer`).

Sistema de color
----------------
✅ ACENTO ÚNICO: azul marino neon.
✅ ADAPTATIVO: fondo, textos y bordes respetan el `color_mode`.

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa los componentes compartidos:

- `ItemFaq` y `acordeon_faq` (de `..componentes.base`).
- `encabezado_seccion` (de `..componentes.base`).
- `separador_secciones` (de `..componentes.base`).

Antes tenía copias locales `_encabezado_seccion` y
`_separador_secciones`. Ahora vive una sola implementación en
`componentes/base/`.

Nota técnica: ACORDEÓN FAQ UNIFICADO
------------------------------------
La sección de FAQ delega en `acordeon_faq` con variante `"light"`.
Usa el `EstadoAcordeonFaq` global.

Nota técnica: JERARQUÍA DE TÍTULOS
----------------------------------
- `h1` → Solo en el hero ("Guía de Admisión").
- `h2` → Encabezados de sección numerados (`encabezado_seccion`).
- `h3` → Subtítulos dentro de secciones (títulos de tarjetas).
- `h4` → Nombres de items individuales (pasos, requisitos).
"""

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
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_SUAVE,
    EMAIL_CONTACTO,
    FONDO_AZUL_SUAVE,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    TELEFONO_PRINCIPAL,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    WHATSAPP_URL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO: str = "80rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ======================================================================
# Tipos
# ======================================================================


class Paso(TypedDict):
    """Paso del proceso de admisión."""
    numero: str
    icono: str
    titulo: str
    descripcion: str


class Requisito(TypedDict):
    """Requisito individual (documento o académico)."""
    icono: str
    texto: str


class Beneficio(TypedDict):
    """Beneficio de estudiar en el instituto."""
    icono: str
    titulo: str
    descripcion: str
    color: str


class FormaInscripcion(TypedDict):
    """Forma de inscripción (presencial, WhatsApp, email)."""
    icono: str
    titulo: str
    subtitulo: str
    descripcion: str
    cta_texto: str
    cta_url: str
    externo: bool
    color: str


# ======================================================================
# Datos estáticos
# ======================================================================

VENTAJAS_DESTACADAS: list[dict] = [
    {
        "icono": "calendar-check",
        "titulo": "Sin fechas límite",
        "descripcion": (
            "Inscripciones abiertas todo el año. No pierdas tu cupo "
            "porque se te pasó una fecha."
        ),
        "color": "green",
    },
    {
        "icono": "shield-check",
        "titulo": "Sin sorteo aleatorio",
        "descripcion": (
            "Los cupos se asignan por orden de inscripción. Tu esfuerzo "
            "y decisión son lo único que importa."
        ),
        "color": "blue",
    },
    {
        "icono": "zap",
        "titulo": "Proceso en 24 horas",
        "descripcion": (
            "Desde que te inscribes hasta que empiezas clases puede "
            "pasar menos de un día."
        ),
        "color": "amber",
    },
]

PASOS_ADMISION: list[Paso] = [
    {
        "numero": "01",
        "icono": "clipboard-list",
        "titulo": "Elige tu carrera",
        "descripcion": (
            "Explora las 5 carreras técnicas disponibles y elige la que "
            "mejor se alinee con tus metas profesionales."
        ),
    },
    {
        "numero": "02",
        "icono": "file-text",
        "titulo": "Reúne los documentos",
        "descripcion": (
            "Prepara tus documentos personales y académicos. La lista "
            "completa está en la sección de requisitos."
        ),
    },
    {
        "numero": "03",
        "icono": "message-circle",
        "titulo": "Contáctanos",
        "descripcion": (
            "Escríbenos por WhatsApp, llámanos o visítanos. Te guiaremos "
            "durante todo el proceso."
        ),
    },
    {
        "numero": "04",
        "icono": "calendar-clock",
        "titulo": "Agenda tu entrevista",
        "descripcion": (
            "Coordinamos una entrevista breve (15-20 minutos) para "
            "conocerte y resolver todas tus dudas."
        ),
    },
    {
        "numero": "05",
        "icono": "graduation-cap",
        "titulo": "¡Inicia tus clases!",
        "descripcion": (
            "Una vez confirmada tu inscripción, te damos la bienvenida "
            "y comienzas el siguiente lunes disponible."
        ),
    },
]

REQUISITOS_DOCUMENTOS: list[Requisito] = [
    {"icono": "file-text", "texto": "Fotocopia del diploma de bachiller"},
    {
        "icono": "id-card",
        "texto": "Fotocopia del carnet de identidad (ambas caras)",
    },
    {
        "icono": "image",
        "texto": "2 fotografías tamaño carnet (fondo rojo)",
    },
    {
        "icono": "file-signature",
        "texto": "Formulario de inscripción (te lo damos nosotros)",
    },
    {"icono": "receipt", "texto": "Comprobante de pago de matrícula"},
]

REQUISITOS_ACADEMICOS: list[Requisito] = [
    {
        "icono": "graduation-cap",
        "texto": "Haber concluido el bachillerato (o estar por concluir)",
    },
    {
        "icono": "users",
        "texto": "Ser mayor de 17 años al momento de la inscripción",
    },
    {
        "icono": "heart",
        "texto": (
            "Compromiso con la formación técnica y los valores "
            "institucionales"
        ),
    },
    {
        "icono": "target",
        "texto": "Disposición para cumplir con el plan de estudios (3 años)",
    },
    {
        "icono": "languages",
        "texto": "Conocimientos básicos de lectoescritura y matemática",
    },
]

BENEFICIOS: list[Beneficio] = [
    {
        "icono": "award",
        "titulo": "Título Nacional",
        "descripcion": "Validez oficial con R.M. 0871/2016",
        "color": "blue",
    },
    {
        "icono": "briefcase",
        "titulo": "Formación práctica",
        "descripcion": "Laboratorios y docentes especializados",
        "color": "cyan",
    },
    {
        "icono": "trending-up",
        "titulo": "100% empleabilidad",
        "descripcion": "Egresados trabajando en su área",
        "color": "violet",
    },
    {
        "icono": "building-2",
        "titulo": "Convenios con empresas",
        "descripcion": "Más de 15 aliados en la industria",
        "color": "orange",
    },
    {
        "icono": "book-open",
        "titulo": "Formación integral",
        "descripcion": "Habilidades técnicas + blandas",
        "color": "green",
    },
    {
        "icono": "users",
        "titulo": "Comunidad activa",
        "descripcion": "Red de 500+ egresados conectados",
        "color": "pink",
    },
    {
        "icono": "wallet",
        "titulo": "Planes de pago",
        "descripcion": "Mensualidades accesibles y becas",
        "color": "amber",
    },
]

FORMAS_INSCRIPCION: list[FormaInscripcion] = [
    {
        "icono": "map-pin",
        "titulo": "Presencial",
        "subtitulo": "Visítanos en el campus",
        "descripcion": (
            "Galería FLOR DE ORO, 1er piso. Calle Jorge Carrasco entre "
            "3 y 4."
        ),
        "cta_texto": "Ver ubicación",
        "cta_url": "/contacto",
        "externo": False,
        "color": "blue",
    },
    {
        "icono": "message-circle",
        "titulo": "WhatsApp",
        "subtitulo": "La forma más rápida",
        "descripcion": (
            f"Escríbenos al {TELEFONO_PRINCIPAL}. Te respondemos en "
            f"minutos."
        ),
        "cta_texto": "Abrir WhatsApp",
        "cta_url": WHATSAPP_URL,
        "externo": True,
        "color": "green",
    },
    {
        "icono": "mail",
        "titulo": "Correo electrónico",
        "subtitulo": "Para consultas formales",
        "descripcion": (
            f"Escríbenos a {EMAIL_CONTACTO} y te enviamos toda la "
            f"información."
        ),
        "cta_texto": "Enviar correo",
        "cta_url": f"mailto:{EMAIL_CONTACTO}",
        "externo": True,
        "color": "violet",
    },
]

PREGUNTAS_ADMISION: list[ItemFaq] = [
    {
        "pregunta": "¿Realmente puedo inscribirme en cualquier momento?",
        "respuesta": (
            "Sí. Como instituto privado, no tenemos fechas límite de "
            "inscripción. Puedes iniciar tu proceso cualquier día del "
            "año y comenzar clases el siguiente lunes disponible."
        ),
    },
    {
        "pregunta": "¿Hay examen de admisión?",
        "respuesta": (
            "No hay examen de admisión. Solo coordinamos una entrevista "
            "breve para conocerte, entender tus metas y asegurarnos de "
            "que la carrera elegida sea la adecuada para ti."
        ),
    },
    {
        "pregunta": "¿Los cupos son limitados?",
        "respuesta": (
            "Cada carrera tiene un cupo máximo por turno para garantizar "
            "la calidad educativa. Por eso recomendamos inscribirse lo "
            "antes posible. Los cupos se asignan por orden de inscripción."
        ),
    },
    {
        "pregunta": "¿Cuánto cuesta estudiar en INSTEIN?",
        "respuesta": (
            "Ofrecemos planes de pago accesibles con mensualidades "
            "cómodas. Escríbenos por WhatsApp para recibir el detalle "
            "de costos de tu carrera específica."
        ),
    },
    {
        "pregunta": "¿Hay becas o descuentos disponibles?",
        "respuesta": (
            "Sí. Contamos con becas por mérito académico, descuentos "
            "por pago anual adelantado y convenios con empresas. "
            "Consulta con admisiones los detalles."
        ),
    },
    {
        "pregunta": "¿Puedo visitar el campus antes de inscribirme?",
        "respuesta": (
            "Por supuesto. Te invitamos a conocer nuestras "
            "instalaciones, laboratorios y aulas. Coordina tu visita "
            "por WhatsApp o teléfono."
        ),
    },
    {
        "pregunta": "¿Qué pasa si no tengo todos los documentos?",
        "respuesta": (
            "No te preocupes. Puedes iniciar el proceso con lo que "
            "tengas y completar la documentación en los primeros días "
            "de clases."
        ),
    },
    {
        "pregunta": "¿Puedo trabajar mientras estudio?",
        "respuesta": (
            "Sí. Todas las carreras tienen turno nocturno (19:00 - "
            "22:00) y turno de sábados (09:00 - 14:30) especialmente "
            "diseñados para estudiantes que trabajan."
        ),
    },
]


# ======================================================================
# Hero
# ======================================================================


def _hero_admision() -> rx.Component:
    """
    Hero de la página de admisión.

    Estilo Neon.com:
    - Badge con punto verde pulsante.
    - Título con énfasis bicolor.
    - Subtítulo descriptivo.
    - Alineado a la izquierda (no centrado).
    """
    return rx.box(
        rx.vstack(
            # ─── Badge ─────────────────────────────────────────
            rx.flex(
                rx.box(
                    height="0.5rem",
                    width="0.5rem",
                    border_radius=RADIO_PASTILLA,
                    background=rx.color("green", 9),
                    animation="pulse 2s ease-in-out infinite",
                    flex_shrink="0",
                ),
                rx.text(
                    "INSCRIPCIONES ABIERTAS TODO EL AÑO",
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
                rx.text.span("Guía de "),
                rx.text.span(
                    "Admisión",
                    color=AZUL_MARINO_NEON,
                ),
                as_="h1",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                letter_spacing="-0.03em",
                line_height="1.1",
                max_width="48rem",
            ),
            # ─── Subtítulo ─────────────────────────────────────
            rx.text(
                "Todo lo que necesitas saber para convertirte en "
                "Técnico Superior. Sin fechas límite, sin sorteo, "
                "sin complicaciones.",
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
            f"4rem {PADDING_SECCION_HORIZONTAL} 2rem {PADDING_SECCION_HORIZONTAL}",
            f"6rem {PADDING_SECCION_HORIZONTAL} 3rem {PADDING_SECCION_HORIZONTAL}",
        ],
        width="100%",
    )


# ======================================================================
# Grid de ventajas destacadas
# ======================================================================


def _tarjeta_ventaja(item: dict) -> rx.Component:
    """Tarjeta de ventaja destacada."""
    color_scheme = item["color"]

    return rx.box(
        rx.vstack(
            rx.flex(
                rx.icon(
                    item["icono"],
                    size=20,
                    color=rx.color(color_scheme, 11),
                ),
                height="2.5rem",
                width="2.5rem",
                border_radius=RADIO_GRANDE,
                background=rx.color(color_scheme, 3),
                border=f"1px solid {rx.color(color_scheme, 7)}",
                align="center",
                justify="center",
                margin_bottom="0.75rem",
                flex_shrink="0",
            ),
            rx.text(
                item["titulo"],
                font_size="0.9375rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
            ),
            rx.text(
                item["descripcion"],
                font_size="0.8125rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
            ),
            align="start",
            spacing="1",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        background=COLOR_FONDO_CARTA,
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={
            "border_color": rx.color(color_scheme, 7),
        },
    )


def _grid_ventajas() -> rx.Component:
    """Grid con las 3 tarjetas de ventajas destacadas."""
    return rx.box(
        rx.grid(
            *[_tarjeta_ventaja(item) for item in VENTAJAS_DESTACADAS],
            columns=rx.breakpoints(initial="1", md="3"),
            spacing="4",
            width="100%",
        ),
        max_width=ANCHO_MAXIMO,
        margin="0 auto",
        padding=[
            f"0 {PADDING_SECCION_HORIZONTAL} 3rem {PADDING_SECCION_HORIZONTAL}",
            f"0 {PADDING_SECCION_HORIZONTAL} 4rem {PADDING_SECCION_HORIZONTAL}",
        ],
        width="100%",
    )


# ======================================================================
# Sección 01 — Proceso de admisión (timeline)
# ======================================================================


def _paso_timeline(
    paso: Paso,
    indice: int,
    total: int,
) -> rx.Component:
    """Paso individual del timeline de admisión."""
    es_ultimo = indice == total - 1

    return rx.flex(
        # ─── Número + línea vertical ────────────────────────────
        rx.vstack(
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
            rx.cond(
                not es_ultimo,
                rx.box(
                    width="2px",
                    background=COLOR_DIVISOR,
                    flex="1",
                    min_height="2rem",
                ),
                rx.fragment(),
            ),
            align="center",
            spacing="0",
            height="100%",
            flex_shrink="0",
        ),
        # ─── Tarjeta con contenido del paso ─────────────────────
        rx.box(
            rx.flex(
                rx.flex(
                    rx.icon(
                        paso["icono"],
                        size=20,
                        color=AZUL_MARINO_NEON,
                    ),
                    height="2.5rem",
                    width="2.5rem",
                    border_radius=RADIO_MEDIO,
                    background=FONDO_AZUL_SUAVE,
                    border=f"1px solid {AZUL_MARINO_NEON}",
                    align="center",
                    justify="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(
                        paso["titulo"],
                        font_size="1rem",
                        font_weight="700",
                        color=TEXTO_HOME_PRINCIPAL,
                        line_height="1.3",
                    ),
                    rx.text(
                        paso["descripcion"],
                        font_size="0.875rem",
                        color=TEXTO_HOME_MAS_SUAVE,
                        line_height="1.6",
                    ),
                    align="start",
                    spacing="1",
                    flex="1",
                    min_width="0",
                ),
                align="start",
                gap="1rem",
                width="100%",
            ),
            padding="1.25rem",
            border_radius=RADIO_EXTRA_GRANDE,
            background=COLOR_FONDO_CARTA,
            border=f"1px solid {COLOR_BORDE_SUAVE}",
            width="100%",
            margin_bottom="1rem" if not es_ultimo else "0",
            margin_left="0.75rem",
            transition="all 0.2s",
            _hover={
                "border_color": AZUL_MARINO_NEON,
            },
        ),
        align="start",
        gap="1rem",
        width="100%",
    )


def _seccion_proceso() -> rx.Component:
    """Sección del proceso de admisión paso a paso."""
    total = len(PASOS_ADMISION)

    return rx.vstack(
        *[
            _paso_timeline(paso, i, total)
            for i, paso in enumerate(PASOS_ADMISION)
        ],
        spacing="0",
        width="100%",
    )


# ======================================================================
# Sección 02 — Requisitos
# ======================================================================


def _tarjeta_requisito(item: Requisito) -> rx.Component:
    """Item individual de requisito."""
    return rx.flex(
        rx.flex(
            rx.icon(
                item["icono"],
                size=16,
                color=AZUL_MARINO_NEON,
            ),
            height="2rem",
            width="2rem",
            border_radius=RADIO_MEDIO,
            background=FONDO_AZUL_SUAVE,
            border=f"1px solid {AZUL_MARINO_NEON}",
            align="center",
            justify="center",
            flex_shrink="0",
        ),
        rx.text(
            item["texto"],
            font_size="0.875rem",
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.5",
            flex="1",
        ),
        align="center",
        gap="0.875rem",
        width="100%",
        padding="0.875rem 1rem",
        border_radius=RADIO_MEDIO,
        background=COLOR_FONDO_SUAVE,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        transition="all 0.2s",
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


def _columna_requisitos(
    titulo: str,
    icono: str,
    items: list[Requisito],
) -> rx.Component:
    """Columna de requisitos (documentos o académicos)."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.flex(
                    rx.icon(
                        icono,
                        size=18,
                        color=AZUL_MARINO_NEON,
                    ),
                    height="2.25rem",
                    width="2.25rem",
                    border_radius=RADIO_MEDIO,
                    background=FONDO_AZUL_SUAVE,
                    border=f"1px solid {AZUL_MARINO_NEON}",
                    align="center",
                    justify="center",
                    flex_shrink="0",
                ),
                rx.text(
                    titulo,
                    font_size="1rem",
                    font_weight="700",
                    color=TEXTO_HOME_PRINCIPAL,
                ),
                align="center",
                gap="0.75rem",
                margin_bottom="1rem",
            ),
            rx.vstack(
                *[_tarjeta_requisito(item) for item in items],
                spacing="2",
                width="100%",
            ),
            align="start",
            spacing="2",
            width="100%",
            height="100%",
        ),
        padding="1.5rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        width="100%",
        height="100%",
    )


def _seccion_requisitos() -> rx.Component:
    """Sección con los requisitos de admisión."""
    return rx.grid(
        _columna_requisitos(
            "Documentos personales",
            "file-text",
            REQUISITOS_DOCUMENTOS,
        ),
        _columna_requisitos(
            "Requisitos académicos",
            "graduation-cap",
            REQUISITOS_ACADEMICOS,
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 03 — Beneficios
# ======================================================================


def _tarjeta_beneficio(item: Beneficio) -> rx.Component:
    """Tarjeta individual de beneficio."""
    color_scheme = item["color"]

    return rx.box(
        rx.vstack(
            rx.flex(
                rx.icon(
                    item["icono"],
                    size=20,
                    color=rx.color(color_scheme, 11),
                ),
                height="2.25rem",
                width="2.25rem",
                border_radius=RADIO_MEDIO,
                background=rx.color(color_scheme, 3),
                border=f"1px solid {rx.color(color_scheme, 7)}",
                align="center",
                justify="center",
                margin_bottom="0.75rem",
                flex_shrink="0",
            ),
            rx.text(
                item["titulo"],
                font_size="0.875rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.3",
            ),
            rx.text(
                item["descripcion"],
                font_size="0.75rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.5",
            ),
            align="start",
            spacing="1",
            width="100%",
            height="100%",
        ),
        padding="1.25rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={
            "border_color": rx.color(color_scheme, 7),
        },
    )


def _seccion_beneficios() -> rx.Component:
    """Sección con los beneficios de elegir INSTEIN."""
    return rx.grid(
        *[_tarjeta_beneficio(item) for item in BENEFICIOS],
        columns=rx.breakpoints(initial="1", sm="2", lg="4"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 04 — Formas de inscripción
# ======================================================================


def _tarjeta_forma_inscripcion(item: FormaInscripcion) -> rx.Component:
    """Tarjeta individual de forma de inscripción."""
    color_scheme = item["color"]

    return rx.box(
        rx.vstack(
            rx.flex(
                rx.icon(
                    item["icono"],
                    size=24,
                    color=rx.color(color_scheme, 11),
                ),
                height="3rem",
                width="3rem",
                border_radius=RADIO_GRANDE,
                background=rx.color(color_scheme, 3),
                border=f"1px solid {rx.color(color_scheme, 7)}",
                align="center",
                justify="center",
                margin_bottom="1rem",
                flex_shrink="0",
            ),
            rx.text(
                item["titulo"],
                font_size="1rem",
                font_weight="800",
                color=TEXTO_HOME_PRINCIPAL,
                line_height="1.2",
            ),
            rx.text(
                item["subtitulo"],
                font_size="0.75rem",
                font_weight="600",
                color=rx.color(color_scheme, 11),
                text_transform="uppercase",
                letter_spacing="0.05em",
            ),
            rx.text(
                item["descripcion"],
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
                line_height="1.6",
                margin_top="0.5rem",
            ),
            rx.link(
                rx.text(
                    item["cta_texto"],
                    as_="span",
                    font_size="0.875rem",
                    font_weight="700",
                    color=rx.color(color_scheme, 11),
                ),
                rx.icon("arrow-right", size=14, color=rx.color(color_scheme, 11)),
                href=item["cta_url"],
                is_external=item["externo"],
                text_decoration="none",
                display="inline-flex",
                align_items="center",
                gap="0.375rem",
                margin_top="1rem",
                padding="0.625rem 1.25rem",
                border_radius=RADIO_PASTILLA,
                background=rx.color(color_scheme, 3),
                border=f"1px solid {rx.color(color_scheme, 7)}",
                transition="all 0.2s",
                _hover={
                    "background": rx.color(color_scheme, 4),
                },
            ),
            align="start",
            spacing="1",
            width="100%",
            height="100%",
        ),
        padding="1.75rem",
        border_radius=RADIO_EXTRA_GRANDE,
        background=COLOR_FONDO_CARTA,
        border=f"1px solid {COLOR_BORDE_SUAVE}",
        width="100%",
        height="100%",
        transition="all 0.2s",
        _hover={
            "border_color": rx.color(color_scheme, 7),
        },
    )


def _seccion_formas_inscripcion() -> rx.Component:
    """Sección con las 3 formas de inscripción."""
    return rx.grid(
        *[
            _tarjeta_forma_inscripcion(item)
            for item in FORMAS_INSCRIPCION
        ],
        columns=rx.breakpoints(initial="1", md="3"),
        spacing="4",
        width="100%",
        align_items="stretch",
    )


# ======================================================================
# Sección 05 — FAQ
# ======================================================================


def _seccion_faq() -> rx.Component:
    """Sección de preguntas frecuentes de admisión."""
    return acordeon_faq(
        items=PREGUNTAS_ADMISION,
        variante="light",
        icono="help-circle",
        color_acento=AZUL_MARINO_NEON,
        max_width="56rem",
    )


# ======================================================================
# Sección 06 — CTA final
# ======================================================================


def _cta_admision() -> rx.Component:
    """Bloque CTA final hacia /contacto."""
    return rx.flex(
        rx.text(
            "¿Listo para dar el primer paso?",
            font_size="1rem",
            color=TEXTO_HOME_MAS_SUAVE,
        ),
        rx.link(
            rx.text(
                "Contáctanos",
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
    route="/admision",
    title=f"Guía de Admisión | {NOMBRE_INSTITUTO}",
    description=(
        "Guía completa de admisión del Instituto Técnico Integrado "
        "San Antonio de Padua (INSTEIN): proceso paso a paso, "
        "requisitos, formas de inscripción y beneficios."
    ),
)
def vista_admision() -> rx.Component:
    """
    Página de la guía de admisión del instituto — estilo Neon.com.

    Estructura semántica HTML5:
    - `<header role="banner">`      → barra de navegación.
    - `<main>`                      → contenido principal.
    - `<section>`                   → cada sección temática.
    - `<footer role="contentinfo">` → pie de página.
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
                _hero_admision(),
                # ─── Grid de ventajas destacadas ────────────────────
                _grid_ventajas(),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 01 — Proceso ───────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="01",
                            etiqueta="Proceso de admisión",
                            titulo="Inscríbete",
                            titulo_enfasis="en 5 pasos",
                            subtitulo=(
                                "Un proceso simple y rápido. Sin "
                                "exámenes de admisión, sin sorteos, "
                                "sin complicaciones."
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
                    aria_label="Proceso de admisión",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 02 — Requisitos ────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="02",
                            etiqueta="Requisitos",
                            titulo="Lo que necesitas",
                            titulo_enfasis="para inscribirte",
                            subtitulo=(
                                "Documentos personales y académicos. "
                                "Si te falta algo, contáctanos y te "
                                "ayudamos a resolverlo."
                            ),
                        ),
                        _seccion_requisitos(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="requisitos",
                    aria_label="Requisitos de admisión",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 03 — Beneficios ────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="03",
                            etiqueta="¿Por qué elegirnos?",
                            titulo="Razones para estudiar",
                            titulo_enfasis="en INSTEIN",
                            subtitulo=(
                                "Formación de excelencia con respaldo "
                                "oficial y proyección profesional real."
                            ),
                        ),
                        _seccion_beneficios(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="beneficios",
                    aria_label="Beneficios de estudiar en INSTEIN",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 04 — Formas de inscripción ─────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="04",
                            etiqueta="Formas de inscripción",
                            titulo="Elige cómo",
                            titulo_enfasis="contactarnos",
                            subtitulo=(
                                "Tres canales para iniciar tu proceso "
                                "de admisión. Elige el que más te "
                                "convenga."
                            ),
                        ),
                        _seccion_formas_inscripcion(),
                        max_width=ANCHO_MAXIMO,
                        margin="0 auto",
                        padding=[
                            f"4rem {PADDING_SECCION_HORIZONTAL}",
                            f"6rem {PADDING_SECCION_HORIZONTAL}",
                        ],
                        width="100%",
                    ),
                    width="100%",
                    id="formas",
                    aria_label="Formas de inscripción",
                    scroll_margin_top="5rem",
                ),
                # ─── Separador ──────────────────────────────────────
                separador_secciones(ancho_maximo=ANCHO_MAXIMO),
                # ─── Sección 05 — FAQ ───────────────────────────────
                rx.el.section(
                    rx.box(
                        encabezado_seccion(
                            numero="05",
                            etiqueta="Preguntas frecuentes",
                            titulo="Dudas comunes",
                            titulo_enfasis="sobre admisión",
                            subtitulo=(
                                "Las preguntas que más nos hacen "
                                "quienes quieren estudiar con nosotros."
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
                    aria_label="Preguntas frecuentes sobre admisión",
                    scroll_margin_top="5rem",
                ),
                # ─── Sección 06 — CTA final ─────────────────────────
                rx.el.section(
                    rx.box(
                        _cta_admision(),
                        max_width=ANCHO_CONTENIDO,
                        margin="0 auto",
                        padding_x=PADDING_SECCION_HORIZONTAL,
                        padding_bottom="6rem",
                        width="100%",
                    ),
                    width="100%",
                    id="cta-final",
                    aria_label="Contacto final",
                    scroll_margin_top="5rem",
                ),
                width="100%",
                aria_label="Guía de admisión",
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
    "Beneficio",
    "FormaInscripcion",
    "Paso",
    "Requisito",
    "vista_admision",
]