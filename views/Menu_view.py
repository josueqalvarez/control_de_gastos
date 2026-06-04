from views import Utilities
import sys

def mostrar_menu(titulo: str, menu):

    if len(menu) != 0:

        var = Utilities.opciones(
            f"\n=== {titulo} ===",
            [opcion for opcion in menu],
        )
        return var

    else:
        var = Utilities.opciones(
            "No hay opciones existentes",
            ["salir"]
        )

        if var == "salir": sys.exit()

