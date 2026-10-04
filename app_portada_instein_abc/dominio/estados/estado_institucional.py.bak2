"""
Estado global de la aplicación pública del instituto.

Centraliza:
- El catálogo de carreras (desde el repositorio).
- La carrera destacada en el home.
- El estado del explorador (sección activa + búsqueda + año).
- La visibilidad del panel flotante.
- Los filtros y ordenamiento de la lista de carreras.
- El carrusel de carreras destacadas.

Nota técnica: PATH PARAMS Y RUTA
--------------------------------
- Los PATH PARAMS se obtienen con `self.router.page.params` (dict).
- La RUTA ACTUAL se obtiene con `self.router.url.path` (str).
- `carrera_id` viene como string; se convierte a int con try/except.
- Si no es convertible, se devuelve `-1` para detectar IDs inválidos.

Nota técnica: TIPADO DE VARS REACTIVAS CON `rx.foreach`
-------------------------------------------------------
Reflex necesita tipos precisos en las `@rx.var` que sirven como
fuente de `rx.foreach`. Si devuelven `dict` genérico, los campos
internos se infieren como `Any` y `rx.foreach` falla con:

    ForeachVarError: Could not foreach over var of type Any

Por eso:
- `carrera_seleccionada` SIEMPRE devuelve un `Carrera` válido
  (fallback a `carreras[0]` si el id es inválido).
- La validez real del id se comprueba con `carrera_es_valida` (bool).
- El `on_load` de la vista usa `carrera_es_valida` para redirigir.

Nota técnica: CARRUSEL AUTOMÁTICO (FIX FUGA DE MEMORIA)
------------------------------------------------------
El auto-avance del carrusel **NO se implementa con una tarea en
background de Python** (`while True` + `@rx.event(background=True)`)
porque eso causaba una fuga de memoria:

- La tarea nunca se detenía al salir de `/carreras`.
- Cada navegación a `/carreras` añadía una tarea infinita nueva.

**Solución**: el auto-avance vive en el **cliente** mediante
`rx.moment(interval=5000)`, que dispara `siguiente_carrusel` cada 5
segundos. El navegador cancela el intervalo automáticamente al
desmontar el componente.

Este State solo expone los eventos `siguiente_carrusel`,
`anterior_carrusel` e `ir_a_banner`, disparados desde el componente
`hero_carreras`.

Nota técnica: `@rx.var` SIN ARGUMENTOS
--------------------------------------
En Reflex 0.9.x, un `@rx.var` NO puede recibir argumentos (más allá
de `self`). Los helpers que necesitan argumentos son métodos
normales de Python, NO decorados.

Nota técnica: `@rx.var(cache=True)`
-----------------------------------
Las `@rx.var` que dependen de otras vars y solo cambian cuando el
catálogo cambia pueden cachearse con `@rx.var(cache=True)`. Esto
evita recalcular la var en cada render del componente que la consume.
"""

from __future__ import annotations

import random
from typing import TypedDict

import reflex as rx

from ...dominio.modelos.carrera import (
    Carrera,
    CarreraConEtiqueta,
    PlanAnual,
    PreguntaFrecuente,
)
from ...infraestructura import (
    AZUL_MARINO_NEON,
    PALETA_COLORES,
    obtener_catalogo,
)


# ======================================================================
# Tipos locales
# ======================================================================


class OpcionAnio(TypedDict):
    """Opción de año para el `rx.segmented_control` del plan."""

    etiqueta: str
    valor: str


# ======================================================================
# Constantes del módulo
# ======================================================================

CANTIDAD_ICONOS_FONDO: int = 30
SEMILLA_ICONOS_FONDO: int = 42
TAMANOS_ICONOS_FONDO: list[int] = [16, 20, 24, 28, 32, 40]

ETIQUETAS_CARRUSEL: list[str] = [
    "Inscripciones abiertas",
    "Cupos limitados",
    "Últimos lugares",
    "Alta demanda",
    "Nuevo plan 2026",
]

