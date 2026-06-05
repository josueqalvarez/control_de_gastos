from InquirerPy import inquirer
from views import utilities_view
from models import navegacion

def mostrar_menu(titulo: str, menu):

    if len(menu) != 0:

        var = utilities_view.opciones(
            f"\n=== {titulo} ===",
            [opcion for opcion in menu],
        )
        return var

    else:
        utilities_view.opciones("", ["Atras"])
        navegacion.navegacion.pop()
        navegacion.navegacion[-1]()


def opciones(mensaje:str, arr:list):
    var = inquirer.select(
        message=mensaje,
        choices=arr
        ).execute()

    return var