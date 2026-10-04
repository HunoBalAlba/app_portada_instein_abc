"""
Estado del Blog Institucional.

Gestiona:
- Filtros por categoría y búsqueda de texto.
- Paginación progresiva (botón "Cargar más").
- Resolución del post seleccionado desde el `post_id` de la URL.
- Navegación al post anterior / siguiente.
- Validación de ruta (redirección a `/404?origen=blog` si no existe).

Nota técnica: TIPADO ESTRICTO CON `Post`
----------------------------------------
Las `@rx.var` que devuelven un post (`post_destacado`,
`post_seleccionado`, `post_anterior`, `post_siguiente`) están tipadas
como `Post`, NO como `dict` genérico.

Esto es CRÍTICO para props tipadas como `rx.image(alt=str)`:

    ❌ dict genérico → post["titulo"] se infiere como str | int | bool
    ✅ Post          → post["titulo"] se infiere como str

Nota técnica: FALLBACK DE `post_seleccionado`
---------------------------------------------
`post_seleccionado` SIEMPRE devuelve un `Post` válido (fallback al
destacado) para garantizar el tipado que `rx.image`/`rx.foreach`
necesitan.

La validez real del id se comprueba con `post_es_valido`, que se usa
en `redirigir_si_post_invalido`.

Nota técnica: FLAGS `hay_post_anterior` / `hay_post_siguiente`
-------------------------------------------------------------
Como `post_anterior` y `post_siguiente` NUNCA son falsy (siempre
devuelven un `Post`), NO se pueden usar en `rx.cond(post_anterior)`.

Para decidir si mostrar u ocultar las tarjetas de navegación, se usan
los flags `hay_post_anterior` y `hay_post_siguiente` (bool).

Nota técnica: ORIGEN DE LOS HELPERS
-----------------------------------
Los helpers `obtener_post()`, `obtener_post_destacado()` y
`obtener_posts()` viven en
`infraestructura.repositorios.repositorio_blog`. Los tipos (`Post`)
viven en `dominio.modelos.blog` (re-exportados desde el repositorio).

Por eso este archivo importa de DOS rutas distintas:

- **Tipos**:     `from ..modelos.blog import Post`
- **Helpers**:   `from ...infraestructura.repositorios.repositorio_blog import (...)`
"""

from __future__ import annotations

import reflex as rx

from ...infraestructura.repositorios.repositorio_blog import (
    obtener_post,
    obtener_post_destacado,
    obtener_posts,
)
from ..modelos.blog import Post


# ======================================================================
# Constantes del módulo
# ======================================================================

POSTS_POR_PAGINA: int = 6
"""Cantidad de posts visibles en cada página."""


# ======================================================================
# Estado
# ======================================================================


