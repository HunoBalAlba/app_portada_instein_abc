"""
Modelos del Calendario Académico.

Contiene los tipos y datos estáticos del calendario:
- Eventos del instituto (`ProximoEvento`).
- Fechas importantes de Bolivia (`FechaImportante`).
- Tipos de evento y de fecha (metadata visual).
- Opciones de filtros (`OPCIONES_CARRERA`, etc.).

Filosofía
---------
Los modelos son `TypedDict` para compatibilidad con `rx.foreach`.
Los datos son listas de `TypedDict` (estáticas, inmutables).

Convención de imports
---------------------
✅ **RECOMENDADO** — importar desde aquí:
    from app_portada_instein.dominio.modelos.calendario import (
        ProximoEvento,
        FechaImportante,
        PROXIMOS_EVENTOS,
        FECHAS_IMPORTANTES,
    )

Nota técnica: TIPOS DE EVENTO Y FECHA
-------------------------------------
Cada tipo (ej: "taller", "feriado_nacional") tiene metadata visual:
- `etiqueta`: nombre visible (ej: "Taller").
- `icono`:    nombre del icono Lucide (kebab-case).
- `color`:    scheme Radix (ej: "blue", "violet").

Esta metadata se resuelve con `color_por_tipo_evento()` y
`color_por_tipo_fecha()` en los helpers de componentes.

Nota técnica: DIAS SIN FECHA FIJA
---------------------------------
Algunas fechas importantes son "movibles" (ej: Semana Santa,
Carnaval). En esos casos `dia = "—"` (guion largo).
"""

from __future__ import annotations

from typing import Literal, TypedDict


# ======================================================================
# 1. Alias de tipos
# ======================================================================

TipoEventoId = Literal[
    "taller",
    "seminario",
    "feria",
    "evaluacion",
    "feriado",
    "institucional",
]
"""Identificadores válidos de tipo de evento del instituto."""

TipoFechaId = Literal[
    "feriado_nacional",
    "efemeride_nacional",
    "feriado_movible",
    "internacional",
]
"""Identificadores válidos de tipo de fecha importante."""

AlcanceFecha = Literal["nacional", "internacional"]
"""Alcance geográfico de una fecha importante."""

SemestreAcademico = Literal["I", "II"]
"""Semestre académico (I = Enero-Junio, II = Julio-Diciembre)."""


# ======================================================================
# 2. Modelos
# ======================================================================


class ProximoEvento(TypedDict):
    """
    Evento del instituto en el timeline.

    Attributes:
        mes:         Mes del evento (mayúsculas, ej: "ABRIL").
        anio:        Año del evento (ej: "2026").
        dia:         Día del mes (ej: "05").
        titulo:      Título del evento.
        descripcion: Descripción del evento.
        tipo:        Clave del tipo (ver `TipoEventoId`).
        carrera:     Clave de carrera asociada (para filtro).
                     "institucional" si aplica a todas.
        lugar:       Lugar donde se realiza.
    """

    mes: str
    anio: str
    dia: str
    titulo: str
    descripcion: str
    tipo: TipoEventoId
    carrera: str
    lugar: str


class FechaImportante(TypedDict):
    """
    Fecha importante de Bolivia o del mundo.

    Attributes:
        mes:      Mes de la fecha (mayúsculas, ej: "ENERO").
        semestre: Semestre académico ("I" o "II").
        dia:      Día del mes (ej: "01"). "—" para fechas movibles.
        titulo:   Nombre de la fecha.
        alcance:  "nacional" o "internacional".
        tipo:     Clave del tipo (ver `TipoFechaId`).
    """

    mes: str
    semestre: SemestreAcademico
    dia: str
    titulo: str
    alcance: AlcanceFecha
    tipo: TipoFechaId


class InfoRapida(TypedDict):
    """Tarjeta de info rápida del hero del calendario."""

    icono: str
    titulo: str
    valor: str
    descripcion: str
    color: str


class OpcionFiltro(TypedDict):
    """Opción de filtro (carrera, tipo de evento, orden)."""

    valor: str
    etiqueta: str
    icono: str


class OpcionOrden(TypedDict):
    """Opción de ordenamiento (sin icono)."""

    valor: str
    etiqueta: str


