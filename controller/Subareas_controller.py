from views import utilities_view, Subareas_view
from models import Subareas, Areas
from controller import navegacion_controller as nav

def ver_subareas():
    
    areas = Areas.obtener_areas()

    if areas: 
        area_nombre = utilities_view.mostrar_menu(
            "Elige un area:", 
            [area["nombre"] for area in Areas.obtener_areas()])
        area = Areas.obtener_area_por_nombre(area_nombre)

        subareas = Subareas.obtener_subareas_por_area_id(area["id"])
        if type(subareas) != list: subareas = [subareas]


        if subareas:
            Subareas_view.mostrar_subareas(area_nombre, subareas)
        else:
            utilities_view.faltan_datos("SUBAREAS")

    else:
        utilities_view.faltan_datos("AREAS")

    nav.navegacion_regresar()


def ver_subareas_detalle():

    area = mostrar_menu(
        "Elige el area:", 
        [area.nombre for area in Area.areas])

    for indice, valor in enumerate(Area.areas):
        if valor.nombre == area:
            area_elegida = valor

    print(f"{area_elegida.nombre} --------------" )
    subarea_elegida = mostrar_menu(
        "Elegir subarea a ver detalle", 
        [subarea.nombre for subarea in Subarea.subareas if subarea.area == area_elegida.nombre])

    for indice, valor in enumerate(Subarea.subareas):
        if valor.nombre == subarea_elegida:
            subarea_elegida = valor
    
    subarea_elegida.__str__()

    navegacion_regresar()


def agregar_subarea():
    areas = Areas.obtener_areas()

    if areas: 
        area_nombre = utilities_view.mostrar_menu(
            "Elige un area:", 
            [area["nombre"] for area in Areas.obtener_areas()])
        area = Areas.obtener_area_por_nombre(area_nombre)

        nombre = utilities_view.pedir_dato_str("Ingresa el nombre del subarea: ")

        Subareas.agregar_subarea(nombre, area["id"])
        mensaje_final = f"Nueva subarea '{nombre}' agregada"
        
    else:
        utilities_view.faltan_datos("AREAS")
        mensaje_final = ""

    nav.navegacion_regresar(mensaje_final)

