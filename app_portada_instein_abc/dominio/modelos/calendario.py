

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
    "deportivo",
    "cultural",
    "charla",
    "taller_tecnico",
    "graduacion",
    # ═══ NUEVOS tipos por bimestre ═══
    "inicio_bimestre",
    "parcial",
    "examen_final",
    "cierre_actas",
]
"""Identificadores válidos de tipo de evento."""

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
"""Semestre académico."""

BimestreNumero = Literal[1, 2, 3, 4]
"""Número de bimestre (1-4)."""


# ======================================================================
# 2. Modelos
# ======================================================================


class ProximoEvento(TypedDict):
    """
    Evento del instituto en el timeline.

    Attributes:
        mes:          Mes del evento (mayúsculas).
        anio:         Año del evento.
        dia:          Día del mes.
        titulo:       Título del evento.
        descripcion:  Descripción del evento.
        tipo:         Clave del tipo de evento.
        carrera:      Clave de carrera ("institucional" si aplica a todas).
        lugar:        Lugar donde se realiza.
        bimestre:     Número de bimestre (1-4) o 0 si aplica a varios.
    """

    mes: str
    anio: str
    dia: str
    titulo: str
    descripcion: str
    tipo: TipoEventoId
    carrera: str
    lugar: str
    bimestre: int


class FechaImportante(TypedDict):
    """Fecha importante de Bolivia o del mundo."""

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


class MetaTipoEvento(TypedDict):
    """Metadata visual de un tipo de evento."""

    etiqueta: str
    icono: str
    color: str          # color principal (hex)
    fondo: str          # fondo suave (hex)
    borde: str          # borde (hex)


class MetaTipoFecha(TypedDict):
    """Metadata visual de un tipo de fecha."""

    etiqueta: str
    icono: str
    color: str
    fondo: str
    borde: str


class BimestreAcademico(TypedDict):
    """
    Info de un bimestre académico.

    Attributes:
        numero:       Número de bimestre (1-4).
        etiqueta:     Texto visible (ej: "I Bimestre").
        periodo:      Rango del período (ej: "Feb - Abr").
        fecha_inicio: Fecha de inicio (texto).
        fecha_fin:    Fecha de fin (texto).
        mes_inicio:   Mes abreviado del inicio (para agrupar).
        mes_fin:      Mes abreviado del fin.
    """

    numero: int
    etiqueta: str
    periodo: str
    fecha_inicio: str
    fecha_fin: str
    mes_inicio: str
    mes_fin: str


# ======================================================================
# 3. Tipos de evento (metadata visual CON COLORES HEX DIRECTOS)
# ======================================================================

