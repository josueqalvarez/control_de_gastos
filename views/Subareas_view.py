def mostrar_subareas(area, subareas):

    if subareas:
        print(f"Las subareas de {area} son:")
        for subarea in subareas:
            print(f" - {subarea["nombre"]}")

    else:
        print("No hay subareas registradas")

