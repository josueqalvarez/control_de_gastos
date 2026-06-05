from InquirerPy import inquirer
from views import utilities_view

class Area:

    areas = []
    areas_cantidad = 0
    areas_porcentaje = 100

    def __init__(self, nombre, monto_limite):
        self.nombre = nombre
        self.monto_limite = monto_limite
        self.monto_usado = 0

    @classmethod
    def atributos(cls):
        print(f"Areas actuales: ({Area.areas_cantidad}):")
        for area in Area.areas:
            print(f" - {area.nombre}: {area.monto_limite}%")

    @staticmethod
    def agregar():
        nombre = input("Nombre del area: ")

        nueva_area = Area(nombre, 0)

        while (True):
            monto_limite = int(input("Monto limite (ingresa el porcentaje maximo sobre el total de tu sueldo a usar, solo numero): "))

            porcentaje_restante = Area.areas_porcentaje - monto_limite

            if porcentaje_restante >= 0:
                Area.areas_porcentaje = porcentaje_restante
                break
            else:
                print(f"El porcentaje ingresado excede al sobrante, solo queda {Area.areas_porcentaje}%")
                print("Las areas actuales son:")
                for area in Area.areas:
                    print(f" - {area.nombre}: {area.monto_limite}%")

        nueva_area.monto_limite = monto_limite

        Area.areas.append(nueva_area)
        Area.areas_cantidad += 1

        return nueva_area




class Subarea:

    subareas = []

    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def __str__(self):
        print(f"Nombre del subarea: {self.nombre}")
        print(f"Area a la que pertenece: {self.area}")

    @classmethod
    def atributos(cls):
        print(f"Subareas actuales: ({len(Subarea.subareas)}):")
        for subarea in Subarea.subareas:
            print(f" - {subarea.nombre} (Area: {subarea.area})")    

    @staticmethod
    def agregar():
        
        area = utilities_view.mostrar_menu(
            "Selecciona una area:", [area.nombre for area in Area.areas]
            )
                    
        nombre = input("Ingresa el nombre del subarea: ")

        nueva_subarea = Subarea(nombre, area)
        Subarea.subareas.append(nueva_subarea)

        return nueva_subarea

