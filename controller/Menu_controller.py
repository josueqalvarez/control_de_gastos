from controller import Registro_controller, Areas_controller, navegacion
import sys


def menu_principal(usuario_activo):

    opciones = ["1. Registrar gasto", "2. Areas", "3. Usuarios", "4. Salir"]

    opciones_accion = [
        lambda: Registro_controller.registrar_gasto(usuario_activo.dni),
        menu_areas,
        None,
        sys.exit,
    ]

    # Agregamos el menu principal a la navegacion por primera vez
    if len(navegacion.navegacion) == 0:
        navegacion.navegacion.append(menu_principal)

    navegacion.navegacion_adelante(opciones, opciones_accion, "Control de Gastos")



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
        navegacion.navegacion_regresar,
    ]

    navegacion.navegacion_adelante(areas, areas_accion, "Areas")




