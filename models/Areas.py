from database import conexion


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


def agregar_area(nombre, monto_limite, monto_usado = 0):

    conexion.realizar_consulta(
        """
        INSERT INTO areas (nombre, monto_limite, monto_usado)
        VALUES (?, ?, ?)
        """,
        (nombre, monto_limite, monto_usado),
    )

# Obtener el monto limi
def obtener_monto_limite():
    pass

def obtener_porcentaje_restante():
    monto_de_cada_area = conexion.realizar_consulta(
        """SELECT monto_limite FROM areas"""
    )
    monto_restante = 100 - sum(monto_de_cada_area)

    # Retorna un decimal
    return monto_restante

def obtener_areas():
    return conexion.realizar_consulta(
        """SELECT * FROM areas"""
    )

def obtener_area_por_nombre(nombre):
    res =  conexion.realizar_consulta(
        """SELECT * FROM areas WHERE nombre = (?)""",
        (nombre)
    )

    if res:
        return res[0]
    else:
        return []

def actualizar_monto_usado(nuevo_monto_usado, area_id):
    conexion.realizar_consulta(
        """UPDATE areas
            SET monto_usado = ?
            WHERE id = ?""",
            (nuevo_monto_usado, area_id)
    )
    