SEGUNDOS_ENTRE_BANNERS: int = 5
"""Segundos entre cada avance del carrusel (usado por `rx.moment`)."""

SECCIONES_EXPLORADOR_VALIDAS: frozenset[str] = frozenset(
    {"info", "plan", "perfil", "campo", "faq"}
)

SECCIONES_DETALLE_VALIDAS: frozenset[str] = frozenset(
    {"info", "plan", "perfil"}
)

FILTROS_VALIDOS: frozenset[str] = frozenset({
    "demanda_alta",
    "puntuacion_top",
    "mas_inscritos",
    "mas_graduados",
})

ORDENES_VALIDAS: frozenset[str] = frozenset({
    "puntuacion_desc",
    "inscritos_desc",
    "graduados_desc",
    "empleabilidad_desc",
    "salario_desc",
})


# ======================================================================
# Estado
# ======================================================================


class EstadoInstitucional(rx.State):
    """Estado central de la aplicación pública."""

    # ==================================================================
    # ESTADO PERSISTENTE
    # ==================================================================

    # --- Catálogo ---
    carreras: list[Carrera] = obtener_catalogo()

    # --- Home: carrera destacada y explorador ---
    id_carrera_destacada: int = 0
    seccion_explorador_activa: str = "info"
    indice_anio_explorador: int = 0
    texto_busqueda_carrera: str = ""
    mostrar_panel_flotante: bool = False

    # --- Detalle: sección y año ---
    indice_anio_seleccionado: int = 0
    seccion_detalle_activa: str = "info"

    # --- Filtros y ordenamiento de la lista ---
    filtro_activo: str = "demanda_alta"
    orden_activo: str = "puntuacion_desc"

    # --- Carrusel ---
    indice_carrusel: int = 0

    # ==================================================================
    # HELPERS INTERNOS (métodos normales, NO decorados con @rx.var)
    # ==================================================================

    def _carrera_por_id(self, id_carrera: int) -> Carrera:
        """
        Busca una carrera por ID con fallback seguro.

        ⚠️ NO está decorado con `@rx.var` porque tiene argumentos.

        Args:
            id_carrera: ID a buscar (puede ser -1 si es inválido).

        Returns:
            La carrera encontrada, o `carreras[0]` si no existe.
        """
        if id_carrera < 0:
            return self.carreras[0]
        for carrera in self.carreras:
            if carrera["id"] == id_carrera:
                return carrera
        return self.carreras[0]

    def _carrera_existe(self, id_carrera: int) -> bool:
        """
        Devuelve `True` si el ID corresponde a una carrera.

        ⚠️ Este método SÍ detecta inválidos (no tiene fallback).
        """
        if id_carrera < 0:
            return False
        return any(c["id"] == id_carrera for c in self.carreras)

    @staticmethod
    def _plan_anual_seguro(
        plan_estudios: list[PlanAnual],
        indice: int,
    ) -> PlanAnual:
        """
        Devuelve el plan anual con fallback seguro.

        Args:
            plan_estudios: Lista de planes anuales.
            indice: Índice solicitado.

        Returns:
            El plan del índice, o el primero si el índice es inválido.
        """
        if not plan_estudios:
            return {"anio": "Sin plan", "materias": []}
        if indice < 0 or indice >= len(plan_estudios):
            return plan_estudios[0]
        return plan_estudios[indice]

    @classmethod
    def _materias_del_plan(
        cls,
        plan_estudios: list[PlanAnual],
        indice: int,
    ) -> list[str]:
        """Devuelve las materias del plan anual indicado."""
        plan = cls._plan_anual_seguro(plan_estudios, indice)
        return plan["materias"]

    # ==================================================================
    # VARIABLES COMPUTADAS: URL
    # ==================================================================

    @rx.var
    def id_carrera_desde_url(self) -> int:
        """
        ID de la carrera desde la URL.

        Returns:
            El ID como `int`, o `-1` si no es convertible.
        """
        valor_crudo = self.router.page.params.get("carrera_id", "")
        try:
            return int(valor_crudo)
        except (ValueError, TypeError):
            return -1

    @rx.var
    def ruta_activa_normalizada(self) -> str:
        """Ruta actual normalizada (sin barra final)."""
        ruta = self.router.url.path or "/"
        if len(ruta) > 1 and ruta.endswith("/"):
            ruta = ruta.rstrip("/")
        if ruta in ("", "/index"):
            ruta = "/"
        return ruta

    @rx.var
    def url_detalle_carrera_destacada(self) -> str:
        """URL del detalle de la carrera destacada."""
        return f"/carrera/{self.id_carrera_destacada}"

    # ==================================================================
    # VARIABLES COMPUTADAS: CARRERA SELECCIONADA (DETALLE)
    # ==================================================================

    @rx.var
    def carrera_seleccionada(self) -> Carrera:
        """
        Carrera activa según la URL.

        ⚠️ SIEMPRE devuelve un `Carrera` válido (con fallback),
        porque `rx.foreach` necesita tipado preciso.
        """
        return self._carrera_por_id(self.id_carrera_desde_url)

    @rx.var
    def carrera_es_valida(self) -> bool:
        """Indica si el `carrera_id` de la URL existe."""
        return self._carrera_existe(self.id_carrera_desde_url)

    @rx.var
    def plan_anual_seleccionado(self) -> PlanAnual:
        """Año del plan de estudios visible en detalle."""
        carrera = self.carrera_seleccionada
        return self._plan_anual_seguro(
            carrera["plan_estudios"],
            self.indice_anio_seleccionado,
        )

    # ==================================================================
    # VARIABLES COMPUTADAS: HOME / EXPLORADOR
    # ==================================================================

    @rx.var
    def carrera_destacada(self) -> Carrera:
        """Carrera destacada en el home."""
        return self._carrera_por_id(self.id_carrera_destacada)

    @rx.var
    def carreras_filtradas(self) -> list[Carrera]:
        """Carreras filtradas por el texto de búsqueda."""
        if not self.texto_busqueda_carrera:
            return self.carreras

        busqueda = self.texto_busqueda_carrera.lower()
        return [
            c
            for c in self.carreras
            if busqueda in c["nombre"].lower()
            or busqueda in c["nombre_corto"].lower()
            or busqueda in c["lema"].lower()
            or busqueda in c["descripcion"].lower()
        ]

    @rx.var
    def hay_resultados_busqueda(self) -> bool:
        """Indica si la búsqueda tiene resultados."""
        return len(self.carreras_filtradas) > 0

    @rx.var
    def materias_carrera_destacada(self) -> list[str]:
        """Todas las materias de la carrera destacada (aplanadas)."""
        carrera = self.carrera_destacada
        materias: list[str] = []
        for anio in carrera["plan_estudios"]:
            for materia in anio["materias"]:
                materias.append(materia)
        return materias

    @rx.var
    def perfil_carrera_destacada(self) -> list[str]:
        """Perfil profesional de la carrera destacada."""
        return self.carrera_destacada["perfil_profesional"]

    @rx.var
    def campo_carrera_destacada(self) -> list[str]:
        """Campo laboral de la carrera destacada."""
        return self.carrera_destacada["campo_laboral"]

    @rx.var
    def plan_agrupado_por_anio(self) -> list[PlanAnual]:
        """Plan de estudios de la carrera destacada."""
        return self.carrera_destacada["plan_estudios"]

    @rx.var
    def anio_explorador_seleccionado(self) -> PlanAnual:
        """Año visible en el explorador del home."""
        carrera = self.carrera_destacada
        return self._plan_anual_seguro(
            carrera["plan_estudios"],
            self.indice_anio_explorador,
        )

    @rx.var
    def materias_anio_explorador(self) -> list[str]:
        """Materias del año seleccionado en el explorador."""
        carrera = self.carrera_destacada
        return self._materias_del_plan(
            carrera["plan_estudios"],
            self.indice_anio_explorador,
        )

    @rx.var
    def preguntas_frecuentes_carrera_destacada(
        self,
    ) -> list[PreguntaFrecuente]:
        """FAQ de la carrera destacada."""
        return self.carrera_destacada.get("preguntas_frecuentes", [])

    # ==================================================================
    # VARIABLES COMPUTADAS: VISTA DE CARRERAS (columnas)
    # ==================================================================

    @rx.var
    def carreras_columna_1(self) -> list[Carrera]:
        return self.carreras[:2]

    @rx.var
    def carreras_columna_2(self) -> list[Carrera]:
        return self.carreras[2:4]

    @rx.var
    def carreras_columna_3(self) -> list[Carrera]:
        return self.carreras[4:]

    # ==================================================================
    # VARIABLES COMPUTADAS: PLAN DE ESTUDIOS (segmented control)
    # ==================================================================

    @rx.var
    def opciones_anio_plan(self) -> list[OpcionAnio]:
        """Opciones de año para el segmented control."""
        carrera = self.carrera_seleccionada
        return [
            {
                "etiqueta": plan_anual["anio"],
                "valor": str(i),
            }
            for i, plan_anual in enumerate(carrera["plan_estudios"])
        ]

    # ==================================================================
    # VARIABLES COMPUTADAS: FILTROS Y ORDENAMIENTO
    # ==================================================================

    @rx.var
    def carreras_filtradas_y_ordenadas(self) -> list[Carrera]:
        """Carreras filtradas y ordenadas según los filtros activos."""
        carreras = list(self.carreras)

        # --- Filtro ---
        if self.filtro_activo == "demanda_alta":
            carreras = [
                c for c in carreras
                if c["estadisticas"]["demanda_laboral"] == "alta"
            ]
        elif self.filtro_activo == "puntuacion_top":
            carreras = [
                c for c in carreras
                if c["estadisticas"]["puntuacion"] >= 4.7
            ]
        elif self.filtro_activo == "mas_inscritos":
            carreras = sorted(
                carreras,
                key=lambda c: c["estadisticas"]["estudiantes_inscritos"],
                reverse=True,
            )[:3]
        elif self.filtro_activo == "mas_graduados":
            carreras = sorted(
                carreras,
                key=lambda c: c["estadisticas"]["estudiantes_graduados"],
                reverse=True,
            )[:3]

        # --- Ordenamiento ---
        ordenamientos = {
            "puntuacion_desc": lambda c: c["estadisticas"]["puntuacion"],
            "inscritos_desc": (
                lambda c: c["estadisticas"]["estudiantes_inscritos"]
            ),
            "graduados_desc": (
                lambda c: c["estadisticas"]["estudiantes_graduados"]
            ),
            "empleabilidad_desc": (
                lambda c: c["estadisticas"]["tasa_empleabilidad"]
            ),
            "salario_desc": (
                lambda c: c["estadisticas"]["salario_promedio_bs"]
            ),
        }

        clave = ordenamientos.get(self.orden_activo)
        if clave is not None:
            carreras = sorted(carreras, key=clave, reverse=True)

        return carreras

    # ==================================================================
    # VARIABLES COMPUTADAS: ICONOS FLOTANTES DEL DETALLE
    # ==================================================================

    @rx.var
    def iconos_flotantes_detalle(self) -> list[rx.Component]:
        """Componentes de iconos flotantes precalculados del detalle."""
        carrera = self.carrera_seleccionada

        iconos_disponibles: list[str] = [carrera["icono"]]
        for icono_animado in carrera["iconos_animados"]:
            iconos_disponibles.append(icono_animado["nombre"])

        rng = random.Random(SEMILLA_ICONOS_FONDO)
        componentes: list[rx.Component] = []

        for _ in range(CANTIDAD_ICONOS_FONDO):
            nombre = rng.choice(iconos_disponibles)
            x = rng.uniform(0, 100)
            y = rng.uniform(0, 100)
            tamano = rng.choice(TAMANOS_ICONOS_FONDO)
            opacidad = rng.uniform(0.06, 0.15)
            delay = rng.uniform(0, 5)
            duracion = rng.uniform(6, 10)

            componentes.append(
                rx.box(
                    rx.icon(
                        tag=nombre,
                        size=tamano,
                        color=AZUL_MARINO_NEON,
                    ),
                    position="absolute",
                    left=f"{x}%",
                    top=f"{y}%",
                    opacity=f"{opacidad}",
                    animation=(
                        f"flotar_icono_particula {duracion}s "
                        f"ease-in-out {delay}s infinite"
                    ),
                    pointer_events="none",
                )
            )

        return componentes

    # ==================================================================
    # VARIABLES COMPUTADAS: CARRUSEL
    # ==================================================================

    @rx.var(cache=True)
    def carreras_destacadas_con_etiquetas(
        self,
    ) -> list[CarreraConEtiqueta]:
        """
        Todas las carreras con su etiqueta contextual.

        ✅ CACHEADA con `@rx.var(cache=True)` porque solo depende de
        `self.carreras`.
        """
        resultado: list[CarreraConEtiqueta] = []
        for i, carrera in enumerate(self.carreras):
            etiqueta = ETIQUETAS_CARRUSEL[i % len(ETIQUETAS_CARRUSEL)]
            resultado.append(
                {
                    "carrera": carrera,
                    "etiqueta": etiqueta,
                }
            )
        return resultado

    @rx.var
    def item_carrusel_actual(self) -> CarreraConEtiqueta:
        """Item actual del carrusel (carrera + etiqueta)."""
        items = self.carreras_destacadas_con_etiquetas
        if not items:
            return {"carrera": self.carreras[0], "etiqueta": "Destacada"}
        if self.indice_carrusel >= len(items):
            return items[0]
        return items[self.indice_carrusel]

    @rx.var
    def total_carrusel(self) -> int:
        """Cantidad total de items del carrusel."""
        return len(self.carreras_destacadas_con_etiquetas)

    # ==================================================================
    # MANEJADORES DE EVENTOS: DETALLE DE CARRERA
    # ==================================================================

    @rx.event
    def seleccionar_anio(self, indice: int):
        """Cambia el año visible del plan de estudios en el detalle."""
        self.indice_anio_seleccionado = indice

    @rx.event
    def seleccionar_seccion_detalle(self, seccion: str):
        """Cambia la sección activa dentro de la vista de detalle."""
        self.seccion_detalle_activa = seccion

    # ==================================================================
    # MANEJADORES DE EVENTOS: VALIDACIÓN DE RUTA
    # ==================================================================

    @rx.event
    def redirigir_si_carrera_invalida(self):
        """
        Redirige a `/404?origen=carrera` si el ID no existe.

        Se dispara desde `on_load` de la vista de detalle.
        """
        if not self.carrera_es_valida:
            return rx.redirect("/404?origen=carrera")
        return None

    # ==================================================================
    # MANEJADORES DE EVENTOS: EXPLORADOR DEL HOME
    # ==================================================================

    @rx.event
    def seleccionar_carrera_destacada(self, id_carrera: int):
        """Cambia la carrera destacada y resetea el explorador."""
        self.id_carrera_destacada = id_carrera
        self.seccion_explorador_activa = "info"
        self.indice_anio_explorador = 0
        self.texto_busqueda_carrera = ""
        self.mostrar_panel_flotante = False

    @rx.event
    def seleccionar_seccion_explorador(self, seccion: str):
        """Cambia la sección activa del explorador."""
        self.seccion_explorador_activa = seccion

    @rx.event
    def seleccionar_anio_explorador(self, indice: int):
        """Cambia el año visible en el explorador."""
        self.indice_anio_explorador = indice

    @rx.event
    def actualizar_busqueda_carrera(self, texto: str):
        """Actualiza el texto de búsqueda de carreras."""
        self.texto_busqueda_carrera = texto

    @rx.event
    def alternar_panel_flotante(self):
        """Muestra u oculta el panel flotante de selección."""
        self.mostrar_panel_flotante = not self.mostrar_panel_flotante

    @rx.event
    def cerrar_panel_flotante(self):
        """Cierra el panel flotante."""
        self.mostrar_panel_flotante = False

    # ==================================================================
    # MANEJADORES DE EVENTOS: FILTROS Y ORDENAMIENTO
    # ==================================================================

    @rx.event
    def cambiar_filtro(self, filtro: str):
        """Cambia el filtro activo de la lista de carreras."""
        self.filtro_activo = filtro

    @rx.event
    def cambiar_orden(self, orden: str):
        """Cambia el ordenamiento activo de la lista de carreras."""
        self.orden_activo = orden

    # ==================================================================
    # MANEJADORES DE EVENTOS: CARRUSEL
    # ==================================================================
    # ⚠️ El auto-avance vive en `hero_carreras` con `rx.moment`.
    #    Este State solo expone los eventos manuales.
    # ==================================================================

    @rx.event
    def siguiente_carrusel(self):
        """
        Avanza al siguiente banner del carrusel.

        Disparado por:
        - `rx.moment(interval=...)` del componente (cada 5s).
        - La flecha derecha del carrusel (clic manual).
        """
        total = len(self.carreras_destacadas_con_etiquetas)
        if total > 0:
            self.indice_carrusel = (self.indice_carrusel + 1) % total

    @rx.event
    def anterior_carrusel(self):
        """Retrocede al banner anterior del carrusel."""
        total = len(self.carreras_destacadas_con_etiquetas)
        if total > 0:
            self.indice_carrusel = (self.indice_carrusel - 1) % total

    @rx.event
    def ir_a_banner(self, indice: int):
        """Salta a un banner específico del carrusel."""
        self.indice_carrusel = indice

    # ==================================================================
    # UTILIDADES
    # ==================================================================

    @rx.event
    def aleatorizar_colores_carreras(self, semilla: int | None = None):
        """
        Reasigna aleatoriamente la paleta de colores a las carreras.

        ⚠️ Función de prototipado. Los colores NO se usan actualmente
        porque el proyecto unificó el acento bajo `AZUL_MARINO_NEON`.

        Args:
            semilla: Semilla aleatoria para reproducibilidad.
        """
        rng = random.Random(semilla)

        cantidad = len(self.carreras)
        paleta_disponible = PALETA_COLORES.copy()

        if len(paleta_disponible) >= cantidad:
            seleccionados = rng.sample(paleta_disponible, cantidad)
        else:
            seleccionados = [
                rng.choice(paleta_disponible) for _ in range(cantidad)
            ]

        rng.shuffle(seleccionados)

        carreras_actualizadas: list[Carrera] = []
        for carrera, colores in zip(self.carreras, seleccionados):
            principal, suave, principal_dark, suave_dark = colores
            nueva_carrera = dict(carrera)
            nueva_carrera["color_principal"] = principal
            nueva_carrera["color_suave"] = suave
            nueva_carrera["color_principal_dark"] = principal_dark
            nueva_carrera["color_suave_dark"] = suave_dark
            carreras_actualizadas.append(nueva_carrera)

        self.carreras = carreras_actualizadas


# ======================================================================
# EXPORTS
# ======================================================================

__all__ = [
    "CANTIDAD_ICONOS_FONDO",
    "ETIQUETAS_CARRUSEL",
    "EstadoInstitucional",
    "FILTROS_VALIDOS",
    "ORDENES_VALIDAS",
    "OpcionAnio",
    "SECCIONES_DETALLE_VALIDAS",
    "SECCIONES_EXPLORADOR_VALIDAS",
    "SEGUNDOS_ENTRE_BANNERS",
    "SEMILLA_ICONOS_FONDO",
    "TAMANOS_ICONOS_FONDO",
]