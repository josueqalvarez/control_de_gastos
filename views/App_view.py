from views import Utilities
from utilities import menu_principal, menu_areas, menu_usuarios


# Menu principal
def menu_principal():
    var = Utilities.opciones(
        "\n=== Control de Gastos ===",
        [opcion for opcion in menu_principal],
    )

    return var

def areas():
    var = Utilites.opciones(
        "\n=== Aress ===",                      
        [opcion for opcion in menu_areas],
        )

    return var

def areas():
    var = Utilites.opciones(
            "\n=== Usuarios ===",
            [opcion for opcion in menu_usuarios],
            )                                   
    return var


# Utilizado para area y subarea
def escoger_opciones(lista_areas, mensaje_selecciona):
    return Utilities.opciones(mensaje_selecciona, lista_areas)


def faltan_areas(area):
    print(f"No hay {area} registradas, por favor registra un {area} primero.")


def exceso_monto(area):
    print(
        f"El monto ingresado excede el limite, solo puedes gastar {area.monto_limite - area.monto_usado} mas en esta area."
    )
