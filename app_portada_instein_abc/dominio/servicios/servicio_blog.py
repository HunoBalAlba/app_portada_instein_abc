

from __future__ import annotations

from ...dominio.modelos.blog import (
    CategoriaId,
    Post,
)
from ...infraestructura.repositorios.repositorio_blog import (
    obtener_post as _obtener_post_repo,
    obtener_posts as _obtener_posts_repo,
)


# ======================================================================
# 1. Filtros por criterios
# ======================================================================


def filtrar_posts_por_categoria(
    categoria: CategoriaId,
) -> list[Post]:
    """
    Filtra posts por categoría.

    Args:
        categoria: Clave de categoría. Si es `"todas"`, devuelve todos.

    Returns:
        Lista de posts de la categoría.
    """
    if categoria == "todas":
        return list(_obtener_posts_repo())
    return [
        p for p in _obtener_posts_repo()
        if p["categoria"] == categoria
    ]


def filtrar_posts_sin_destacado() -> list[Post]:
    """
    Devuelve todos los posts EXCEPTO el destacado.

    Útil para el grid principal del blog, ya que el destacado se
    renderiza aparte.

    Returns:
        Lista de posts sin el destacado.
    """
    return [p for p in _obtener_posts_repo() if not p["destacado"]]


def filtrar_posts_por_autor(autor: str) -> list[Post]:
    """
    Filtra posts por autor.

    Args:
        autor: Nombre del autor (búsqueda exacta, case-insensitive).

    Returns:
        Lista de posts del autor.
    """
    autor_normalizado = autor.strip().lower()
    return [
        p for p in _obtener_posts_repo()
        if p["autor"].lower() == autor_normalizado
    ]


def filtrar_posts_por_tiempo_lectura_maximo(
    minutos: int,
) -> list[Post]:
    """
    Filtra posts que se lean en <= `minutos`.

    Args:
        minutos: Tiempo máximo de lectura.

    Returns:
        Lista de posts cortos.
    """
    return [
        p for p in _obtener_posts_repo()
        if p["minutos_lectura"] <= minutos
    ]


# ======================================================================
# 2. Búsqueda por texto
# ======================================================================


def buscar_posts_por_texto(
    texto: str,
    categoria: CategoriaId = "todas",
) -> list[Post]:
    """
    Busca posts por texto en múltiples campos.

    Busca en: `titulo`, `extracto`, `autor`.
    La búsqueda es case-insensitive.

    Args:
        texto: Texto a buscar. Si está vacío, devuelve todos (filtrado
            por categoría).
        categoria: Categoría opcional para filtrar antes de buscar.

    Returns:
        Lista de posts que coinciden.
    """
    posts = filtrar_posts_por_categoria(categoria)

    # Excluir el destacado del grid de búsqueda
    posts = [p for p in posts if not p["destacado"]]

    if not texto.strip():
        return posts

    busqueda = texto.strip().lower()

    return [
        p for p in posts
        if busqueda in p["titulo"].lower()
        or busqueda in p["extracto"].lower()
        or busqueda in p["autor"].lower()
    ]


# ======================================================================
# 3. Ordenamientos
# ======================================================================


def ordenar_posts_por_id(
    posts: list[Post] | None = None,
    descendente: bool = True,
) -> list[Post]:
    """
    Ordena posts por ID.

    Como los IDs se asignan cronológicamente (id 0 = más antiguo),
    ordenar por id descendente = más recientes primero.

    Args:
        posts: Lista a ordenar. Si es `None`, usa todos los posts.
        descendente: Si `True`, IDs altos primero (más recientes).

    Returns:
        Lista ordenada.
    """
    if posts is None:
        posts = list(_obtener_posts_repo())

    return sorted(posts, key=lambda p: p["id"], reverse=descendente)


def ordenar_posts_por_tiempo_lectura(
    posts: list[Post] | None = None,
    descendente: bool = False,
) -> list[Post]:
    """
    Ordena posts por tiempo de lectura.

    Args:
        posts: Lista a ordenar. Si es `None`, usa todos los posts.
        descendente: Si `True`, más largos primero. Por defecto `False`
            (más cortos primero).

    Returns:
        Lista ordenada.
    """
    if posts is None:
        posts = list(_obtener_posts_repo())

    return sorted(
        posts,
        key=lambda p: p["minutos_lectura"],
        reverse=descendente,
    )


# ======================================================================
# 4. Combinaciones (filtro + orden + paginación)
# ======================================================================


