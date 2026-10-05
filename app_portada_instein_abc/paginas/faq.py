"""
Vista de Preguntas Frecuentes (ruta "/faq") — estilo Neon.com.

Contenido
---------
1. Hero con título + subtítulo (alineado a la izquierda).
2. Chips de filtro por carrera (6 opciones):
   - General (instituto).
   - Sistemas.
   - Contaduría.
   - Secretariado.
   - Comercio Internacional.
   - Electrónica.
3. Acordeón con las preguntas filtradas.
4. CTA final hacia /contacto.

Diseño
------
Refactorizado al estilo Neon.com:

1. **Layout izquierdo** del hero.
2. **Chips de filtro** con icono + estado activo.
3. **State tipado** con handler `cambiar_carrera`.
4. **Acordeón reutilizado** del componente unificado.
5. **Responsive mobile-first**.
6. **Dark mode adaptativo**.

Sistema de color
----------------
✅ ADAPTATIVO: todos los colores respetan el `color_mode`.
✅ ACENTO ÚNICO: azul marino neon (`#3b5bdb`).

Nota técnica: FUENTE DE LAS PREGUNTAS
-------------------------------------
Hay 2 fuentes de preguntas:

1. **Generales** (`PREGUNTAS_GENERALES`): preguntas sobre el
   instituto, inscripciones, títulos, etc.

2. **Por carrera** (`PREGUNTAS_POR_CARRERA`): preguntas específicas
   de cada carrera técnica.

El filtro "General" muestra las generales; cualquier otra opción
muestra las específicas de esa carrera.

Nota técnica: STATE
-------------------
`EstadoFAQ` maneja el filtro activo. Al cambiar de carrera, el
acordeón se re-renderiza con las nuevas preguntas.

⚠️ El acordeón `EstadoAcordeonFaq` (global) mantiene el índice
abierto. Si cambias de carrera con un item abierto, el índice puede
apuntar a un item que ya no existe. Por eso, al cambiar de carrera
se resetea el índice a -1.

Nota técnica: SIN ENCABEZADO NUMERADO
-------------------------------------
Esta vista NO usa `encabezado_seccion` con número. A diferencia
de `inicio.py` o `carreras.py` (que tienen múltiples secciones
temáticas), esta página es un flujo único: hero + filtros +
acordeón. Un encabezado numerado `01` sería redundante con el hero
y rompería la coherencia visual.

Nota técnica: COMPONENTES COMPARTIDOS
-------------------------------------
Este archivo usa los componentes compartidos:

- `ItemFaq` y `acordeon_faq` (de `..componentes.base`).
- `separador_secciones` (de `..componentes.base`).

Antes tenía copias locales `_separador_secciones`. Ahora vive
una sola implementación en `componentes/base/`.
"""

from __future__ import annotations

from typing import TypedDict

import reflex as rx

from ..componentes.base import (
    ItemFaq,
    acordeon_faq,
)
from ..componentes.navegacion import (
    barra_navegacion_superior,
    pie_pagina_institucional,
)
from ..dominio.estados.estado_acordeon_faq import EstadoAcordeonFaq
from ..infraestructura import (
    AZUL_MARINO_NEON,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    COLOR_DIVISOR,
    FONDO_HOME,
    NOMBRE_INSTITUTO,
    RADIO_PASTILLA,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
)


# ======================================================================
# Constantes locales
# ======================================================================

ANCHO_MAXIMO_CONTENIDO: str = "72rem"
PADDING_SECCION_HORIZONTAL: str = "1.5rem"


# ======================================================================
# Tipos
# ======================================================================


class CarreraFiltro(TypedDict):
    """Opción de filtro por carrera."""

    valor: str
    etiqueta: str
    icono: str


# ======================================================================
# Datos: filtros por carrera
# ======================================================================

FILTROS_CARRERA: list[CarreraFiltro] = [
    {
        "valor": "general",
        "etiqueta": "General",
        "icono": "building-2",
    },
    {
        "valor": "sistemas",
        "etiqueta": "Sistemas",
        "icono": "cpu",
    },
    {
        "valor": "contaduria",
        "etiqueta": "Contaduría",
        "icono": "calculator",
    },
    {
        "valor": "secretariado",
        "etiqueta": "Secretariado",
        "icono": "briefcase",
    },
    {
        "valor": "comercio",
        "etiqueta": "Comercio Int.",
        "icono": "globe",
    },
    {
        "valor": "electronica",
        "etiqueta": "Electrónica",
        "icono": "zap",
    },
]


