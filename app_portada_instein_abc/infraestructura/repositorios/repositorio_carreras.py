"""
Repositorio de carreras técnicas del INSTEIN.

Este módulo encapsula el acceso al catálogo de carreras. Hoy el
catálogo es estático (hardcoded), pero el patrón repository permite
migrar a API/BD sin cambiar la capa de dominio ni los componentes.

Contenido
---------
- `Carrera`:              TypedDict con la estructura completa.
- `PlanAnual`:            TypedDict con el plan de estudios por año.
- `PreguntaFrecuente`:    TypedDict con las FAQ de cada carrera.
- `IconoAnimado`:         TypedDict con la config orbital de iconos.
- `EstadisticasCarrera`:  TypedDict con métricas de la carrera.
- `CaracteristicaCarrera`: TypedDict con badges informativos.
- `Turno`, `Modalidad`:   Literals con valores válidos.
- `CATALOGO_CARRERAS`:    Lista estática de las 5 carreras.
- `obtener_catalogo()`:   Devuelve una copia inmutable del catálogo.
- `obtener_carrera_por_id(id)`: Devuelve una carrera por ID.
- `obtener_carrera_destacada()`: Devuelve la carrera con `destacada=True`.

Nota técnica: TIPADO ESTRICTO CON `TypedDict`
---------------------------------------------
Los modelos usan `TypedDict` (no dataclasses) para ser compatibles
con `rx.foreach` sin `ForeachVarError`. Cada campo tiene un tipo
concreto (`str`, `int`, `list[T]`) que Reflex puede inferir.

Nota técnica: CACHÉ CON `@lru_cache`
------------------------------------
`obtener_catalogo()` y `obtener_carrera_por_id()` usan caché porque
el catálogo es inmutable. Esto evita reconstruir la lista completa
en cada render.

⚠️ Si en el futuro el catálogo se vuelve mutable, eliminar el caché.

Nota técnica: CAMPOS DE COLOR
-----------------------------
Cada carrera expone 4 colores para light/dark:
- `color_principal`, `color_suave`            → light mode
- `color_principal_dark`, `color_suave_dark`  → dark mode

⚠️ ACTUALMENTE NO SE USAN. El proyecto unificó el acento visual bajo
un único azul marino (`AZUL_MARINO_NEON`). Los campos se mantienen
para facilitar la reversión si se decide volver a colorear por
carrera.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal, TypedDict


# ======================================================================
# 1. Alias de tipos
# ======================================================================

ColorHex = str
"""Color en formato hexadecimal `#RRGGBB`."""

DemandaLaboral = Literal["alta", "media", "baja"]
"""Nivel de demanda laboral de una carrera."""

Modalidad = Literal["Presencial", "Semipresencial", "Virtual"]
"""Modalidad de cursado de la carrera."""

Turno = Literal["Mañana", "Tarde", "Noche", "Sábado"]
"""Turno de cursado de la carrera.