def obtener_posts_filtrados(
    categoria: CategoriaId = "todas",
    texto_busqueda: str = "",
    limite: int | None = None,
) -> list[Post]:
    """
    Combina filtro por categoría + búsqueda por texto + límite.

    Args:
        categoria: Categoría a filtrar. "todas" = sin filtro.
        texto_busqueda: Texto a buscar. "" = sin búsqueda.
        limite: Número máximo de resultados. `None` = sin límite.

    Returns:
        Lista filtrada (y opcionalmente limitada).
    """
    posts = buscar_posts_por_texto(texto_busqueda, categoria)

    if limite is not None:
        posts = posts[:limite]

    return posts


def obtener_posts_recientes(limite: int = 3) -> list[Post]:
    """
    Devuelve los N posts más recientes (excluyendo el destacado).

    Args:
        limite: Número máximo de posts.

    Returns:
        Lista de posts recientes.
    """
    posts = filtrar_posts_sin_destacado()
    return ordenar_posts_por_id(posts, descendente=True)[:limite]


def obtener_posts_de_categoria(
    categoria: CategoriaId,
    limite: int | None = None,
) -> list[Post]:
    """
    Obtiene posts de una categoría específica.

    Args:
        categoria: Clave de categoría.
        limite: Número máximo de resultados. `None` = sin límite.

    Returns:
        Lista de posts de la categoría.
    """
    posts = filtrar_posts_por_categoria(categoria)
    posts = [p for p in posts if not p["destacado"]]
    posts = ordenar_posts_por_id(posts, descendente=True)

    if limite is not None:
        posts = posts[:limite]

    return posts


# ======================================================================
# 5. Navegación entre posts
# ======================================================================


def obtener_post_anterior(post_id: int) -> Post | None:
    """
    Devuelve el post inmediatamente anterior (id - 1).

    Args:
        post_id: ID del post actual.

    Returns:
        Post anterior, o `None` si no existe.
    """
    return _obtener_post_repo(post_id - 1)


def obtener_post_siguiente(post_id: int) -> Post | None:
    """
    Devuelve el post inmediatamente siguiente (id + 1).

    Args:
        post_id: ID del post actual.

    Returns:
        Post siguiente, o `None` si no existe.
    """
    return _obtener_post_repo(post_id + 1)


def hay_post_anterior(post_id: int) -> bool:
    """Indica si existe un post anterior al `post_id` dado."""
    return _obtener_post_repo(post_id - 1) is not None


def hay_post_siguiente(post_id: int) -> bool:
    """Indica si existe un post siguiente al `post_id` dado."""
    return _obtener_post_repo(post_id + 1) is not None


# ======================================================================
# 6. Estadísticas agregadas
# ======================================================================


def contar_posts() -> int:
    """Cantidad total de posts (incluyendo el destacado)."""
    return len(_obtener_posts_repo())


def contar_posts_por_categoria(categoria: CategoriaId) -> int:
    """Cantidad de posts de una categoría."""
    return len(filtrar_posts_por_categoria(categoria))


def calcular_tiempo_lectura_promedio() -> float:
    """Tiempo promedio de lectura entre todos los posts (minutos)."""
    posts = _obtener_posts_repo()
    if not posts:
        return 0.0
    return sum(p["minutos_lectura"] for p in posts) / len(posts)


def calcular_tiempo_lectura_total() -> int:
    """Tiempo total de lectura de todos los posts (minutos)."""
    return sum(p["minutos_lectura"] for p in _obtener_posts_repo())


def contar_posts_por_autor(autor: str) -> int:
    """Cantidad de posts de un autor."""
    return len(filtrar_posts_por_autor(autor))


# ======================================================================
# 7. Validaciones
# ======================================================================


def es_categoria_valida(categoria: str) -> bool:
    """Verifica si un string es una categoría válida."""
    categorias_validas = {
        "todas",
        "tecnologia",
        "contaduria",
        "empleabilidad",
        "institucional",
        "estudiantes",
        "tutoriales",
    }
    return categoria in categorias_validas


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    # --- Búsqueda ---
    "buscar_posts_por_texto",
    # --- Estadísticas agregadas ---
    "calcular_tiempo_lectura_promedio",
    "calcular_tiempo_lectura_total",
    # --- Conteos ---
    "contar_posts",
    "contar_posts_por_autor",
    "contar_posts_por_categoria",
    # --- Validaciones ---
    "es_categoria_valida",
    # --- Filtros ---
    "filtrar_posts_por_autor",
    "filtrar_posts_por_categoria",
    "filtrar_posts_por_tiempo_lectura_maximo",
    "filtrar_posts_sin_destacado",
    # --- Navegación entre posts ---
    "hay_post_anterior",
    "hay_post_siguiente",
    "obtener_post_anterior",
    "obtener_post_siguiente",
    # --- Combinaciones ---
    "obtener_posts_de_categoria",
    "obtener_posts_filtrados",
    "obtener_posts_recientes",
    # --- Ordenamientos ---
    "ordenar_posts_por_id",
    "ordenar_posts_por_tiempo_lectura",
]