
class Registro:
    
    registros = []
    
    def __init__(self, subarea, monto, fecha, dni_usuario, notas=""):
        self.fecha = fecha
        self.subarea = subarea
        self.dni_usuario = dni_usuario
        self.monto = monto
        self.notas = notas

    @staticmethod
    def registrar_agregar(subarea, monto, fecha, usuario, notas=""):

        Registro.registros.append(Registro(subarea, monto, fecha, usuario.dni, notas))
        