- `"Mañana"`  → 08:30 - 12:30
- `"Tarde"`   → 14:30 - 18:30
- `"Noche"`   → 19:00 - 22:00 (para quienes trabajan)
- `"Sábado"`  → 09:00 - 14:30 (intensivo)
"""


# ======================================================================
# 2. Constantes de turnos
# ======================================================================

TURNOS_VALIDOS: tuple[Turno, ...] = ("Mañana", "Tarde", "Noche", "Sábado")
"""Tupla con todos los turnos válidos."""

HORARIOS_TURNO: dict[Turno, str] = {
    "Mañana": "08:30 - 12:30",
    "Tarde": "14:30 - 18:30",
    "Noche": "19:00 - 22:00",
    "Sábado": "09:00 - 14:30",
}
"""Horario aproximado de cada turno (para UI)."""


# ======================================================================
# 3. Modelos anidados
# ======================================================================


class PlanAnual(TypedDict):
    """Un año del plan de estudios con sus materias."""

    anio: str
    materias: list[str]


class PreguntaFrecuente(TypedDict):
    """Pregunta frecuente específica de una carrera."""

    pregunta: str
    respuesta: str


class IconoAnimado(TypedDict):
    """
    Icono que orbita alrededor de la imagen de la carrera.

    Parámetros de una órbita elíptica kepleriana:
    - `semieje_mayor`      → radio horizontal (% del contenedor)
    - `excentricidad`      → 0.0 = círculo, 0.99 = muy elíptica
    - `factor_perspectiva` → aplanamiento vertical (0.5 = disco de lado)
    - `angulo_inicial`     → orientación en grados
    - `periodo`            → duración de una vuelta (segundos)
    - `desfase_temporal`   → retraso inicial (segundos)
    - `keyframe_orbita`    → nombre del @keyframes CSS generado
    """

    nombre: str
    semieje_mayor: float
    excentricidad: float
    factor_perspectiva: float
    angulo_inicial: int
    periodo: float
    desfase_temporal: float
    color: ColorHex
    tiene_anillos: bool
    keyframe_orbita: str


class EstadisticasCarrera(TypedDict):
    """Métricas cuantitativas de una carrera."""

    demanda_laboral: DemandaLaboral
    puntuacion: float
    estudiantes_inscritos: int
    estudiantes_graduados: int
    tasa_empleabilidad: int
    salario_promedio_bs: int


class CaracteristicaCarrera(TypedDict):
    """Característica destacada de una carrera (badge informativo)."""

    icono: str
    etiqueta: str
    descripcion: str


# ======================================================================
# 4. Modelo principal: Carrera
# ======================================================================


class Carrera(TypedDict):
    """
    Estructura completa de una carrera técnica.

    Sistema de color
    ----------------
    Cada carrera expone 4 colores para adaptarse al `color_mode`:

    **Light mode:**
        - `color_principal`: color de marca (hex).
        - `color_suave`:     tinte de fondo suave (hex).

    **Dark mode:**
        - `color_principal_dark`: color de marca ajustado (más luminoso).
        - `color_suave_dark`:     tinte de fondo oscuro con matiz.

    ⚠️ ACTUALMENTE NO SE USAN: el proyecto unificó el acento visual
    bajo un único azul marino (`AZUL_MARINO_NEON`).
    """

    # --- Identificación ---
    id: int
    nombre: str
    nombre_corto: str
    duracion: str
    lema: str
    descripcion: str
    destacada: bool

    # --- Contenido académico ---
    perfil_profesional: list[str]
    campo_laboral: list[str]
    preguntas_frecuentes: list[PreguntaFrecuente]
    plan_estudios: list[PlanAnual]

    # --- Icono principal ---
    icono: str

    # --- Colores (light + dark) ---
    color_principal: ColorHex
    color_suave: ColorHex
    color_principal_dark: ColorHex
    color_suave_dark: ColorHex

    # --- Recursos multimedia ---
    imagen_archivo: str
    imagen_banner: str
    iconos_animados: list[IconoAnimado]

    # --- Métricas y características ---
    estadisticas: EstadisticasCarrera
    caracteristicas: list[CaracteristicaCarrera]

    # --- Cursado ---
    modalidad: Modalidad
    turnos: list[Turno]
    cupos_disponibles: int


class CarreraConEtiqueta(TypedDict):
    """Carrera + etiqueta contextual (para el carrusel del hero)."""

    carrera: Carrera
    etiqueta: str


# ======================================================================
# 5. Helper de construcción de iconos orbitales
# ======================================================================

PERSPECTIVA_DEFECTO: float = 0.5
"""Factor de aplanamiento vertical por defecto para las órbitas."""


def _icono_orbital_config(
    nombre: str,
    semieje_mayor: float,
    excentricidad: float,
    factor_perspectiva: float,
    angulo_inicial: int,
    periodo: float,
    desfase_temporal: float,
    color: str,
    tiene_anillos: bool = False,
) -> IconoAnimado:
    """
    Construye un `IconoAnimado` con sus parámetros orbitales.

    Args:
        nombre: Nombre del icono Lucide (kebab-case).
        semieje_mayor: Radio horizontal de la elipse (% contenedor).
        excentricidad: Excentricidad orbital (0 = círculo).
        factor_perspectiva: Aplanamiento vertical (0.5 = disco de lado).
        angulo_inicial: Ángulo inicial en grados.
        periodo: Duración de una vuelta completa (segundos).
        desfase_temporal: Retraso inicial (segundos).
        color: Color hex del icono.
        tiene_anillos: Si debe llevar anillos tipo Saturno.

    Returns:
        `IconoAnimado` listo para renderizar.
    """
    sufijo = f"{angulo_inicial}_{int(semieje_mayor * 10)}"

    return {
        "nombre": nombre,
        "semieje_mayor": semieje_mayor,
        "excentricidad": excentricidad,
        "factor_perspectiva": factor_perspectiva,
        "angulo_inicial": angulo_inicial,
        "periodo": periodo,
        "desfase_temporal": desfase_temporal,
        "color": color,
        "tiene_anillos": tiene_anillos,
        "keyframe_orbita": f"orbita_{sufijo}",
    }


# ======================================================================
# 6. Catálogo de carreras
# ======================================================================

_CATALOGO_CARRERAS: list[Carrera] = [
    # ==================================================================
    # Carrera 0 — Sistemas Informáticos
    # ==================================================================
    {
        "id": 0,
        "nombre": "Sistemas Informáticos",
        "nombre_corto": "Sistemas",
        "duracion": "3 Años",
        "lema": "Tecnología, desarrollo y soluciones digitales",
        "descripcion": (
            "El Técnico Superior en Sistemas Informáticos es un profesional "
            "integral capacitado para diseñar, desarrollar, implementar y "
            "mantener soluciones informáticas orientadas a las necesidades "
            "de empresas, instituciones y emprendimientos."
        ),
        "destacada": True,
        "perfil_profesional": [
            "Desarrollo de software y aplicaciones web y móviles.",
            "Administración de bases de datos y sistemas de información.",
            "Instalación y mantenimiento de redes y equipos informáticos.",
            "Soporte técnico especializado en hardware y software.",
            "Aplicación de buenas prácticas de ciberseguridad.",
        ],
        "campo_laboral": [
            "Empresas de desarrollo de software.",
            "Departamentos de TI en instituciones públicas y privadas.",
            "Emprendimientos tecnológicos independientes.",
            "Soporte técnico y consultoría informática.",
        ],
        "preguntas_frecuentes": [
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
                "pregunta": "¿Puedo trabajar mientras estudio?",
                "respuesta": (
                    "Sí, ofrecemos turno nocturno (19:00-22:00) y turno de "
                    "sábados (09:00-14:30) especialmente diseñados para "
                    "estudiantes que trabajan."
                ),
            },
            {
                "pregunta": "¿Qué equipos necesito tener?",
                "respuesta": (
                    "Contamos con laboratorios equipados. Si quieres practicar "
                    "en casa, una laptop básica con 8GB de RAM es suficiente."
                ),
            },
            {
                "pregunta": "¿Qué salidas laborales tengo al egresar?",
                "respuesta": (
                    "Desarrollador junior, soporte técnico, administrador de "
                    "redes, tester QA, analista de sistemas y más."
                ),
            },
        ],
        "plan_estudios": [
            {
                "anio": "Primer Año",
                "materias": [
                    "Introducción a la Informática",
                    "Matemática Aplicada",
                    "Lógica de Programación",
                    "Ofimática Avanzada",
                    "Ensamblaje y Mantenimiento de PCs",
                    "Comunicación y Redacción",
                    "Inglés Técnico I",
                ],
            },
            {
                "anio": "Segundo Año",
                "materias": [
                    "Programación Estructurada",
                    "Base de Datos I",
                    "Redes de Computadoras I",
                    "Diseño Web (HTML/CSS/JS)",
                    "Sistemas Operativos",
                    "Contabilidad Básica",
                    "Inglés Técnico II",
                ],
            },
            {
                "anio": "Tercer Año",
                "materias": [
                    "Programación Orientada a Objetos",
                    "Base de Datos II",
                    "Redes de Computadoras II",
                    "Desarrollo de Aplicaciones Web",
                    "Desarrollo de Aplicaciones Móviles",
                    "Seguridad Informática",
                    "Proyecto de Grado",
                ],
            },
        ],
        "icono": "cpu",
        "color_principal": "#2563eb",
        "color_suave": "#eff6ff",
        "color_principal_dark": "#60a5fa",
        "color_suave_dark": "#1e3a8a",
        "imagen_archivo": "sistemas.png",
        "imagen_banner": "sistemas_banner.avif",
        "iconos_animados": [
            _icono_orbital_config(
                "code-xml", 55.0, 0.25, PERSPECTIVA_DEFECTO,
                0, 18.0, 0.0, "#2563eb", True,
            ),
            _icono_orbital_config(
                "database", 70.0, 0.15, PERSPECTIVA_DEFECTO,
                90, 24.0, 3.0, "#0891b2",
            ),
            _icono_orbital_config(
                "wifi", 62.0, 0.30, PERSPECTIVA_DEFECTO,
                180, 21.0, 6.0, "#7c3aed",
            ),
            _icono_orbital_config(
                "terminal", 85.0, 0.20, PERSPECTIVA_DEFECTO,
                270, 27.0, 9.0, "#ea580c",
            ),
        ],
        "estadisticas": {
            "demanda_laboral": "alta",
            "puntuacion": 4.8,
            "estudiantes_inscritos": 87,
            "estudiantes_graduados": 234,
            "tasa_empleabilidad": 95,
            "salario_promedio_bs": 4500,
        },
        "caracteristicas": [
            {
                "icono": "cpu",
                "etiqueta": "Laboratorios equipados",
                "descripcion": "20 PCs con hardware moderno",
            },
            {
                "icono": "award",
                "etiqueta": "Certificación Cisco",
                "descripcion": "Preparación para CCNA",
            },
            {
                "icono": "code-2",
                "etiqueta": "Proyecto real",
                "descripcion": "Desarrollo con clientes reales",
            },
            {
                "icono": "briefcase",
                "etiqueta": "Pasantías",
                "descripcion": "Convenios con 15+ empresas de TI",
            },
        ],
        "modalidad": "Presencial",
        "turnos": ["Mañana", "Tarde", "Noche", "Sábado"],
        "cupos_disponibles": 30,
    },
    # ==================================================================
    # Carrera 1 — Contaduría General
    # ==================================================================
    {
        "id": 1,
        "nombre": "Contaduría General",
        "nombre_corto": "Contaduría",
        "duracion": "3 Años",
        "lema": "Gestión contable, tributaria y financiera",
        "descripcion": (
            "El Técnico Superior en Contaduría General es un profesional "
            "preparado para llevar registros contables, elaborar estados "
            "financieros, gestionar obligaciones tributarias y asesorar a "
            "empresas y emprendimientos."
        ),
        "destacada": False,
        "perfil_profesional": [
            "Registro y análisis de operaciones contables.",
            "Elaboración de estados financieros y balances.",
            "Gestión de impuestos y obligaciones tributarias.",
            "Manejo de sistemas contables computarizados.",
            "Asesoramiento financiero a empresas y emprendedores.",
        ],
        "campo_laboral": [
            "Departamentos contables de empresas privadas.",
            "Instituciones públicas y organizaciones sin fines de lucro.",
            "Estudios contables y de auditoría.",
            "Emprendimientos propios como asesor contable.",
        ],
        "preguntas_frecuentes": [
            {
                "pregunta": "¿Necesito conocimientos previos de contabilidad?",
                "respuesta": (
                    "No, comenzamos desde contabilidad básica. Solo se "
                    "requiere manejo de matemática básica."
                ),
            },
            {
                "pregunta": "¿Qué software contable voy a aprender?",
                "respuesta": (
                    "Aprenderás sistemas contables computarizados, manejo de "
                    "hojas de cálculo y software tributario boliviano."
                ),
            },
            {
                "pregunta": "¿Puedo firmar balances al egresar?",
                "respuesta": (
                    "Como Técnico Superior puedes llevar contabilidad de "
                    "empresas, aunque la firma oficial requiere título "
                    "profesional universitario."
                ),
            },
            {
                "pregunta": "¿La carrera incluye práctica tributaria?",
                "respuesta": (
                    "Sí, en segundo y tercer año trabajarás con casos reales "
                    "de declaraciones de impuestos."
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
        "plan_estudios": [
            {
                "anio": "Primer Año",
                "materias": [
                    "Contabilidad Básica",
                    "Matemática Financiera",
                    "Documentos Mercantiles",
                    "Ofimática Aplicada",
                    "Introducción al Derecho",
                    "Comunicación y Redacción",
                    "Inglés Técnico I",
                ],
            },
            {
                "anio": "Segundo Año",
                "materias": [
                    "Contabilidad Intermedia",
                    "Contabilidad de Costos",
                    "Legislación Tributaria",
                    "Sistemas Contables Computarizados",
                    "Derecho Comercial",
                    "Estadística Aplicada",
                    "Inglés Técnico II",
                ],
            },
            {
                "anio": "Tercer Año",
                "materias": [
                    "Contabilidad Superior",
                    "Auditoría",
                    "Análisis de Estados Financieros",
                    "Contabilidad Gubernamental",
                    "Legislación Laboral y Social",
                    "Ética Profesional",
                    "Proyecto de Grado",
                ],
            },
        ],
        "icono": "calculator",
        "color_principal": "#0891b2",
        "color_suave": "#ecfeff",
        "color_principal_dark": "#22d3ee",
        "color_suave_dark": "#164e63",
        "imagen_archivo": "contaduria.png",
        "imagen_banner": "contaduria_banner.avif",
        "iconos_animados": [
            _icono_orbital_config(
                "receipt", 55.0, 0.25, PERSPECTIVA_DEFECTO,
                0, 18.0, 0.0, "#0891b2", True,
            ),
            _icono_orbital_config(
                "coins", 70.0, 0.15, PERSPECTIVA_DEFECTO,
                90, 24.0, 3.0, "#16a34a",
            ),
            _icono_orbital_config(
                "chart-line", 62.0, 0.30, PERSPECTIVA_DEFECTO,
                180, 21.0, 6.0, "#ea580c",
            ),
            _icono_orbital_config(
                "wallet", 85.0, 0.20, PERSPECTIVA_DEFECTO,
                270, 27.0, 9.0, "#7c3aed",
            ),
        ],
        "estadisticas": {
            "demanda_laboral": "alta",
            "puntuacion": 4.7,
            "estudiantes_inscritos": 72,
            "estudiantes_graduados": 198,
            "tasa_empleabilidad": 92,
            "salario_promedio_bs": 4200,
        },
        "caracteristicas": [
            {
                "icono": "calculator",
                "etiqueta": "Software contable",
                "descripcion": "SIAT, SICON, hojas de cálculo",
            },
            {
                "icono": "award",
                "etiqueta": "Auxiliar tributario",
                "descripcion": "Preparación en impuestos",
            },
            {
                "icono": "file-text",
                "etiqueta": "Declaraciones reales",
                "descripcion": "Práctica con empresas",
            },
        ],
        "modalidad": "Presencial",
        "turnos": ["Mañana", "Noche", "Sábado"],
        "cupos_disponibles": 25,
    },
    # ==================================================================
    # Carrera 2 — Secretariado Ejecutivo
    # ==================================================================
    {
        "id": 2,
        "nombre": "Secretariado Ejecutivo",
        "nombre_corto": "Secretariado",
        "duracion": "3 Años",
        "lema": "Gestión administrativa y organización ejecutiva",
        "descripcion": (
            "El Técnico Superior en Secretariado Ejecutivo es un profesional "
            "altamente capacitado en la gestión administrativa, organización "
            "de agendas ejecutivas, atención al cliente, redacción de "
            "documentos y manejo de herramientas ofimáticas."
        ),
        "destacada": False,
        "perfil_profesional": [
            "Redacción y gestión de correspondencia oficial.",
            "Organización de agendas, reuniones y eventos ejecutivos.",
            "Manejo avanzado de herramientas ofimáticas.",
            "Atención al cliente y protocolo empresarial.",
            "Gestión documental y archivo digital.",
        ],
        "campo_laboral": [
            "Gerencias y direcciones ejecutivas.",
            "Instituciones públicas y privadas.",
            "Recepción y atención al cliente.",
            "Coordinación de eventos corporativos.",
        ],
        "preguntas_frecuentes": [
            {
                "pregunta": "¿Qué habilidades voy a desarrollar?",
                "respuesta": (
                    "Redacción ejecutiva, manejo de agendas, organización de "
                    "eventos, atención al cliente y ofimática avanzada."
                ),
            },
            {
                "pregunta": "¿Se enseña inglés?",
                "respuesta": (
                    "Sí, Inglés Técnico I y II en los dos primeros años, "
                    "enfocado a comunicación empresarial."
                ),
            },
            {
                "pregunta": "¿Qué software aprenderé?",
                "respuesta": (
                    "Word, Excel avanzado, PowerPoint, gestión documental "
                    "y sistemas de gestión ejecutiva."
                ),
            },
            {
                "pregunta": "¿Puedo trabajar en empresas grandes?",
                "respuesta": (
                    "Sí, el perfil está diseñado para gerencias, direcciones "
                    "ejecutivas y atención al cliente."
                ),
            },
            {
                "pregunta": "¿Qué salidas laborales tengo al egresar?",
                "respuesta": (
                    "Secretaria ejecutiva, asistente administrativa, "
                    "recepcionista bilingüe, coordinadora de eventos."
                ),
            },
        ],
        "plan_estudios": [
            {
                "anio": "Primer Año",
                "materias": [
                    "Técnicas de Secretariado I",
                    "Ofimática Básica",
                    "Redacción y Ortografía",
                    "Introducción a la Administración",
                    "Documentos Mercantiles",
                    "Relaciones Humanas",
                    "Inglés Técnico I",
                ],
            },
            {
                "anio": "Segundo Año",
                "materias": [
                    "Técnicas de Secretariado II",
                    "Ofimática Avanzada",
                    "Contabilidad Básica",
                    "Legislación Laboral",
                    "Comunicación Empresarial",
                    "Protocolo y Etiqueta",
                    "Inglés Técnico II",
                ],
            },
            {
                "anio": "Tercer Año",
                "materias": [
                    "Gestión Ejecutiva",
                    "Administración de Recursos Humanos",
                    "Marketing y Atención al Cliente",
                    "Organización de Eventos",
                    "Gestión Documental Digital",
                    "Ética Profesional",
                    "Proyecto de Grado",
                ],
            },
        ],
        "icono": "briefcase",
        "color_principal": "#7c3aed",
        "color_suave": "#f5f3ff",
        "color_principal_dark": "#a78bfa",
        "color_suave_dark": "#4c1d95",
        "imagen_archivo": "secretariado.png",
        "imagen_banner": "secretariado_banner.avif",
        "iconos_animados": [
            _icono_orbital_config(
                "calendar-clock", 55.0, 0.25, PERSPECTIVA_DEFECTO,
                0, 18.0, 0.0, "#7c3aed", True,
            ),
            _icono_orbital_config(
                "mail", 70.0, 0.15, PERSPECTIVA_DEFECTO,
                90, 24.0, 3.0, "#db2777",
            ),
            _icono_orbital_config(
                "users", 62.0, 0.30, PERSPECTIVA_DEFECTO,
                180, 21.0, 6.0, "#0891b2",
            ),
            _icono_orbital_config(
                "file-text", 85.0, 0.20, PERSPECTIVA_DEFECTO,
                270, 27.0, 9.0, "#ea580c",
            ),
        ],
        "estadisticas": {
            "demanda_laboral": "media",
            "puntuacion": 4.6,
            "estudiantes_inscritos": 45,
            "estudiantes_graduados": 156,
            "tasa_empleabilidad": 88,
            "salario_promedio_bs": 3500,
        },
        "caracteristicas": [
            {
                "icono": "languages",
                "etiqueta": "Inglés técnico",
                "descripcion": "2 niveles conversacionales",
            },
            {
                "icono": "users",
                "etiqueta": "Protocolo empresarial",
                "descripcion": "Etiqueta y eventos",
            },
            {
                "icono": "briefcase",
                "etiqueta": "Atención al cliente",
                "descripcion": "Prácticas con clientes reales",
            },
        ],
        "modalidad": "Presencial",
        "turnos": ["Mañana", "Tarde", "Sábado"],
        "cupos_disponibles": 20,
    },
    # ==================================================================
    # Carrera 3 — Comercio Internacional
    # ==================================================================
    {
        "id": 3,
        "nombre": "Comercio Internacional y Administración Aduanera",
        "nombre_corto": "Comercio Int.",
        "duracion": "3 Años",
        "lema": "Comercio exterior, aduanas y logística global",
        "descripcion": (
            "El Técnico Superior en Comercio Internacional y Administración "
            "Aduanera es un profesional capacitado para gestionar operaciones "
            "de importación y exportación, trámites aduaneros, logística "
            "internacional y negociaciones comerciales."
        ),
        "destacada": False,
        "perfil_profesional": [
            "Gestión de trámites de importación y exportación.",
            "Aplicación de normativa aduanera nacional e internacional.",
            "Coordinación de logística y transporte internacional.",
            "Negociación en mercados internacionales.",
            "Manejo de tratados comerciales y regímenes aduaneros.",
        ],
        "campo_laboral": [
            "Agencias despachantes de aduana.",
            "Empresas importadoras y exportadoras.",
            "Operadores logísticos y de transporte internacional.",
            "Instituciones aduaneras y comerciales.",
        ],
        "preguntas_frecuentes": [
            {
                "pregunta": "¿Qué es el SIDUNEA?",
                "respuesta": (
                    "Es el Sistema Informático Aduanero usado en Bolivia y "
                    "varios países. Aprenderás a usarlo en tercer año."
                ),
            },
            {
                "pregunta": "¿Se enseña normativa aduanera?",
                "respuesta": (
                    "Sí, Legislación Aduanera I y II cubren toda la normativa "
                    "vigente boliviana y tratados internacionales."
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
                    "Inglés Técnico I y II enfocado a comercio exterior."
                ),
            },
            {
                "pregunta": "¿Qué salidas laborales tengo al egresar?",
                "respuesta": (
                    "Auxiliar de despachante, asistente de comercio exterior, "
                    "operador logístico, analista de importaciones."
                ),
            },
        ],
        "plan_estudios": [
            {
                "anio": "Primer Año",
                "materias": [
                    "Introducción al Comercio Internacional",
                    "Legislación Aduanera I",
                    "Documentación Comercial",
                    "Contabilidad Básica",
                    "Ofimática Aplicada",
                    "Comunicación y Redacción",
                    "Inglés Técnico I",
                ],
            },
            {
                "anio": "Segundo Año",
                "materias": [
                    "Regímenes Aduaneros",
                    "Legislación Aduanera II",
                    "Logística Internacional",
                    "Marketing Internacional",
                    "Medios de Pago Internacionales",
                    "Estadística Aplicada",
                    "Inglés Técnico II",
                ],
            },
            {
                "anio": "Tercer Año",
                "materias": [
                    "Gestión Aduanera",
                    "Tratados y Acuerdos Comerciales",
                    "Transporte Internacional",
                    "Negociación Internacional",
                    "Sistemas Informáticos Aduaneros (SIDUNEA)",
                    "Ética Profesional",
                    "Proyecto de Grado",
                ],
            },
        ],
        "icono": "globe",
        "color_principal": "#ea580c",
        "color_suave": "#fff7ed",
        "color_principal_dark": "#fb923c",
        "color_suave_dark": "#7c2d12",
        "imagen_archivo": "comercio.png",
        "imagen_banner": "comercio_banner.avif",
        "iconos_animados": [
            _icono_orbital_config(
                "ship", 55.0, 0.25, PERSPECTIVA_DEFECTO,
                0, 18.0, 0.0, "#ea580c", True,
            ),
            _icono_orbital_config(
                "package", 70.0, 0.15, PERSPECTIVA_DEFECTO,
                90, 24.0, 3.0, "#0891b2",
            ),
            _icono_orbital_config(
                "file-text", 62.0, 0.30, PERSPECTIVA_DEFECTO,
                180, 21.0, 6.0, "#7c3aed",
            ),
            _icono_orbital_config(
                "truck", 85.0, 0.20, PERSPECTIVA_DEFECTO,
                270, 27.0, 9.0, "#16a34a",
            ),
        ],
        "estadisticas": {
            "demanda_laboral": "alta",
            "puntuacion": 4.9,
            "estudiantes_inscritos": 58,
            "estudiantes_graduados": 145,
            "tasa_empleabilidad": 94,
            "salario_promedio_bs": 5000,
        },
        "caracteristicas": [
            {
                "icono": "globe",
                "etiqueta": "SIDUNEA",
                "descripcion": "Sistema aduanero oficial",
            },
            {
                "icono": "ship",
                "etiqueta": "Logística global",
                "descripcion": "Importación y exportación",
            },
            {
                "icono": "file-check",
                "etiqueta": "Tratados comerciales",
                "descripcion": "MERCOSUR, CAN",
            },
        ],
        "modalidad": "Presencial",
        "turnos": ["Mañana", "Noche", "Sábado"],
        "cupos_disponibles": 25,
    },
    # ==================================================================
    # Carrera 4 — Electrónica
    # ==================================================================
    {
        "id": 4,
        "nombre": "Electrónica",
        "nombre_corto": "Electrónica",
        "duracion": "3 Años",
        "lema": "Circuitos, automatización y sistemas electrónicos",
        "descripcion": (
            "El Técnico Superior en Electrónica es un profesional capacitado "
            "para diseñar, instalar, mantener y reparar circuitos "
            "electrónicos, sistemas de control, telecomunicaciones y "
            "automatización industrial."
        ),
        "destacada": False,
        "perfil_profesional": [
            "Diseño y montaje de circuitos electrónicos.",
            "Instalación y mantenimiento de sistemas de telecomunicación.",
            "Programación de microcontroladores y automatización.",
            "Reparación de equipos electrónicos industriales y domésticos.",
            "Aplicación de normas de seguridad eléctrica.",
        ],
        "campo_laboral": [
            "Empresas de electrónica y telecomunicaciones.",
            "Industria de automatización y control.",
            "Servicios técnicos especializados.",
            "Emprendimientos independientes de reparación e instalación.",
        ],
        "preguntas_frecuentes": [
            {
                "pregunta": "¿Qué equipos voy a usar en los laboratorios?",
                "respuesta": (
                    "Osciloscopios, multímetros, generadores de señales, "
                    "estaciones de soldadura y microcontroladores."
                ),
            },
            {
                "pregunta": "¿Se enseña programación de microcontroladores?",
                "respuesta": (
                    "Sí, en tercer año. Trabajarás con Arduino, PIC y ESP32 "
                    "para proyectos de automatización y domótica."
                ),
            },
            {
                "pregunta": "¿Puedo reparar equipos electrónicos al egresar?",
                "respuesta": (
                    "Sí, tendrás las competencias para reparar equipos "
                    "domésticos, industriales y de telecomunicaciones."
                ),
            },
            {
                "pregunta": "¿La carrera incluye automatización industrial?",
                "respuesta": (
                    "Sí, es parte del tercer año. Aprenderás PLCs, sensores "
                    "y sistemas de control industrial."
                ),
            },
            {
                "pregunta": "¿Qué salidas laborales tengo al egresar?",
                "respuesta": (
                    "Técnico electrónico, mantenedor industrial, instalador "
                    "de telecomunicaciones y emprendedor de servicios técnicos."
                ),
            },
        ],
        "plan_estudios": [
            {
                "anio": "Primer Año",
                "materias": [
                    "Electricidad Básica",
                    "Matemática Aplicada",
                    "Física Aplicada",
                    "Dibujo Electrónico",
                    "Componentes Electrónicos",
                    "Ofimática Aplicada",
                    "Inglés Técnico I",
                ],
            },
            {
                "anio": "Segundo Año",
                "materias": [
                    "Electrónica Analógica",
                    "Electrónica Digital",
                    "Instrumentación y Medición",
                    "Circuitos Impresos",
                    "Sistemas de Audio y Video",
                    "Seguridad Eléctrica",
                    "Inglés Técnico II",
                ],
            },
            {
                "anio": "Tercer Año",
                "materias": [
                    "Microcontroladores",
                    "Automatización Industrial",
                    "Telecomunicaciones",
                    "Sistemas de Control",
                    "Mantenimiento de Equipos Electrónicos",
                    "Ética Profesional",
                    "Proyecto de Grado",
                ],
            },
        ],
        "icono": "zap",
        "color_principal": "#16a34a",
        "color_suave": "#f0fdf4",
        "color_principal_dark": "#4ade80",
        "color_suave_dark": "#14532d",
        "imagen_archivo": "electronica.png",
        "imagen_banner": "electronica_banner.avif",
        "iconos_animados": [
            _icono_orbital_config(
                "circuit-board", 55.0, 0.25, PERSPECTIVA_DEFECTO,
                0, 18.0, 0.0, "#16a34a", True,
            ),
            _icono_orbital_config(
                "cpu", 70.0, 0.15, PERSPECTIVA_DEFECTO,
                90, 24.0, 3.0, "#2563eb",
            ),
            _icono_orbital_config(
                "radio", 62.0, 0.30, PERSPECTIVA_DEFECTO,
                180, 21.0, 6.0, "#ea580c",
            ),
            _icono_orbital_config(
                "plug-zap", 85.0, 0.20, PERSPECTIVA_DEFECTO,
                270, 27.0, 9.0, "#7c3aed",
            ),
        ],
        "estadisticas": {
            "demanda_laboral": "alta",
            "puntuacion": 4.7,
            "estudiantes_inscritos": 52,
            "estudiantes_graduados": 178,
            "tasa_empleabilidad": 91,
            "salario_promedio_bs": 4800,
        },
        "caracteristicas": [
            {
                "icono": "circuit-board",
                "etiqueta": "PLC y automatización",
                "descripcion": "Siemens, Schneider",
            },
            {
                "icono": "cpu",
                "etiqueta": "Microcontroladores",
                "descripcion": "Arduino, PIC, ESP32",
            },
            {
                "icono": "zap",
                "etiqueta": "Energía solar",
                "descripcion": "Instalación fotovoltaica",
            },
        ],
        "modalidad": "Presencial",
        "turnos": ["Mañana", "Tarde", "Noche", "Sábado"],
        "cupos_disponibles": 30,
    },
]
"""Catálogo estático de las 5 carreras del instituto.

