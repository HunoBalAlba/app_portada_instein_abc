"""
Capa de infraestructura: constantes, repositorios y utilidades.

Esta capa agrupa todo lo técnico-transversal que NO depende de la
lógica de negocio ni de la UI:

1. **constantes**:   valores inmutables (identidad, colores, dimensiones,
   tipografía, redes sociales).
2. **repositorios**: acceso a fuentes de datos (catálogo de carreras,
   posts del blog).
3. **utilidades**:   helpers puros (manipulación de colores, formateo
   de texto/números).

Filosofía
---------
- **Sin lógica de negocio**: eso vive en `dominio/`.
- **Sin UI**: eso vive en `componentes/` y `paginas/`.
- **Sin acoplamiento a Reflex** (excepto `colores.py` que usa
  `rx.color` para tokens semánticos).

Convención de imports
---------------------
✅ **CORRECTO** — importar desde la capa raíz:
    from app_portada_instein.infraestructura import (
        # Constantes
        NOMBRE_INSTITUTO,
        AZUL_MARINO_NEON,
        RADIO_MEDIO,
        FUENTE_PRINCIPAL,
        # Repositorios
        obtener_catalogo,
        obtener_post,
        # Utilidades
        invertir_color_hexadecimal,
        formatear_numero,
    )

✅ **TAMBIÉN VÁLIDO** — importar desde el subpaquete:
    from app_portada_instein.infraestructura.constantes import (
        NOMBRE_INSTITUTO,
    )

❌ **EVITAR** — importar desde el módulo interno:
    from app_portada_instein.infraestructura.constantes.identidad import (
        NOMBRE_INSTITUTO,
    )

Motivo: la ruta interna puede cambiar sin romper consumidores,
siempre que la API pública se mantenga estable.

Recomendación de granularidad
-----------------------------
- **1-5 símbolos de distintos subpaquetes** → importar de `infraestructura`.
- **6+ símbolos del mismo subpaquete** → importar del subpaquete
  específico (`infraestructura.constantes`, etc.).

Esto evita imports innecesariamente largos sin perder claridad.

Qué NO exponer aquí
-------------------
- Estados de Reflex (`rx.State`): viven en `dominio.estados`.
- Modelos de dominio: viven en `dominio.modelos`.
- Componentes: viven en `componentes`.
- Vistas: viven en `paginas`.

Capa `infraestructura` vs capa `dominio`
----------------------------------------
- **infraestructura**: cómo acceder a datos y qué constantes usar.
- **dominio**:        qué hacer con esos datos (reglas de negocio).
"""

from __future__ import annotations


# ======================================================================
# Constantes (re-exportadas desde `constantes/`)
# ======================================================================

