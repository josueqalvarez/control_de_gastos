from models.Areas import Area, Subarea


def ver_areas():
 
    if len(Area.areas) == 0:
        print("No hay areas registradas")
    else:
        for area in Area.areas:
            print(f" - {area.nombre}: {area.monto_limite}%")



def ver_subareas(area):

    subareas = [subarea for subarea in Subarea.subareas if subarea.area == area.nombre]

    if len(subareas) == 0:
        print(f"No hay subareas registradas para el area '{area.nombre}'")
    else:
        
        print(f"Subareas del area {area.nombre}:")    
        for subarea in subareas:
            print(f" - {subarea.nombre}")