# ======================================================================
# 3. Tipos de evento (metadata visual)
# ======================================================================

TIPOS_EVENTO: dict[str, dict] = {
    "taller": {
        "etiqueta": "Taller",
        "icono": "wrench",
        "color": "blue",
    },
    "seminario": {
        "etiqueta": "Seminario",
        "icono": "mic",
        "color": "violet",
    },
    "feria": {
        "etiqueta": "Feria",
        "icono": "store",
        "color": "orange",
    },
    "evaluacion": {
        "etiqueta": "Evaluación",
        "icono": "clipboard-check",
        "color": "amber",
    },
    "feriado": {
        "etiqueta": "Feriado",
        "icono": "party-popper",
        "color": "red",
    },
    "institucional": {
        "etiqueta": "Institucional",
        "icono": "landmark",
        "color": "crimson",
    },
}


# ======================================================================
# 4. Tipos de fecha (metadata visual)
# ======================================================================

TIPOS_FECHA: dict[str, dict] = {
    "feriado_nacional": {
        "etiqueta": "Feriado nacional",
        "icono": "flag",
        "color": "red",
    },
    "efemeride_nacional": {
        "etiqueta": "Efeméride nacional",
        "icono": "landmark",
        "color": "amber",
    },
    "feriado_movible": {
        "etiqueta": "Feriado movible",
        "icono": "calendar-days",
        "color": "red",
    },
    "internacional": {
        "etiqueta": "Día internacional",
        "icono": "globe",
        "color": "blue",
    },
}


# ======================================================================
# 5. Info rápida (cards del hero)
# ======================================================================

INFO_RAPIDA: list[InfoRapida] = [
    {
        "icono": "calendar-check",
        "titulo": "Inscripciones",
        "valor": "Abiertas todo el año",
        "descripcion": "No hay fecha límite. Inscríbete cuando quieras.",
        "color": "green",
    },
    {
        "icono": "play-circle",
        "titulo": "Inicio de clases",
        "valor": "Primer lunes de cada mes",
        "descripcion": "Ingreso escalonado según tu fecha de inscripción.",
        "color": "blue",
    },
    {
        "icono": "clock",
        "titulo": "Duración",
        "valor": "3 años · 6 semestres",
        "descripcion": "Título de Técnico Superior en Provisión Nacional.",
        "color": "violet",
    },
    {
        "icono": "building-2",
        "titulo": "Modalidad",
        "valor": "Presencial · 3 turnos",
        "descripcion": "Mañana, tarde y noche. Elige el que mejor te convenga.",
        "color": "orange",
    },
]


# ======================================================================
# 6. Opciones de filtros
# ======================================================================

OPCIONES_CARRERA: list[OpcionFiltro] = [
    {"valor": "todas", "etiqueta": "Todas las carreras", "icono": "list"},
    {"valor": "sistemas", "etiqueta": "Sistemas", "icono": "cpu"},
    {"valor": "contaduria", "etiqueta": "Contaduría", "icono": "calculator"},
    {
        "valor": "secretariado",
        "etiqueta": "Secretariado",
        "icono": "briefcase",
    },
    {"valor": "comercio", "etiqueta": "Comercio Int.", "icono": "globe"},
    {"valor": "electronica", "etiqueta": "Electrónica", "icono": "zap"},
    {
        "valor": "institucional",
        "etiqueta": "Institucional",
        "icono": "landmark",
    },
]

OPCIONES_TIPO_EVENTO: list[OpcionFiltro] = [
    {"valor": "todos", "etiqueta": "Todos los tipos", "icono": "filter"},
    {"valor": "taller", "etiqueta": "Talleres", "icono": "wrench"},
    {"valor": "seminario", "etiqueta": "Seminarios", "icono": "mic"},
    {"valor": "feria", "etiqueta": "Ferias", "icono": "store"},
    {
        "valor": "evaluacion",
        "etiqueta": "Evaluaciones",
        "icono": "clipboard-check",
    },
    {
        "valor": "institucional",
        "etiqueta": "Institucionales",
        "icono": "landmark",
    },
]