class EstadoBlog(rx.State):
    """Estado de filtros y paginación del blog."""

    # ==================================================================
    # ESTADO PERSISTENTE
    # ==================================================================

    categoria_activa: str = "todas"
    """Categoría activa del filtro (clave de `CATEGORIAS`, o "todas")."""

    texto_busqueda: str = ""
    """Texto de búsqueda por título, extracto o autor."""

    posts_visibles: int = POSTS_POR_PAGINA
    """Cantidad de posts visibles actualmente."""

    # ==================================================================
    # VARS COMPUTADAS: LISTAS FILTRADAS
    # ==================================================================

    @rx.var
    def posts_filtrados(self) -> list[Post]:
        """
        Posts filtrados por categoría y búsqueda (sin el destacado).

        El post destacado se excluye porque se renderiza aparte.
        """
        posts: list[Post] = [
            p for p in obtener_posts() if not p["destacado"]
        ]

        # --- Filtro por categoría ---
        if self.categoria_activa != "todas":
            posts = [
                p for p in posts
                if p["categoria"] == self.categoria_activa
            ]

        # --- Filtro por búsqueda ---
        if self.texto_busqueda:
            busqueda = self.texto_busqueda.lower()
            posts = [
                p for p in posts
                if busqueda in p["titulo"].lower()
                or busqueda in p["extracto"].lower()
                or busqueda in p["autor"].lower()
            ]

        return posts

    @rx.var
    def posts_paginados(self) -> list[Post]:
        """Posts filtrados, limitados por la paginación actual."""
        return self.posts_filtrados[: self.posts_visibles]

    @rx.var
    def post_destacado(self) -> Post:
        """
        Post destacado (el primero con `destacado=True`).

        ✅ Devuelve `Post` (no dict) para que Reflex sepa que
        `post["titulo"]` es `str`.
        """
        return obtener_post_destacado()

    # ==================================================================
    # VARS COMPUTADAS: CONTADORES Y FLAGS
    # ==================================================================

    @rx.var
    def hay_resultados(self) -> bool:
        """Indica si hay posts que coincidan con los filtros."""
        return len(self.posts_filtrados) > 0

    @rx.var
    def contador_resultados(self) -> str:
        """Texto con el número de resultados."""
        return str(len(self.posts_filtrados))

    @rx.var
    def hay_mas_posts(self) -> bool:
        """Indica si hay más posts por cargar."""
        return len(self.posts_filtrados) > self.posts_visibles

    @rx.var
    def hay_filtros_activos(self) -> bool:
        """Indica si hay algún filtro activo."""
        return (
            self.categoria_activa != "todas"
            or self.texto_busqueda != ""
        )

    # ==================================================================
    # VARS COMPUTADAS: POST SELECCIONADO (ruta /blog/[post_id])
    # ==================================================================

    @rx.var
    def post_id_desde_url(self) -> int:
        """
        Extrae el `post_id` de la URL como `int`.

        Devuelve `-1` si no es convertible a int.
        """
        valor_crudo = self.router.page.params.get("post_id", "")
        try:
            return int(valor_crudo)
        except (ValueError, TypeError):
            return -1

    @rx.var
    def post_seleccionado(self) -> Post:
        """
        Post correspondiente al `post_id` de la URL.

        ⚠️ SIEMPRE devuelve un `Post` válido (fallback al destacado).
        """
        post = obtener_post(self.post_id_desde_url)
        return post if post else obtener_post_destacado()

    @rx.var
    def post_es_valido(self) -> bool:
        """Indica si el `post_id` de la URL corresponde a un post real."""
        return obtener_post(self.post_id_desde_url) is not None

    # ==================================================================
    # VARS COMPUTADAS: NAVEGACIÓN ENTRE POSTS
    # ==================================================================

    @rx.var
    def hay_post_anterior(self) -> bool:
        """
        Indica si existe un post anterior al actual.

        ✅ Se usa para decidir si mostrar la tarjeta de navegación
        al post anterior.
        """
        actual = obtener_post(self.post_id_desde_url)
        if actual is None:
            return False
        return obtener_post(actual["id"] - 1) is not None

    @rx.var
    def hay_post_siguiente(self) -> bool:
        """Indica si existe un post siguiente al actual."""
        actual = obtener_post(self.post_id_desde_url)
        if actual is None:
            return False
        return obtener_post(actual["id"] + 1) is not None

    @rx.var
    def post_anterior(self) -> Post:
        """
        Post inmediatamente anterior al actual.

        ⚠️ Si no hay anterior, devuelve el destacado (fallback).

        Para saber si HAY un post anterior real, usar
        `hay_post_anterior`.
        """
        actual = obtener_post(self.post_id_desde_url)
        if actual is None:
            return obtener_post_destacado()
        anterior = obtener_post(actual["id"] - 1)
        return anterior if anterior else obtener_post_destacado()

    @rx.var
    def post_siguiente(self) -> Post:
        """
        Post inmediatamente siguiente al actual.

        ⚠️ Si no hay siguiente, devuelve el destacado (fallback).

        Para saber si HAY un post siguiente real, usar
        `hay_post_siguiente`.
        """
        actual = obtener_post(self.post_id_desde_url)
        if actual is None:
            return obtener_post_destacado()
        siguiente = obtener_post(actual["id"] + 1)
        return siguiente if siguiente else obtener_post_destacado()

    # ==================================================================
    # EVENT HANDLERS: FILTROS Y PAGINACIÓN
    # ==================================================================

    @rx.event
    def seleccionar_categoria(self, categoria: str):
        """Cambia la categoría activa y resetea la paginación."""
        self.categoria_activa = categoria
        self.posts_visibles = POSTS_POR_PAGINA

    @rx.event
    def actualizar_busqueda(self, texto: str):
        """Actualiza el texto de búsqueda y resetea la paginación."""
        self.texto_busqueda = texto
        self.posts_visibles = POSTS_POR_PAGINA

    @rx.event
    def limpiar_filtros(self):
        """Restablece todos los filtros a sus valores por defecto."""
        self.categoria_activa = "todas"
        self.texto_busqueda = ""
        self.posts_visibles = POSTS_POR_PAGINA

    @rx.event
    def cargar_mas_posts(self):
        """Incrementa el número de posts visibles en una página más."""
        self.posts_visibles += POSTS_POR_PAGINA

    # ==================================================================
    # EVENT HANDLERS: VALIDACIÓN DE RUTA
    # ==================================================================

    @rx.event
    def redirigir_si_post_invalido(self):
        """
        Redirige a `/404?origen=blog` si el `post_id` no existe.

        Se dispara desde `on_load` de la vista `/blog/[post_id]`.
        """
        if not self.post_es_valido:
            return rx.redirect("/404?origen=blog")
        return None


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "EstadoBlog",
    "POSTS_POR_PAGINA",
]