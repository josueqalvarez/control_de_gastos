from database import conexion

class Registro:
    
    registros = []
    
    def __init__(self, subarea, monto, fecha, dni_usuario, notas=""):
        self.fecha = fecha
        self.subarea = subarea
        self.dni_usuario = dni_usuario
        self.monto = monto
        self.notas = notas


def registrar_agregar(subarea, periodo, dni_usuario, monto, notas=""):

    conexion.realizar_consulta(
        """INSERT INTO 
            registros (subarea, periodo, dni_usuario, monto, notas) 
            VALUES (?, ?, ?, ?, ?)
            """,
        (subarea, periodo, dni_usuario, monto, notas)
    )


    

