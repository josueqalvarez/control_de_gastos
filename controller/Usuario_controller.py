from models.Usuario import Usuario
from views import App_view

def seleccionar_usuario():

    # Validamos el USUARIO =======================
    if len(Usuario.bd_temp) == 0:

        # No hay usuarios registrados, se registra el primero
        print("Primero, vamos a registrar tu usuario")
        Usuario.agregar()

        usuario_activo = Usuario.bd_temp[0]

    elif len(Usuario.bd_temp) > 1:
        # Hay varios usuarios registrados, se le pregunta al usuario cual es el suyo

        print("Hay varios usuarios registrados, selecciona uno:")

        usuario_activo_nombre = App_view.escoger_opciones(
            [usuarios.nombre for usuarios in Usuario.bd_temp],
            "Selecciona el usuario que realizó el gasto:",
        )

        usuario_activo = [
            usuario
            for usuario in Usuario.bd_temp
            if usuario.nombre == usuario_activo_nombre
        ][0]

    else:
        # Solo hay un usuario registrado, se selecciona automáticamente
        usuario_activo = Usuario.bd_temp[0]

    Usuario.usuario_activo = usuario_activo
    print(f"Hola {usuario_activo.nombre}")
    
    return usuario_activo
