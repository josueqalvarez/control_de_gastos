from database import conexion

class Registro:
    
    registros = []
    
    def __init__(self, subarea, monto, fecha, dni_usuario, notas=""):
        self.fecha = fecha
        self.subarea = subarea
        self.dni_usuario = dni_usuario
        self.monto = monto
        self.notas = notas


def registro_agregar(subarea, periodo, dni_usuario, monto, notas=""):

    conexion.realizar_consulta(
        """INSERT INTO 
            registros (subarea, periodo, dni_usuario, monto, notas) 
            VALUES (?, ?, ?, ?, ?)
            """,
        (subarea, periodo, dni_usuario, monto, notas)
    )

def obtener_ultimos_gastos(dni_usuario, cantidad= 10):
    return conexion.realizar_consulta(
        """
        SELECT * FROM registros
        WHERE dni_usuario = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (dni_usuario, cantidad)
    )    

def obtener_monto_maximo_a_gastar_segun_area(usuario, area):
    # Obtenemos el monto maximo a utilizar en soles segun el porcentaje asignado del area
    return (usuario["sueldo"] * area["monto_limite"])/100

def obtener_monto_disponible_a_gastar_segun_area(usuario, area, gasto):
    
    return f" {obtener_monto_maximo_a_gastar_segun_area(usuario , area) - gasto - area["monto_usado"]}"
    
