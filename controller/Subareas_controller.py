from views import utilities_view, Subareas_view
from models import Subareas, Areas
from controller import navegacion_controller as nav

def ver_subareas():
    
    areas = Areas.obtener_areas()

    if areas: 
        area_nombre = utilities_view.mostrar_menu(
            "Elige el area:", 
            [area["nombre"] for area in Areas.obtener_areas()])
        print ("asdadasdasdadaads", area_nombre, type(area_nombre))
        area = Areas.obtener_areas_por_nombre(area_nombre)

        subareas = Subareas.obtener_subarea_por_area_id(area["id"])

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
    nueva_subarea = Subarea.agregar()
    navegacion_regresar(f"Nueva subarea '{nueva_subarea.nombre}' agregada")