TIPOS_EVENTO: dict[str, MetaTipoEvento] = {
    # ─── Categorías académicas ────────────────────────────────
    "taller": {
        "etiqueta": "Taller",
        "icono": "wrench",
        "color": "#3b82f6",       # blue-500
        "fondo": "#eff6ff",       # blue-50
        "borde": "#bfdbfe",       # blue-200
    },
    "taller_tecnico": {
        "etiqueta": "Taller técnico",
        "icono": "code",
        "color": "#6366f1",       # indigo-500
        "fondo": "#eef2ff",       # indigo-50
        "borde": "#c7d2fe",       # indigo-200
    },
    "seminario": {
        "etiqueta": "Seminario",
        "icono": "mic",
        "color": "#8b5cf6",       # violet-500
        "fondo": "#f5f3ff",       # violet-50
        "borde": "#ddd6fe",       # violet-200
    },
    "charla": {
        "etiqueta": "Charla",
        "icono": "graduation-cap",
        "color": "#06b6d4",       # cyan-500
        "fondo": "#ecfeff",       # cyan-50
        "borde": "#a5f3fc",       # cyan-200
    },
    # ─── Categorías de evaluación ─────────────────────────────
    "evaluacion": {
        "etiqueta": "Evaluación",
        "icono": "clipboard-check",
        "color": "#f59e0b",       # amber-500
        "fondo": "#fffbeb",       # amber-50
        "borde": "#fde68a",       # amber-200
    },
    "parcial": {
        "etiqueta": "Parcial",
        "icono": "file-pen",
        "color": "#f97316",       # orange-500
        "fondo": "#fff7ed",       # orange-50
        "borde": "#fed7aa",       # orange-200
    },
    "examen_final": {
        "etiqueta": "Examen final",
        "icono": "file-check",
        "color": "#dc2626",       # red-600
        "fondo": "#fef2f2",       # red-50
        "borde": "#fecaca",       # red-200
    },
    "cierre_actas": {
        "etiqueta": "Cierre de actas",
        "icono": "file-lock",
        "color": "#7c3aed",       # violet-600
        "fondo": "#f5f3ff",       # violet-50
        "borde": "#ddd6fe",       # violet-200
    },
    "graduacion": {
        "etiqueta": "Graduación",
        "icono": "award",
        "color": "#eab308",       # yellow-500
        "fondo": "#fefce8",       # yellow-50
        "borde": "#fef08a",       # yellow-200
    },
    # ─── Categorías institucionales ───────────────────────────
    "inicio_bimestre": {
        "etiqueta": "Inicio de bimestre",
        "icono": "play_circle",
        "color": "#16a34a",       # green-600
        "fondo": "#f0fdf4",       # green-50
        "borde": "#bbf7d0",       # green-200
    },
    "institucional": {
        "etiqueta": "Institucional",
        "icono": "landmark",
        "color": "#dc2626",       # red-600
        "fondo": "#fef2f2",       # red-50
        "borde": "#fecaca",       # red-200
    },
    "feria": {
        "etiqueta": "Feria",
        "icono": "store",
        "color": "#f97316",       # orange-500
        "fondo": "#fff7ed",       # orange-50
        "borde": "#fed7aa",       # orange-200
    },
    "feriado": {
        "etiqueta": "Feriado",
        "icono": "party-popper",
        "color": "#ef4444",       # red-500
        "fondo": "#fef2f2",       # red-50
        "borde": "#fecaca",       # red-200
    },
    # ─── Categorías recreativas ───────────────────────────────
    "deportivo": {
        "etiqueta": "Deportivo",
        "icono": "trophy",
        "color": "#22c55e",       # green-500
        "fondo": "#f0fdf4",       # green-50
        "borde": "#bbf7d0",       # green-200
    },
    "cultural": {
        "etiqueta": "Cultural",
        "icono": "music",
        "color": "#ec4899",       # pink-500
        "fondo": "#fdf2f8",       # pink-50
        "borde": "#fbcfe8",       # pink-200
    },
}


# ======================================================================
# 4. Tipos de fecha (metadata visual CON COLORES HEX DIRECTOS)
# ======================================================================

TIPOS_FECHA: dict[str, MetaTipoFecha] = {
    "feriado_nacional": {
        "etiqueta": "Feriado nacional",
        "icono": "flag",
        "color": "#ef4444",
        "fondo": "#fef2f2",
        "borde": "#fecaca",
    },
    "efemeride_nacional": {
        "etiqueta": "Efeméride nacional",
        "icono": "landmark",
        "color": "#f59e0b",
        "fondo": "#fffbeb",
        "borde": "#fde68a",
    },
    "feriado_movible": {
        "etiqueta": "Feriado movible",
        "icono": "calendar-days",
        "color": "#ef4444",
        "fondo": "#fef2f2",
        "borde": "#fecaca",
    },
    "internacional": {
        "etiqueta": "Día internacional",
        "icono": "globe",
        "color": "#3b82f6",
        "fondo": "#eff6ff",
        "borde": "#bfdbfe",
    },
}


# ======================================================================
# 5. Bimestres académicos 2026
# ======================================================================