⚠️ Privado (prefijo `_`): usar `obtener_catalogo()` para acceder.
"""


# ======================================================================
# 7. Paleta de colores (para reasignación aleatoria)
# ======================================================================

PALETA_COLORES: list[tuple[str, str, str, str]] = [
    ("#2563eb", "#eff6ff", "#60a5fa", "#1e3a8a"),  # blue
    ("#0891b2", "#ecfeff", "#22d3ee", "#164e63"),  # cyan
    ("#7c3aed", "#f5f3ff", "#a78bfa", "#4c1d95"),  # violet
    ("#ea580c", "#fff7ed", "#fb923c", "#7c2d12"),  # orange
    ("#16a34a", "#f0fdf4", "#4ade80", "#14532d"),  # green
    ("#db2777", "#fdf2f8", "#f472b6", "#831843"),  # pink
    ("#0d9488", "#f0fdfa", "#2dd4bf", "#134e4a"),  # teal
    ("#d97706", "#fffbeb", "#fbbf24", "#78350f"),  # amber
    ("#4f46e5", "#eef2ff", "#818cf8", "#312e81"),  # indigo
    ("#dc2626", "#fef2f2", "#f87171", "#7f1d1d"),  # red
    ("#059669", "#ecfdf5", "#34d399", "#064e3b"),  # emerald
    ("#9333ea", "#faf5ff", "#c084fc", "#581c87"),  # purple
]
"""Paleta de 12 colores para asignación aleatoria.

