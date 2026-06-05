from views.Utilities import mostrar_menu
from views import Utilities as utilities_views

navegacion = []

def navegacion_regresar():
    utilities_views.opciones("", ["Atras"])
    navegacion.pop()
    navegacion[-1]()


def navegacion_adelante(opciones: list, opciones_accion: list, titulo: str):
    for i in range(len(navegacion)):
        print(i)
    
    opcion_seleccionada = mostrar_menu(titulo, opciones)

    for indice, valor in enumerate(opciones):
        if valor == opcion_seleccionada:
            # Agregamos la opcion a la navegacion para poder volver atras
            navegacion.append(opciones_accion[indice])
            
            opciones_accion[indice]()

