from models.Menu import Menu
from views.Menu_view import mostrar_menu
from controller import Registro_controller, Areas_controller
import sys


def menu_principal(usuario_activo):

    opciones = ["1. Registrar gasto", "2. Areas", "3. Usuarios", "4. Salir"]

    opciones_accion = [
        lambda: Registro_controller.registrar_gasto(usuario_activo.dni),
        menu_areas,
        None,
        sys.exit,
    ]

    _proceso(opciones, opciones_accion, "Control de Gastos")



def menu_areas():
    areas = [
        "1. Ver areas",
        "2. Ver subareas",
        "3. Ver detalle de area",
        "4. Agregar area",
        "5. Agregar subarea",
        "6. Atrás",
    ]
    areas_accion = [
        Areas_controller.ver_areas,
        Areas_controller.ver_subareas,
        Areas_controller.ver_subareas_detalle,
        Areas_controller.agregar_area,
        Areas_controller.agregar_subarea,
        sys.exit,
    ]

    _proceso(areas, areas_accion, "Areas")




def _proceso(opciones: list, opciones_accion: list, titulo: str):

    opcion_seleccionada = mostrar_menu(titulo, opciones)

    for indice, valor in enumerate(opciones):
        if valor == opcion_seleccionada:
            opciones_accion[indice]()