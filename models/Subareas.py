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

def obtener_subareas_por_nombre(nombre):
    res = conexion.realizar_consulta(
        """SELECT * FROM subareas WHERE nombre = (?)""",
        (nombre,)
    )

    if len(res) == 1:
        return res[0]
    elif len(res) > 1:
        return res
    else:
        return []

def obtener_subareas_por_area_id(area_id):
    # Al ser 1 solo item, retorna 1 valor de la lista (1 dict)
    res = conexion.realizar_consulta(
        """SELECT * FROM subareas WHERE area = (?)""",
        (area_id,)
    )
    
    if len(res) > 1:
        return res
    else:
        return []


def agregar_subarea(nombre, area_id):
    print(nombre, area_id)
    conexion.realizar_consulta(
        """INSERT INTO subareas (nombre, area) VALUES (?, ?)""",
        (nombre, area_id)
    )
