"""
Paquete `infraestructura.repositorios`: acceso a datos.

Este paquete encapsula el acceso a las fuentes de datos del proyecto
(catálogo de carreras, posts del blog, eventos del calendario, etc.).

Patrón Repository
-----------------
Cada repositorio expone una API estable (funciones públicas) sobre
una fuente de datos concreta. Los consumidores (dominio, componentes)
NO acceden directamente a la fuente de datos: pasan por el repositorio.

Ventajas:
- **Abstracción**: cambiar de estático a API/BD no afecta al dominio.
- **Testabilidad**: se puede mockear el repositorio.
- **Caché**: el repositorio puede cachear lecturas costosas.

Contenido
---------
- **repositorio_carreras**:  catálogo de las 5 carreras técnicas.
- **repositorio_blog**:      posts y categorías del blog.

Convención de imports
---------------------
✅ **CORRECTO** — importar desde el paquete:
    from app_portada_instein.infraestructura.repositorios import (
        obtener_catalogo,
        obtener_post,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el módulo específico:
    from app_portada_instein.infraestructura.repositorios.repositorio_carreras import (
        obtener_catalogo,
    )

Qué exponer y qué no
--------------------
Se exponen:
- Modelos (`Carrera`, `Post`, `Categoria`, etc.): son tipos públicos.
- Funciones de acceso (`obtener_catalogo()`, `obtener_post()`, etc.).
- Constantes públicas (`CATEGORIAS`, `PALETA_COLORES`, etc.).

NO se exponen:
- Datos crudos privados (`_CATALOGO_CARRERAS`, `_POSTS`).
- Helpers internos (`_icono_orbital_config`).
"""

from __future__ import annotations


# ======================================================================
# Repositorio de carreras
# ======================================================================

from .repositorio_carreras import (
    # Constantes
    HORARIOS_TURNO,
    PALETA_COLORES,
    PERSPECTIVA_DEFECTO,
    TURNOS_VALIDOS,
    # API pública
    carrera_existe,
    obtener_carrera_destacada,
    obtener_carrera_por_id,
    obtener_catalogo,
    obtener_ids_carreras,
    # Tipos
    CaracteristicaCarrera,
    Carrera,
    CarreraConEtiqueta,
    ColorHex,
    DemandaLaboral,
    EstadisticasCarrera,
    IconoAnimado,
    Modalidad,
    PlanAnual,
    PreguntaFrecuente,
    Turno,
)

# ======================================================================
# Repositorio del blog
# ======================================================================

from .repositorio_blog import (
    # Datos
    CATEGORIAS,
    # API pública
    obtener_post,
    obtener_post_destacado,
    obtener_posts,
    obtener_posts_por_categoria,
    # Tipos
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # Repositorio de carreras: constantes
    # ==================================================================
    "HORARIOS_TURNO",
    "PALETA_COLORES",
    "PERSPECTIVA_DEFECTO",
    "TURNOS_VALIDOS",
    # ==================================================================
    # Repositorio de carreras: API pública
    # ==================================================================
    "carrera_existe",
    "obtener_carrera_destacada",
    "obtener_carrera_por_id",
    "obtener_catalogo",
    "obtener_ids_carreras",
    # ==================================================================
    # Repositorio de carreras: tipos
    # ==================================================================
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
    # ==================================================================
    # Repositorio del blog: datos
    # ==================================================================
    "CATEGORIAS",
    # ==================================================================
    # Repositorio del blog: API pública
    # ==================================================================
    "obtener_post",
    "obtener_post_destacado",
    "obtener_posts",
    "obtener_posts_por_categoria",
    # ==================================================================
    # Repositorio del blog: tipos
    # ==================================================================
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
]