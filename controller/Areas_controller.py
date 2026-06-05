from controller.navegacion import navegacion_regresar
from views.Utilities import mostrar_menu
from models.Areas import Area, Subarea
from views import Areas_view


def ver_areas():

    Areas_view.ver_areas()
    navegacion_regresar()




def ver_subareas():
    
    area = mostrar_menu("Elige el area para ver sus subareas", Area.areas, "No hay areas registradas")

    Areas_view.ver_subareas(area)

    navegacion_regresar()



def ver_subareas_detalle():

    areas = mostrar_menu("Elegir area", Area.areas)
    subarea = mostrar_menu("Elegir subarea", Subarea.subareas)

    pass

def agregar_area():
    pass

def agregar_subarea():
    pass