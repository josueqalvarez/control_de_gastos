from datetime import datetime
from database import conexion

class Periodo:

    bd_temporal = []

    def __init__(self):

        fecha_actual = datetime.now()
        self.año = fecha_actual.year
        self.mes = fecha_actual.month

        # Ejemplo: 202605
        self.id_periodo = int(
                f"{self.año}{self.mes:02d}"
                )
        

def agregar_periodo(id_periodo, anio, mes):
    conexion.realizar_consulta(
        """ INSERT INTO periodo (id_periodo, anio, mes) VALUES (?,?,?) """,
        (id_periodo, anio, mes),
    )

def obtener_periodo_por_id(id_periodo):
    res = conexion.realizar_consulta(
        """SELECT * FROM periodo WHERE id_periodo = (?)""",
        (id_periodo,)
        )

    if res:
        return res[0]
    else:
        return []
