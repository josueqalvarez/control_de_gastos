from InquirerPy import inquirer


class Area:

    areas = []
    areas_cantidad = 0
    areas_porcentaje = 100

    def __init__(self):
        self.nombre = None
        self.monto_limite = None

    @staticmethod
    def agregar():
        nombre = input("Nombre del area: ")
        monto_limite = input("Monto limite: ")

        nueva_area = Area()
        nueva_area.nombre = nombre

        while (True):
            monto_limite = input("Monto limite (ingresa el porcentaje maximo sobre el total de tu sueldo a usar, solo numero): ")

            porcentaje_restante = Area.areas_porcentaje - monto_limite

            if porcentaje_restante >= 0:
                Area.areas_porcentaje = porcentaje_restante
                break
            else:
                print(f"El porcentaje restante excede al sobrante, solo queda {Area.areas_porcentaje}%")
                #mostrar porcentajes de cada area

        nueva_area.monto_limite = monto_limite

        Area.areas.append(nueva_area)
        areas_cantidad += 1


class Subarea:

    subareas = []

    def __init__(self):
        self.nombre = None
        self.area = None

    @staticmethod
    def agregar():
        
        if len(Area.areas) > 0:
            area = inquirer.select(
                message ="Selecciona una area:",
                choices = [
                    area.nombre for area in Area.areas
                    ]
            ).execute()
            
            nombre = input("Ingresa el nombre del subarea")

            nueva_subarea = Subarea()
            nueva_subarea.nombre = nombre
            nueva_subarea.area = area

            Subarea.subareas.append(nueva_subarea)

        else:
            print("No hay áreas existentes")


        return
