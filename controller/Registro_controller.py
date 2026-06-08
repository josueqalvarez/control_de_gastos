from views import App_view, Registro_view, utilities_view
from models import (Areas, Subareas, Registro, Periodo, utilities)

def registrar_gasto():

    area, subarea = _elegir_area_y_subarea()
    if area is None or subarea is None:
        utilities_view.faltan_datos("AREAS")
        return
    
    monto = _calculamos_gasto(area)
    fecha = Periodo().id_periodo
    notas = utilities_view.pedir_dato_str("Ingrese notas adicionales (opcional): ")

    Registro.registrar_agregar(subarea, fecha, utilities.usuario_activo["id_dni"], monto, notas)
    Registro_view.estado_registro('exitoso')

def _calculamos_gasto(area):
    
    while True:
        monto = utilities_view.pedir_dato_int("Ingrese monto: ")

        if area.monto_usado + monto <= area.monto_limite:
            area.monto_usado += monto
            return monto
        else:
            App_view.exceso_monto(area)

def _elegir_area_y_subarea():

    # Validamos el AREA =======================
    areas_disponibles = Areas.obtener_areas()
    
    if len(areas_disponibles) == 0:
        return None, None
    
    
    area_elegida_nombre = utilities_view.opciones(
        "Selecciona el area de tu gasto:",
        [area["nombre"] for area in areas_disponibles]
        )
    
    area = Areas.obtener_area_por_nombre(area_elegida_nombre)
    

    # Validamos la SUBAREA =======================
    subareas_disponibles = Subareas.obtener_subareas_por_nombre(area["nombre"])
    
    #### HASTA AQUI ME QUEDE
    
    subareas_correspondientes = [sub.nombre for sub in Areas.Subarea.subareas if sub.area == area_elegida_nombre]
    
    if len(subareas_correspondientes) == 0:
        utilities_view.faltan_datos("subareas")
        return None, None
    
    subarea_nombre = utilities_view.opciones(
        "Selecciona la subarea a la que pertenece el gasto:",
        subareas_correspondientes)
    

    # Obtenemos los objetos area y subarea a partir de los nombres seleccionados
    area = [area for area in Areas.Area.areas if area.nombre == area_elegida_nombre][0]
    subarea = [sub for sub in Areas.Subarea.subareas if sub.nombre == subarea_nombre][0]


    return area, subarea


def ultimos_gastos():
    gastos = Registro.obtener_ultimos_gastos()
    Registro_view.mostrar_ultimos_gastos(gastos)