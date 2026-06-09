from views import Registro_view, utilities_view
from models import (Areas, Subareas, Registro, utilities)

def registrar_gasto():

    # Area y Subarea
    area, subarea = _elegir_area_y_subarea()
    if area is None or subarea is None:
        utilities_view.faltan_datos("AREAS")
        return
    
    # Periodo
    fecha = utilities.periodo_actual_id
    # Usuario
    dni_usuario = utilities.usuario_activo["id_dni"]
    # Monto
    gasto = _calculamos_gasto(area)
    # Notas
    notas = utilities_view.pedir_dato_str("Ingrese notas adicionales (opcional): ")

    Registro.registrar_agregar(subarea["id"], fecha, dni_usuario, gasto, notas)
    Registro_view.estado_registro('exitoso')


def _calculamos_gasto(area):

    sueldo_usuario = utilities.usuario_activo["sueldo"]

    monto_maximo_a_gastar = (sueldo_usuario * area["monto_limite"])/100
    

    while True:
        
        gasto = utilities_view.pedir_dato_float("Ingresa el monto: ")

        if gasto + area["monto_usado"] <= monto_maximo_a_gastar:
            Areas.actualizar_monto_usado(gasto + area["monto_usado"], area["id"])
            return gasto

        else:
            utilities_view.mostrar_texto_simple(
                f"El monto ingresado excede el limite, solo puedes gastar {monto_maximo_a_gastar - area["monto_usado"]} mas en esta area.")


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
        subareas_disponibles = Subareas.obtener_subareas_por_nombre(area["nombre"])
        
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
    gastos = Registro.obtener_ultimos_gastos()
    Registro_view.mostrar_ultimos_gastos(gastos)