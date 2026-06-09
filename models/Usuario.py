from database import conexion


class Usuario:

    def __init__(self, dni=None, nombre=None, sueldo=None):
        self.dni = dni
        self.nombre = nombre
        self.sueldo = sueldo


def agregar_usuario(dni, nombre, sueldo):

    # Agregamos a la bd
    conexion.realizar_consulta(
        """ INSERT INTO usuario (id_dni, nombre, sueldo) VALUES (?,?,?) """,
        (dni, nombre, sueldo),
    )


def obtener_usuarios():
    return conexion.realizar_consulta("""SELECT * FROM usuario""")

def obtener_usuario_por_dni(dni):
    # Devuelve un objeto 
    res = conexion.realizar_consulta(
        "SELECT * FROM usuario WHERE id_dni = ?",
        (dni,)
    )

    if res:
        return res[0]
    else:
        return False 