OPCIONES_ORDEN: list[OpcionOrden] = [
    {"valor": "fecha_asc", "etiqueta": "Fecha (más próximos primero)"},
    {"valor": "fecha_desc", "etiqueta": "Fecha (más lejanos primero)"},
    {"valor": "tipo_asc", "etiqueta": "Tipo (A-Z)"},
]


# ======================================================================
# 7. Próximos eventos del instituto
# ======================================================================

PROXIMOS_EVENTOS: list[ProximoEvento] = [
    {
        "mes": "ABRIL",
        "anio": "2026",
        "dia": "05",
        "titulo": "Inicio de clases · Gestión II",
        "descripcion": (
            "Comienzo oficial de las actividades académicas para "
            "estudiantes nuevos y antiguos."
        ),
        "tipo": "institucional",
        "carrera": "institucional",
        "lugar": "Campus INSTEIN",
    },
    {
        "mes": "ABRIL",
        "anio": "2026",
        "dia": "18",
        "titulo": "Taller: Metodología de estudio universitario",
        "descripcion": (
            "Taller práctico para estudiantes de primer semestre. "
            "Técnicas de lectura, apuntes y organización del tiempo."
        ),
        "tipo": "taller",
        "carrera": "institucional",
        "lugar": "Aula Magna",
    },
    {
        "mes": "MAYO",
        "anio": "2026",
        "dia": "08",
        "titulo": "Seminario: Inteligencia Artificial aplicada",
        "descripcion": (
            "Seminario abierto sobre IA en el mundo laboral técnico. "
            "Expositores invitados de la industria."
        ),
        "tipo": "seminario",
        "carrera": "sistemas",
        "lugar": "Auditorio Principal",
    },
    {
        "mes": "MAYO",
        "anio": "2026",
        "dia": "22",
        "titulo": "Primer parcial · Bloque I",
        "descripcion": (
            "Evaluaciones del primer parcial. Consulta horarios "
            "específicos en la plataforma académica."
        ),
        "tipo": "evaluacion",
        "carrera": "institucional",
        "lugar": "Aulas asignadas",
    },
    {
        "mes": "JUNIO",
        "anio": "2026",
        "dia": "12",
        "titulo": "Feria de innovación y proyectos",
        "descripcion": (
            "Exposición anual de proyectos estudiantiles de todas las "
            "carreras. Abierto al público."
        ),
        "tipo": "feria",
        "carrera": "institucional",
        "lugar": "Patio Central",
    },
    {
        "mes": "JUNIO",
        "anio": "2026",
        "dia": "29",
        "titulo": "Taller: Emprendimiento técnico",
        "descripcion": (
            "Cómo convertir tu formación técnica en un emprendimiento. "
            "Casos reales de egresados."
        ),
        "tipo": "taller",
        "carrera": "comercio",
        "lugar": "Aula 205",
    },
    {
        "mes": "JULIO",
        "anio": "2026",
        "dia": "20",
        "titulo": "Segundo parcial · Bloque II",
        "descripcion": "Evaluaciones del segundo parcial del semestre.",
        "tipo": "evaluacion",
        "carrera": "institucional",
        "lugar": "Aulas asignadas",
    },
    {
        "mes": "AGOSTO",
        "anio": "2026",
        "dia": "14",
        "titulo": "Seminario: Ciberseguridad para pymes",
        "descripcion": (
            "Seminario técnico sobre protección de datos y seguridad "
            "informática en pequeñas empresas."
        ),
        "tipo": "seminario",
        "carrera": "sistemas",
        "lugar": "Auditorio Principal",
    },
    {
        "mes": "SEPTIEMBRE",
        "anio": "2026",
        "dia": "11",
        "titulo": "Examen final · Bloque III",
        "descripcion": "Evaluaciones finales del semestre.",
        "tipo": "evaluacion",
        "carrera": "institucional",
        "lugar": "Aulas asignadas",
    },
    {
        "mes": "SEPTIEMBRE",
        "anio": "2026",
        "dia": "28",
        "titulo": "Ceremonia de graduación",
        "descripcion": (
            "Entrega de títulos a los nuevos Técnicos Superiores en "
            "Provisión Nacional."
        ),
        "tipo": "institucional",
        "carrera": "institucional",
        "lugar": "Auditorio Principal",
    },
    {
        "mes": "OCTUBRE",
        "anio": "2026",
        "dia": "05",
        "titulo": "Inicio de clases · Gestión III",
        "descripcion": "Comienzo del nuevo semestre académico.",
        "tipo": "institucional",
        "carrera": "institucional",
        "lugar": "Campus INSTEIN",
    },
]


