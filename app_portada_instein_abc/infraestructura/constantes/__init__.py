

from __future__ import annotations


# ======================================================================
# 1. Identidad institucional
# ======================================================================

from .identidad import (
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
)

# ======================================================================
# 2. Redes sociales
# ======================================================================

from .redes import (
    REDES_SOCIALES,
    URL_DISCORD,
    URL_FACEBOOK,
    URL_INSTAGRAM,
    URL_TELEGRAM,
    URL_TIKTOK,
    URL_WHATSAPP_CANAL,
    URL_YOUTUBE,
    URLS_REDES,
    RedSocial,
)

# ======================================================================
# 3. Colores
# ======================================================================

from .colores import (
    ACCENT_COLOR_TEMA,
    AZUL_MARINO_CLARO,
    AZUL_MARINO_HEX,
    AZUL_MARINO_NEON,
    AZUL_MARINO_PROFUNDO,
    BORDE_HOME_AZUL,
    BORDE_HOME_MEDIO,
    BORDE_HOME_SUAVE,
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
    FONDO_AZUL_MUY_SUAVE,
    FONDO_AZUL_SUAVE,
    FONDO_BARRA_HOME,
    FONDO_HOME,
    FONDO_HOME_CARD,
    FONDO_HOME_CARD_ADAPTATIVO,   # ← alias retrocompatible
    FONDO_HOME_HERO,
    GRADIENTE_HOME_BANNER,
    GRADIENTE_TEXTO_HOME,
    SOMBRA_HOVER_CARD_HOME,
    TEXTO_HOME_MAS_SUAVE,
    TEXTO_HOME_PRINCIPAL,
    TEXTO_HOME_SUAVE,
    color_categoria,
)

# ======================================================================
# 4. Dimensiones
# ======================================================================

from .dimensiones import (
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
)

# ======================================================================
# 5. Tipografía
# ======================================================================

from .tipografia import (
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
)


# ======================================================================
# API pública del paquete
# ======================================================================

__all__ = [
    # ==================================================================
    # 1. Identidad
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
    # 2. Redes sociales
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
    # 3. Colores
    # ==================================================================
    # Acento de marca
    "ACCENT_COLOR_TEMA",
    "AZUL_MARINO_CLARO",
    "AZUL_MARINO_HEX",
    "AZUL_MARINO_NEON",
    "AZUL_MARINO_PROFUNDO",
    # Tokens semánticos
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
    # Tokens adaptativos (home)
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
    # Helper
    "color_categoria",
    # ==================================================================
    # 4. Dimensiones
    # ==================================================================
    # Anchos
    "ANCHO_CONTENIDO",
    "ANCHO_CONTENIDO_MENU",
    "ANCHO_CONTENIDO_VW",
    "ANCHO_LECTURA",
    "ANCHO_MAXIMO",
    "ANCHO_MENU_LATERAL",
    "ANCHO_SECCION",
    # Espaciados
    "GAP_GRANDE",
    "GAP_MEDIO",
    "GAP_PEQUENO",
    "PADDING_LATERAL",
    "PADDING_LATERAL_MOVIL",
    "PADDING_SECCION",
    "PADDING_TARJETA",
    # Radios
    "RADIO_BORDE",
    "RADIO_EXTRA_GRANDE",
    "RADIO_GRANDE",
    "RADIO_MEDIO",
    "RADIO_PASTILLA",
    "RADIO_PEQUENO",
    # Sombras
    "SOMBRA_CAJA",
    "SOMBRA_FUERTE",
    "SOMBRA_GLOW_AZUL",
    "SOMBRA_MEDIA",
    "SOMBRA_SUAVE",
    # Tamaños
    "TAMANO_BOTON_FLOTANTE",
    "TAMANO_ICONO_ESTADO_VACIO",
    "TAMANO_LOGO",
    "TAMANOS_CAJA_COLOR",
    # Referencia
    "BREAKPOINTS_RADIX",
    # ==================================================================
    # 5. Tipografía
    # ==================================================================
    # Fuentes
    "FALLBACK_MONO",
    "FALLBACK_MONOESPACIADO",
    "FALLBACK_PRINCIPAL",
    "FALLBACK_SANS",
    "FUENTE_MONOESPACIADA",
    "FUENTE_PRINCIPAL",
    # Hojas de estilo y estilo base
    "ESTILO_BASE",
    "HOJAS_DE_ESTILO_BASE",
    # Pesos
    "PESO_BLACK",
    "PESO_BOLD",
    "PESO_EXTRABOLD",
    "PESO_MEDIO",
    "PESO_REGULAR",
    "PESO_SEMIBOLD",
    # Tamaños de texto
    "TAMANO_TEXTO_BASE",
    "TAMANO_TEXTO_LG",
    "TAMANO_TEXTO_SM",
    "TAMANO_TEXTO_XL",
    "TAMANO_TEXTO_XS",
    # Tamaños de heading
    "TAMANO_HEADING_1",
    "TAMANO_HEADING_2",
    "TAMANO_HEADING_3",
    "TAMANO_HEADING_4",
    "TAMANO_HEADING_5",
    "TAMANO_HEADING_6",
    # Line-heights
    "LINE_HEIGHT_LOOSE",
    "LINE_HEIGHT_NORMAL",
    "LINE_HEIGHT_RELAXED",
    "LINE_HEIGHT_SNUG",
    "LINE_HEIGHT_TIGHT",
]