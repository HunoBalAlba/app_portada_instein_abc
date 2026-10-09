

from __future__ import annotations

import re
import unicodedata


# ======================================================================
# 1. Formateo de números
# ======================================================================


def formatear_numero(
    valor: int | float,
    separador_miles: str = ".",
    separador_decimal: str = ",",
) -> str:
    """
    Formatea un número con separadores de miles y decimales.

    Args:
        valor: Número a formatear.
        separador_miles: Separador de miles (default: ".").
        separador_decimal: Separador decimal (default: ",").

    Returns:
        String formateado.

    Examples:
        >>> formatear_numero(1234567)
        '1.234.567'
        >>> formatear_numero(1234.56)
        '1.234,56'
        >>> formatear_numero(1234.56, separador_miles=",",
        ...                   separador_decimal=".")
        '1,234.56'
    """
    if isinstance(valor, int):
        return f"{valor:,}".replace(",", separador_miles)

    # Floats: 2 decimales por defecto
    formateado = f"{valor:,.2f}"
    return (
        formateado
        .replace(",", "TEMP")
        .replace(".", separador_decimal)
        .replace("TEMP", separador_miles)
    )


def formatear_porcentaje(
    valor: float,
    decimales: int = 0,
) -> str:
    """
    Formatea un valor como porcentaje.

    Args:
        valor: Valor a formatear (0-100).
        decimales: Cantidad de decimales a mostrar.

    Returns:
        String con el porcentaje.

    Examples:
        >>> formatear_porcentaje(95)
        '95%'
        >>> formatear_porcentaje(94.567, 2)
        '94.57%'
    """
    return f"{valor:.{decimales}f}%"


def formatear_salario(
    monto: int,
    moneda: str = "Bs",
) -> str:
    """
    Formatea un monto de salario con separador de miles.

    Args:
        monto: Monto en la moneda local.
        moneda: Símbolo de la moneda (default: "Bs").

    Returns:
        String formateado (ej: "Bs 4.500").

    Examples:
        >>> formatear_salario(4500)
        'Bs 4.500'
        >>> formatear_salario(5000, "USD")
        'USD 5.000'
    """
    return f"{moneda} {formatear_numero(monto)}"


# ======================================================================
# 2. Formateo de texto
# ======================================================================


def truncar_texto(
    texto: str,
    longitud_maxima: int,
    sufijo: str = "...",
) -> str:
    """
    Trunca un texto si excede la longitud máxima.

    Args:
        texto: Texto a truncar.
        longitud_maxima: Longitud máxima antes de truncar.
        sufijo: Sufijo a añadir al truncar (default: "...").

    Returns:
        Texto truncado (o el original si no excede).

    Examples:
        >>> truncar_texto("Hola mundo", 20)
        'Hola mundo'
        >>> truncar_texto("Hola mundo", 6)
        'Hola m...'
        >>> truncar_texto("Hola mundo", 6, sufijo="…")
        'Hola m…'
    """
    if len(texto) <= longitud_maxima:
        return texto
    return texto[:longitud_maxima].rstrip() + sufijo


def pluralizar(
    cantidad: int,
    singular: str,
    plural: str | None = None,
) -> str:
    """
    Devuelve la forma singular o plural según la cantidad.

    Args:
        cantidad: Cantidad a evaluar.
        singular: Forma singular (ej: "carrera").
        plural: Forma plural. Si es `None`, añade "s" al singular.

    Returns:
        String con la forma correcta.

    Examples:
        >>> pluralizar(1, "carrera")
        '1 carrera'
        >>> pluralizar(5, "carrera")
        '5 carreras'
        >>> pluralizar(2, "lápiz", "lápices")
        '2 lápices'
    """
    if plural is None:
        plural = f"{singular}s"

    return f"{cantidad} {singular if cantidad == 1 else plural}"


def iniciales(nombre_completo: str, maximo: int = 2) -> str:
    """
    Extrae las iniciales de un nombre.

    Args:
        nombre_completo: Nombre completo (ej: "Juan Pérez López").
        maximo: Número máximo de iniciales a extraer.

    Returns:
        String con las iniciales (ej: "JP").

    Examples:
        >>> iniciales("Juan Pérez")
        'JP'
        >>> iniciales("Ana María González Ruiz")
        'AM'
        >>> iniciales("Ana María González Ruiz", maximo=3)
        'AMG'
    """
    palabras = nombre_completo.split()
    return "".join(p[0].upper() for p in palabras[:maximo] if p)


def slugify(texto: str) -> str:
    """
    Convierte un texto a slug (URL-friendly).

    Elimina acentos, reemplaza espacios por guiones y convierte a
    minúsculas.

    Args:
        texto: Texto a convertir.

    Returns:
        Slug en minúsculas con guiones.

    Examples:
        >>> slugify("Sistemas Informáticos")
        'sistemas-informaticos'
        >>> slugify("Carrera N°1: 2026")
        'carrera-n1-2026'
    """
    # Normalizar caracteres Unicode (eliminar acentos)
    normalizado = unicodedata.normalize("NFKD", texto)
    sin_acentos = normalizado.encode("ascii", "ignore").decode("ascii")

    # Minúsculas, reemplazar no-alfanuméricos por guiones
    slug = re.sub(r"[^a-z0-9]+", "-", sin_acentos.lower())

    # Eliminar guiones al inicio/final
    return slug.strip("-")


# ======================================================================
# 3. Helpers varios
# ======================================================================


def capitalizar_primera(texto: str) -> str:
    """
    Capitaliza solo la primera letra del texto.

    Args:
        texto: Texto a capitalizar.

    Returns:
        Texto con la primera letra en mayúscula y el resto igual.

    Examples:
        >>> capitalizar_primera("hola mundo")
        'Hola mundo'
        >>> capitalizar_primera("HOLA MUNDO")
        'HOLA MUNDO'
    """
    if not texto:
        return texto
    return texto[0].upper() + texto[1:]


def titulo_case(texto: str) -> str:
    """
    Convierte un texto a Title Case (cada palabra capitalizada).

    Args:
        texto: Texto a convertir.

    Returns:
        Texto en Title Case.

    Examples:
        >>> titulo_case("sistemas informáticos")
        'Sistemas Informáticos'
    """
    return " ".join(
        palabra.capitalize() for palabra in texto.split()
    )


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
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