from controller import (
    Registro_controller,
    Areas_controller,
    navegacion_controller as nav,
    Subareas_controller
)
from models import navegacion
import sys


# ========================= MENU PRINCIPAL =========================
def menu_principal():

    opciones = ["1. Registrar gasto", "2. Areas", "3. Usuarios", "4. Salir"]

    opciones_accion = [
        menu_registro,
        menu_areas,
        None,
        sys.exit,
    ]

    # Agregamos el menu principal a la navegacion por primera vez
    if len(navegacion.navegacion) == 0:
        nav.navegacion.append(menu_principal)

    nav.navegacion_adelante(opciones, opciones_accion, "Control de Gastos")


# ======== REGISTRO ===========
def menu_registro():
    opciones = [
        "1. Registrar gasto",
        "2. Ver ultimos gastos",
        "3. Ver resumen actual",
        "4. Ver resumen por periodo",
        "5. Atrás",
    ]
    opciones_accion = [
        Registro_controller.registrar_gasto,
        None,
        None,
        lambda: nav.navegacion_regresar("", "si"),
    ]

    nav.navegacion_adelante(opciones, opciones_accion, "Registro de Gastos")


# ======== AREAS ===========
def menu_areas():
    areas = [
        "1. Ver areas",
        "2. Ver subareas",
        "3. Ver detalle de subarea",
        "4. Agregar area",
        "5. Agregar subarea",
        "Atrás",
    ]
    areas_accion = [
        Areas_controller.ver_areas,
        Subareas_controller.ver_subareas,
        Subareas_controller.ver_subareas_detalle,
        Areas_controller.agregar_area,
        Subareas_controller.agregar_subarea,
        lambda: nav.navegacion_regresar("", "si"),
    ]

    nav.navegacion_adelante(areas, areas_accion, "Areas")