BIMESTRES_2026: list[BimestreAcademico] = [
    {
        "numero": 1,
        "etiqueta": "I Bimestre",
        "periodo": "Feb - Abr",
        "fecha_inicio": "02 Feb",
        "fecha_fin": "30 Abr",
        "mes_inicio": "FEBRERO",
        "mes_fin": "ABRIL",
    },
    {
        "numero": 2,
        "etiqueta": "II Bimestre",
        "periodo": "May - Jun",
        "fecha_inicio": "04 May",
        "fecha_fin": "30 Jun",
        "mes_inicio": "MAYO",
        "mes_fin": "JUNIO",
    },
    {
        "numero": 3,
        "etiqueta": "III Bimestre",
        "periodo": "Jul - Sep",
        "fecha_inicio": "06 Jul",
        "fecha_fin": "30 Sep",
        "mes_inicio": "JULIO",
        "mes_fin": "SEPTIEMBRE",
    },
    {
        "numero": 4,
        "etiqueta": "IV Bimestre",
        "periodo": "Oct - Dic",
        "fecha_inicio": "05 Oct",
        "fecha_fin": "18 Dic",
        "mes_inicio": "OCTUBRE",
        "mes_fin": "DICIEMBRE",
    },
]


# ======================================================================
# 6. Info rápida (cards del hero)
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
        "icono": "layers",
        "titulo": "Bimestres",
        "valor": "4 bimestres por año",
        "descripcion": "Cada bimestre con parciales, finales y cierre de actas.",
        "color": "blue",
    },
    {
        "icono": "clock",
        "titulo": "Duración",
        "valor": "3 años · 12 bimestres",
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
# 7. Opciones de filtros
# ======================================================================

OPCIONES_CARRERA: list[OpcionFiltro] = [
    {"valor": "todas", "etiqueta": "Todas las carreras", "icono": "list"},
    {"valor": "sistemas", "etiqueta": "Sistemas", "icono": "cpu"},
    {"valor": "contaduria", "etiqueta": "Contaduría", "icono": "calculator"},
    {"valor": "secretariado", "etiqueta": "Secretariado", "icono": "briefcase"},
    {"valor": "comercio", "etiqueta": "Comercio Int.", "icono": "globe"},
    {"valor": "electronica", "etiqueta": "Electrónica", "icono": "zap"},
    {"valor": "institucional", "etiqueta": "Institucional", "icono": "landmark"},
]

OPCIONES_TIPO_EVENTO: list[OpcionFiltro] = [
    {"valor": "todos", "etiqueta": "Todos los tipos", "icono": "filter"},
    {"valor": "inicio_bimestre", "etiqueta": "Inicios de bimestre", "icono": "play_circle"},
    {"valor": "parcial", "etiqueta": "Parciales", "icono": "file-pen"},
    {"valor": "examen_final", "etiqueta": "Exámenes finales", "icono": "file_check"},
    {"valor": "cierre_actas", "etiqueta": "Cierres de actas", "icono": "file_lock"},
    {"valor": "taller", "etiqueta": "Talleres", "icono": "wrench"},
    {"valor": "taller_tecnico", "etiqueta": "Talleres técnicos", "icono": "code"},
    {"valor": "seminario", "etiqueta": "Seminarios", "icono": "mic"},
    {"valor": "charla", "etiqueta": "Charlas", "icono": "graduation_cap"},
    {"valor": "feria", "etiqueta": "Ferias", "icono": "store"},
    {"valor": "deportivo", "etiqueta": "Deportivos", "icono": "trophy"},
    {"valor": "cultural", "etiqueta": "Culturales", "icono": "music"},
    {"valor": "institucional", "etiqueta": "Institucionales", "icono": "landmark"},
]

OPCIONES_ORDEN: list[OpcionOrden] = [
    {"valor": "fecha_asc", "etiqueta": "Fecha (más próximos primero)"},
    {"valor": "fecha_desc", "etiqueta": "Fecha (más lejanos primero)"},
    {"valor": "bimestre_asc", "etiqueta": "Bimestre (1° al 4°)"},
    {"valor": "tipo_asc", "etiqueta": "Tipo (A-Z)"},
]


# ======================================================================
# 8. Próximos eventos del instituto (CON BIMESTRES)
# ======================================================================

PROXIMOS_EVENTOS: list[ProximoEvento] = [
    # ══════════════════════════════════════════════════════════════════
    # I BIMESTRE (Feb - Abr)
    # ══════════════════════════════════════════════════════════════════
    {
        "mes": "FEBRERO", "anio": "2026", "dia": "02",
        "titulo": "Inicio del I Bimestre",
        "descripcion": "Apertura oficial del primer bimestre académico.",
        "tipo": "inicio_bimestre", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 1,
    },
    {
        "mes": "FEBRERO", "anio": "2026", "dia": "09",
        "titulo": "Charla: Primeros pasos en la vida técnica",
        "descripcion": (
            "Charla de orientación para estudiantes nuevos: cómo "
            "organizarse y aprovechar los recursos del instituto."
        ),
        "tipo": "charla", "carrera": "institucional",
        "lugar": "Aula Magna", "bimestre": 1,
    },
    {
        "mes": "FEBRERO", "anio": "2026", "dia": "16",
        "titulo": "Taller técnico: Herramientas ofimáticas",
        "descripcion": "Taller práctico de ofimática para primer año.",
        "tipo": "taller_tecnico", "carrera": "institucional",
        "lugar": "Laboratorio 1", "bimestre": 1,
    },
    {
        "mes": "MARZO", "anio": "2026", "dia": "02",
        "titulo": "Seminario: Metodología de investigación",
        "descripcion": "Introducción a la investigación técnica.",
        "tipo": "seminario", "carrera": "institucional",
        "lugar": "Auditorio Principal", "bimestre": 1,
    },
    {
        "mes": "MARZO", "anio": "2026", "dia": "23",
        "titulo": "Parciales · I Bimestre",
        "descripcion": "Exámenes parciales del I Bimestre (23 al 27).",
        "tipo": "parcial", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 1,
    },
    {
        "mes": "ABRIL", "anio": "2026", "dia": "27",
        "titulo": "Examen final · I Bimestre",
        "descripcion": "Exámenes finales del I Bimestre (27 al 30).",
        "tipo": "examen_final", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 1,
    },
    {
        "mes": "ABRIL", "anio": "2026", "dia": "30",
        "titulo": "Fin del I Bimestre",
        "descripcion": "Cierre del primer bimestre académico.",
        "tipo": "institucional", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 1,
    },
    # ══════════════════════════════════════════════════════════════════
    # II BIMESTRE (May - Jun)
    # ══════════════════════════════════════════════════════════════════
    {
        "mes": "MAYO", "anio": "2026", "dia": "04",
        "titulo": "Inicio del II Bimestre",
        "descripcion": "Apertura oficial del segundo bimestre.",
        "tipo": "inicio_bimestre", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 2,
    },
    {
        "mes": "MAYO", "anio": "2026", "dia": "05",
        "titulo": "Cierre de actas · I Bimestre",
        "descripcion": "Plazo máximo para entrega de actas del I Bimestre.",
        "tipo": "cierre_actas", "carrera": "institucional",
        "lugar": "Secretaría Académica", "bimestre": 1,
    },
    {
        "mes": "MAYO", "anio": "2026", "dia": "08",
        "titulo": "Seminario: Inteligencia Artificial aplicada",
        "descripcion": "Seminario abierto sobre IA en el mundo laboral.",
        "tipo": "seminario", "carrera": "sistemas",
        "lugar": "Auditorio Principal", "bimestre": 2,
    },
    {
        "mes": "MAYO", "anio": "2026", "dia": "15",
        "titulo": "Taller técnico: Git y control de versiones",
        "descripcion": "Taller hands-on de Git y GitHub para Sistemas.",
        "tipo": "taller_tecnico", "carrera": "sistemas",
        "lugar": "Laboratorio 3", "bimestre": 2,
    },
    {
        "mes": "MAYO", "anio": "2026", "dia": "25",
        "titulo": "Parciales · II Bimestre",
        "descripcion": "Exámenes parciales del II Bimestre (25 al 29).",
        "tipo": "parcial", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 2,
    },
    {
        "mes": "MAYO", "anio": "2026", "dia": "29",
        "titulo": "Festival cultural · Día del Estudiante",
        "descripcion": "Celebración por el Día del Estudiante.",
        "tipo": "cultural", "carrera": "institucional",
        "lugar": "Patio Central", "bimestre": 2,
    },
    {
        "mes": "JUNIO", "anio": "2026", "dia": "12",
        "titulo": "Feria de innovación y proyectos",
        "descripcion": "Exposición anual de proyectos estudiantiles.",
        "tipo": "feria", "carrera": "institucional",
        "lugar": "Patio Central", "bimestre": 2,
    },
    {
        "mes": "JUNIO", "anio": "2026", "dia": "19",
        "titulo": "Charla: Cómo preparar tu CV técnico",
        "descripcion": "Charla con reclutadores sobre CV técnico.",
        "tipo": "charla", "carrera": "institucional",
        "lugar": "Aula 205", "bimestre": 2,
    },
    {
        "mes": "JUNIO", "anio": "2026", "dia": "29",
        "titulo": "Examen final · II Bimestre",
        "descripcion": "Exámenes finales del II Bimestre (29 al 30).",
        "tipo": "examen_final", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 2,
    },
    {
        "mes": "JUNIO", "anio": "2026", "dia": "30",
        "titulo": "Fin del II Bimestre",
        "descripcion": "Cierre del segundo bimestre.",
        "tipo": "institucional", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 2,
    },
    # ══════════════════════════════════════════════════════════════════
    # III BIMESTRE (Jul - Sep)
    # ══════════════════════════════════════════════════════════════════
    {
        "mes": "JULIO", "anio": "2026", "dia": "06",
        "titulo": "Inicio del III Bimestre",
        "descripcion": "Apertura oficial del tercer bimestre.",
        "tipo": "inicio_bimestre", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 3,
    },
    {
        "mes": "JULIO", "anio": "2026", "dia": "07",
        "titulo": "Cierre de actas · II Bimestre",
        "descripcion": "Plazo máximo para entrega de actas del II Bimestre.",
        "tipo": "cierre_actas", "carrera": "institucional",
        "lugar": "Secretaría Académica", "bimestre": 2,
    },
    {
        "mes": "JULIO", "anio": "2026", "dia": "10",
        "titulo": "Taller técnico: Automatización con Python",
        "descripcion": "Automatización de tareas con Python.",
        "tipo": "taller_tecnico", "carrera": "sistemas",
        "lugar": "Laboratorio 1", "bimestre": 3,
    },
    {
        "mes": "JULIO", "anio": "2026", "dia": "20",
        "titulo": "Parciales · III Bimestre",
        "descripcion": "Exámenes parciales del III Bimestre (20 al 24).",
        "tipo": "parcial", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 3,
    },
    {
        "mes": "AGOSTO", "anio": "2026", "dia": "14",
        "titulo": "Seminario: Ciberseguridad para pymes",
        "descripcion": "Seminario sobre ciberseguridad en pymes.",
        "tipo": "seminario", "carrera": "sistemas",
        "lugar": "Auditorio Principal", "bimestre": 3,
    },
    {
        "mes": "AGOSTO", "anio": "2026", "dia": "21",
        "titulo": "Hackathon interno · Innovación",
        "descripcion": "Hackathon interno de 24 horas.",
        "tipo": "taller_tecnico", "carrera": "sistemas",
        "lugar": "Laboratorios", "bimestre": 3,
    },
    {
        "mes": "SEPTIEMBRE", "anio": "2026", "dia": "21",
        "titulo": "Festival cultural · Año Nuevo Andino",
        "descripcion": "Celebración del Willka Kuti.",
        "tipo": "cultural", "carrera": "institucional",
        "lugar": "Patio Central", "bimestre": 3,
    },
    {
        "mes": "SEPTIEMBRE", "anio": "2026", "dia": "29",
        "titulo": "Examen final · III Bimestre",
        "descripcion": "Exámenes finales del III Bimestre (29 al 30).",
        "tipo": "examen_final", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 3,
    },
    {
        "mes": "SEPTIEMBRE", "anio": "2026", "dia": "30",
        "titulo": "Fin del III Bimestre",
        "descripcion": "Cierre del tercer bimestre.",
        "tipo": "institucional", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 3,
    },
    # ══════════════════════════════════════════════════════════════════
    # IV BIMESTRE (Oct - Dic)
    # ══════════════════════════════════════════════════════════════════
    {
        "mes": "OCTUBRE", "anio": "2026", "dia": "05",
        "titulo": "Inicio del IV Bimestre",
        "descripcion": "Apertura oficial del cuarto bimestre.",
        "tipo": "inicio_bimestre", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 4,
    },
    {
        "mes": "OCTUBRE", "anio": "2026", "dia": "06",
        "titulo": "Cierre de actas · III Bimestre",
        "descripcion": "Plazo máximo para entrega de actas del III Bimestre.",
        "tipo": "cierre_actas", "carrera": "institucional",
        "lugar": "Secretaría Académica", "bimestre": 3,
    },
    {
        "mes": "OCTUBRE", "anio": "2026", "dia": "16",
        "titulo": "Charla: Empleabilidad en el mundo tech",
        "descripcion": "Charla con líderes de la industria.",
        "tipo": "charla", "carrera": "sistemas",
        "lugar": "Auditorio Principal", "bimestre": 4,
    },
    {
        "mes": "OCTUBRE", "anio": "2026", "dia": "31",
        "titulo": "Noche de talentos · Halloween institucional",
        "descripcion": "Evento cultural y recreativo.",
        "tipo": "cultural", "carrera": "institucional",
        "lugar": "Patio Central", "bimestre": 4,
    },
    {
        "mes": "NOVIEMBRE", "anio": "2026", "dia": "13",
        "titulo": "Seminario: Blockchain y contratos inteligentes",
        "descripcion": "Introducción a blockchain y contratos inteligentes.",
        "tipo": "seminario", "carrera": "sistemas",
        "lugar": "Auditorio Principal", "bimestre": 4,
    },
    {
        "mes": "NOVIEMBRE", "anio": "2026", "dia": "23",
        "titulo": "Parciales · IV Bimestre",
        "descripcion": "Exámenes parciales del IV Bimestre (23 al 27).",
        "tipo": "parcial", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 4,
    },
    {
        "mes": "NOVIEMBRE", "anio": "2026", "dia": "27",
        "titulo": "Feria de empleo · Empresas aliadas",
        "descripcion": "Encuentro con empresas aliadas.",
        "tipo": "feria", "carrera": "institucional",
        "lugar": "Patio Central", "bimestre": 4,
    },
    {
        "mes": "DICIEMBRE", "anio": "2026", "dia": "17",
        "titulo": "Examen final · IV Bimestre",
        "descripcion": "Exámenes finales del IV Bimestre (17 al 18).",
        "tipo": "examen_final", "carrera": "institucional",
        "lugar": "Aulas asignadas", "bimestre": 4,
    },
    {
        "mes": "DICIEMBRE", "anio": "2026", "dia": "18",
        "titulo": "Fin del IV Bimestre · Cierre del año",
        "descripcion": "Cierre del cuarto bimestre y del año académico.",
        "tipo": "institucional", "carrera": "institucional",
        "lugar": "Campus INSTEIN", "bimestre": 4,
    },
    {
        "mes": "DICIEMBRE", "anio": "2026", "dia": "22",
        "titulo": "Cierre de actas · IV Bimestre",
        "descripcion": "Plazo máximo para entrega de actas del IV Bimestre.",
        "tipo": "cierre_actas", "carrera": "institucional",
        "lugar": "Secretaría Académica", "bimestre": 4,
    },
    {
        "mes": "DICIEMBRE", "anio": "2026", "dia": "18",
        "titulo": "Cena de fin de año · Estudiantes y docentes",
        "descripcion": "Celebración de cierre de año.",
        "tipo": "cultural", "carrera": "institucional",
        "lugar": "Salón de Eventos", "bimestre": 4,
    },
]


# ======================================================================
# 9. Fechas importantes de Bolivia y el mundo
# ======================================================================

FECHAS_IMPORTANTES: list[FechaImportante] = [
    # ══════════════════════════════════════════════════════════════════
    # PRIMER SEMESTRE (Enero - Junio)
    # ══════════════════════════════════════════════════════════════════
    {"mes": "ENERO", "semestre": "I", "dia": "01", "titulo": "Año Nuevo", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "ENERO", "semestre": "I", "dia": "22", "titulo": "Día del Estado Plurinacional de Bolivia", "alcance": "nacional", "tipo": "feriado_nacional"},
    {"mes": "ENERO", "semestre": "I", "dia": "24", "titulo": "Fiesta de la Alasita (Tributo al Ekeko)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "FEBRERO", "semestre": "I", "dia": "10", "titulo": "Efeméride de Oruro", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "FEBRERO", "semestre": "I", "dia": "21", "titulo": "Día Internacional de la Lengua Materna", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "FEBRERO", "semestre": "I", "dia": "—", "titulo": "Carnaval de Oruro y feriados de Carnaval", "alcance": "nacional", "tipo": "feriado_movible"},
    {"mes": "MARZO", "semestre": "I", "dia": "08", "titulo": "Día Internacional de la Mujer", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "MARZO", "semestre": "I", "dia": "19", "titulo": "Día del Padre Boliviano", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "MARZO", "semestre": "I", "dia": "22", "titulo": "Día Mundial del Agua", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "MARZO", "semestre": "I", "dia": "23", "titulo": "Día del Mar (Recordatorio de la pérdida del litoral)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "ABRIL", "semestre": "I", "dia": "07", "titulo": "Día Mundial de la Salud", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "ABRIL", "semestre": "I", "dia": "15", "titulo": "Efeméride de Tarija", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "ABRIL", "semestre": "I", "dia": "22", "titulo": "Día de la Tierra", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "ABRIL", "semestre": "I", "dia": "—", "titulo": "Semana Santa (Viernes Santo es feriado)", "alcance": "nacional", "tipo": "feriado_movible"},
    {"mes": "MAYO", "semestre": "I", "dia": "01", "titulo": "Día del Trabajo", "alcance": "internacional", "tipo": "feriado_nacional"},
    {"mes": "MAYO", "semestre": "I", "dia": "25", "titulo": "Efeméride de Chuquisaca (Primer Grito Libertario)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "MAYO", "semestre": "I", "dia": "27", "titulo": "Día de la Madre Boliviana (Heroínas de la Coronilla)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "JUNIO", "semestre": "I", "dia": "05", "titulo": "Día Mundial del Medio Ambiente", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "JUNIO", "semestre": "I", "dia": "06", "titulo": "Día del Maestro Boliviano", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "JUNIO", "semestre": "I", "dia": "21", "titulo": "Año Nuevo Andino Amazónico Chaqueño (Willka Kuti)", "alcance": "nacional", "tipo": "feriado_nacional"},
    {"mes": "JUNIO", "semestre": "I", "dia": "—", "titulo": "Corpus Christi", "alcance": "nacional", "tipo": "feriado_movible"},
    # ══════════════════════════════════════════════════════════════════
    # SEGUNDO SEMESTRE (Julio - Diciembre)
    # ══════════════════════════════════════════════════════════════════
    {"mes": "JULIO", "semestre": "II", "dia": "16", "titulo": "Efeméride de La Paz (Grito libertario de 1809)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "JULIO", "semestre": "II", "dia": "18", "titulo": "Día Internacional de Nelson Mandela", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "AGOSTO", "semestre": "II", "dia": "06", "titulo": "Día de la Independencia de Bolivia (Fiesta Nacional)", "alcance": "nacional", "tipo": "feriado_nacional"},
    {"mes": "AGOSTO", "semestre": "II", "dia": "07", "titulo": "Día de las Fuerzas Armadas", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "AGOSTO", "semestre": "II", "dia": "09", "titulo": "Día Internacional de los Pueblos Indígenas", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "AGOSTO", "semestre": "II", "dia": "17", "titulo": "Día de la Bandera Nacional", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "SEPTIEMBRE", "semestre": "II", "dia": "14", "titulo": "Efeméride de Cochabamba", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "SEPTIEMBRE", "semestre": "II", "dia": "21", "titulo": "Día del Estudiante, Médico y de la Juventud", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "SEPTIEMBRE", "semestre": "II", "dia": "21", "titulo": "Día Internacional de la Paz", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "SEPTIEMBRE", "semestre": "II", "dia": "24", "titulo": "Efeméride de Santa Cruz y de Pando", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "OCTUBRE", "semestre": "II", "dia": "11", "titulo": "Día de la Mujer Boliviana (Homenaje a Adela Zamudio)", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "OCTUBRE", "semestre": "II", "dia": "16", "titulo": "Día Mundial de la Alimentación", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "OCTUBRE", "semestre": "II", "dia": "24", "titulo": "Día de las Naciones Unidas", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "NOVIEMBRE", "semestre": "II", "dia": "02", "titulo": "Día de Todos los Difuntos / Todos los Santos", "alcance": "nacional", "tipo": "feriado_nacional"},
    {"mes": "NOVIEMBRE", "semestre": "II", "dia": "10", "titulo": "Efeméride de Potosí", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "NOVIEMBRE", "semestre": "II", "dia": "18", "titulo": "Efeméride del Beni", "alcance": "nacional", "tipo": "efemeride_nacional"},
    {"mes": "NOVIEMBRE", "semestre": "II", "dia": "20", "titulo": "Día Universal del Niño", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "DICIEMBRE", "semestre": "II", "dia": "01", "titulo": "Día Mundial del SIDA", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "DICIEMBRE", "semestre": "II", "dia": "10", "titulo": "Día de los Derechos Humanos", "alcance": "internacional", "tipo": "internacional"},
    {"mes": "DICIEMBRE", "semestre": "II", "dia": "25", "titulo": "Navidad", "alcance": "internacional", "tipo": "feriado_nacional"},
]


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Alias de tipos ---
    "AlcanceFecha",
    "BimestreNumero",
    "SemestreAcademico",
    "TipoEventoId",
    "TipoFechaId",
    # --- Modelos ---
    "BimestreAcademico",
    "FechaImportante",
    "InfoRapida",
    "MetaTipoEvento",
    "MetaTipoFecha",
    "OpcionFiltro",
    "OpcionOrden",
    "ProximoEvento",
    # --- Tipos (metadata) ---
    "TIPOS_EVENTO",
    "TIPOS_FECHA",
    # --- Datos estáticos ---
    "BIMESTRES_2026",
    "FECHAS_IMPORTANTES",
    "INFO_RAPIDA",
    "OPCIONES_CARRERA",
    "OPCIONES_ORDEN",
    "OPCIONES_TIPO_EVENTO",
    "PROXIMOS_EVENTOS",
]