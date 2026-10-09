

from __future__ import annotations

from functools import lru_cache
from typing import Literal, TypedDict


# ======================================================================
# 1. Alias de tipos
# ======================================================================

CategoriaId = Literal[
    "todas",
    "tecnologia",
    "contaduria",
    "empleabilidad",
    "institucional",
    "estudiantes",
    "tutoriales",
]
"""Identificadores válidos de categoría.

`Literal` restringe el tipo a estos strings exactos. El IDE y mypy
te avisarán si escribes mal un ID (ej: "tecnologiaa").
"""

ColorScheme = Literal[
    "gray",
    "blue",
    "violet",
    "green",
    "crimson",
    "orange",
    "cyan",
]
"""Nombres de color scheme de Radix Themes usados por las categorías."""


# ======================================================================
# 2. Modelos
# ======================================================================


class Categoria(TypedDict):
    """Metadatos visuales de una categoría del blog."""

    valor: CategoriaId
    etiqueta: str
    icono: str
    color: ColorScheme


class Post(TypedDict):
    """Estructura completa de un post del blog."""

    id: int
    titulo: str
    extracto: str
    contenido: str
    categoria: CategoriaId
    autor: str
    fecha: str
    minutos_lectura: int
    destacado: bool
    imagen: str


# ======================================================================
# 3. Categorías
# ======================================================================

CATEGORIAS: list[Categoria] = [
    {
        "valor": "todas",
        "etiqueta": "Todas",
        "icono": "list",
        "color": "gray",
    },
    {
        "valor": "tecnologia",
        "etiqueta": "Tecnología",
        "icono": "cpu",
        "color": "blue",
    },
    {
        "valor": "contaduria",
        "etiqueta": "Contaduría",
        "icono": "calculator",
        "color": "violet",
    },
    {
        "valor": "empleabilidad",
        "etiqueta": "Empleabilidad",
        "icono": "trending-up",
        "color": "green",
    },
    {
        "valor": "institucional",
        "etiqueta": "Institucional",
        "icono": "landmark",
        "color": "crimson",
    },
    {
        "valor": "estudiantes",
        "etiqueta": "Estudiantes",
        "icono": "graduation-cap",
        "color": "orange",
    },
    {
        "valor": "tutoriales",
        "etiqueta": "Tutoriales",
        "icono": "book-open",
        "color": "cyan",
    },
]


# ======================================================================
# 4. Posts del blog
# ======================================================================

