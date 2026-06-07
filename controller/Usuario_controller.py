from models.Usuario import agregar_usuario, obtener_usuarios, obtener_usuario_por_dni
from models.utilities import usuario_activo
from views import App_view, Usuario_view

def seleccionar_usuario():

    usuarios = obtener_usuarios()

    # Validamos el USUARIO =======================
    if len(usuarios) == 0:

        # No hay usuarios registrados, se registra el primero
        print("Primero, vamos a registrar tu usuario")
        
        nuevo_usuario = agregar_nuevo_usuario()
        usuario_actual = nuevo_usuario

    elif len(usuarios) > 1:
        # Hay varios usuarios registrados, se le pregunta al usuario cual es el suyo

        usuario = App_view.escoger_opciones(
            # Volver a usuarios una lista de objetos, para reemplazar en la siguiente linea
            [f"{usuarios.id_dni} - {usuarios.nombre}" for usuarios in obtener_usuarios()],
            "Elije tu usuario:",
        )

        usuario_actual = obtener_usuario_por_dni(usuario[:8])

    else:
        # Solo hay un usuario registrado, se selecciona automáticamente
        usuario_actual = obtener_usuarios()[0]
        print(usuario_actual)

    usuario_activo = usuario_actual
    print(f"Hola {usuario_activo["nombre"]}")
    

def agregar_nuevo_usuario():
    while True:
        dni = Usuario_view.pedir_dni()

        # Consultamos a la bd siesque el dni ya existe
        if obtener_usuario_por_dni(dni) == False:
            nombre, sueldo = Usuario_view.pedir_datos_extra()  
            return agregar_usuario(dni, nombre, sueldo)


        else:
            print("DNI ya existe, intenta de nuevo.")
