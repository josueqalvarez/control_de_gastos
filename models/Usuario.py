class Usuario:

    bd_temp = []

    def __init__(self, dni = None, nombre = None, sueldo = None):
        self.dni = dni
        self.nombre = nombre
        self.sueldo = sueldo


    @staticmethod
    def agregar():
        while True:
            dni = int(input("DNI: "))
            if dni not in [usuario.dni for usuario in Usuario.bd_temp]:
                break
            else:
                print("DNI ya existe, intenta de nuevo.")
        nombre = input("Nombre: ")
        sueldo = int(input("Sueldo: "))

        Usuario.bd_temp.append(Usuario(dni, nombre, sueldo))