from .constantes import (
    # --- Identidad ---
    ANIO_COPYRIGHT,
    DESCRIPCION_INSTITUCIONAL,
    DIRECCION,
    DIRECCION_COMPLETA,
    DURACION_CARRERA_ANIOS,
    DURACION_CARRERA_SEMESTRES,
    EMAIL_CONTACTO,
    ENTIDAD_COPYRIGHT,
    GITHUB_URL,
    HORARIO_ATENCION,
    NOMBRE_COMPLETO,
    NOMBRE_INSTITUTO,
    RESOLUCION_MINISTERIAL,
    SIGLAS,
    TELEFONO_PRINCIPAL,
    TELEFONO_SECUNDARIO,
    TITULO_OTORGADO,
    UBICACION_FISICA,
    WHATSAPP_URL,
    # --- Redes sociales ---
    REDES_SOCIALES,
    RedSocial,
    URLS_REDES,
    URL_DISCORD,
    URL_FACEBOOK,
    URL_INSTAGRAM,
    URL_TELEGRAM,
    URL_TIKTOK,
    URL_WHATSAPP_CANAL,
    URL_YOUTUBE,
    # --- Colores: acento de marca ---
    ACCENT_COLOR_TEMA,
    AZUL_MARINO_CLARO,
    AZUL_MARINO_HEX,
    AZUL_MARINO_NEON,
    AZUL_MARINO_PROFUNDO,
    # --- Colores: semánticos ---
    BORDE_PREDETERMINADO,
    COLOR_ACENTO_BORDE,
    COLOR_ACENTO_FONDO,
    COLOR_ACENTO_SOLIDO,
    COLOR_ACENTO_TEXTO,
    COLOR_ACENTO_TEXTO_SOLIDO,
    COLOR_ALERTA_FONDO,
    COLOR_ALERTA_TEXTO,
    COLOR_BORDE_ACTIVO,
    COLOR_BORDE_HOVER,
    COLOR_BORDE_SUAVE,
    COLOR_DIVISOR,
    COLOR_ERROR_FONDO,
    COLOR_ERROR_TEXTO,
    COLOR_EXITO_FONDO,
    COLOR_EXITO_SOLIDO,
    COLOR_EXITO_TEXTO,
    COLOR_FONDO_CARTA,
    COLOR_FONDO_GRIS,
    COLOR_FONDO_SUAVE,
    COLOR_TEXTO_APAGADO,
    COLOR_TEXTO_CUERPO,
    COLOR_TEXTO_PRINCIPAL,
    COLOR_TEXTO_SECUNDARIO,
    # --- Colores: adaptativos home ---
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_BARRA_HOME,
    FONDO_HOME,
    FONDO_HOME_CARD,
    FONDO_HOME_CARD_ADAPTATIVO,
    FONDO_HOME_HERO,
    GRADIENTE_HOME_BANNER,
    GRADIENTE_TEXTO_HOME,
    SOMBRA_HOVER_CARD_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
    # --- Dimensiones ---
    ANCHO_CONTENIDO,
    ANCHO_CONTENIDO_MENU,
    ANCHO_CONTENIDO_VW,
    ANCHO_LECTURA,
    ANCHO_MAXIMO,
    ANCHO_MENU_LATERAL,
    ANCHO_SECCION,
    BREAKPOINTS_RADIX,
    GAP_GRANDE,
    GAP_MEDIO,
    GAP_PEQUENO,
    PADDING_LATERAL,
    PADDING_LATERAL_MOVIL,
    PADDING_SECCION,
    PADDING_TARJETA,
    RADIO_BORDE,
    RADIO_EXTRA_GRANDE,
    RADIO_GRANDE,
    RADIO_MEDIO,
    RADIO_PASTILLA,
    RADIO_PEQUENO,
    SOMBRA_CAJA,
    SOMBRA_FUERTE,
    SOMBRA_GLOW_AZUL,
    SOMBRA_MEDIA,
    SOMBRA_SUAVE,
    TAMANO_BOTON_FLOTANTE,
    TAMANO_ICONO_ESTADO_VACIO,
    TAMANO_LOGO,
    TAMANOS_CAJA_COLOR,
    # --- Tipografía ---
    ESTILO_BASE,
    FALLBACK_MONO,
    FALLBACK_MONOESPACIADO,
    FALLBACK_PRINCIPAL,
    FALLBACK_SANS,
    FUENTE_MONOESPACIADA,
    FUENTE_PRINCIPAL,
    HOJAS_DE_ESTILO_BASE,
    LINE_HEIGHT_LOOSE,
    LINE_HEIGHT_NORMAL,
    LINE_HEIGHT_RELAXED,
    LINE_HEIGHT_SNUG,
    LINE_HEIGHT_TIGHT,
    PESO_BLACK,
    PESO_BOLD,
    PESO_EXTRABOLD,
    PESO_MEDIO,
    PESO_REGULAR,
    PESO_SEMIBOLD,
    TAMANO_HEADING_1,
    TAMANO_HEADING_2,
    TAMANO_HEADING_3,
    TAMANO_HEADING_4,
    TAMANO_HEADING_5,
    TAMANO_HEADING_6,
    TAMANO_TEXTO_BASE,
    TAMANO_TEXTO_LG,
    TAMANO_TEXTO_SM,
    TAMANO_TEXTO_XL,
    TAMANO_TEXTO_XS,
    # --- Helpers de constantes ---
    color_categoria,
)

# ======================================================================
# Repositorios (re-exportados desde `repositorios/`)
# ======================================================================

from .repositorios import (
    # --- Datos estáticos ---
    CATEGORIAS,
    HORARIOS_TURNO,
    PALETA_COLORES,
    PERSPECTIVA_DEFECTO,
    TURNOS_VALIDOS,
    # --- API: carreras ---
    carrera_existe,
    obtener_carrera_destacada,
    obtener_carrera_por_id,
    obtener_catalogo,
    obtener_ids_carreras,
    # --- API: blog ---
    obtener_post,
    obtener_post_destacado,
    obtener_posts,
    obtener_posts_por_categoria,
    # --- Tipos: carreras ---
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
    # --- Tipos: blog ---
    Categoria,
    CategoriaId,
    ColorScheme,
    Post,
)

