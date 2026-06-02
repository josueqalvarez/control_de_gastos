from InquirerPy import inquirer


class Area:

    areas = []

    def __init__(self, nombre, monto_limite: float):
        self.nombre = nombre
        self.monto_limite = monto_limite

        Area.areas.append(self.nombre)



class Subarea:

    def __init__(self):
        self.nombre = None
        self.area_perteneciente = None

    @staticmethod
    def agregar(self):
        
        if len(Area.areas) > 0:
            area_perteneciente = inquirer.select(
                message="Selecciona una area perteneciente:",
                choices= Area.areas
            ).execute()
            nombre = input("Ingresa el nombre del subarea")

            nueva_subarea = Subarea()
            nueva_subarea.nombre = nombre
            nueva_subarea.area_perteneciente = area_perteneciente

            Subarea.subareas.append(nueva_subarea)

        else:
            print("No hay áreas existentes")


        return
