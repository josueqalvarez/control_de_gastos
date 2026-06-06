from views import App_view, Registro_view
from models import Areas, Registro, Periodo

def registrar_gasto():

    area, subarea = _elegir_area_y_subarea()
    if area is None or subarea is None:
        return
    monto = _calculamos_gasto(area)
    fecha = Periodo().id_periodo
    notas = input("Ingrese notas adicionales (opcional): ")

    Registro.registrar_agregar(subarea, monto, fecha, Registro.usuario_activo, notas)
    Registro_view.estado_registro('exitoso')

def _calculamos_gasto(area):
    
    while True:
        monto = int(input("Ingrese monto: "))
        if area.monto_usado + monto <= area.monto_limite:
            area.monto_usado += monto
            return monto
        else:
            App_view.exceso_monto(area)

def _elegir_area_y_subarea():

    # Validamos el AREA =======================
    if len(Areas.Area.areas) == 0:
        App_view.faltan_areas("areas")
        return None, None

    area_elegida_nombre = App_view.escoger_opciones(
        [area.nombre for area in Areas.Area.areas],  
        "Selecciona el area al que deseas registrar:")
    

    # Validamos la SUBAREA =======================
    subareas_correspondientes = [sub.nombre for sub in Areas.Subarea.subareas if sub.area == area_elegida_nombre]
    
    if len(subareas_correspondientes) == 0:
        App_view.faltan_areas("subareas")
        return None, None
    
    subarea_nombre = App_view.escoger_opciones(
        subareas_correspondientes,
        "Selecciona la subarea a la que pertenece el gasto:")
    

    # Obtenemos los objetos area y subarea a partir de los nombres seleccionados
    area = [area for area in Areas.Area.areas if area.nombre == area_elegida_nombre][0]
    subarea = [sub for sub in Areas.Subarea.subareas if sub.nombre == subarea_nombre][0]


    return area, subarea


def ultimos_gastos():
    gastos = Registro.obtener_ultimos_gastos()
    Registro_view.mostrar_ultimos_gastos(gastos)