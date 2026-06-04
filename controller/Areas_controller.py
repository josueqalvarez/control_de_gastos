from views.Menu_view import mostrar_menu
from models import Areas

def ver_areas():

    return # lista de areas


def ver_subareas():
    
    areas = mostrar_menu("Elegir area", Areas.Area.areas)

    return # lista de subareas


def ver_subareas_detalle():

    areas = mostrar_menu("Elegir area", Areas.Area.areas)
    subarea = mostrar_menu("Elegir subarea", Areas.Subarea.subareas)

    pass

def agregar_area():
    pass

def agregar_subarea():
    pass