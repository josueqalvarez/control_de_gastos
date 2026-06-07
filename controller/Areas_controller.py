from controller.navegacion_controller import navegacion_regresar
from models import Areas
from views import Areas_view, utilities_view


def ver_areas():

    Areas_view.mostrar_areas(Areas.obtener_areas())
    navegacion_regresar()



def agregar_area():
    nombre = utilities_view.pedir_dato_str("Nombre del area: ")

    while (True):
        porcentaje_restante = Areas.obtener_porcentaje_restante()

        monto_limite = utilities_view.pedir_dato_int("Ingresa su porcentaje: ")

        if monto_limite <= porcentaje_restante:
            Areas.agregar_area(nombre, monto_limite)
            navegacion_regresar(f"Nueva area '{nombre}' agregada")

            break
        else:
            Areas_view.mostrar_porcentaje_restante(
                "El porcentaje ingresado excede al restante, solo te queda: ", porcentaje_restante)
            Areas_view.mostrar_areas(Areas.obtener_areas())



