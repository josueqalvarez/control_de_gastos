class Usuario:

    bd_temp = []

    def __init__(self, dni, nombre, sueldo):
        self.dni = dni
        self.nombre = nombre
        self.sueldo = sueldo
        
        Usuario.bd_temp.append(dni)