# ======================================================================
# Utilidades (re-exportadas desde `utilidades/`)
# ======================================================================

from .utilidades import (
    # --- Color ---
    PATRON_HEX,
    aclarar_color,
    calcular_contraste,
    cumple_contraste_wcag_aa,
    es_hex_valido,
    hex_a_rgb,
    hex_a_rgba,
    invertir_color_hexadecimal,
    mezclar_colores,
    oscurecer_color,
    rgb_a_hex,
    # --- Formato ---
    capitalizar_primera,
    formatear_numero,
    formatear_porcentaje,
    formatear_salario,
    iniciales,
    pluralizar,
    slugify,
    titulo_case,
    truncar_texto,
)


# ======================================================================
# API pública de la capa
# ======================================================================

__all__ = [
    # ==================================================================
    # Constantes: identidad
    # ==================================================================
    "ANIO_COPYRIGHT",
    "DESCRIPCION_INSTITUCIONAL",
    "DIRECCION",
    "DIRECCION_COMPLETA",
    "DURACION_CARRERA_ANIOS",
    "DURACION_CARRERA_SEMESTRES",
    "EMAIL_CONTACTO",
    "ENTIDAD_COPYRIGHT",
    "GITHUB_URL",
    "HORARIO_ATENCION",
    "NOMBRE_COMPLETO",
    "NOMBRE_INSTITUTO",
    "RESOLUCION_MINISTERIAL",
    "SIGLAS",
    "TELEFONO_PRINCIPAL",
    "TELEFONO_SECUNDARIO",
    "TITULO_OTORGADO",
    "UBICACION_FISICA",
    "WHATSAPP_URL",
    # ==================================================================
    # Constantes: redes sociales
    # ==================================================================
    "REDES_SOCIALES",
    "RedSocial",
    "URLS_REDES",
    "URL_DISCORD",
    "URL_FACEBOOK",
    "URL_INSTAGRAM",
    "URL_TELEGRAM",
    "URL_TIKTOK",
    "URL_WHATSAPP_CANAL",
    "URL_YOUTUBE",
    # ==================================================================
    # Constantes: colores (acento de marca)
    # ==================================================================
    "ACCENT_COLOR_TEMA",
    "AZUL_MARINO_CLARO",
    "AZUL_MARINO_HEX",
    "AZUL_MARINO_NEON",
    "AZUL_MARINO_PROFUNDO",
    # ==================================================================
    # Constantes: colores (semánticos)
    # ==================================================================
    "BORDE_PREDETERMINADO",
    "COLOR_ACENTO_BORDE",
    "COLOR_ACENTO_FONDO",
    "COLOR_ACENTO_SOLIDO",
    "COLOR_ACENTO_TEXTO",
    "COLOR_ACENTO_TEXTO_SOLIDO",
    "COLOR_ALERTA_FONDO",
    "COLOR_ALERTA_TEXTO",
    "COLOR_BORDE_ACTIVO",
    "COLOR_BORDE_HOVER",
    "COLOR_BORDE_SUAVE",
    "COLOR_DIVISOR",
    "COLOR_ERROR_FONDO",
    "COLOR_ERROR_TEXTO",
    "COLOR_EXITO_FONDO",
    "COLOR_EXITO_SOLIDO",
    "COLOR_EXITO_TEXTO",
    "COLOR_FONDO_CARTA",
    "COLOR_FONDO_GRIS",
    "COLOR_FONDO_SUAVE",
    "COLOR_TEXTO_APAGADO",
    "COLOR_TEXTO_CUERPO",
    "COLOR_TEXTO_PRINCIPAL",
    "COLOR_TEXTO_SECUNDARIO",
    # ==================================================================
    # Constantes: colores (adaptativos home)
    # ==================================================================
    "BORDE_HOME_AZUL",
    "BORDE_HOME_MEDIO",
    "BORDE_HOME_SUAVE",
    "FONDO_AZUL_MUY_SUAVE",
    "FONDO_AZUL_SUAVE",
    "FONDO_BARRA_HOME",
    "FONDO_HOME",
    "FONDO_HOME_CARD",
    "FONDO_HOME_CARD_ADAPTATIVO",
    "FONDO_HOME_HERO",
    "GRADIENTE_HOME_BANNER",
    "GRADIENTE_TEXTO_HOME",
    "SOMBRA_HOVER_CARD_HOME",
    "TEXTO_HOME_MAS_SUAVE",
    "TEXTO_HOME_PRINCIPAL",
    "TEXTO_HOME_SUAVE",
    # ==================================================================
    # Constantes: dimensiones
    # ==================================================================
    "ANCHO_CONTENIDO",
    "ANCHO_CONTENIDO_MENU",
    "ANCHO_CONTENIDO_VW",
    "ANCHO_LECTURA",
    "ANCHO_MAXIMO",
    "ANCHO_MENU_LATERAL",
    "ANCHO_SECCION",
    "BREAKPOINTS_RADIX",
    "GAP_GRANDE",
    "GAP_MEDIO",
    "GAP_PEQUENO",
    "PADDING_LATERAL",
    "PADDING_LATERAL_MOVIL",
    "PADDING_SECCION",
    "PADDING_TARJETA",
    "RADIO_BORDE",
    "RADIO_EXTRA_GRANDE",
    "RADIO_GRANDE",
    "RADIO_MEDIO",
    "RADIO_PASTILLA",
    "RADIO_PEQUENO",
    "SOMBRA_CAJA",
    "SOMBRA_FUERTE",
    "SOMBRA_GLOW_AZUL",
    "SOMBRA_MEDIA",
    "SOMBRA_SUAVE",
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_LOGO",
    "TAMANOS_CAJA_COLOR",
    # ==================================================================
    # Constantes: tipografía
    # ==================================================================
    "ESTILO_BASE",
    "FALLBACK_MONO",
    "FALLBACK_MONOESPACIADO",
    "FALLBACK_PRINCIPAL",
    "FALLBACK_SANS",
    "FUENTE_MONOESPACIADA",
    "FUENTE_PRINCIPAL",
    "HOJAS_DE_ESTILO_BASE",
    "LINE_HEIGHT_LOOSE",
    "LINE_HEIGHT_NORMAL",
    "LINE_HEIGHT_RELAXED",
    "LINE_HEIGHT_SNUG",
    "LINE_HEIGHT_TIGHT",
    "PESO_BLACK",
    "PESO_BOLD",
    "PESO_EXTRABOLD",
    "PESO_MEDIO",
    "PESO_REGULAR",
    "PESO_SEMIBOLD",
    "TAMANO_HEADING_1",
    "TAMANO_HEADING_2",
    "TAMANO_HEADING_3",
    "TAMANO_HEADING_4",
    "TAMANO_HEADING_5",
    "TAMANO_HEADING_6",
    "TAMANO_TEXTO_BASE",
    "TAMANO_TEXTO_LG",
    "TAMANO_TEXTO_SM",
    "TAMANO_TEXTO_XL",
    "TAMANO_TEXTO_XS",
    # ==================================================================
    # Constantes: helpers
    # ==================================================================
    "color_categoria",
    # ==================================================================
    # Repositorios: datos estáticos
    # ==================================================================
    "CATEGORIAS",
    "HORARIOS_TURNO",
    "PALETA_COLORES",
    "PERSPECTIVA_DEFECTO",
    "TURNOS_VALIDOS",
    # ==================================================================
    # Repositorios: API pública (carreras)
    # ==================================================================
    "carrera_existe",
    "obtener_carrera_destacada",
    "obtener_carrera_por_id",
    "obtener_catalogo",
    "obtener_ids_carreras",
    # ==================================================================
    # Repositorios: API pública (blog)
    # ==================================================================
    "obtener_post",
    "obtener_post_destacado",
    "obtener_posts",
    "obtener_posts_por_categoria",
    # ==================================================================
    # Repositorios: tipos (carreras)
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
    # Repositorios: tipos (blog)
    # ==================================================================
    "Categoria",
    "CategoriaId",
    "ColorScheme",
    "Post",
    # ==================================================================
    # Utilidades: color
    # ==================================================================
    "PATRON_HEX",
    "aclarar_color",
    "calcular_contraste",
    "cumple_contraste_wcag_aa",
    "es_hex_valido",
    "hex_a_rgb",
    "hex_a_rgba",
    "invertir_color_hexadecimal",
    "mezclar_colores",
    "oscurecer_color",
    "rgb_a_hex",
    # ==================================================================
    # Utilidades: formato
    # ==================================================================
    "capitalizar_primera",
    "formatear_numero",
    "formatear_porcentaje",
    "formatear_salario",
    "iniciales",
    "pluralizar",
    "slugify",
    "titulo_case",
    "truncar_texto",
]