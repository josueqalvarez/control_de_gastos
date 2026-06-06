from views.utilities_view import mostrar_menu
from views import utilities_view as utilities_views
from models.navegacion import navegacion

def navegacion_regresar(mensaje="", opcion_existente="no"):
    if opcion_existente == "no":
        utilities_views.opciones(mensaje, ["Atras"])
    navegacion.pop()
    navegacion[-1]()


def navegacion_adelante(opciones: list, opciones_accion: list, titulo: str):
    
    opcion_seleccionada = mostrar_menu(titulo, opciones)

    for indice, valor in enumerate(opciones):
        if valor == opcion_seleccionada:
            # Agregamos la opcion a la cola de navegacion para poder volver atras siempre que no sea retroceder
            if opcion_seleccionada != "Atrás":
                navegacion.append(opciones_accion[indice])
            
            opciones_accion[indice]()

