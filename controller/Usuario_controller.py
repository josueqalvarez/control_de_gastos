from models.Usuario import agregar_usuario, obtener_usuarios, obtener_usuario_por_dni
from models import utilities
from views import Usuario_view, utilities_view

def seleccionar_usuario():

    usuarios = obtener_usuarios()

    # Validamos el USUARIO =======================
    if len(usuarios) == 0:

        # No hay usuarios registrados, se registra el primero
        print("Primero, vamos a registrar tu usuario")
        
        crear_usuario()
        usuario_actual = obtener_usuarios()[0]

    elif len(usuarios) > 1:
        # Hay varios usuarios registrados, se le pregunta al usuario cual es el suyo
        print(usuarios)
        usuario = utilities_view.opciones(
            # Volver a usuarios una lista de objetos, para reemplazar en la siguiente linea
            "Elije tu usuario:", 
            [f"{usuarios.id_dni} - {usuarios.nombre}" for usuarios in obtener_usuarios()]            
        )

        usuario_actual = obtener_usuario_por_dni(usuario[:8])

    else:
        # Solo hay un usuario registrado, se selecciona automáticamente
        usuario_actual = obtener_usuarios()[0]

    utilities.usuario_activo = usuario_actual

    print(f"Hola {utilities.usuario_activo["nombre"]}")
    

def crear_usuario():
    while True:
        dni = Usuario_view.pedir_dni()

        # Consultamos a la bd siesque el dni ya existe
        if obtener_usuario_por_dni(dni) == False:
            nombre, sueldo = Usuario_view.pedir_datos_extra()  
            agregar_usuario(dni, nombre, sueldo)
            break
        else:
            print("DNI ya existe, intenta de nuevo.")


def editar_usuario():
    pass

def eliminar_usuario():
    pass

def cambiar_usuario_actual():
    pass