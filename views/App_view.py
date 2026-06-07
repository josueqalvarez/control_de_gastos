from views import utilities_view


# Utilizado para area y subarea
def escoger_opciones(lista_areas, mensaje_selecciona):
    return utilities_view.opciones(mensaje_selecciona, lista_areas)

def exceso_monto(area):
    print(
        f"El monto ingresado excede el limite, solo puedes gastar {area.monto_limite - area.monto_usado} mas en esta area."
    )