# ======================================================================
# Datos: preguntas generales (instituto)
# ======================================================================

PREGUNTAS_GENERALES: list[ItemFaq] = [
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
# Datos: preguntas específicas por carrera
# ======================================================================

PREGUNTAS_POR_CARRERA: dict[str, list[ItemFaq]] = {
    # ─── Sistemas Informáticos ─────────────────────────────────
    "sistemas": [
        {
            "pregunta": "¿Necesito saber programar antes de entrar?",
            "respuesta": (
                "No, empezamos desde cero. En el primer año aprenderás "
                "lógica de programación y fundamentos de informática."
            ),
        },
        {
            "pregunta": "¿Qué lenguajes de programación voy a aprender?",
            "respuesta": (
                "Python, JavaScript, SQL y fundamentos de Java. Además, "
                "HTML/CSS para desarrollo web y frameworks modernos."
            ),
        },
        {
            "pregunta": "¿Qué equipos necesito tener?",
            "respuesta": (
                "Contamos con laboratorios equipados. Si quieres "
                "practicar en casa, una laptop básica con 8GB de RAM "
                "es suficiente."
            ),
        },
        {
            "pregunta": "¿Qué salidas laborales tengo al egresar?",
            "respuesta": (
                "Desarrollador junior, soporte técnico, administrador "
                "de redes, tester QA, analista de sistemas y más."
            ),
        },
        {
            "pregunta": "¿Qué certificaciones puedo obtener?",
            "respuesta": (
                "Preparamos para certificaciones Cisco CCNA, AWS "
                "Cloud Practitioner y fundamentos de ciberseguridad."
            ),
        },
    ],
    # ─── Contaduría General ────────────────────────────────────
    "contaduria": [
        {
            "pregunta": "¿Necesito conocimientos previos de contabilidad?",
            "respuesta": (
                "No, comenzamos desde contabilidad básica. Solo se "
                "requiere manejo de matemática básica y ganas de "
                "aprender."
            ),
        },
        {
            "pregunta": "¿Qué software contable voy a aprender?",
            "respuesta": (
                "Aprenderás sistemas contables computarizados, manejo "
                "de hojas de cálculo y software tributario boliviano "
                "(SIAT, SICON)."
            ),
        },
        {
            "pregunta": "¿Puedo firmar balances al egresar?",
            "respuesta": (
                "Como Técnico Superior puedes llevar contabilidad de "
                "empresas, aunque la firma oficial de balances "
                "requiere título profesional universitario."
            ),
        },
        {
            "pregunta": "¿La carrera incluye práctica tributaria?",
            "respuesta": (
                "Sí, en segundo y tercer año trabajarás con casos "
                "reales de declaraciones de impuestos y normativa "
                "vigente."
            ),
        },
        {
            "pregunta": "¿Qué salidas laborales tengo al egresar?",
            "respuesta": (
                "Auxiliar contable, asistente tributario, contador de "
                "microempresas, analista de costos y más."
            ),
        },
    ],
    # ─── Secretariado Ejecutivo ────────────────────────────────
    "secretariado": [
        {
            "pregunta": "¿Qué habilidades voy a desarrollar?",
            "respuesta": (
                "Redacción ejecutiva, manejo de agendas, organización "
                "de eventos, atención al cliente y herramientas "
                "ofimáticas avanzadas."
            ),
        },
        {
            "pregunta": "¿Se enseña inglés?",
            "respuesta": (
                "Sí, Inglés Técnico I y II en los dos primeros años, "
                "enfocado a comunicación empresarial y protocolo."
            ),
        },
        {
            "pregunta": "¿Qué software aprenderé?",
            "respuesta": (
                "Word, Excel avanzado, PowerPoint, herramientas de "
                "gestión documental y sistemas de gestión ejecutiva."
            ),
        },
        {
            "pregunta": "¿Puedo trabajar en empresas grandes?",
            "respuesta": (
                "Sí, el perfil está diseñado para trabajar en "
                "gerencias, direcciones ejecutivas y atención al "
                "cliente en empresas e instituciones."
            ),
        },
        {
            "pregunta": "¿Qué salidas laborales tengo al egresar?",
            "respuesta": (
                "Secretaria ejecutiva, asistente administrativa, "
                "recepcionista bilingüe, coordinadora de eventos y más."
            ),
        },
    ],
    # ─── Comercio Internacional ────────────────────────────────
    "comercio": [
        {
            "pregunta": "¿Qué es el SIDUNEA?",
            "respuesta": (
                "Es el Sistema Informático Aduanero usado en Bolivia "
                "y varios países de la región. Aprenderás a usarlo en "
                "tercer año."
            ),
        },
        {
            "pregunta": "¿Se enseña normativa aduanera?",
            "respuesta": (
                "Sí, Legislación Aduanera I y II cubren toda la "
                "normativa vigente boliviana y tratados "
                "internacionales."
            ),
        },
        {
            "pregunta": "¿Puedo trabajar en agencias despachantes?",
            "respuesta": (
                "Sí, es una de las principales salidas. También en "
                "importadoras, exportadoras y operadores logísticos."
            ),
        },
        {
            "pregunta": "¿Qué idiomas se enseñan?",
            "respuesta": (
                "Inglés Técnico I y II enfocado a comercio exterior. "
                "Se recomienda inglés básico previo pero no es "
                "obligatorio."
            ),
        },
        {
            "pregunta": "¿Qué salidas laborales tengo al egresar?",
            "respuesta": (
                "Auxiliar de despachante, asistente de comercio "
                "exterior, operador logístico, analista de "
                "importaciones y más."
            ),
        },
    ],
    # ─── Electrónica ───────────────────────────────────────────
    "electronica": [
        {
            "pregunta": "¿Qué equipos voy a usar en los laboratorios?",
            "respuesta": (
                "Osciloscopios, multímetros, generadores de señales, "
                "estaciones de soldadura y microcontroladores "
                "PIC/Arduino/ESP32."
            ),
        },
        {
            "pregunta": "¿Se enseña programación de microcontroladores?",
            "respuesta": (
                "Sí, en tercer año. Trabajarás con Arduino, PIC y "
                "ESP32 para proyectos de automatización y domótica."
            ),
        },
        {
            "pregunta": "¿Puedo reparar equipos electrónicos al egresar?",
            "respuesta": (
                "Sí, tendrás todas las competencias para reparar "
                "equipos domésticos, industriales y de "
                "telecomunicaciones."
            ),
        },
        {
            "pregunta": "¿La carrera incluye automatización industrial?",
            "respuesta": (
                "Sí, es parte del tercer año. Aprenderás PLCs, "
                "sensores y sistemas de control industrial."
            ),
        },
        {
            "pregunta": "¿Qué salidas laborales tengo al egresar?",
            "respuesta": (
                "Técnico electrónico, mantenedor industrial, "
                "instalador de telecomunicaciones y emprendedor de "
                "servicios técnicos."
            ),
        },
    ],
}


# ======================================================================
# Estado
# ======================================================================


class EstadoFAQ(rx.State):
    """
    Estado de los filtros de la página de FAQ.

    Atributos:
        carrera_activa: Clave de la carrera seleccionada
            (`"general"` por defecto).
    """

    carrera_activa: str = "general"

    @rx.event
    def cambiar_carrera(self, valor: str):
        """
        Cambia la carrera activa del filtro.

        ⚠️ Resetea el índice del acordeón global (`EstadoAcordeonFaq`)
        porque al cambiar de filtro las preguntas cambian y el
        índice abierto podría apuntar a un item que ya no existe.

        Args:
            valor: Clave de la carrera (`"general"`, `"sistemas"`,
                etc.).
        """
        self.carrera_activa = valor
        # Cerrar el acordeón al cambiar de filtro
        yield EstadoAcordeonFaq.alternar(-1)

    @rx.var
    def preguntas_visibles(self) -> list[ItemFaq]:
        """
        Preguntas visibles según el filtro activo.

        - Si `carrera_activa == "general"` → preguntas generales.
        - Si no → preguntas de la carrera específica.

        Returns:
            Lista de `ItemFaq` a mostrar en el acordeón.
        """
        if self.carrera_activa == "general":
            return PREGUNTAS_GENERALES
        return PREGUNTAS_POR_CARRERA.get(
            self.carrera_activa,
            PREGUNTAS_GENERALES,
        )

    @rx.var
    def total_preguntas(self) -> int:
        """Cantidad de preguntas visibles."""
        return len(self.preguntas_visibles)

    @rx.var
    def etiqueta_filtro_activo(self) -> str:
        """Etiqueta legible del filtro activo."""
        for filtro in FILTROS_CARRERA:
            if filtro["valor"] == self.carrera_activa:
                return filtro["etiqueta"]
        return "General"


# ======================================================================
# Chip de filtro
# ======================================================================


def _chip_filtro(filtro: CarreraFiltro) -> rx.Component:
    """
    Chip de filtro por carrera.

    Estilo Neon.com:
    - Activo: fondo azul marino + texto blanco.
    - Inactivo: fondo plano + borde sutil.
    - Hover: borde azul marino.

    Args:
        filtro: `CarreraFiltro` con `valor`, `etiqueta`, `icono`.

    Returns:
        Chip clicable.
    """
    esta_activo = EstadoFAQ.carrera_activa == filtro["valor"]

    return rx.box(
        rx.flex(
            rx.icon(
                filtro["icono"],
                size=14,
                color=rx.cond(
                    esta_activo,
                    "white",
                    AZUL_MARINO_NEON,
                ),
            ),
            rx.text(
                filtro["etiqueta"],
                font_size="0.8125rem",
                font_weight="600",
                color=rx.cond(
                    esta_activo,
                    "white",
                    TEXTO_HOME_PRINCIPAL,
                ),
                white_space="nowrap",
            ),
            align="center",
            gap="0.375rem",
        ),
        padding="0.5rem 0.875rem",
        border_radius=RADIO_PASTILLA,
        background=rx.cond(
            esta_activo,
            AZUL_MARINO_NEON,
            "transparent",
        ),
        border=rx.cond(
            esta_activo,
            f"1px solid {AZUL_MARINO_NEON}",
            f"1px solid {BORDE_HOME_MEDIO}",
        ),
        cursor="pointer",
        transition="all 0.2s",
        on_click=EstadoFAQ.cambiar_carrera(filtro["valor"]),
        _hover={
            "border_color": AZUL_MARINO_NEON,
        },
    )


def _fila_chips_filtros() -> rx.Component:
    """
    Fila de chips de filtro por carrera.

    Layout:
    - Flex-wrap: los chips se envuelven en múltiples líneas.
    - Gap: 0.5rem.
    """
    return rx.flex(
        *[_chip_filtro(f) for f in FILTROS_CARRERA],
        gap="0.5rem",
        flex_wrap="wrap",
        width="100%",
    )


# ======================================================================
# Hero
# ======================================================================


def _hero_faq() -> rx.Component:
    """
    Hero de la página FAQ con layout izquierdo.

    Estilo Neon.com:
    - Badge "PREGUNTAS FRECUENTES".
    - Título grande con énfasis bicolor.
    - Subtítulo descriptivo.
    - Alineado a la izquierda.
    """
    return rx.vstack(
        # ─── Badge ─────────────────────────────────────────────
        rx.flex(
            rx.icon("circle-help", size=12, color=AZUL_MARINO_NEON),
            rx.text(
                "PREGUNTAS FRECUENTES",
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
        # ─── Título con énfasis bicolor ────────────────────────
        rx.heading(
            rx.text.span("¿En qué podemos "),
            rx.text.span(
                "ayudarte?",
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
        # ─── Subtítulo ─────────────────────────────────────────
        rx.text(
            "Encuentra respuestas a las dudas más comunes sobre "
            "inscripciones, carreras, horarios y títulos. Filtra por "
            "carrera para ver preguntas específicas.",
            font_size=["1rem", "1.125rem"],
            color=TEXTO_HOME_MAS_SUAVE,
            line_height="1.6",
            max_width="48rem",
            margin_top="1rem",
        ),
        align="start",
        spacing="0",
        width="100%",
    )


# ======================================================================
# Sección de filtros + acordeón
# ======================================================================
def _seccion_preguntas() -> rx.Component:
    """
    Sección con chips de filtro + contador + acordeón.

    Estructura:
    1. Chips de filtro por carrera.
    2. Separador (divider).
    3. Header con contador dinámico.
    4. Acordeón con preguntas filtradas.

    Espaciado:
    - Chips → divider: 3rem (respiro suficiente).
    - Divider → contador: 3rem (respiro suficiente).
    """
    return rx.vstack(
        # ─── Chips de filtro ────────────────────────────────────
        rx.box(
            _fila_chips_filtros(),
            width="100%",
            padding_bottom="1rem",
        ),
        # ─── Separador interno ──────────────────────────────────
        rx.box(
            height="1px",
            width="100%",
            background=COLOR_DIVISOR,
            margin_y="3rem",
        ),
        # ─── Contador de preguntas ──────────────────────────────
        rx.flex(
            rx.text(
                "Mostrando",
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.text(
                EstadoFAQ.total_preguntas.to_string(),
                font_size="0.875rem",
                font_weight="700",
                color=AZUL_MARINO_NEON,
                padding="0.125rem 0.5rem",
                border_radius=RADIO_PASTILLA,
                background=rx.color_mode_cond(
                    light="rgba(59, 91, 219, 0.1)",
                    dark="rgba(59, 91, 219, 0.15)",
                ),
                border=f"1px solid {BORDE_HOME_AZUL}",
            ),
            rx.text(
                "preguntas sobre",
                font_size="0.875rem",
                color=TEXTO_HOME_MAS_SUAVE,
            ),
            rx.text(
                EstadoFAQ.etiqueta_filtro_activo,
                font_size="0.875rem",
                font_weight="700",
                color=TEXTO_HOME_PRINCIPAL,
            ),
            align="center",
            gap="0.5rem",
            flex_wrap="wrap",
            width="100%",
            margin_bottom="2rem",
        ),
        # ─── Acordeón con preguntas filtradas ───────────────────
        acordeon_faq(
            items=EstadoFAQ.preguntas_visibles,
            variante="light",
            icono="help-circle",
            color_acento=AZUL_MARINO_NEON,
            tamano_texto_pregunta="1rem",
            tamano_texto_respuesta="0.9375rem",
            padding_cabecera="1.25rem 1.5rem",
            padding_respuesta="0 1.5rem 1.25rem 3.5rem",
            max_width="56rem",
        ),
        spacing="0",
        width="100%",
        align="start",
    )

# ======================================================================
# CTA final
# ======================================================================


def _cta_final() -> rx.Component:
    """
    CTA final: "¿No encontraste tu respuesta?".
    """
    return rx.flex(
        rx.text(
            "¿No encontraste tu respuesta?",
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
            rx.icon(
                "arrow-right",
                size=16,
                color=AZUL_MARINO_NEON,
            ),
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
    route="/faq",
    title=f"Preguntas frecuentes | {NOMBRE_INSTITUTO}",
    description=(
        "Preguntas frecuentes sobre el Instituto Técnico Integrado "
        "San Antonio de Padua (INSTEIN): inscripciones, carreras, "
        "horarios, títulos y más."
    ),
)
def vista_faq() -> rx.Component:
    """
    Página dedicada a las preguntas frecuentes del instituto.

    Estructura semántica HTML5:
    - `<header>`               → barra de navegación.
    - `<main>`                 → contenido principal.
    - `<section>`              → sección de FAQ.
    - `<footer>`               → pie de página.
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
                rx.box(
                    rx.vstack(
    # ─── Hero ───────────────────────────────
    _hero_faq(),
    # ─── Sección de preguntas ───────────────
    rx.box(
        _seccion_preguntas(),
        padding_top="4rem",
        width="100%",
    ),
    # ─── CTA final ──────────────────────────
    _cta_final(),
    spacing="0",
    width="100%",
    align="start",
),
                    max_width=ANCHO_MAXIMO_CONTENIDO,
                    margin="0 auto",
                    padding=[
                        f"4rem {PADDING_SECCION_HORIZONTAL}",
                        f"6rem {PADDING_SECCION_HORIZONTAL}",
                    ],
                    width="100%",
                ),
                width="100%",
                aria_label="Preguntas frecuentes",
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
    "FILTROS_CARRERA",
    "PREGUNTAS_GENERALES",
    "PREGUNTAS_POR_CARRERA",
    "CarreraFiltro",
    "EstadoFAQ",
    "vista_faq",
]