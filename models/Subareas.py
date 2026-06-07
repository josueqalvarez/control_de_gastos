from database import conexion

class Subarea:

    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def __str__(self):
        print(f"Nombre del subarea: {self.nombre}")
        print(f"Area a la que pertenece: {self.area}")


def obtener_subareas():
    return conexion.realizar_consulta(
        """SELECT * FROM subareas"""
    )

def obtener_subarea_por_nombre(nombre):
    return conexion.realizar_consulta(
        """SELECT * FROM subareas WHERE nombre = (?)""",
        (nombre)
    )

def obtener_subarea_por_area_id(area_id):
    return conexion.realizar_consulta(
        """SELECT * FROM subareas WHERE area = (?)""",
        (area_id)
    )

@staticmethod
def agregar(nombre, area):

    conexion.realizar_consulta(
        """INSERT INTO subareas (nombre, area) VALUES (?, ?)""",
        (nombre, area)
    )

    return 
    area = utilities_view.mostrar_menu(
        "Selecciona una area:", [area.nombre for area in Area.areas]
    )

    nombre = input("Ingresa el nombre del subarea: ")

    nueva_subarea = Subarea(nombre, area)
    Subarea.subareas.append(nueva_subarea)

    return nueva_subarea