_POSTS: list[Post] = [
    # ==================================================================
    # POST DESTACADO
    # ==================================================================
    {
        "id": 0,
        "titulo": "Cómo la IA está transformando la formación técnica en Bolivia",
        "extracto": (
            "Las herramientas de inteligencia artificial están cambiando "
            "la forma en que los estudiantes técnicos aprenden, practican "
            "y se preparan para el mundo laboral."
        ),
        "contenido": (
            "La inteligencia artificial (IA) dejó de ser una promesa "
            "futurista para convertirse en una realidad cotidiana en las "
            "aulas técnicas de Bolivia. Desde asistentes de código hasta "
            "plataformas adaptativas de aprendizaje, la IA está "
            "redefiniendo cómo se enseña y cómo se aprende.\n\n"
            "En INSTEIN, por ejemplo, los estudiantes de Sistemas ya "
            "utilizan herramientas de IA para revisar su código, generar "
            "pruebas automatizadas y documentar proyectos."
        ),
        "categoria": "tecnologia",
        "autor": "Equipo INSTEIN",
        "fecha": "15 de abril, 2026",
        "minutos_lectura": 8,
        "destacado": True,
        "imagen": "ia_formacion_tecnica.webp",
    },
    # ==================================================================
    # POSTS REGULARES
    # ==================================================================
    {
        "id": 1,
        "titulo": "5 habilidades técnicas que todo programador junior debe dominar",
        "extracto": (
            "Desde control de versiones hasta testing automatizado, estas "
            "son las competencias que te harán destacar en tu primer empleo."
        ),
        "contenido": (
            "El mercado laboral técnico en Bolivia es cada vez más "
            "competitivo. Para destacar como programador junior, no basta "
            "con saber un lenguaje: necesitas dominar un conjunto de "
            "habilidades transversales.\n\n"
            "1. Control de versiones con Git.\n"
            "2. Testing automatizado.\n"
            "3. Lectura de código ajeno.\n"
            "4. Manejo de la terminal.\n"
            "5. Inglés técnico."
        ),
        "categoria": "tecnologia",
        "autor": "Prof. Juan Pérez",
        "fecha": "10 de abril, 2026",
        "minutos_lectura": 6,
        "destacado": False,
        "imagen": "habilidades_programador.webp",
    },
    {
        "id": 2,
        "titulo": "Guía completa para inscribirte en el turno nocturno",
        "extracto": (
            "¿Trabajas y quieres estudiar? Te explicamos paso a paso cómo "
            "matricularte en el turno nocturno."
        ),
        "contenido": (
            "El turno nocturno fue diseñado específicamente para "
            "personas que trabajan durante el día pero quieren estudiar "
            "una carrera técnica.\n\n"
            "Paso 1: elige tu carrera.\n"
            "Paso 2: reúne los documentos.\n"
            "Paso 3: contáctanos por WhatsApp.\n"
            "Paso 4: agenda una entrevista.\n"
            "Paso 5: comienza clases."
        ),
        "categoria": "institucional",
        "autor": "Admisiones INSTEIN",
        "fecha": "08 de abril, 2026",
        "minutos_lectura": 4,
        "destacado": False,
        "imagen": "turno_nocturno.webp",
    },
    {
        "id": 3,
        "titulo": "Contabilidad digital: herramientas que debes conocer en 2026",
        "extracto": (
            "SIAT, SICON, hojas de cálculo avanzadas y software en la "
            "nube. Estas son las herramientas que todo técnico contable "
            "debe manejar."
        ),
        "contenido": (
            "La contabilidad tradicional dejó de ser un ejercicio de "
            "papel y lápiz. Hoy, el técnico contable boliviano debe "
            "manejar un ecosistema de herramientas digitales.\n\n"
            "SIAT, SICON, Excel avanzado y software en la nube son las "
            "herramientas básicas."
        ),
        "categoria": "contaduria",
        "autor": "Prof. María González",
        "fecha": "05 de abril, 2026",
        "minutos_lectura": 7,
        "destacado": False,
        "imagen": "contabilidad_digital.webp",
    },
    {
        "id": 4,
        "titulo": "Cómo prepararte para tu primera entrevista técnica",
        "extracto": (
            "La entrevista técnica puede ser intimidante. Aquí te damos "
            "las estrategias que usan nuestros egresados."
        ),
        "contenido": (
            "La primera entrevista técnica es un momento decisivo. "
            "Muchos candidatos con excelentes habilidades técnicas fallan "
            "por no saber comunicarse.\n\n"
            "Antes de la entrevista: investiga la empresa y prepara "
            "ejemplos de proyectos. Durante: piensa en voz alta. Después: "
            "envía un correo de agradecimiento."
        ),
        "categoria": "empleabilidad",
        "autor": "Equipo INSTEIN",
        "fecha": "02 de abril, 2026",
        "minutos_lectura": 5,
        "destacado": False,
        "imagen": "entrevista_tecnica.webp",
    },
    {
        "id": 5,
        "titulo": "Electrónica aplicada: proyecto de domótica para principiantes",
        "extracto": (
            "Tutorial paso a paso para construir un sistema básico de "
            "domótica con Arduino, sensores y relés."
        ),
        "contenido": (
            "La domótica es la automatización de una vivienda. En este "
            "tutorial construiremos un sistema básico que enciende y "
            "apaga luces según la luz ambiental.\n\n"
            "Materiales: Arduino UNO, sensor LDR, módulo de relé."
        ),
        "categoria": "tutoriales",
        "autor": "Prof. Carlos Rojas",
        "fecha": "28 de marzo, 2026",
        "minutos_lectura": 10,
        "destacado": False,
        "imagen": "proyecto_domotica.webp",
    },
    {
        "id": 6,
        "titulo": "Cómo elegir tu carrera técnica según tus intereses",
        "extracto": (
            "¿Sistemas, Contaduría, Secretariado, Comercio o Electrónica? "
            "Te ayudamos a tomar una decisión informada."
        ),
        "contenido": (
            "Elegir una carrera técnica es una decisión que marcará los "
            "próximos 3 años de tu vida. Aquí te damos una guía práctica.\n\n"
            "Pregúntate: ¿qué actividades disfruto hacer? Piensa en tu "
            "futuro. Conversa con profesionales. Visítanos."
        ),
        "categoria": "estudiantes",
        "autor": "Orientación Vocacional",
        "fecha": "25 de marzo, 2026",
        "minutos_lectura": 6,
        "destacado": False,
        "imagen": "elegir_carrera.webp",
    },
    {
        "id": 7,
        "titulo": "Casos de éxito: egresados que emprendieron en Bolivia",
        "extracto": (
            "Conoce las historias de 3 egresados de INSTEIN que hoy "
            "lideran sus propios emprendimientos técnicos."
        ),
        "contenido": (
            "Nuestros egresados no solo trabajan en empresas: muchos "
            "crean sus propios emprendimientos.\n\n"
            "Carlos (Sistemas, 2022): agencia de desarrollo web.\n"
            "María (Contaduría, 2021): estudio contable.\n"
            "José (Electrónica, 2023): servicio técnico de domótica."
        ),
        "categoria": "empleabilidad",
        "autor": "Equipo INSTEIN",
        "fecha": "20 de marzo, 2026",
        "minutos_lectura": 8,
        "destacado": False,
        "imagen": "egresados_emprendedores.webp",
    },
    {
        "id": 8,
        "titulo": "Comercio internacional: oportunidades para técnicos en 2026",
        "extracto": (
            "El comercio exterior boliviano está en expansión. "
            "Analizamos las oportunidades laborales para técnicos."
        ),
        "contenido": (
            "Bolivia está ampliando sus relaciones comerciales con "
            "varios países de la región. Esto genera una demanda "
            "creciente de técnicos en comercio internacional."
        ),
        "categoria": "empleabilidad",
        "autor": "Prof. Ana Vargas",
        "fecha": "18 de marzo, 2026",
        "minutos_lectura": 7,
        "destacado": False,
        "imagen": "comercio_internacional.webp",
    },
    {
        "id": 9,
        "titulo": "Secretariado ejecutivo: habilidades blandas que marcan la diferencia",
        "extracto": (
            "Más allá de la ofimática, el éxito como secretaria ejecutiva "
            "depende de habilidades como comunicación y organización."
        ),
        "contenido": (
            "El secretariado ejecutivo es una carrera técnico-profesional "
            "que combina tecnología con habilidades humanas.\n\n"
            "Comunicación asertiva, organización impecable, discreción "
            "y protocolo empresarial."
        ),
        "categoria": "estudiantes",
        "autor": "Prof. Laura Méndez",
        "fecha": "15 de marzo, 2026",
        "minutos_lectura": 5,
        "destacado": False,
        "imagen": "secretariado_ejecutivo.webp",
    },
    {
        "id": 10,
        "titulo": "Cómo aprovechar las ferias de innovación del instituto",
        "extracto": (
            "Las ferias internas son una oportunidad única para mostrar "
            "tu talento, ganar becas y conectar con empresas."
        ),
        "contenido": (
            "Dos veces al año, INSTEIN organiza ferias de innovación. "
            "Estas ferias no son solo exhibiciones: son competencias "
            "reales con premios reales."
        ),
        "categoria": "institucional",
        "autor": "Equipo INSTEIN",
        "fecha": "12 de marzo, 2026",
        "minutos_lectura": 6,
        "destacado": False,
        "imagen": "feria_innovacion.webp",
    },
    {
        "id": 11,
        "titulo": "Tutorial: crear tu primer sitio web con HTML y CSS",
        "extracto": (
            "Guía completa desde cero para crear un sitio web responsive "
            "usando solo HTML y CSS."
        ),
        "contenido": (
            "Este tutorial te guiará paso a paso para crear un sitio "
            "web básico pero funcional usando HTML y CSS.\n\n"
            "Paso 1: estructura HTML. Paso 2: estilos CSS. "
            "Paso 3: responsive. Paso 4: publicar."
        ),
        "categoria": "tutoriales",
        "autor": "Prof. Juan Pérez",
        "fecha": "08 de marzo, 2026",
        "minutos_lectura": 12,
        "destacado": False,
        "imagen": "primer_sitio_web.webp",
    },
    {
        "id": 12,
        "titulo": "La importancia de la ética profesional en el mundo técnico",
        "extracto": (
            "Los técnicos toman decisiones todos los días que impactan a "
            "las personas y las empresas."
        ),
        "contenido": (
            "La ética profesional no es un tema abstracto: es lo que "
            "define cómo actúas cuando nadie te está mirando.\n\n"
            "En Sistemas, Contaduría y Electrónica, las decisiones éticas "
            "son parte del día a día."
        ),
        "categoria": "institucional",
        "autor": "Dirección Académica",
        "fecha": "05 de marzo, 2026",
        "minutos_lectura": 5,
        "destacado": False,
        "imagen": "etica_profesional.webp",
    },
]
"""Posts del blog institucional.

⚠️ Privado (prefijo `_`): usar las funciones públicas del repositorio.
"""


