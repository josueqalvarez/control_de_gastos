from controller.navegacion_controller import navegacion_regresar
from views.utilities_view import mostrar_menu
from models.Areas import Area, Subarea
from views import Areas_view


def ver_areas():

    Areas_view.ver_areas()
    navegacion_regresar()




def ver_subareas():
    
    area = mostrar_menu(
        "Elige el area para ver sus subareas", 
        [area.nombre for area in Area.areas])

    for indice, valor in enumerate(Area.areas):
        if valor.nombre == area:
            area_elegida = valor

    Areas_view.ver_subareas(area_elegida)

    navegacion_regresar()



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



def agregar_area():
    nueva_area = Area.agregar()
    navegacion_regresar(f"Nueva area '{nueva_area.nombre}' agregada")

def agregar_subarea():
    nueva_subarea = Subarea.agregar()
    navegacion_regresar(f"Nueva subarea '{nueva_subarea.nombre}' agregada")