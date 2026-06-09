from views import Registro_view, utilities_view
from models import (Areas, Subareas, Registro, utilities)
from controller import navegacion_controller as nav

def registrar_gasto():

    # Area y Subarea
    area, subarea = _elegir_area_y_subarea()
    if area is None or subarea is None:
        utilities_view.faltan_datos("AREAS")
        return
    
    # POR ARREGLAR. Los nombres no son PK, por ello es que puede haber mas de 1 ======
    if type(subarea) == list:
        if len(subarea) > 1:
            print("Error, hay mas de 1 subarea llamada igual")
            return
        elif len(area) > 1:
            print("Error, hay mas de 1 subarea llamada igual")
            return
    # ================================================================================

    # Periodo
    fecha = utilities.periodo_actual_id
    # Usuario
    dni_usuario = utilities.usuario_activo["id_dni"]
    # Monto
    gasto = _calculamos_gasto(area)
    # Notas
    notas = utilities_view.pedir_dato_str("Ingrese notas adicionales (opcional): ")

    # Agregamos el registro
    Registro.registro_agregar(subarea["id"], fecha, dni_usuario, gasto, notas)
    # Actualizamos el monto que uso el area en la bd
    Areas.actualizar_monto_usado(gasto + area["monto_usado"], area["id"])
    
    Registro_view.estado_registro('exitoso\n')
    
    # Actualizamos el monto que uso el area en la bd
    utilities_view.mostrar_texto_simple(
        f"Solo te queda S/ "
        f" {Registro.obtener_monto_disponible_a_gastar_segun_area(utilities.usuario_activo, area, gasto)} "
            f"en {(area["nombre"]).upper()} por gastar."
        )


def _calculamos_gasto(area):

    monto_maximo_a_gastar = Registro.obtener_monto_maximo_a_gastar_segun_area(utilities.usuario_activo, area)
    
    while True:
        
        gasto = utilities_view.pedir_dato_float("Ingresa el monto: ")

        if gasto + area["monto_usado"] <= monto_maximo_a_gastar:
            return gasto
        else:
            utilities_view.mostrar_texto_simple(
                f"El monto ingresado excede el limite, solo puedes gastar {monto_maximo_a_gastar - area["monto_usado"]} mas en esta area.")
            return


def _elegir_area_y_subarea():

    # Validamos el AREA =======================
    areas_disponibles = Areas.obtener_areas()
    
    if len(areas_disponibles) == 0:
        return None, None
    else:        
        area_elegida_nombre = utilities_view.opciones(
            "Selecciona el area de tu gasto:",
            [area["nombre"] for area in areas_disponibles]
            )
        
        # Obtenemos el area elegida
        area = Areas.obtener_area_por_nombre(area_elegida_nombre)
    

        # Validamos la SUBAREA =======================
        subareas_disponibles = Subareas.obtener_subareas_por_area_id(area["id"])
        
        if len(subareas_disponibles) == 0:
            utilities_view.faltan_datos("subareas")
            return None, None
        else:
            subarea_elegida_nombre = utilities_view.opciones(
                "Selecciona la subarea a la que pertenece el gasto:",
                [subarea["nombre"] for subarea in subareas_disponibles])

            # Obtenemos el subarea elegida
            subarea = Subareas.obtener_subareas_por_nombre(subarea_elegida_nombre)

            # Devuelve 2 dict
            return area, subarea


def ultimos_gastos():
    cantidad = utilities_view.pedir_dato_int("¿Deseas una cantidad especifica? (opcional):")
    gastos = Registro.obtener_ultimos_gastos(utilities.usuario_activo["id_dni"] ,cantidad)

    Registro_view.mostrar_ultimos_gastos(gastos, cantidad)
    nav.navegacion_regresar()
