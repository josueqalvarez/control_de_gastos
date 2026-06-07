def mostrar_areas(areas):
 
    if len(areas) == 0:
        print("No hay areas registradas")
    else:
        print("Las areas actuales son:")
        for area in areas:
            print(f" - {area["nombre"]}: {area["monto_limite"]}%")


def mostrar_porcentaje_restante(
        mensaje="", porcentaje_sobrante = ""):
    print(f"{mensaje}{porcentaje_sobrante}%")