# ======================================================================
# 5. API pública del repositorio
# ======================================================================


@lru_cache(maxsize=1)
def obtener_posts() -> list[Post]:
    """
    Devuelve todos los posts del blog.

    Returns:
        Lista de `Post`. La lista se cachea tras la primera llamada.

    ⚠️ La lista devuelta NO debe mutarse.
    """
    return _POSTS


@lru_cache(maxsize=None)
def obtener_post(post_id: int) -> Post | None:
    """
    Busca un post por su ID.

    Args:
        post_id: ID del post a buscar.

    Returns:
        El post encontrado, o `None` si no existe.
    """
    for post in _POSTS:
        if post["id"] == post_id:
            return post
    return None


@lru_cache(maxsize=1)
def obtener_post_destacado() -> Post:
    """
    Devuelve el primer post con `destacado=True`.

    Returns:
        El post destacado, o el primer post del catálogo si ninguno
        está marcado.
    """
    for post in _POSTS:
        if post["destacado"]:
            return post
    return _POSTS[0]


def obtener_posts_por_categoria(categoria: CategoriaId) -> list[Post]:
    """
    Filtra los posts por categoría.

    Args:
        categoria: Clave de categoría. Si es `"todas"`, devuelve todos.

    Returns:
        Lista de `Post` que pertenecen a la categoría.
    """
    if categoria == "todas":
        return list(_POSTS)
    return [p for p in _POSTS if p["categoria"] == categoria]


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Tipos ---
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
    # --- Datos ---
    "CATEGORIAS",
    # --- API pública ---
    "obtener_post",
    "obtener_post_destacado",
    "obtener_posts",
    "obtener_posts_por_categoria",
]