# ======================================================================
# 8. Fechas importantes de Bolivia y el mundo
# ======================================================================

FECHAS_IMPORTANTES: list[FechaImportante] = [
    # ==================================================================
    # PRIMER SEMESTRE (Enero - Junio)
    # ==================================================================
    # --- ENERO ---
    {
        "mes": "ENERO",
        "semestre": "I",
        "dia": "01",
        "titulo": "Año Nuevo",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "ENERO",
        "semestre": "I",
        "dia": "22",
        "titulo": "Día del Estado Plurinacional de Bolivia",
        "alcance": "nacional",
        "tipo": "feriado_nacional",
    },
    {
        "mes": "ENERO",
        "semestre": "I",
        "dia": "24",
        "titulo": "Fiesta de la Alasita (Tributo al Ekeko)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    # --- FEBRERO ---
    {
        "mes": "FEBRERO",
        "semestre": "I",
        "dia": "10",
        "titulo": "Efeméride de Oruro",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "FEBRERO",
        "semestre": "I",
        "dia": "21",
        "titulo": "Día Internacional de la Lengua Materna",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "FEBRERO",
        "semestre": "I",
        "dia": "—",
        "titulo": "Carnaval de Oruro y feriados de Carnaval",
        "alcance": "nacional",
        "tipo": "feriado_movible",
    },
    # --- MARZO ---
    {
        "mes": "MARZO",
        "semestre": "I",
        "dia": "08",
        "titulo": "Día Internacional de la Mujer",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "MARZO",
        "semestre": "I",
        "dia": "19",
        "titulo": "Día del Padre Boliviano",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "MARZO",
        "semestre": "I",
        "dia": "22",
        "titulo": "Día Mundial del Agua",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "MARZO",
        "semestre": "I",
        "dia": "23",
        "titulo": "Día del Mar (Recordatorio de la pérdida del litoral)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    # --- ABRIL ---
    {
        "mes": "ABRIL",
        "semestre": "I",
        "dia": "07",
        "titulo": "Día Mundial de la Salud",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "ABRIL",
        "semestre": "I",
        "dia": "15",
        "titulo": "Efeméride de Tarija",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "ABRIL",
        "semestre": "I",
        "dia": "22",
        "titulo": "Día de la Tierra",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "ABRIL",
        "semestre": "I",
        "dia": "—",
        "titulo": "Semana Santa (Viernes Santo es feriado)",
        "alcance": "nacional",
        "tipo": "feriado_movible",
    },
    # --- MAYO ---
    {
        "mes": "MAYO",
        "semestre": "I",
        "dia": "01",
        "titulo": "Día del Trabajo",
        "alcance": "internacional",
        "tipo": "feriado_nacional",
    },
    {
        "mes": "MAYO",
        "semestre": "I",
        "dia": "25",
        "titulo": "Efeméride de Chuquisaca (Primer Grito Libertario)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "MAYO",
        "semestre": "I",
        "dia": "27",
        "titulo": "Día de la Madre Boliviana (Heroínas de la Coronilla)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    # --- JUNIO ---
    {
        "mes": "JUNIO",
        "semestre": "I",
        "dia": "05",
        "titulo": "Día Mundial del Medio Ambiente",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "JUNIO",
        "semestre": "I",
        "dia": "06",
        "titulo": "Día del Maestro Boliviano",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "JUNIO",
        "semestre": "I",
        "dia": "21",
        "titulo": "Año Nuevo Andino Amazónico Chaqueño (Willka Kuti)",
        "alcance": "nacional",
        "tipo": "feriado_nacional",
    },
    {
        "mes": "JUNIO",
        "semestre": "I",
        "dia": "—",
        "titulo": "Corpus Christi",
        "alcance": "nacional",
        "tipo": "feriado_movible",
    },
    # ==================================================================
    # SEGUNDO SEMESTRE (Julio - Diciembre)
    # ==================================================================
    # --- JULIO ---
    {
        "mes": "JULIO",
        "semestre": "II",
        "dia": "16",
        "titulo": "Efeméride de La Paz (Grito libertario de 1809)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "JULIO",
        "semestre": "II",
        "dia": "18",
        "titulo": "Día Internacional de Nelson Mandela",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    # --- AGOSTO ---
    {
        "mes": "AGOSTO",
        "semestre": "II",
        "dia": "06",
        "titulo": "Día de la Independencia de Bolivia (Fiesta Nacional)",
        "alcance": "nacional",
        "tipo": "feriado_nacional",
    },
    {
        "mes": "AGOSTO",
        "semestre": "II",
        "dia": "07",
        "titulo": "Día de las Fuerzas Armadas",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "AGOSTO",
        "semestre": "II",
        "dia": "09",
        "titulo": "Día Internacional de los Pueblos Indígenas",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "AGOSTO",
        "semestre": "II",
        "dia": "17",
        "titulo": "Día de la Bandera Nacional",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    # --- SEPTIEMBRE ---
    {
        "mes": "SEPTIEMBRE",
        "semestre": "II",
        "dia": "14",
        "titulo": "Efeméride de Cochabamba",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "SEPTIEMBRE",
        "semestre": "II",
        "dia": "21",
        "titulo": "Día del Estudiante, Médico y de la Juventud",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "SEPTIEMBRE",
        "semestre": "II",
        "dia": "21",
        "titulo": "Día Internacional de la Paz",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "SEPTIEMBRE",
        "semestre": "II",
        "dia": "24",
        "titulo": "Efeméride de Santa Cruz y de Pando",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    # --- OCTUBRE ---
    {
        "mes": "OCTUBRE",
        "semestre": "II",
        "dia": "11",
        "titulo": "Día de la Mujer Boliviana (Homenaje a Adela Zamudio)",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "OCTUBRE",
        "semestre": "II",
        "dia": "16",
        "titulo": "Día Mundial de la Alimentación",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "OCTUBRE",
        "semestre": "II",
        "dia": "24",
        "titulo": "Día de las Naciones Unidas",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    # --- NOVIEMBRE ---
    {
        "mes": "NOVIEMBRE",
        "semestre": "II",
        "dia": "02",
        "titulo": "Día de Todos los Difuntos / Todos los Santos",
        "alcance": "nacional",
        "tipo": "feriado_nacional",
    },
    {
        "mes": "NOVIEMBRE",
        "semestre": "II",
        "dia": "10",
        "titulo": "Efeméride de Potosí",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "NOVIEMBRE",
        "semestre": "II",
        "dia": "18",
        "titulo": "Efeméride del Beni",
        "alcance": "nacional",
        "tipo": "efemeride_nacional",
    },
    {
        "mes": "NOVIEMBRE",
        "semestre": "II",
        "dia": "20",
        "titulo": "Día Universal del Niño",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    # --- DICIEMBRE ---
    {
        "mes": "DICIEMBRE",
        "semestre": "II",
        "dia": "01",
        "titulo": "Día Mundial del SIDA",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "DICIEMBRE",
        "semestre": "II",
        "dia": "10",
        "titulo": "Día de los Derechos Humanos",
        "alcance": "internacional",
        "tipo": "internacional",
    },
    {
        "mes": "DICIEMBRE",
        "semestre": "II",
        "dia": "25",
        "titulo": "Navidad",
        "alcance": "internacional",
        "tipo": "feriado_nacional",
    },
]


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Alias de tipos ---
    "AlcanceFecha",
    "SemestreAcademico",
    "TipoEventoId",
    "TipoFechaId",
    # --- Modelos ---
    "FechaImportante",
    "InfoRapida",
    "OpcionFiltro",
    "OpcionOrden",
    "ProximoEvento",
    # --- Tipos (metadata) ---
    "TIPOS_EVENTO",
    "TIPOS_FECHA",
    # --- Datos estáticos ---
    "FECHAS_IMPORTANTES",
    "INFO_RAPIDA",
    "OPCIONES_CARRERA",
    "OPCIONES_ORDEN",
    "OPCIONES_TIPO_EVENTO",
    "PROXIMOS_EVENTOS",
]