Cada tupla: (principal, suave, principal_dark, suave_dark).
"""


# ======================================================================
# 8. API pública del repositorio
# ======================================================================


@lru_cache(maxsize=1)
def obtener_catalogo() -> list[Carrera]:
    """
    Devuelve el catálogo completo de carreras.

    Returns:
        Lista de `Carrera`. La lista se cachea tras la primera llamada.

    ⚠️ La lista devuelta NO debe mutarse. Si necesitas modificarla,
    haz una copia: `copia = list(obtener_catalogo())`.
    """
    return _CATALOGO_CARRERAS


@lru_cache(maxsize=None)
def obtener_carrera_por_id(carrera_id: int) -> Carrera | None:
    """
    Devuelve una carrera por su ID.

    Args:
        carrera_id: ID de la carrera (0-4).

    Returns:
        La carrera encontrada, o `None` si no existe.
    """
    for carrera in _CATALOGO_CARRERAS:
        if carrera["id"] == carrera_id:
            return carrera
    return None


@lru_cache(maxsize=1)
def obtener_carrera_destacada() -> Carrera:
    """
    Devuelve la carrera marcada como destacada.

    Returns:
        La primera `Carrera` con `destacada=True`, o la primera del
        catálogo si ninguna está marcada.
    """
    for carrera in _CATALOGO_CARRERAS:
        if carrera["destacada"]:
            return carrera
    return _CATALOGO_CARRERAS[0]


def obtener_ids_carreras() -> list[int]:
    """Devuelve la lista de IDs de todas las carreras."""
    return [c["id"] for c in _CATALOGO_CARRERAS]


def carrera_existe(carrera_id: int) -> bool:
    """Indica si el ID corresponde a una carrera del catálogo."""
    return any(c["id"] == carrera_id for c in _CATALOGO_CARRERAS)


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Tipos ---
    "CaracteristicaCarrera",
    "Carrera",
    "CarreraConEtiqueta",
    "ColorHex",
    "DemandaLaboral",
    "EstadisticasCarrera",
    "IconoAnimado",
    "Modalidad",
    "PlanAnual",
    "PreguntaFrecuente",
    "Turno",
    # --- Constantes ---
    "HORARIOS_TURNO",
    "PALETA_COLORES",
    "PERSPECTIVA_DEFECTO",
    "TURNOS_VALIDOS",
    # --- API pública ---
    "carrera_existe",
    "obtener_carrera_destacada",
    "obtener_carrera_por_id",
    "obtener_catalogo",
    "obtener_ids_carreras",
]